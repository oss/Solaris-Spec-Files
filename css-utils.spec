Summary:	Commonly used Rutgers utilities
Name:		css-utils
Version:	1.11
Release:	2
Group:		System Environment/Base
License:	Rutgers
Source:		%{name}-%{version}.tar.gz
BuildRoot:	/var/tmp/%{name}-root
Requires: 	perl-module-Quota perl
Provides: 	check-criteria
Provides:	sos-utils
Provides:	becomedata
Obsoletes: 	check-criteria
Obsoletes:	sos-utils

%description
The css-utils are fix.hme, hme-status, findg, logrotate-ru, ruquota, check-config, becomedata,  and namechange.

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
/usr/local/sbin/namechange
/usr/local/sbin/user_info
%attr(0555,root,bin) /usr/local/sbin/findg
%attr(0555,root,bin) /usr/local/sbin/becomedata
%attr(0755,root,other) /usr/local/sbin/logrotate-ru
%attr(0755,root,other) /usr/local/bin/ruquota
%attr(0755,root,other) /usr/local/bin/check-criteria

%changelog
* Thu Jun 13 2013 Matt Robinson <mwr54@nbcs.rutgers.edu> - 1.11-2
- added user_info and updated namechange
* Mon Apr 15 2013 Kaitlin Poskaitis <katiepru@nbcs.rutgers.edu> - 1.11-1
- Verify vhosts point to us and docroot exists
* Mon Aug 06 2012 Kaitlin Poskaitis <katiepru@nbcs.rutgers.edu> - 1.9-1
- Updated source
- rm read permission check for become.log so user sees failure handle the nbcs -> rci prepend of '*become' to /etc/groupadd getent output as part of -v (verbose) flag
* Thu Jun 14 2012 Kaitlin Poskaitis <katiepru@nbcs.rutgers.edu> - 1.9-1
- Updated source
- Add become.log lookup, redefine options, and handle no become data found
* Tue May 29 2012 Kaitlin Poskaitis <katiepru@nbcs.rutgers.edu> - 1.8-1
- Updated source
- Added provides sos-utils
* Mon May 21 2012 Kaitlin Poskaitis <katiepru@nbcs.rutgers.edu> -1.7-1
- Renamed to css-utils
- Removed netcheck script
- Added becomedata script
* Thu May 19 2011 Jarek Sedlacek <jarek@nbcs.rutgers.edu> - 1.6-4
- updated ruquota
* Thu May 19 2011 Jarek Sedlacek <jarek@nbcs.rutgers.edu> - 1.6-3
- updated description and added check-criteria
- added conflicts:check-criteria (check-criteria is no longer its own package)
* Thu May 05 2011 Jarek Sedlacek <jarek@nbcs.rutgers.edu> -1.6-2
- changed shebang in ruquota
* Mon Apr 25 2011 Jarek Sedlacek <jarek@nbcs.rutgers.edu - 1.6
- bumped to 1.6
* Tue Jan 12 2010 Jarek Sedlacek <jarek@nbcs.rutgers.edu> - 1.4
- bumped to version 1.4 
* Thu Mar 26 2009 David Diffenbaugh <davediff@nbcs.rutgers.edu> - 1.3
- added namechange 
- bump to 1.3
* Mon Feb 25 2008 David Diffenbaugh <davediff@nbcs.rutgers.edu> - 1.2
- Added logrotate-ru
- Bumped to 1.2
* Tue Aug 28 2007 David Lee Halik <dhalik@nbcs.rutgers.edu> - 1.1-1
- Added findg
- Bumped to 1.1
