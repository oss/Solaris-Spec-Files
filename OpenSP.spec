Name: OpenSP
Summary: OpenSP
Version: 1.5
Release: 6
Source: OpenSP-%{version}.tar.gz
Copyright: Other
Group: Applications/XML
BuildRoot: /var/tmp/%{name}-root

%description
OpenSP

%prep
%setup -q

%build
./configure --prefix=/usr/local --exec-prefix=/usr/local --with-libxml-libs-prefix=/usr/local/lib/ 
make

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/local
make install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
/usr/local/bin
/usr/local/bin/onsgmls
/usr/local/bin/osgmlnorm
/usr/local/bin/ospam
/usr/local/bin/ospcat
/usr/local/bin/ospent
/usr/local/bin/osx
/usr/local/doc
/usr/local/doc/OpenSP/*
/usr/local/include
/usr/local/include/OpenSP/*
/usr/local/lib/libosp.a
/usr/local/lib/libosp.la
/usr/local/lib/libosp.so
/usr/local/lib/libosp.so.3
/usr/local/lib/libosp.so.3.0.0
/usr/local/man
/usr/local/man/man1
/usr/local/man/man1/onsgmls.1
/usr/local/man/man1/osgmlnorm.1
/usr/local/man/man1/ospam.1
/usr/local/man/man1/ospent.1
/usr/local/man/man1/osx.1
/usr/local/share/OpenSP/*
/usr/local/share/doc/*
