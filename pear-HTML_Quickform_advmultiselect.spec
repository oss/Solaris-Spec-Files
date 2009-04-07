Summary: Element for HTML_QuickForm that emulate a multi-select.
Name: pear-HTML_QuickForm_advmultiselect
Version: 1.5.1
Release: 1
License: PHP License
Group: Development/Libraries
Source: http://pear.php.net/get/HTML_QuickForm_advmultiselect-%{version}.tgz
BuildRoot: %{_tmppath}/%{name}-root
URL: http://pear.php.net/
Packager:      Dave Diffenbaugh <davediff@nbcs.rutgers.edu>
Prefix: %{_prefix}
Requires: pear-HTML_QuickForm >= 3.2.10 pear-HTML_Common >= 1.2.5

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
cp *.js %{buildroot}/usr/local/lib/php/HTML/QuickForm
cp -r examples/ %{buildroot}/usr/local/lib/php/HTML/QuickForm

%files
%defattr(-,root,bin)
%doc
/usr/local/lib/php/HTML/QuickForm/*


%changelog
* Tue Apr 7 2009 David Diffenbaugh <davediff@nbcs.rutgers.edu> - 1.5.1
- updated to 1.5.1
* Fri Apr 11 2008 Kevin Mulvey <kmulvey at nbcs dot rutgers dot edu> - 1.4.0-1
- Updated to 1.4
