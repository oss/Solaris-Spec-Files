Summary: PEAR: Provides methods for processing HTML forms.
Name: pear-HTML
Version: 3.2.5
Release: 1
License: PHP License
Group: Development/Libraries
Source: HTML_QuickForm-%{version}.tgz
BuildRoot: %{_tmppath}/%{name}-root
URL: http://pear.php.net/
Prefix: %{_prefix}
Requires: php-common pear-HTML_Common


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
%setup -q -n HTML_Quickform-%{version}

%build
mkdir -p %{buildroot}/usr/local/lib/php/HTML
mkdir -p %{buildroot}/usr/local/lib/php/doc/HTML_QuickForm

%clean
[ -n "%{buildroot}" -a "%{buildroot}" != / ] && rm -rf %{buildroot}

%install
cp Quickform.php %{buildroot}/usr/local/lib/php/HTML
cp -r Quickform/ %{buildroot}/usr/local/lib/php/HTML
cp -r docs/ %{buildroot}/usr/local/lib/php/doc/HTML_QuickForm

%files
%defattr(-,root,bin)
%dir /usr/local/lib/php/HTML/Quickform/
%dir /usr/local/lib/php/doc/HTML_QuickForm
/usr/local/lib/php/HTML/Quickform.php
/usr/local/lib/php/HTML/Quickform/*
/usr/local/lib/php/doc/HTML_QuickForm/*
