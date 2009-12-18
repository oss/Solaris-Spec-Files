%{!?python_sitelib: %define python_sitelib %(python -c "from distutils.sysconfig import get_python_lib; print get_python_lib()")}

Summary: RPM installer/updater
Name: yum
Version: 3.2.25
Release: 5%{?dist}
License: GPLv2+
Group: System Environment/Base
Source0: http://yum.baseurl.org/download/3.2/%{name}-%{version}.tar.gz
Source1: yum.conf.solaris
Source2: rutgers-solaris.repo
Patch1: yum-mirror-priority.patch

URL: http://yum.baseurl.org/
#BuildArch: noarch
BuildRequires: python
BuildRequires: gettext
BuildRequires: intltool
Conflicts: pirut < 1.1.4
Requires: python >= 2.4, rpm-python, rpm >= 0:4.4.2
Requires: python-iniparse
Requires: python-sqlite
Requires: python-urlgrabber >= 3.9.0-8
Requires: yum-metadata-parser >= 1.1.0
Requires: pygpgme
Obsoletes: yum-skip-broken, yum-basearchonly
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

%description
Yum is a utility that can check for and automatically download and
install updated RPM packages. Dependencies are obtained and downloaded 
automatically prompting the user as necessary.

%package updatesd
Summary: Update notification daemon
Group: Applications/System
Requires: yum = %{version}-%{release}
Requires: dbus-python
Requires: pygobject2
Requires(preun): /sbin/chkconfig
Requires(post): /sbin/chkconfig
Requires(preun): /sbin/service
Requires(post): /sbin/service

%description updatesd
yum-updatesd provides a daemon which checks for available updates and 
can notify you when they are available via email, syslog or dbus. 

%prep
%setup -q
%patch1 -p0

# Correct directory locations
sed -i -e 's|/usr/bin|%{_bindir}|' bin/*
sed -i -e 's|make|gmake|g' -e 's|/usr/|%{_prefix}/|g' -e 's|/var/|%{_var}/|g' Makefile 
sed -i -e 's|/usr/share/man/|%{_mandir}/|g' docs/Makefile
sed -i -e 's|/etc/|%{_sysconfdir}/|g' etc/Makefile
sed -i -e 's|/usr/share|%{_datadir}|g' bin/yum.py
sed -i -e 's|/etc/|%{_sysconfdir}/|g' cli.py
sed -i -e 's|/etc/yum/yum\.conf|/etc/yum.conf|g' cli.py

sed -i -e 's|/etc/|%{_sysconfdir}/|g' yum/*
sed -i -e 's|/etc/yum/yum\.conf|/etc/yum.conf|g' yum/*
sed -i -e 's|/var/|%{_var}/|' yum/*
sed -i -e 's|\$releasever|12|' yum/config.py
sed -i -e 's|/usr/share/|%{_datadir}|' yum/*
sed -i -e 's|/usr/lib/|%{_libdir}|' yum/*

# We need a directory where everyone can write:
sed -i -e 's|/var/local/tmp|/tmp|g' yum/*

# Correct arch
sed -i -e 's|sparc64v|sun4u|g' rpmUtils/arch.py

%build
gmake %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/%{_sysconfdir}/yum/repos.d
install -pm 644 %{SOURCE2} $RPM_BUILD_ROOT/%{_sysconfdir}/yum/repos.d/
gmake INSTALL="install -p" YUMETC=$RPM_BUILD_ROOT/%{_sysconfdir}/yum/ DESTDIR=$RPM_BUILD_ROOT install
install -m 644 %{SOURCE1} $RPM_BUILD_ROOT/%{_sysconfdir}/yum.conf
mkdir -p $RPM_BUILD_ROOT/%{_sysconfdir}/yum/pluginconf.d $RPM_BUILD_ROOT/usr/local/lib/yum-plugins

# for now, move repodir/yum.conf back
mv $RPM_BUILD_ROOT/%{_sysconfdir}/yum/repos.d $RPM_BUILD_ROOT/%{_sysconfdir}/yum.repos.d
rm -f $RPM_BUILD_ROOT/%{_sysconfdir}/yum/yum.conf

# yum-updatesd has moved to the separate source version
rm -f $RPM_BUILD_ROOT/%{_sysconfdir}/yum/yum-updatesd.conf 
rm -f $RPM_BUILD_ROOT/%{_sysconfdir}/rc.d/init.d/yum-updatesd
rm -f $RPM_BUILD_ROOT/%{_sysconfdir}/dbus-1/system.d/yum-updatesd.conf
rm -f $RPM_BUILD_ROOT/%{_sbindir}/yum-updatesd
rm -f $RPM_BUILD_ROOT/%{_mandir}/man*/yum-updatesd*
rm -f $RPM_BUILD_ROOT/%{_datadir}/yum-cli/yumupd.py*

