Summary: Script to clean up duplicate entries in $PATH
Name: cleanpath
Version: 1
Release: 2
Group: System Environment/Base
Copyright: Rutgers
Source: cleanpath.tar.gz
BuildRoot: /var/tmp/%{name}-root

%description
Cleanpath is a script that cleans up duplicate entries in $PATH.

%prep
%setup -q -n files

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT
find . -print | cpio -pdm $RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,other)
/usr/local/man/man1/cleanpath.1
/usr/local/bin/cleanpath
