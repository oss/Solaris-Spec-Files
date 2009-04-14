Summary: 	PEAR: DHTML replacement for the standard JavaScript alert window for client-side validation using the tableless renderer
Name: 		pear-HTML_QuickForm_DHTMLRulesTableless
Version: 	0.3.3
Release: 	1
License: 	New BSD
Group: 		Development/Libraries
Source: 	HTML_QuickForm_DHTMLRulesTableless-%{version}.tgz
URL: 		http://pear.php.net/package/HTML_QuickForm_DHTMLRulesTableless
Distribution:   RU-Solaris
Vendor:         NBCS-OSS
Packager:       David Diffenbaugh <davediff@nbcs.rutgers.edu>
BuildRoot: 	%{_tmppath}/%{name}-root
Prefix: 	%{_prefix}
Requires: 	pear-HTML_QuickForm_Controller >= 1.0.7 pear-HTML_QuickForm_Renderer_Tableless >= 0.6.1

%description
This is a DHTML replacement for the standard JavaScript alert window for
client-side validation of forms built with HTML_QuickForm when using the
HTML_QuickForm_Renderer_Tableless renderer.

%prep
%setup -q -n HTML_QuickForm_DHTMLRulesTableless-%{version}

%build
mkdir -p %{buildroot}/usr/local/lib/php/HTML/QuickForm
mkdir -p %{buildroot}/usr/local/lib/php/doc/HTML_QuickForm_DHTMLRulesTableless

%clean
[ -n "%{buildroot}" -a "%{buildroot}" != / ] && rm -rf %{buildroot}

%install
cp HTML/QuickForm/*.php %{buildroot}/usr/local/lib/php/HTML/QuickForm/
cp -r docs/examples %{buildroot}/usr/local/lib/php/doc/HTML_QuickForm_DHTMLRulesTableless

%files
%defattr(-,root,bin)
%doc
%dir /usr/local/lib/php/doc/HTML_QuickForm_DHTMLRulesTableless
/usr/local/lib/php/HTML/QuickForm/*
/usr/local/lib/php/doc/HTML_QuickForm_DHTMLRulesTableless/*

%changelog
* Tue Apr 7 2009 David Diffenbaugh <davediff@nbcs.rutgers.edu> - 0.3.3
- initial release
