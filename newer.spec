Summary: Compares last-modified date of files
Name: newer
Version: 1.0
Release: 2
Group: System Environment/Base
Copyright: Rutgers
Source: newer.tar.gz
BuildRoot: /var/tmp/%{name}-root
Requires: perl

%description
Newer will exit with a status equal to the number of files that are
newer than the first file listed.  If any files are not found a
negative number is returned.

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
/usr/local/bin/newer
/usr/local/man/man1/newer.1
