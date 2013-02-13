Summary: Fast anti-spam filtering by Bayesian statistical analysis
Name: bogofilter
Version: 1.2.3
Release: 2
License: GPLv2
Group: Applications/Internet
URL: http://bogofilter.sourceforge.net/
Source: http://downloads.sourceforge.net/bogofilter/bogofilter-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
Requires: db4
BuildRequires: flex db4-devel gsl-devel
BuildRequires: /usr/local/bin/iconv

%description
Bogofilter is a Bayesian spam filter.  In its normal mode of
operation, it takes an email message or other text on standard input,
does a statistical check against lists of "good" and "bad" words, and
returns a status code indicating whether or not the message is spam.
Bogofilter is designed with fast algorithms (including Berkeley DB system),
coded directly in C, and tuned for speed, so it can be used for production
by sites that process a lot of mail.

%package bogoupgrade
Summary: Upgrades bogofilter database to current version
Group: Applications/Internet
Provides: bogoupgrade
Requires: bogofilter = %{version}-%{release}

%description bogoupgrade
bogoupgrade is a command to upgrade bogofilter's databases from an old
format to the current format. Since the format of the database changes
once in a while, the utility is designed to make the upgrade easy.

bogoupgrade is in an extra package to remove the perl dependency on the
main bogofilter package.

%prep
%setup -q
iconv -f iso-8859-1 -t utf-8 \
 doc/bogofilter-faq-fr.html > doc/bogofilter-faq-fr.html.utf8
%{__mv} -f doc/bogofilter-faq-fr.html.utf8 \
 doc/bogofilter-faq-fr.html

%build
CC="gcc" CFLAGS="-I/usr/local/include/db4" \
LDFLAGS="-R/usr/local/lib -L/usr/local/lib -ldb-4" \
  ./configure --prefix=/usr/local --mandir=/usr/local/man --with-libdb-prefix=/usr/local/lib
gmake


%install
%{__rm} -rf %{buildroot}
gmake DESTDIR=%{buildroot} install

%{__mv} -f %{buildroot}%{_sysconfdir}/bogofilter.cf.example \
 %{buildroot}%{_sysconfdir}/bogofilter.cf

%{__install} -d -m0755 rpm-doc/xml/ rpm-doc/html/
%{__install} -m644 doc/*.xml rpm-doc/xml/
%{__install} -m644 doc/*.html rpm-doc/html/

%{__chmod} -x contrib/*

%clean
%{__rm} -rf %{buildroot}

%files bogoupgrade
%defattr(-, root, root, 0755)
%{_bindir}/bogoupgrade
%{_mandir}/man1/bogoupgrade*

%files
%defattr(-, root, root, 0755)
%doc AUTHORS COPYING NEWS README* RELEASE.NOTES* TODO bogofilter.cf.example
%doc doc/bogofilter-SA* doc/bogofilter-tuning.HOWTO* doc/integrating* doc/programmer/
%doc rpm-doc/html/ rpm-doc/xml/ contrib
%{_mandir}/man1/bogo*.1*
%{_mandir}/man1/bf_*.1*
%config(noreplace) %{_sysconfdir}/bogofilter.cf
%{_bindir}/bogo*
%{_bindir}/bf_*
%exclude %{_bindir}/bogoupgrade
%exclude %{_mandir}/man1/bogoupgrade*

%changelog
* Thu Feb 07 2013 Harry Stern <hcs42@nbcs.rutgers.edu> - 1.2.3-2
- Rebuild for Solaris 

* Tue Dec 04 2012 Adrian Reber <adrian@lisas.de> - 1.2.3-1
- updated to 1.2.3 (fixes #883358, CVE-2012-5468)

* Thu Jul 26 2012 Adrian Reber <adrian@lisas.de> - 1.2.2-5
- add new libdb4 include path to configure options

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Jan 12 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Aug 16 2010 Adrian Reber <adrian@lisas.de> - 1.2.2-1
- updated to 1.2.2 (fixes #611511, CVE-2010-2494)

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Mon Feb 26 2009 Adrian Reber <adrian@lisas.de> - 1.2.0-1
- updated to 1.2.0

* Mon Feb 23 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Thu Jul 10 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 1.1.7-2
- rebuild against db4-4.7
- use make DESTDIR install
- disable rpaths

* Sat May 31 2008 Adrian Reber <adrian@lisas.de> - 1.1.7-1
- updated to 1.1.7
- moved bogoupgrade to its own package to remove the perl
  dependency on bogofilter (bz #442843)

* Thu Feb 14 2008 Adrian Reber <adrian@lisas.de> - 1.1.6-2
- rebuilt for gcc43

* Thu Dec 13 2007 Adrian Reber <adrian@lisas.de> - 1.1.6-1
- updated to 1.1.6
- made rpmlint happy
- upstream confirmed that bogofilter is GPLv2

* Thu Aug 23 2007 Adrian Reber <adrian@lisas.de> - 1.1.5-2
- rebuilt
- added patch to build with new glibc

* Wed Mar 07 2007 Adrian Reber <adrian@lisas.de> - 1.1.5-1
- updated to 1.1.5

* Tue Sep 05 2006 Adrian Reber <adrian@lisas.de> - 1.0.3-1
- updated to 1.0.3

* Wed Apr 19 2006 Adrian Reber <adrian@lisas.de> - 1.0.2-1
- updated to 1.0.2

* Mon Jan 02 2006 Dries Verachtert <dries@ulyssis.org> - 1.0.1-1 - 3875/dries
- Updated to release 1.0.1.

* Fri Dec 02 2005 Dag Wieers <dag@wieers.com> - 1.0.0-1
- Updated to release 1.0.0.

* Tue Nov 22 2005 Dries Verachtert <dries@ulyssis.org> - 0.96.6-1
- Updated to release 0.96.6.

* Mon Aug 02 2004 Dag Wieers <dag@wieers.com> - 0.92.4-1
- Updated to release 0.92.4.

* Sat Apr 10 2004 Dag Wieers <dag@wieers.com> - 0.17.5-1
- Updated to release 0.17.5.

* Mon Jan 26 2004 Dag Wieers <dag@wieers.com> - 0.16.4-0
- Initial package. (using DAR)
