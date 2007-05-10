%define name gdb
%define version 6.6
%define release 1
%include machine-header.spec

Name:		%{name}
Version:	%{version}
Release:	%{release}
License:	GPL
Group:		Development/Debuggers
Source:		%{name}-%{version}.tar.gz
Summary:	GNU debugger
BuildRoot:	%{_tmppath}/%{name}-root
Conflicts:	vpkg-SFWgdb
BuildRequires:	texinfo

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
Version:	%{version}
License:	GPL
Group:		Documentation
Summary:	The GNU coding standards
BuildRequires:	texinfo
Requires:	info

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
Version:	%{version}
License:	GPL
Group:		Development/Libraries
Requires:	gcc
Summary:	Binary file descriptor libraries and headers

%description -n bfdlibs
Bfdlibs contains the binary file descriptor libraries and headers; you
only need them if you are building programs with them.

%prep
%setup -q

%build
rm -rf %{buildroot}

PATH="/usr/local/bin:/usr/local/gnu/bin:${PATH}" \
CPPFLAGS="-I/usr/local/include" \
LDFLAGS="-L/usr/local/lib -R/usr/local/lib" \
CC="gcc"
export PATH CPPFLAGS LDFLAGS CC

./configure \
	--prefix=/usr/local \
	--enable-libada \
	--enable-libssp

gmake
gmake info

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/local
gmake install prefix=%{buildroot}/usr/local 
gmake install-info prefix=%{buildroot}/usr/local

#conflicts with gcc
#rm $RPM_BUILD_ROOT/usr/local/lib/libiberty.a

%clean
rm -rf %{buildroot}

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
/usr/local/bin/gdb
/usr/local/bin/gdbtui
/usr/local/man/man1/gdb.1
/usr/local/man/man1/gdbtui.1
/usr/local/info/dir
/usr/local/info/annotate.*
/usr/local/info/configure.*
/usr/local/info/gdb.*
/usr/local/info/gdbint.*
/usr/local/info/stabs.*
/usr/local/share/*

%files -n bfdlibs
%defattr(-, root, root)
/usr/local/lib/*a
/usr/local/info/bfd.*
/usr/local/include/*

%files -n gnu-standards
%defattr(-, root, root)
/usr/local/info/standards.info

%changelog
* Thu May 10 2007 David Lee Halik <dhalik@nbcs.rutgers.edu> - 6.6-1
- Version update.
- spec file weirdness fixing

