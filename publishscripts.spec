%define prefix /usr/local

Summary: 	Publish Scripts - Software to automatically publish RPM packages into repository
Name:	 	publishscripts
Version: 	1.6
Release:	3	
Group: 		System Environment/Base
License: 	GPL
Source0: 	publishscripts-%{version}.tar.bz2
BuildRoot: 	%{_tmppath}/%{name}-root
Requires: 	mysql >= 3, mysql < 4, php >= 4, php < 5, python, Smarty, apt-server-tools, apache >= 1, apache < 2
Requires:       createrepo

%description
This package deploys the rpm package publish scripts for rpm.rutgers.edu.

%prep
%setup -q -n %{name}-%{version}

%build
rm -rf %{buildroot}
PATH="/opt/SUNWspro/bin:${PATH}" \
CC="cc" CXX="CC" CPPFLAGS="-I/usr/local/include" \
CFLAGS="-D__unix__" \
LD="/usr/ccs/bin/ld" \
LDFLAGS="-L/usr/local/lib -R/usr/local/lib" \
export PATH CC CXX CPPFLAGS LD LDFLAGS CFLAGS

%install
mkdir -p $RPM_BUILD_ROOT/usr/local/bin/publish
mkdir -p $RPM_BUILD_ROOT/var/local/lib/vpkgs_only
mkdir -p $RPM_BUILD_ROOT/etc/init.d

cp -R  bin/* $RPM_BUILD_ROOT%{prefix}/bin/
cp -R vpkgs_only/ $RPM_BUILD_ROOT/var/local/lib/
cd init
cp -R * $RPM_BUILD_ROOT/etc/init.d/

%post
cat << EOF
The README is located in /usr/local/doc/publishscripts-%{version}
There are install instructions there.
READ IT!!
EOF

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc README
/usr/local/bin/checkrelease.sh
/usr/local/bin/publish/*
/usr/local/bin/rm_unstable_cruft.sh
/var/local/lib/vpkgs_only/*
/usr/local/bin/publish-agent.sh
/usr/local/bin/publish.sh
/usr/local/bin/automysqlbackup.sh
/etc/init.d/publish

%changelog
* Tue Feb 15 2011 Daiyan Alamgir <daiyan@nbcs.rutgers.edu> - 1.6.2
- pending_scan issue for locating srpms solved
- rpm name parsing issue solved
- added backup script
* Mon Dec 09 2009 Orcan Ogetbil <orcan@nbcs.rutgers.edu> - 1.6-1
- Support for yum repo update
* Wed May 27 2009 Brian Schubert <schubert@nbcs.rutgers.edu> - 1.5-2
- vpkg changes
* Wed May 13 2009 Naveen Gavini <ngavini@nbcs.rutgers.edu> - 1.5-1
- Reorganized package, fixed publish.sh issue in /usr/local/bin. 
* Fri Aug 15 2008 Brian Schubert <schubert@nbcs.rutgers.edu> - 1.4-5
- More spec file checking fixes
* Tue Aug 12 2008 Brian Schuebrt <schubert@nbcs.rutgers.edu> - 1.4-4
- Updated for new vpkgs
* Wed Aug 06 2008 Brian Schubert <schubert@nbcs.rutgers.edu> - 1.4-3
- Fixed spec file checking for cases in which multiple spec files fail.
- Added spec file checking for unstable repository.
* Thu Jul 31 2008 David Diffenbaugh <davediff@nbcs.rutgers.edu> 1.4-2
- changed from address "Testing publish scripts"  to oss@oss.rutgers.edu
- changed all email addresses to fully qualified names
* Mon Jun 30 2008 Brian Schubert <schubert@nbcs.rutgers.edu> 1.4-1
- Specific reason for spec file rejection is now indicated.
* Fri Jun 27 2008 Naveen Gavini <ngavini@nbcs.rutgers.edu> - 1.3-1
- Added spec file checking.
* Wed Apr 16 2008 Naveen Gavini <ngavini@nbcs.rutgers.edu> - 1.1-3
- Fixed publish.sh tar issue.
* Wed Jan 16 2008 Naveen Gavini <ngavini@nbcs.rutgers.edu> - 1.1-1
- Added MySQL dump script.
* Fri Oct 05 2007 Naveen Gavini <ngavini@nbcs.rutgers.edu> - 1.0-5
- Added uranium to publishscripts
* Tue Aug 14 2007 Naveen Gavini <ngavini@nbcs.rutgers.edu> - 1.0-4
- Fixed rebuild-apt script
* Tue Aug 14 2007 Naveen Gavini <ngavini@nbcs.rutgers.edu> - 1.0-3
- Removed excess files and updated docs
* Mon Aug 06 2007 Naveen Gavini <ngavini@nbcs.rutgers.edu> - 1.0-2
- Updated email wording
* Fri Aug 03 2007 Naveen Gavini <ngavini@nbcs.rutgers.edu> - 1.0-1
- Initial build
