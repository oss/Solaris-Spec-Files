%define webbin_dir %{_prefix}/webtools/webbin

Name:		webtools_restoremail
Version:	0.3
Release:	1
Group: 		Applications/Internet
License:	Rutgers
Source:		restoremail-%{version}
BuildRoot: 	%{_tmppath}/%{name}-%{version}-%{release}-root
Requires: 	webtools, squirrelmail

Summary:        Script for restoring mail folders

%description
This is a bash script for restoring mail folders. 
It is used by the squirrelmail-webtools-plugins package. 

%install
rm -rf %{buildroot}
%{__install} -D -m0555 %{SOURCE0} %{buildroot}%{webbin_dir}/restoremail

%clean 
rm -rf %{buildroot}

%files
%defattr(-, root, www)
%{webbin_dir}/restoremail

%changelog
* Fri Jan 08 2010 Brian Schubert <schubert@nnbcs.rutgers.edu> - 0.3-1
- In version 0.3, restoremail copies messages from snapshot. 
- Rewrote essentially the entire spec file.
- Added changelog.
