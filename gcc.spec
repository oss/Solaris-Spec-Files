%include machine-header.spec

# This specfile is based on Redhat's specfile for egcs.

%define STDC_VERSION 2.10.0
%define GCC_VERSION 2.95.3

Name: gcc
Version: %{GCC_VERSION}
Release: 4
Copyright: GPL
Group: Development/Languages
Summary: The GNU C compiler
BuildRoot: /var/tmp/%{name}-root
Source: gcc-%{GCC_VERSION}.tar.gz
Provides: libstdc++.so.%{STDC_VERSION} libstdc++.so
BuildRequires: texinfo
Conflicts: vpkg-SFWgcc

%description
This package contains the entire gcc distribution -- it includes gcc,
g++, g77, gcj, chill, cpp, and libstdc++.

%package cpp
Version: %{GCC_VERSION}
Release: 1
Copyright: GPL
Group: Development/Languages
Summary: The GNU C preprocessor
BuildRoot: /var/tmp/%{name}-root

%description cpp
This package only contains cpp.  You don't need to install this if you
install gcc.

%package -n libstdc++
Version: %{STDC_VERSION}
Release: 7
Copyright: GPL
Group: Development/Languages
Summary: GNU libstdc++
Provides: libstdc++.so.%{STDC_VERSION} libstdc++.so

%description -n libstdc++ 
This package contains just the libstdc++ libraries.  You don't need to
install this if you install gcc.

%prep
%setup -q

%build
rm -rf obj-sparc-solaris
mkdir obj-sparc-solaris
cd obj-sparc-solaris
../configure --prefix=/usr/local --enable-shared --enable-threads
make
make info

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/local
mkdir -p $RPM_BUILD_ROOT/usr/lib
cd obj-sparc-solaris
make install prefix=$RPM_BUILD_ROOT/usr/local
(cd %{sparc_arch}/libio && make install-info prefix=$RPM_BUILD_ROOT/usr/local)
for i in libstdc++.a.%{STDC_VERSION} libstdc++.so.%{STDC_VERSION} ; do
    ln -s ../local/lib/$i $RPM_BUILD_ROOT/usr/lib/$i
done

%post
if [ -x /usr/local/bin/install-info ] ; then
    for i in gcc chill cpp iostream g77 ; do
        /usr/local/bin/install-info --info-dir=/usr/local/info \
 	     /usr/local/info/$i.info
    done
fi

%preun
if [ -x /usr/local/bin/install-info ] ; then
    for i in gcc chill cpp iostream g77 ; do
        /usr/local/bin/install-info --delete --info-dir=/usr/local/info \
	    /usr/local/info/$i.info
    done
fi

%post cpp
if [ -x /usr/local/bin/install-info ] ; then
    /usr/local/bin/install-info --info-dir=/usr/local/info \
       /usr/local/info/cpp.info
fi

%preun cpp
if [ -x /usr/local/bin/install-info ] ; then
    /usr/local/bin/install-info --delete --info-dir=/usr/local/info \
       /usr/local/info/cpp.info
fi

%clean
rm -rf $RPM_BUILD_ROOT

%files 
%defattr(-, root, bin)
%doc COPYING
/usr/local/lib/*
/usr/lib/*
/usr/local/bin/*
/usr/local/include/*
/usr/local/%{sparc_arch}/*
/usr/local/info/*
/usr/local/man/man1/*

%files -n libstdc++
%defattr(-, root, bin)
/usr/lib/libstdc++*
/usr/local/lib/libstdc++*
/usr/local/lib/gcc-lib/%{sparc_arch}/%{GCC_VERSION}/libstdc++*

%files cpp
%defattr(-, root, bin)
/usr/local/bin/cpp
/usr/local/info/cpp*
/usr/local/lib/gcc-lib/%{sparc_arch}/%{GCC_VERSION}/cpp0
/usr/local/man/man1/cccp.1
