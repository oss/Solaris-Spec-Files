Name: openjade
Version: 1.3.2
Release: 0
Summary: OpenJade DSSSL Processer
Source: openjade-%{version}.tar.gz
Copyright: Other
Group: Applications/XML
BuildRoot: /var/tmp/%{name}-root

%description
Jade is James Clark's implementation of DSSSL -- Document Style Semantics and Specification Language -- an ISO standard for formatting SGML (and XML) documents.

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
