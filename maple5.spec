Summary: Commercial math software
Name: maple
Version: 5.0
Release: 1
Group: Licensed
Copyright: Licensed
Source: %{name}-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-root
BuildRequires: tar

%description
Maple is a commericial computer algebra system.

%prep
%setup -q -n files

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}
find . -print | cpio -pdmuv %{buildroot}

%post

%clean
rm -rf %{buildroot}

%files
%defattr(-, root, bin)
/usr/local/man/*/*
/usr/local/maple

