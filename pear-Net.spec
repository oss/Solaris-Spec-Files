Summary: PEAR: NET meta-package
Name: pear-NET
Version: 1.0
Release: 1
License: PHP License
Group: Development/Libraries
BuildRoot: %{_tmppath}/%{name}-root
URL: http://pear.php.net/
Prefix: %{_prefix}
Requires: pear-Net_SMTP pear-Net_Socket


%description
pear-NET a meta-package for PEAR packages Net_SMTP and Net_Socket
This facilitates easy installation of PEAR Net packages.

%prep

%build

%clean
[ -n "%{buildroot}" -a "%{buildroot}" != / ] && rm -rf %{buildroot}

%install

%files

