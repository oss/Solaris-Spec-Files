Summary:	Commonly used Rutgers utilities
Name:		sos-utils
Version:	1.3
Release:	1
Group:		System Environment/Base
License:	Rutgers
Source:		sos-utils-%{version}.tar.gz
BuildRoot:	/var/tmp/%{name}-root

%description
The sos-utils are fix.hme, hme-status, findg, logrotate-ru, netcheck, and namechange.

%prep
%setup -q -n files

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT
find . -print | cpio -pdm $RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%doc
%defattr(0700,root,other) 
/usr/local/sbin/fix.hme
/usr/local/sbin/hme-status
/usr/local/sbin/netcheck
/usr/local/sbin/namechange

%attr(0555,root,bin) /usr/local/sbin/findg
%attr(0755,root,other) /usr/local/sbin/logrotate-ru

%changelog
* Thu Mar 26 2009 David Diffenbaugh <davediff@nbcs.rutgers.edu> - 1.3
- added namechange 
- bump to 1.3
* Mon Feb 25 2008 David Diffenbaugh <davediff@nbcs.rutgers.edu> - 1.2
- Added logrotate-ru
- Bumped to 1.2
* Tue Aug 28 2007 David Lee Halik <dhalik@nbcs.rutgers.edu> - 1.1-1
- Added findg
- Bumped to 1.1
