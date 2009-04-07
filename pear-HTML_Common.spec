Summary:	PEAR: Base Class for other HTML classes
Name: 		pear-HTML_Common
Version: 	1.2.5
Release: 	1
License: 	PHP License
Group: 		Development/Libraries
Source: 	HTML_Common-%{version}.tgz
Packager: 	David Diffenbaugh <davediff@nbcs.rutgers.edu>
BuildRoot: 	%{_tmppath}/%{name}-root
URL: 		http://pear.php.net/
Prefix: 	%{_prefix}


%description
The PEAR::HTML_Common package provides methods for html code display and attributes handling.
* Methods to set, remove, update html attributes.
* Handles comments in HTML code.
* Handles layout, tabs, line endings for nicer HTML code.

%prep
%setup -q -n HTML_Common-%{version}

%build
mkdir -p %{buildroot}/usr/local/lib/php/HTML

%clean
[ -n "%{buildroot}" -a "%{buildroot}" != / ] && rm -rf %{buildroot}

%install
cp Common.php %{buildroot}/usr/local/lib/php/HTML

%files
%defattr(-,root,bin)
%doc
/usr/local/lib/php/HTML/Common.php

%changelog
* Tue Apr 7 2009 David Diffenbaugh <davediff@nbcs.rutgers.edu> - 1.2.5
- updated to 1.2.5
