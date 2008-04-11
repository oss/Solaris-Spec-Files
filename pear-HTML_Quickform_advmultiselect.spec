Summary: Element for HTML_QuickForm that emulate a multi-select.
Name: pear-HTML_QuickForm_advmultiselect
Version: 1.4.0
Release: 1
License: PHP License
Group: Development/Libraries
Source: http://pear.php.net/get/HTML_QuickForm_advmultiselect-%{version}.tgz
BuildRoot: %{_tmppath}/%{name}-root
URL: http://pear.php.net/
Prefix: %{_prefix}
Requires: pear-HTML_QuickForm

%description
The HTML_QuickForm_advmultiselect package adds an element to the
HTML_QuickForm package that is two select boxes next to each other
emulating a multi-select.

%prep
%setup -q -n HTML_QuickForm_advmultiselect-%{version}

%build
mkdir -p %{buildroot}/usr/local/lib/php/HTML/QuickForm
mkdir -p %{buildroot}/usr/local/lib/php/doc/HTML_QuickForm_advmultiselect

%clean
[ -n "%{buildroot}" -a "%{buildroot}" != / ] && rm -rf %{buildroot}

%install
cp *.php %{buildroot}/usr/local/lib/php/HTML/QuickForm
cp -r docs/ %{buildroot}/usr/local/lib/php/doc/HTML_QuickForm_advmultiselect

%files
%defattr(-,root,bin)
%dir /usr/local/lib/php/doc/HTML_QuickForm_advmultiselect
/usr/local/lib/php/HTML/QuickForm/*
/usr/local/lib/php/doc/HTML_QuickForm_advmultiselect/*