%find_lang %name

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(-, root, root, -)
%doc README AUTHORS COPYING TODO INSTALL ChangeLog
%config(noreplace) %{_sysconfdir}/yum.conf
%dir %{_sysconfdir}/yum
%config(noreplace) %{_sysconfdir}/yum/version-groups.conf
%dir %{_sysconfdir}/yum.repos.d
%{_sysconfdir}/yum.repos.d/*
%config(noreplace) %{_sysconfdir}/logrotate.d/yum
%dir %{_datadir}/yum-cli
%{_datadir}/yum-cli/*
%{_bindir}/yum
%{python_sitelib}/yum
%{python_sitelib}/rpmUtils
%dir /var/local/cache/yum
%dir /var/local/lib/yum
%{_mandir}/man*/yum.*
%{_mandir}/man*/yum-shell*
# plugin stuff
%dir %{_sysconfdir}/yum/pluginconf.d 
%dir /usr/local/lib/yum-plugins

%changelog
* Fri Dec 11 2009 Orcan Ogetbil <orcan at fedoraproject.org> - 3.2.25-5
- Fix Permission denied to write to '/var/local/tmp/' issue

* Wed Dec 09 2009 Orcan Ogetbil <orcan at fedoraproject.org> - 3.2.25-4
- Add .repo file for real this time

* Wed Dec 09 2009 Orcan Ogetbil <orcan at fedoraproject.org> - 3.2.25-3
- Add .repo file with OSS configuration

* Fri Nov 06 2009 Orcan Ogetbil <orcan at fedoraproject.org> - 3.2.25-2
- Solaris port

* Wed Oct 14 2009 Seth Vidal <skvidal at fedoraproject.org> - 3.2.25-1
- 3.2.25

* Wed Sep 30 2009 Seth Vidal <skvidal at fedoraproject.org> - 3.2.24-9
- revert yum. import patch b/c it breaks a bunch of things

* Wed Sep 30 2009 Seth Vidal <skvidal at fedoraproject.org> - 3.2.24-8
- fix up broken build b/c of version-groups.conf file

* Tue Sep 29 2009 Seth Vidal <skvidal at fedoraproject.org> - 3.2.24-7
- fixes for odd outputs from ts.run and logs for what we store in history

* Wed Sep 23 2009 Seth Vidal <skvidal at fedoraproject.org> - 3.2.24-6
- new head patch - fixes some issues with history and chroots

* Mon Sep 21 2009 Seth Vidal <skvidal at fedoraproject.org> - 3.2.24-5
- latest head patch - includes yum history feature.

* Tue Sep 15 2009 Seth Vidal <skvidal at fedoraproject.org> - 3.2.24-4
- new head patch - translation updates and a few bug fixes

* Wed Sep  9 2009 Seth Vidal <skvidal at fedoraproject.org> - 3.2.24-3
- add geode arch patch for https://bugzilla.redhat.com/show_bug.cgi?id=518415


* Thu Sep  3 2009 Seth Vidal <skvidal at fedoraproject.org> - 3.2.24-2
- modify cachedir to include variables

* Thu Sep  3 2009 Seth Vidal <skvidal at fedoraproject.org> - 3.2.24-1
- 3.2.24

* Wed Sep  2 2009 Seth Vidal <skvidal at fedoraproject.org> - 3.2.23-16
- fix globbing issue 520810

* Mon Aug 31 2009 Seth Vidal <skvidal at fedoraproject.org> - 3.2.23-15
- one more head update - fixes some fairly ugly but kind of minor bugs

* Tue Aug 18 2009 Seth Vidal <skvidal at fedoraproject.org> - 3.2.23-14
- update to latest head pre 3.2.24
- add requirement on python-urlgrabber 3.9.0 and up

* Wed Aug  5 2009 Seth Vidal <skvidal at fedoraproject.org> - 3.2.23-13
- latest head - right after freeze

* Tue Aug  4 2009 Seth Vidal <skvidal at fedoraproject.org> - 3.2.23-12
- latest head - right before freeze :)

* Mon Jul 27 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.2.23-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Jul 22 2009 Seth Vidal <skvidal at fedoraproject.org> - 3.2.23-10
- remove exactarchlist by request for rawhide

* Thu Jul  2 2009 Seth Vidal <skvidal at fedoraproject.org> - 3.2.23-9
- update to latest head - make livecd creation work again in rawhide
- disable one of the man page patches until after 3.2.24 is released b/c
  of the changes to the man page in the head patch


* Mon Jun 22 2009 James Antill <james at fedoraproject.org> - 3.2.23-8
- Update to latest head:
- Fix old recursion bug, found by new code.
- Resolves: bug#507220

