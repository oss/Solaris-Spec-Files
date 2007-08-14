%define prefix /usr/local

Summary: Publish Scripts - Software to automatically publish RPM packages into repository
Name: publishscripts
Version: 1.0
Release: 3
Group: System Environment/Base
Copyright: GPL
Packager: Naveen Gavini <ngavini@nbcs.rutgers.edu>
Source0: publishscripts-1.0-main.tar
Source1: publishscripts-1.0-bin.tar
Source2: publishscripts-1.0-vpkgs_only.tar
Source3: publishscripts-1.0-init.tar
Source4: publishscripts-1.0-doc.tar
BuildRoot: %{_tmppath}/%{name}-root
Requires: mysql >= 3, mysql < 4, php >= 4, php < 5, python, Smarty, apt-server-tools, apache >= 1, apache < 2
%description
This package deploys the rpm package publish scripts for rpm.rutgers.edu.

%prep

%setup -q -n publish

%build


%install
rm -rf %{buildroot}
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
The README is located in /usr/local/doc/publishscripts-1.0
There are install instructions there.
READ IT!!
EOF

%clean
rm -rf %{buildroot}

%files
%doc README
/usr/local/bin/checkrelease.sh
/usr/local/bin/publish/*
/usr/local/bin/rm_unstable_cruft.sh
/var/local/lib/vpkgs_only/*
/usr/local/bin/publish-agent.sh
/usr/local/bin/publish.sh
/etc/init.d/publish

%changelog
* Tue Aug 14 2007 Naveen Gavini <ngavini@nbcs.rutgers.edu> - 1.0-3
- Removed excess files and updated docs
* Mon Aug 06 2007 Naveen Gavini <ngavini@nbcs.rutgers.edu> - 1.0-2
- Updated email wording
* Fri Aug 03 2007 Naveen Gavini <ngavini@nbcs.rutgers.edu> - 1.0-1
- Initial build
