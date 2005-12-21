Summary: PEAR: The add-on to HTML_QuickForm package that allows building of multipage forms
Name: pear-HTML_QuickForm_Controller
Version: 1.0.5
Release: 1
License: PHP License
Group: Development/Libraries
Source: HTML_QuickForm_Controller-%{version}.tgz
BuildRoot: %{_tmppath}/%{name}-root
URL: http://pear.php.net/
Prefix: %{_prefix}
Requires: pear-HTML_QuickForm


%description
The package is essentially an implementation of a PageController pattern.

Architecture:
* Controller class that examines HTTP requests and manages form values
persistence across requests.
* Page class (subclass of QuickForm) representing a single page of the form.
* Business logic is contained in subclasses of Action class.

Cool features:
* Includes several default Actions that allow easy building of multipage forms.
* Includes usage examples for common usage cases (single-page form, wizard,
tabbed form).

%prep
%setup -q -n HTML_QuickForm_Controller-%{version}

%build
mkdir -p %{buildroot}/usr/local/lib/php/HTML/QuickForm
mkdir -p %{buildroot}/usr/local/lib/php/doc/HTML_QuickForm_Controller

%clean
[ -n "%{buildroot}" -a "%{buildroot}" != / ] && rm -rf %{buildroot}

%install
cp *.php %{buildroot}/usr/local/lib/php/HTML/QuickForm
cp -r Action/ %{buildroot}/usr/local/lib/php/HTML/QuickForm
cp -r examples/ %{buildroot}/usr/local/lib/php/doc/HTML_QuickForm_Controller

%files
%defattr(-,root,bin)
%dir /usr/local/lib/php/doc/HTML_QuickForm_Controller
%dir /usr/local/lib/php/HTML/QuickForm/Action/
/usr/local/lib/php/HTML/QuickForm/*.php
/usr/local/lib/php/doc/HTML_QuickForm_Controller/*
/usr/local/lib/php/HTML/QuickForm/Action/*.php

