Summary:	Rutgers check-criteria script
Name:		check-criteria
Version:	1.1
Release:	1
Group:		Utilities/System
License:	Rutgers
Vendor:		NBCS-OSS
Distribution:   RU-Solaris
Packager:	Brian Schubert <schubert@nbcs.rutgers.edu>
Source:		%{name}
Buildroot:	%{_tmppath}/%{name}-root
BuildRequires:	coreutils

%description
A shell script for file criteria checking

%prep
# No prep needed

%build
# Nothing to build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{_bindir}
%{__install} -m 0555 $RPM_SOURCE_DIR/check-criteria %{buildroot}%{_bindir}

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,other)
%doc
%{_bindir}/check-criteria

%changelog
* Thu Aug 28 2008 Brian Schubert <schubert@nbcs.rutgers.edu> - 1.1-1
- Updated to version 1.1

