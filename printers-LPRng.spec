Summary: Parses LPRng output
Name: printers-LPRng
Version: 1.0
Release: 2ru
Copyright: ?
Group: Applications/Printing
Source: printers
Distribution: RU-Solaris
Vendor: NBCS-OSS
Packager: Robert Renaud <rrenaud@nbcs.rutgers.edu>
BuildRoot: %{_tmppath}/%{name}-root
Requires: LPRng

%description
Parses LPRng output

%prep
%build

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/local/bin
cp %{_sourcedir}/printers $RPM_BUILD_ROOT/usr/local/bin
%post

%clean
rm -rf $RPM_BUILD_ROOT

%files
%attr (755, root, other) /usr/local/bin/printers



