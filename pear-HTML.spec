Summary: PEAR: HTML meta-package
Name: pear-HTML
Version: 1.0
Release: 1
License: PHP License
Group: Development/Libraries
BuildRoot: %{_tmppath}/%{name}-root
URL: http://pear.php.net/
Prefix: %{_prefix}
Requires: pear-HTML_Common pear-HTML_Quickform


%description
pear-HTML a meta-package for PEAR packages HTML_Common and HTML_Quickform.
This facilitates easy installation of PEAR HTML packages.

%prep

%build

%clean
[ -n "%{buildroot}" -a "%{buildroot}" != / ] && rm -rf %{buildroot}

%install

%files

