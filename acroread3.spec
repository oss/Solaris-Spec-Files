Summary: Adobe Acrobat Reader
Name: acroread
Version: 3.0
Release: 1
Group: Applications/Printing
License: Commerical software
Source: acroread-3.tar.gz
BuildRoot: /var/tmp/%{name}-root

%description
Acroread is a PDF viewer.

%prep
%setup -q -n files

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}
find . | cpio -pdmuv %{buildroot}
mv %{buildroot}/usr/local/bin/acroread %{buildroot}/usr/local/bin/acroread3

%clean
rm -rf %{buildroot}

%files
%defattr(-, root, bin)
/usr/local/bin/acroread3
/opt/Acrobat3
