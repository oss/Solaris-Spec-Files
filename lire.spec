Name:lire 
Version: 1.3
Release: 4
Summary: Log analyzer
Source: %{name}-%{version}.tar.gz
Copyright: GPL
Group: Applications/Logging
BuildRoot: /var/tmp/%{name}-root
Requires: docbook dockbook-dsssl docbook-xsl
%description
Loganalyzer

%prep
%setup -q

%build
#PATHTOXMLCATALOG=/usr/local/share/xml/docbook.cat
PATH="$PATH:/usr/local/perl5/bin/:/usr/perl5/5.6.1/bin/"
export PATH PATHTOXMLCATALOG
./configure --prefix=/usr/local --with-docbookdir=/usr/local/share/xml/docbook/docbook.cat
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
