Summary:	PEAR package for RSS parsing
Name:		pear-XML_RSS
Version:	0.9.2
Release:	1
License:	PHP
Group:		Development/Libraries
Vendor:		NBCS-OSS
Distribution:	RU-Solaris
Packager:	Brian Schubert <schubert@nbcs.rutgers.edu>
Source:		XML_RSS-%{version}.tgz
BuildRoot:	%{_tmppath}/%{name}-root
URL:		http://pear.php.net/package/XML_RSS
Requires:	php-common

%description
Parser for Resource Description Framework (RDF) Site Summary (RSS)
documents.

%prep
%setup -q -n XML_RSS-%{version}

%build
mkdir -p %{buildroot}%{_libdir}/php/XML

%clean
rm -rf %{buildroot}

%install
%{__install} RSS.php %{buildroot}%{_libdir}/php/XML

%files
%defattr(-,root,bin)
%doc tests
%{_libdir}/php/XML/RSS.php

%changelog
* Tue Sep 09 2008 Brian Schubert <schubert@nbcs.rutgers.edu> - 0.9.2-1
- Initial build.

