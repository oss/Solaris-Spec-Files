Summary: Converts mail formats
Name: from-maildir
Version: 1.0
Release: 1ru
Copyright: BSD
Group: Applications/Editors
Source: from
Distribution: RU-Solaris
Vendor: NBCS-OSS
Packager: Robert Renaud <rrenaud@nbcs.rutgers.edu>
BuildRoot: %{_tmppath}/%{name}-root
Requires: perl-module-TimeDate

%description
Converts maildir formats.

%prep
%build

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/local/bin
cp %{_sourcedir}/from $RPM_BUILD_ROOT/usr/local/bin
%post
echo "You might want to break any other 'from' command on your system that"
echo "does not work for mail in Maildir format (ex: chmod 000 /usr/ucb/from)"

%clean
rm -rf $RPM_BUILD_ROOT

%files
%attr (755, root, other) /usr/local/bin/from



