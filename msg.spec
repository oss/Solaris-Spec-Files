Summary: Shell script to read system announcements newsgroup
Name: msg
Version: 1.0
Release: 2
Group: System Environment/Base
Copyright: Rutgers
Source: msg-%{version}.tar.gz
BuildRoot: /var/tmp/%{name}-root
Requires: inews
Requires: nn

%description
msg is a shell script used to read the system announcements newsgroup.

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

