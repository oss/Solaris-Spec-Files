Summary:	XML parsing class based on PHP's bundled expat
Name:		pear-XML_Parser
Version:	1.3.2
Release:	2	
License:	PHP
Group:		Development/Libraries
Vendor:		NBCS-OSS
Distribution:	RU-Solaris
Packager:	Naveen Gavini<schubert@nbcs.rutgers.edu>
Source:		XML_Parser-%{version}.tgz
BuildRoot:	%{_tmppath}/%{name}-root
URL:		http://pear.php.net/package/XML_Parser

%description
This is an XML parser based on PHPs built-in xml extension.

It supports two basic modes of operation: "func" and "event". In "func" mode, 
it will look for a function named after each element (xmltag_ELEMENT for start 
tags and xmltag_ELEMENT_ for end tags), and in "event" mode it uses a set of 
generic callbacks.

%prep
%setup -q -n XML_Parser-%{version}

%build
# Nothing to build.

%clean
rm -rf %{buildroot}

%install
%{__install} -d -m 0755 %{buildroot}%{_libdir}/php/XML/Parser
%{__install} -m 0644 Parser.php %{buildroot}%{_libdir}/php/XML
%{__install} -m 0644 Parser/Simple.php %{buildroot}%{_libdir}/php/XML/Parser

%files
%defattr(-,root,bin)
%doc tests examples
%{_libdir}/php/XML/Parser.php
%{_libdir}/php/XML/Parser

%changelog
* Mon Jul 27 2009 Naveen Gavini <ngavini@nbcs.rutgers.edu> - 1.3.2-1
- Fixed php requires.
* Mon Sep 15 2008 Brian Schubert <schubert@nbcs.rutgers.edu> - 1.3.0-1
- Initial build.
