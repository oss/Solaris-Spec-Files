Summary:	PEAR package for RSS parsing
Name:		pear-XML_RSS
Version:	0.9.10
Release:	1
License:	PHP
Group:		Development/Libraries
Vendor:		NBCS-OSS
Distribution:	RU-Solaris
Packager:	Brian Schubert <schubert@nbcs.rutgers.edu>
Source:		XML_RSS-%{version}.tgz
BuildRoot:	%{_tmppath}/%{name}-root
URL:		http://pear.php.net/package/XML_RSS
Requires:	pear-XML_Parser

%description
Parser for Resource Description Framework (RDF) Site Summary (RSS)
documents.

%prep
%setup -q -n XML_RSS-%{version}

%build
# Nothing to build.

%clean
rm -rf %{buildroot}

%install
%{__install} -d -m 0755 %{buildroot}%{_libdir}/php/XML
%{__install} -m 0644 RSS.php %{buildroot}%{_libdir}/php/XML

%files
%defattr(-,root,bin)
%doc tests
%{_libdir}/php/XML/RSS.php

%changelog
* Mon Sep 15 2008 Brian Schubert <schubert@nbcs.rutgers.edu> - 0.9.10-1
- Initial build.

