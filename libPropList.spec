Name: libPropList
Version: 0.10.1
Copyright: GPL
Group: Development/Libraries
Summary: libPropList library
Release: 3
Source: libPropList-%{version}.tar.gz
BuildRoot: /var/tmp/%{name}-root

%description
libPropList is a library used by WindowMaker.  

%prep
%setup -q

%build
./configure --prefix=/usr/local
make

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/local
make install prefix=$RPM_BUILD_ROOT/usr/local

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
/usr/local/lib/lib*.so*
/usr/local/lib/lib*a
/usr/local/include/*