* Sun Jun 21 2009 James Antill <james at fedoraproject.org> - 3.2.23-6
- Update to latest head:
- Unbreak delPackage() excludes.
- Other fixes/etc.

* Fri Jun 19 2009 James Antill <james at fedoraproject.org> - 3.2.23-5
- Actually apply the HEAD patch included yesterday :).

* Thu Jun 18 2009 Seth Vidal <skvidal at fedoraproject.org> - 3.2.23-4
- update to latest head

* Mon Jun  8 2009 Seth Vidal <skvidal at fedoraproject.org>
- truncate changelog

* Wed May 20 2009 Seth Vidal <skvidal at fedoraproject.org> - 3.2.23-2
- add patch to close rpmdb completely

* Tue May 19 2009 Seth Vidal <skvidal at fedoraproject.org> - 3.2.23-1
- 3.2.23

* Mon May 11 2009 Seth Vidal <skvidal at fedoraproject.org> - 3.2.22-5
- jump up to almost 3.2.23. 
- had to move patch0 around a bit until we rebase to 3.2.23

* Thu Apr  9 2009 James Antill <james at fedoraproject.org> - 3.2.22-4
- fix typo for yum-complete-transaction message.

* Wed Apr  8 2009 Seth Vidal <skvidal at fedoraproject.org> - 3.2.22-3
- fix for file:// urls which makes things in pungi/mash work

* Tue Apr  7 2009 Seth Vidal <skvidal at fedoraproject.org> - 3.2.22-2
- yum-HEAD minus the yumdb patches

* Tue Mar 24 2009 Seth Vidal <skvidal at fedoraproject.org> - 3.2.22-1
- 3.2.22 - 3 patches beyond 3.2.21-16

* Mon Mar 16 2009 Seth Vidal <skvidal at fedoraproject.org> - 3.2.21-16
- fix for 490490

* Fri Mar 13 2009 Seth Vidal <skvidal at fedoraproject.org> - 3.2.21-15
- update to upstream git to fix conditionals problem on anaconda installs

* Thu Mar 12 2009 Seth Vidal <skvidal at fedoraproject.org> - 3.2.21-14
- latest HEAD

* Tue Mar 10 2009 Seth Vidal <skvidal at fedoraproject.org> - 3.2.21-13
- f11beta build

* Wed Mar  4 2009 Seth Vidal <skvidal at fedoraproject.org> - 3.2.21-12
- second verse, same as the first

* Fri Feb 27 2009 Seth Vidal <skvidal at fedoraproject.org> - 3.2.21-10
- merge up a lot of fixes from latest HEAD

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.2.21-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Tue Feb 10 2009 Seth Vidal <skvidal at fedoraproject.org> - 3.2.21-9
- merge up to latest yum head - sort of a pre 3.2.22

* Wed Feb  4 2009 Seth Vidal <skvidal at fedoraproject.org> - 3.2.21-8
- fix for YumHeaderPackages so it plays nicely w/createrepo and mergerepo, etc

* Thu Jan 29 2009 Seth Vidal <skvidal at fedoraproject.org> - 3.2.21-7
- update HEAD patch to fix repodiff (and EVR comparisons in certain cases)

* Tue Jan 27 2009 Seth Vidal <skvidal at fedoraproject.org> - 3.2.21-6
- patch to keep anaconda (and other callers) happy
- remove old 6hr patch which is now upstream

* Mon Jan 26 2009 Seth Vidal <skvidal at fedoraproject.org> - 3.2.21-4
- patch to latest HEAD to test a number of fixes for alpha

* Tue Jan 20 2009 Seth Vidal <skvidal at fedoraproject.org> - 3.2.21-3
- add a small patch to make things play a bit nicer with the logging module
  in 2.6


* Wed Jan  7 2009 Seth Vidal <skvidal at fedoraproject.org> - 3.2.21-1
- bump to 3.2.21

* Thu Dec 18 2008 James Antill <james@fedoraproject.org> - 3.2.20-8
- merge latest from upstream
- move to 6hr metadata

* Mon Dec  8 2008 Seth Vidal <skvidal at fedoraproject.org> - 3.2.20-7
- merge patch from upstream and remove now old obsoletes patch

* Thu Dec 04 2008 Jesse Keating <jkeating@redhat.com> - 3.2.20-6
- Add patch from upstream to fix cases where obsoletes are disabled. (jantill)

* Sat Nov 29 2008 Ignacio Vazquez-Abrams <ivazqueznet+rpm@gmail.com> - 3.2.20-5
- Rebuild for Python 2.6

* Wed Nov 26 2008 Seth Vidal <skvidal at fedoraproject.org> - 3.2.20-4
- update head patch

* Wed Oct 29 2008 Seth Vidal <skvidal at fedoraproject.org> - 3.2.20-3
- full patch against HEAD for skipbroken fixes (among others)

