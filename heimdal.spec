Summary: Heimdal, free kerberos implementation
Name: heimdal
Version: 0.5.2
Release: 2
Copyright: maybe
Group: System Enviroment/Base
Source: heimdal-%{version}.tar.gz
URL: http://www.pdc.kth.se/heimdal/
Distribution: RU-Solaris
Vendor: NBCS-OSS
Packager: Robert Renaud <rrenaud@nbcs.rutgers.edu>
BuildRoot: %{_tmppath}/%{name}-root
# FIX!!, depends on OpenSSL, doesn't build on some archs
%description
Heimdal is a free implementation of Kerberos 5.

%prep
%setup -q

%build
./configure --prefix=/usr/local --with-openssl=/usr/local/ssl CC=cc LDFLAGS="-L/usr/local/lib -R/usr/local/lib" CPPFLAGS="-I/usr/local/ssl/include"
make 

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/local
make install DESTDIR=$RPM_BUILD_ROOT

find $RPM_BUILD_ROOT -name *.la
find $RPM_BUILD_ROOT -name *.la | xargs rm -f

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
/usr/local/bin/*
/usr/local/include/*
/usr/local/info/*
/usr/local/lib/*
/usr/local/libexec/*
/usr/local/man/*
/usr/local/sbin/*




