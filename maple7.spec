Summary: Maple math software
Name: maple
Version: 7
Release: 1
Group: Licensed
Copyright: Licensed
Source: %{name}-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-root
BuildRequires: tar

%description
You may have to edit the scripts in /usr/local/maple7/bin to run this
software.

%prep
%setup -q -n maple7

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/local/maple7
find . -print | cpio -pdmuv %{buildroot}/usr/local/maple7

%post
cat <<EOF
You may have to edit the scripts in /usr/local/maple7/bin to run this
software.
EOF

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,bin)
/usr/local/maple7
