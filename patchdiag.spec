Summary: Sun patch-checking tool
Name: patchdiag
Version: 1.0.4
Release: 1
Group: System Environment/Base
Copyright: Rutgers
Source: patchdiag-%{version}.tar.gz
BuildRoot: /var/tmp/%{name}-root

%description
Patchdiag determines the patch levels on your system against Sun's
Recommended and Security patch list.  Additionally, it operates from
input files and lists all patches that pertain to packages installed
on the system.

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
