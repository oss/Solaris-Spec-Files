Summary: Vacation program for use in .qmail files
Name: vacation-perl+qmail
Version: 1
Release: 2
Group: System Environment/Base
Copyright: Rutgers
Source: %{name}.tar.gz
BuildRoot: /var/tmp/%{name}-root
Requires: qmail
Requires: perl

%description
Vacation-perl+qmail is a vacation program for use in .qmail files.

%prep
%setup -q -n files

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT
find . -print | cpio -pdm $RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,bin,bin)
/usr/local/bin/vacation
/usr/bin/vacation
