Name: libxslt
Version: 1.0.31
Release: 0
Summary: xslt Library
Source: libxslt-%{version}.tar.gz
Copyright: GPL
Group: Librarys/XML
BuildRoot: /var/tmp/%{name}-root

%description
XSLT Library. Some XML thing.

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
/usr/local/*
