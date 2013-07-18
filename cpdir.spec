Summary: Tar wrapper for copying directories
Name: cpdir
Version: 1.1
Release: 1
Group: System Environment/Base
Copyright: Rutgers
Source: cpdir.tar.gz
BuildRoot: /var/tmp/%{name}-root

%description
Recursively copy the entire contents of sourcedir into dest- dir,
creating subdirectories as necessary.  As many attri- butes of the
copied file are preserved as possible, includ- ing creation date,
owner, mode, and links.

cpdir creatively uses tar(1) to pack the source directory onto
standard output, which is piped into another invocation of tar which
unpacks standard input.

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
/usr/local/bin/cpdir
/usr/local/man/man1/cpdir.1

%changelog
* Thu Jul 18 2013 Matt Robinson <mwr54@nbcs.rutgers.edu> 1.1-1
- First Changelog entry
- Added 'g' and 'p' options