* Mon Oct 27 2008 James Antill <james@fedoraproject.org> - 3.2.20-2
- Fix listTransaction for skipped packages.

* Mon Oct 27 2008 Seth Vidal <skvidal at fedoraproject.org> - 3.2.20-1
- 3.2.20

* Thu Oct 23 2008 Seth Vidal <skvidal at fedoraproject.org> - 3.2.19-6
- update HEAD patch

* Wed Oct 15 2008 Seth Vidal <skvidal at fedoraproject.org> - 3.2.19-5
- rebase against 3.2.X HEAD

* Tue Oct 14 2008 Seth Vidal <skvidal at fedoraproject.org> - 3.2.19-4
- pull patch from git to bring us up to current(ish)

* Wed Sep  3 2008 Seth Vidal <skvidal at fedoraproject.org> - 3.2.19-3
- add patch to fix yum install name.arch matching

* Thu Aug 28 2008 Seth Vidal <skvidal at fedoraproject.org> - 3.2.19-2
- add patch to fix mash's parser use.

* Wed Aug 27 2008 Seth Vidal <skvidal at fedoraproject.org> - 3.2.19-1
- 3.2.19

* Thu Aug  7 2008 Seth Vidal <skvidal at fedoraproject.org> - 3.2.18-1
- 3.2.18

* Wed Jul 10 2008 Seth Vidal <skvidal@fedoraproject.org> - 3.2.17-2
- add patch from upstream for bug in compare_providers

* Wed Jul  9 2008 Seth Vidal <skvidal@fedoraproject.org> - 3.2.17-1
- 3.2.17

* Tue Jun 24 2008 Jesse Keating <jkeating@redhat.com> - 3.2.16-4
- Add a couple more upstream patches for even more multilib fixes

* Tue Jun 24 2008 Jesse Keating <jkeating@redhat.com> - 3.2.16-3
- Add another patch from upstream for multilib policy and noarch

* Sun May 18 2008 Seth Vidal <skvidal at fedoraproject.org> 3.2.16-2
- stupid, stupid, stupid


* Fri May 16 2008 Seth Vidal <skvidal at fedoraproject.org> 3.2.16-1
- 3.2.16

* Tue Apr 15 2008 Seth Vidal <skvidal at fedoraproject.org> 3.2.14-9
- nine is the luckiest number that there will ever be

* Tue Apr 15 2008 Seth Vidal <skvidal at fedoraproject.org> 3.2.14-8
- after many tries - this one fixes translations AND pungi

* Thu Apr 10 2008 Seth Vidal <skvidal at fedoraproject.org> 3.2.14-5
- once more, with feeling

* Thu Apr 10 2008 Seth Vidal <skvidal at fedoraproject.org> 3.2.14-4
- another big-head-patch

* Wed Apr  9 2008 Seth Vidal <skvidal at fedoraproject.org> 3.2.14-3
- apply patch to bring this up to where HEAD is now.

* Tue Apr  8 2008 Seth Vidal <skvidal at fedoraproject.org> 3.2.14-1
- remove committed patch
- obsoletes yum-basearchonly

* Tue Apr  1 2008 Seth Vidal <skvidal at fedoraproject.org> 3.2.13-2
- fix minor typo in comps.py for jkeating

* Thu Mar 20 2008 Seth Vidal <skvidal at fedoraproject.org> 3.2.13-1
- 3.2.13

* Mon Mar 17 2008 Seth Vidal <skvidal at fedoraproject.org> 3.2.12-5
- update manpage patch to close bug 437703. Thakns to Kulbir Saini for the patch


* Fri Mar 14 2008 Seth Vidal <skvidal at fedoraproject.org> 3.2.12-4
- multilib_policy=best is  now the default

* Thu Mar 13 2008 Seth Vidal <skvidal at fedoraproject.org> 
- add jeff sheltren's patch to close rh bug 428825

* Tue Mar  4 2008 Seth Vidal <skvidal at fedoraproject.org> 3.2.12-3
- set failovermethod to 'priority' to make jkeating happy

* Tue Mar  4 2008 Seth Vidal <skvidal at fedoraproject.org> 3.2.12-2
- fix mutually obsoleting providers (like glibc!)

* Mon Mar  3 2008 Seth Vidal <skvidal at fedoraproject.org> - 3.2.12-1
- 3.2.12

* Fri Feb  8 2008 Seth Vidal <skvidal at fedoraproject.org> - 3.2.11-1
- 3.2.11

* Sun Jan 27 2008 James Bowes <jbowes@redhat.com> 3.2.10-3
- Remove yumupd.py

* Fri Jan 25 2008 Seth Vidal <skvidal at fedoraproject.org> - 3.2.10-1
- 3.2.10
- add pygpgme dep

