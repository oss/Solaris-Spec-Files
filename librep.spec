%include machine-header.spec

Summary: librep Lisp system 
Name: librep
Version: 0.13.3
Release: 4
Group: Development/Languages
Copyright: GPL
Source: librep-%{version}.tar.gz
BuildRoot: /var/tmp/%{name}-root
Provides: librep.so.9
Provides: librep.so
Requires: gmp, gdbm
BuildRequires: gmp-devel, gdbm

%description
This is librep, a Lisp system for UNIX. It contains a Lisp interpreter,
byte-code compiler and virtual machine. Applications may use the Lisp
interpreter as an extension language, or it may be used for stand-alone
scripts.   [from README]

%package devel
Summary: librep header files
Group: Development/Languages
Requires: librep = %{version}

%description devel 
This package contains static libraries and header files for librep.

%prep
%setup -q

# As of librep 0.13.3, librep.so no longer exports rep_file_type, which 
# rep-gtk uses ...

cd src
mv librep.sym librep.sym.old
echo "rep_file_type" | cat - librep.sym.old | sort > librep.sym


%build
LDFLAGS="-L/usr/local/lib -R/usr/local/lib" \
    LD="/usr/ccs/bin/ld -L/usr/local/lib -R/usr/local/lib" ./configure \
    --with-gmp-prefix=/usr/local --with-gdbm-prefix=/usr/local \
    --without-readline --enable-static --enable-shared
make

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/local/share/aclocal
make install DESTDIR=$RPM_BUILD_ROOT
install -c -m 0644 rep.m4 $RPM_BUILD_ROOT/usr/local/share/aclocal

%clean
rm -rf $RPM_BUILD_ROOT

%post
if [ -x /usr/local/bin/install-info ] ; then
	/usr/local/bin/install-info --info-dir=/usr/local/info \
		 /usr/local/info/librep.info
fi

%preun
if [ -x /usr/local/bin/install-info ] ; then
	/usr/local/bin/install-info --delete --info-dir=/usr/local/info \
		 /usr/local/info/librep.info
fi

%files
%defattr(-,bin,bin)
%doc README COPYING
/usr/local/share/rep/%{version}
/usr/local/share/aclocal/*
/usr/local/bin/*
/usr/local/libexec/rep/%{version}/%{sparc_arch}
/usr/local/lib/lib*.so*
/usr/local/info/*info*

%files devel
%defattr(-,bin,bin)
/usr/local/libexec/rep/%{sparc_arch}/*
/usr/local/include/*
/usr/local/lib/lib*a
