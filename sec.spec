%include perl-header.spec

%define _mandir /usr/local/man
%define _bindir /usr/local/bin
%define _sharedir /usr/local/share
%define _tmppath /var/tmp

Name: sec
Summary: Simple Event Correlator
Version: 2.3.1
Release: 2
Group: Utilities/System
License: GPL
URL: http://www.estpak.ee/~risto/sec/
Vendor: NBCS-OSS
Packager: Eric Rivas <kc2hmv@nbcs.rutgers.edu>
Source0: %{name}-%{version}.tar.gz
Requires: perl >= 5.005
BuildRoot: %{_tmppath}/%{name}-root

%description
SEC is an event correlation tool. SEC accepts input from regular files, named pipes, and standard input, and can thus be employed as an event correlator for any application that is able to write its output events to a file stream.

%prep
%setup

%build
%if %{which_perl} == "REPOSITORY"
mv sec.pl sec.pl.orig
mv convert.pl convert.pl.orig
sed '1s,#!/usr/bin/perl,#!/usr/local/bin/perl,' sec.pl.orig > sec.pl
sed '1s,#!/usr/bin/perl,#!/usr/local/bin/perl,' convert.pl.orig > convert.pl
rm sec.pl.orig convert.pl.orig
%endif

mv sec.pl.man sec.pl.1
rm itostream.c  # We don't want this file (see below also)

%install
rm -rf ${RPM_BUILD_ROOT}
mkdir -p ${RPM_BUILD_ROOT}
mkdir -p ${RPM_BUILD_ROOT}%{_bindir}
mkdir -p ${RPM_BUILD_ROOT}%{_sharedir}/sec
mkdir -p ${RPM_BUILD_ROOT}%{_mandir}/man1

install -m 0755 sec.pl ${RPM_BUILD_ROOT}%{_bindir}
install -m 0755 convert.pl ${RPM_BUILD_ROOT}%{_sharedir}/sec
# We don't want this file  (see above also)
#install -m 0644 itostream.c ${RPM_BUILD_ROOT}%{_sharedir}/sec
install -m 0644 sec.startup ${RPM_BUILD_ROOT}%{_sharedir}/sec
install -m 0644 sec.pl.1 ${RPM_BUILD_ROOT}%{_mandir}/man1

%files
%defattr(-,root,root)
%doc COPYING ChangeLog README
%attr(0755,root,root) %{_bindir}/sec.pl
%attr(0755,root,root) %dir %{_sharedir}/sec
%attr(0755,root,root) %{_sharedir}/sec/convert.pl
#%attr(0644,root,root) %{_sharedir}/sec/itostream.c
%attr(0644,root,root) %{_sharedir}/sec/sec.startup
%attr(0644,root,root) %{_mandir}/man1/sec.pl.1

%clean
rm -rf $RPM_BUILD_ROOT

%changelog
* Wed Jun 29 2005 Eric Rivas <kc2hmv@nbcs.rutgers.edu>
 - Initial Package, version 2.3.1
