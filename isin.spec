Summary:	Determines if a given user is in a given group.
Name:		isin
Version:	1.0
Release:	1
Group:		Utilities/System
Vendor:		NBCS-OSS
Distribution:	RU-Solaris
Packager:	Brian Schubert <schubert@nbcs.rutgers.edu>
License:	Rutgers
Source:		isin
BuildRoot:      %{_tmppath}/%{name}-root
Requires:	perl

%description
isin is a 15 line perl script to tell you if a given user is in a given group.                

%prep

%build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{_bindir}

%{__install} -m 0755 $RPM_SOURCE_DIR/isin %{buildroot}%{_bindir}

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,bin)
%{_bindir}/isin
%doc

%changelog
* Wed Sep 24 2008 Brian Schubert <schubert@nbcs.rutgers.edu> - 1.0-1
- Initial package build.

