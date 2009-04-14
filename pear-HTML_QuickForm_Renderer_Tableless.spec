Summary: 	PEAR: Replacement tableless renderer that outputs valid XHTML. 
Name: 		pear-HTML_QuickForm_Renderer_Tableless
Version: 	0.6.1
Release: 	1
License: 	New BSD
Group: 		Development/Libraries
Source: 	HTML_QuickForm_Renderer_Tableless-%{version}.tgz
URL: 		http://pear.php.net/package/HTML_QuickForm_Renderer_Tableless
Distribution:   RU-Solaris
Vendor:         NBCS-OSS
Packager:       David Diffenbaugh <davediff@nbcs.rutgers.edu>
BuildRoot: 	%{_tmppath}/%{name}-root
Prefix: 	%{_prefix}
Requires: 	pear-HTML_QuickForm >= 3.2.10

%description
Replacement for the default renderer of HTML_QuickForm that uses only XHTML and
CSS but no table tags, and generates fully valid XHTML output.

%prep
%setup -q -n HTML_QuickForm_Renderer_Tableless-%{version}

%build
mkdir -p %{buildroot}/usr/local/lib/php/HTML/QuickForm
mkdir -p %{buildroot}/usr/local/lib/php/doc/HTML_QuickForm_Renderer_Tableless

%clean
[ -n "%{buildroot}" -a "%{buildroot}" != / ] && rm -rf %{buildroot}

%install
cp -r HTML/QuickForm/* %{buildroot}/usr/local/lib/php/HTML/QuickForm/
cp -r docs/examples %{buildroot}/usr/local/lib/php/doc/HTML_QuickForm_Renderer_Tableless
cp -r data/ %{buildroot}/usr/local/lib/php/HTML/QuickForm/
%files
%defattr(-,root,bin)
%doc
%dir /usr/local/lib/php/HTML/QuickForm/data
%dir /usr/local/lib/php/doc/HTML_QuickForm_Renderer_Tableless
%dir /usr/local/lib/php/doc/HTML_QuickForm_Renderer_Tableless/examples
/usr/local/lib/php/HTML/QuickForm/Renderer/*
/usr/local/lib/php/HTML/QuickForm/data/stylesheet.css
/usr/local/lib/php/doc/HTML_QuickForm_Renderer_Tableless/*

%changelog
* Tue Apr 7 2009 David Diffenbaugh <davediff@nbcs.rutgers.edu> - 0.6.1
- initial release
