%define prefix /usr/local

Summary: 	Publish Scripts - Software to automatically publish RPM packages into repository
Name:	 	publishscripts
Version: 	1.2
Release:	1	
Group: 		System Environment/Base
Copyright: 	GPL
Packager: 	Naveen Gavini <ngavini@nbcs.rutgers.edu>
Source0: 	publishscripts-1.2-main.tar
Source1: 	publishscripts-1.2-bin.tar
Source2: 	publishscripts-1.2-vpkgs_only.tar
Source3: 	publishscripts-1.2-init.tar
Source4: 	publishscripts-1.2-doc.tar
BuildRoot: 	%{_tmppath}/%{name}-root
Requires: 	mysql >= 3, mysql < 4, php >= 4, php < 5, python, Smarty, apt-server-tools, apache >= 1, apache < 2

%description
This package deploys the rpm package publish scripts for rpm.rutgers.edu.

%prep
%setup -q -n publish

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

cp -R  * $RPM_BUILD_ROOT%{prefix}/bin/publish/

tar -xf %{SOURCE4}
tar -xf %{SOURCE2}
cd vpkgs_only
cp -R * $RPM_BUILD_ROOT/var/local/lib/vpkgs_only/
cd ..
mkdir bin
cd bin
tar -xf %{SOURCE1}
cp -R *.sh $RPM_BUILD_ROOT%{prefix}/bin/
cd ..
mkdir init
cd init
tar -xf %{SOURCE3}
cp -R * $RPM_BUILD_ROOT/etc/init.d/

%post
cat << EOF
The README is located in /usr/local/doc/publishscripts-1.1
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
