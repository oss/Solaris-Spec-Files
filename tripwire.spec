Name: tripwire
Version: 1.3.1
Release: 2
Summary: Tripwire is a security tool
Group: System Environment/Base
Copyright: Rutgers
Source: Tripwire-1.3.1-1.rutgers.tar.gz
BuildRoot: /var/tmp/%{name}-root

%description
From the README:

    Tripwire is a file and directory integrity checker, a utility that
compares a designated set of files and directories against information
stored in a previously generated database.  Any differences are
flagged and logged, including added or deleted entries.  When run
against system files on a regular basis, any changes in critical
system files will be spotted -- and appropriate damage control
measures can be taken immediately.  With Tripwire, system
administrators can conclude with a high degree of certainty that a
given set of files remain free of unauthorized modifications if
Tripwire reports no changes.

%prep
%setup -q -n tw_ASR_1.3.1_src

%build
make clean
make

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/var/adm/tcheck
mkdir -p $RPM_BUILD_ROOT/usr/local/sbin
cp src/tripwire $RPM_BUILD_ROOT/usr/local/sbin
cp src/siggen $RPM_BUILD_ROOT/usr/local/sbin
cp $RPM_SOURCE_DIR/tw.conf.example $RPM_BUILD_ROOT/var/adm/tcheck

%clean
rm -rf $RPM_BUILD_ROOT

%files
%attr(400, bin, bin) /var/adm/tcheck/tw.conf.example
%attr(500, bin, bin) /usr/local/sbin/tripwire
%attr(500, bin, bin) /usr/local/sbin/siggen

