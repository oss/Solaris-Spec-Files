Summary: PEAR: Provides methods for processing HTML forms.
Name: pear-HTML_QuickForm
Version: 3.2.10
Release: 1
License: PHP License
Group: Development/Libraries
Source: HTML_QuickForm-%{version}.tgz
Packager: David Diffenbaugh <davediff@nbcs.rutgers.edu>
BuildRoot: %{_tmppath}/%{name}-root
URL: http://pear.php.net/
Prefix: %{_prefix}
Requires: pear-HTML_Common >= 1.2.5


%description
The HTML_QuickForm package provides methods for dynamically create, validate and render HTML forms.

Features:
* More than 20 ready-to-use form elements.
* XHTML compliant generated code.
* Numerous mixable and extendable validation rules.
* Automatic server-side validation and filtering.
* On request javascript code generation for client-side validation.
* File uploads support.
* Total customization of form rendering.
* Support for external template engines (ITX, Sigma, Flexy, Smarty).
* Pluggable elements, rules and renderers extensions.

%prep
%setup -q -n HTML_QuickForm-%{version}

%build
mkdir -p %{buildroot}/usr/local/lib/php/HTML
mkdir -p %{buildroot}/usr/local/lib/php/doc/HTML_QuickForm

%clean
[ -n "%{buildroot}" -a "%{buildroot}" != / ] && rm -rf %{buildroot}

%install
cp QuickForm.php %{buildroot}/usr/local/lib/php/HTML
cp -r QuickForm/ %{buildroot}/usr/local/lib/php/HTML
cp -r docs/ %{buildroot}/usr/local/lib/php/doc/HTML_QuickForm

%files
%defattr(-,root,bin)
%doc
%dir /usr/local/lib/php/HTML/QuickForm/
%dir /usr/local/lib/php/doc/HTML_QuickForm
/usr/local/lib/php/HTML/QuickForm.php
/usr/local/lib/php/HTML/QuickForm/*
/usr/local/lib/php/doc/HTML_QuickForm/*

%changelog
* Tue Apr 7 2009 David Diffenbaugh <davediff@nbcs.rutgers.edu> - 3.2.10
- updated to 3.2.10
