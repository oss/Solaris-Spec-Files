Summary: Replacement NDC for Sun BIND
Name: bind-dns-replacement-ndc
Version: 1.0
Release: 1
Group: System Environment/Base
Copyright: Rutgers
Source: bind-dns-SUNtools-%{version}.tar.gz
BuildRoot: /var/tmp/%{name}-root

%description
This package is a replacement ndc for Sun's bind.

%prep
%setup -q -n files

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}
find . -print | cpio -pdm %{buildroot}

echo "%defattr(-, root, bin)" >RPM_FILE_LIST
find . -type f -print | grep -v RPM_FILE_LIST | sed 's/^\.//' >>RPM_FILE_LIST

%clean
rm -rf %{buildroot}

%files -f RPM_FILE_LIST
