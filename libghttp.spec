Summary: GNOME http client library
Name: libghttp
Version: 1.0.8
Release: 2
Group: X11/Gnome
Copyright: LGPL
Source: libghttp-%{version}.tar.gz
BuildRoot: /var/tmp/%{name}-root

%description
Library for making HTTP 1.1 requests.

%package devel
Summary: GNOME http client development
Group: X11/gnome
Requires: libghttp

%description devel
Libraries and includes files you can use for libghttp development

%prep
%setup -q

%build
LD="/usr/ccs/bin/ld -L/usr/local/lib -R/usr/local/lib" \
     LDFLAGS="-L/usr/local/lib -R/usr/local/lib" ./configure \
     --enable-shared --enable-static
make

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/local
make install prefix=$RPM_BUILD_ROOT/usr/local

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,bin,bin)
%doc AUTHORS COPYING ChangeLog NEWS README doc/ghttp.html COPYING.LIB
/usr/local/lib/lib*.so*

%files devel
%defattr(-,bin,bin)
/usr/local/include/*
/usr/local/lib/lib*a

