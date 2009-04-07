Summary: 	PEAR: PHP and JavaScript AJAX library
Name: 		pear-HTML_AJAX
Version: 	0.5.6
Release: 	1
License: 	LGPL
Group: 		Development/Libraries
Source: 	HTML_AJAX-%{version}.tgz
URL: 		http://pear.php.net/package/HTML_AJAX
Distribution:   RU-Solaris
Vendor:         NBCS-OSS
Packager:       David Diffenbaugh <davediff@nbcs.rutgers.edu>
BuildRoot: 	%{_tmppath}/%{name}-root
Prefix: 	%{_prefix}
Requires: 	pear-HTML_Common >= 1.2.5

%description
Provides PHP and JavaScript libraries for performing AJAX (Communication 

%prep
%setup -q -n HTML_AJAX-%{version}

%build
mkdir -p %{buildroot}/usr/local/lib/php/HTML
mkdir -p %{buildroot}/usr/local/lib/php/doc/HTML_AJAX

%clean
[ -n "%{buildroot}" -a "%{buildroot}" != / ] && rm -rf %{buildroot}

%install
cp AJAX.php %{buildroot}/usr/local/lib/php/HTML
cp -r AJAX/ %{buildroot}/usr/local/lib/php/HTML
cp -r docs/ %{buildroot}/usr/local/lib/php/doc/HTML_AJAX
cp -r js/ %{buildroot}/usr/local/lib/php/HTML/AJAX/js
cp -r examples/ %{buildroot}/usr/local/lib/php/HTML/AJAX/examples

%files
%defattr(-,root,bin)
%doc
%dir /usr/local/lib/php/HTML/AJAX/
%dir /usr/local/lib/php/doc/HTML_AJAX
/usr/local/lib/php/HTML/AJAX.php
/usr/local/lib/php/HTML/AJAX/*
/usr/local/lib/php/doc/HTML_AJAX/*

%changelog
*Tue Apr 7 2009 David Diffenbaugh <davediff@nbcs.rutgers.edu> - 0.5.6
- updated to 0.5.6
