%define gdb_version 6.3
%include machine-header.spec

Name: gdb
Version: %{gdb_version}
Release: 2
Copyright: GPL
Group: Development/Debuggers
Source: gdb-%{version}.tar.bz2
Summary: GNU debugger
BuildRoot: %{_tmppath}/%{name}-root
Conflicts: vpkg-SFWgdb

%description -n gdb
GDB has support for C, C++, and Fortran, as well as partial support for
Modula-2, Chill, and Pascal.

From the documentation:

   The purpose of a debugger such as GDB is to allow you to see what is
going on "inside" another program while it executes--or what another
program was doing at the moment it crashed.

   GDB can do four main kinds of things (plus other things in support of
these) to help you catch bugs in the act:

   * Start your program, specifying anything that might affect its
     behavior.

   * Make your program stop on specified conditions.

   * Examine what has happened, when your program has stopped.

   * Change things in your program, so you can experiment with
     correcting the effects of one bug and go on to learn about another.

%package -n gnu-standards
Version: 3.13.1998
Copyright: GPL
Group: Documentation
Summary: The GNU coding standards
BuildRequires: texinfo
Requires: info

%description -n gnu-standards
From the preface:

   The GNU Coding Standards were written by Richard Stallman and other
GNU Project volunteers.  Their purpose is to make the GNU system clean,
consistent, and easy to install.  This document can also be read as a
guide to writing portable, robust and reliable programs.  It focuses on
programs written in C, but many of the rules and principles are useful
even if you write in another programming language.  The rules often
state reasons for writing in a certain way.


%package -n bfdlibs
Version: %{gdb_version}
Copyright: GPL
Group: Development/Libraries
Requires: gcc
Summary: Binary file descriptor libraries and headers

%description -n bfdlibs
Bfdlibs contains the binary file descriptor libraries and headers; you
only need them if you are building programs with them.

%prep
%setup -q -n gdb-%{gdb_version}

%build

%ifarch sparc64
# gdb seems to prefer gcc for 64 bit builds
LDFLAGS="-L/usr/local/lib/sparcv9 -R/usr/local/lib/sparcv9" CC="sparcv9-sun-%{sol_os}-gcc" ./configure --prefix=/usr/local
#LDFLAGS="-L/usr/local/lib/sparcv9 -R/usr/local/lib/sparcv9" CC="cc" CFLAGS="-xarch=v9" ./configure --prefix=/usr/local
make
mkdir -p sparcv9
mkdir -p sparcv9/libs
mv gdb/gdb sparcv9/gdb
# dont know if we need these
for i in opcodes bfd 
    do mv $i/lib${i}.a sparcv9/libs
done;
make distclean
echo finished 64 bit build
%endif

#CC="/opt/SUNWspro/bin/cc" ./configure --prefix=/usr/local
./configure --prefix=/usr/local
make
make info

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/local
make install prefix=$RPM_BUILD_ROOT/usr/local 
make install-info prefix=$RPM_BUILD_ROOT/usr/local

%ifarch sparc64
mkdir -p %{buildroot}/usr/local/bin/sparcv9
mv sparcv9/gdb %{buildroot}/usr/local/bin/sparcv9
mkdir -p %{buildroot}/usr/local/lib/sparcv9
mv sparcv9/libs/* %{buildroot}/usr/local/lib/sparcv9
%endif

#conflicts with gcc
rm $RPM_BUILD_ROOT/usr/local/lib/libiberty.a

%clean
rm -rf $RPM_BUILD_ROOT

%post -n gdb
if [ -x /usr/local/bin/install-info ] ; then
	/usr/local/bin/install-info --info-dir=/usr/local/info /usr/local/info/gdb.info
	/usr/local/bin/install-info --info-dir=/usr/local/info /usr/local/info/stabs.info
	/usr/local/bin/install-info --info-dir=/usr/local/info /usr/local/info/gdbint.info
fi

%post -n bfdlibs
if [ -x /usr/local/bin/install-info ] ; then
	/usr/local/bin/install-info --info-dir=/usr/local/info /usr/local/info/bfd.info
fi


%preun -n gdb
if [ -x /usr/local/bin/install-info ] ; then
	/usr/local/bin/install-info --delete --info-dir=/usr/local/info \
		/usr/local/info/gdb.info
	/usr/local/bin/install-info --delete --info-dir=/usr/local/info \
		/usr/local/info/stabs.info
	/usr/local/bin/install-info --delete --info-dir=/usr/local/info \
		/usr/local/info/gdbint.info
fi

%preun -n bfdlibs
if [ -x /usr/local/bin/install-info ] ; then
	/usr/local/bin/install-info --delete --info-dir=/usr/local/info \
		/usr/local/info/bfd.info
fi

%post -n gnu-standards
if [ -x /usr/local/bin/install-info ] ; then
	/usr/local/bin/install-info --info-dir=/usr/local/info /usr/local/info/standards.info
fi

%preun -n gnu-standards
if [ -x /usr/local/bin/install-info ] ; then
	/usr/local/bin/install-info --delete --info-dir=/usr/local/info \ 
		/usr/local/info/standards.info
fi

%files
%defattr(-, root, root)
%doc COPYING gdb/doc/refcard.tex COPYING.LIB README
%ifarch sparc64
/usr/local/bin/sparcv9/gdb
%endif
/usr/local/bin/gdb
/usr/local/bin/gdbtui
/usr/local/man/man1/gdb.1
/usr/local/man/man1/gdbtui.1
#/usr/local/info/mmalloc.info
/usr/local/info/annotate.*
/usr/local/info/configure.*
/usr/local/info/gdb.*
/usr/local/info/gdbint.*
/usr/local/info/stabs.*
#/usr/local/info/dir
/usr/local/share/*

%files -n bfdlibs
%defattr(-, root, root)
%ifarch sparc64
/usr/local/lib/sparcv9/*
%endif
/usr/local/lib/*a
/usr/local/info/bfd.*
/usr/local/include/*

%files -n gnu-standards
%defattr(-, root, root)
/usr/local/info/standards.info
