Summary: wrapper script for Emacs tutorial
Name: teach-emacs
Version: 1.0
Release: 1
Group: System Environment/Base
Copyright: Rutgers
Source: teach-emacs-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-root

%description
Teach-emacs runs emacs and loads the TUTORIAL (which you can read in
Emacs by typing "C-h t")

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
