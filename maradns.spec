Summary: An authoritative and recursive DNS server made with security in mind
Name: maradns
Version: 1.0.11
Release: 2ru
Copyright: Public domain
Group: Networking/Daemons
Source: http://www.maradns.org/download/maradns-%{version}.tar.bz2
Patch0: maradns-0.9.23.rpm.patch
#Patch1: maradns-1.0.09.tar.bz2.asc
BuildRoot: /var/tmp/%{name}-buildroot

%description
Erre con erre cigarro
Erre con erre barril
Rápido ruedan los carros
En el ferrocarril

MaraDNS is an authoritative and recursive DNS server made with 
security in mind.  More information is at http://www.maradns.org

%prep
%setup 
%patch0 -p1

%build
make 

%install
rm -fr $RPM_BUILD_ROOT/
mkdir -p $RPM_BUILD_ROOT/usr/local/etc/maradns
mkdir -p $RPM_BUILD_ROOT/usr/local/sbin
mkdir -p $RPM_BUILD_ROOT/usr/local/bin
mkdir -p $RPM_BUILD_ROOT/usr/local/man/man8
mkdir -p $RPM_BUILD_ROOT/usr/local/man/man1
mkdir -p $RPM_BUILD_ROOT/usr/local/man/man5
mkdir -p $RPM_BUILD_ROOT/etc/init.d
mkdir -p $RPM_BUILD_ROOT/var/local/log
# stupid install scripts....

cp tools/askmara tuzona/getzone $RPM_BUILD_ROOT/usr/local/bin
cp server/maradns tuzona/zoneserver $RPM_BUILD_ROOT/usr/local/sbin
cp doc/en/man/*.1 $RPM_BUILD_ROOT/usr/local/man/man1
cp doc/en/man/*.5 $RPM_BUILD_ROOT/usr/local/man/man5
cp doc/en/man/*.8 $RPM_BUILD_ROOT/usr/local/man/man8
sed "s/\/etc\/maradns/\/usr\/local\/etc\/maradns/" build/rpm.mararc > $RPM_BUILD_ROOT/usr/local/etc/maradns/mararc
cp sqa/testbed/db.example.com $RPM_BUILD_ROOT/usr/local/etc/maradns
#cp build/mara.startup $RPM_BUILD_ROOT/etc/init.d/maradns

sed "s/\/etc\/mararc/\/usr\/local\/etc\/maradns\/mararc/" build/mara.startup > mara.startup
sed "s/\/var\/log/\/var\/local\/log/" mara.startup >$RPM_BUILD_ROOT/etc/init.d/maradns 
chmod 0744 $RPM_BUILD_ROOT/etc/init.d/maradns


%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc doc/en

/usr/local/sbin/maradns
/usr/local/sbin/zoneserver
/usr/local/bin/getzone
/usr/local/bin/askmara
/usr/local/man/man8/maradns.8
/usr/local/man/man8/zoneserver.8
/usr/local/man/man1/askmara.1
/usr/local/man/man1/getzone.1
/usr/local/man/man5/csv1.5
/usr/local/man/man5/mararc.5
%config(noreplace) /etc/init.d/maradns
/var/local/log
%config(noreplace) /usr/local/etc/maradns/mararc
%config /usr/local/etc/maradns/db.example.com

%changelog
* Fri Nov 15 2002 Sam Trenholme <rpmbuild@samiam.org>
- MaraDNS rpm package updated for version 1.0.09

* Sun Oct  6 2002 Sam Trenholme <rpmbuild@samiam.org>
- MaraDNS rpm package updated for version 1.0.08

* Mon Aug 26 2002 Sam Trenholme <rpmbuild@samiam.org>
- MaraDNS rpm package updated for version 1.0.07

* Mon Jul 30 2002 Sam Trenholme <rpmbuild@samiam.org>
- MaraDNS rpm package updated for version 1.0.06

* Sat Jul 28 2002 Sam Trenholme <rpmbuild@samiam.org>
- MaraDNS rpm package updated for version 1.0.05

* Sun Jul 14 2002 Sam Trenholme <rpmbuild@samiam.org>
- MaraDNS rpm package updated for version 1.0.04

* Fri Jul 12 2002 Sam Trenholme <rpmbuild@samiam.org>
- MaraDNS rpm package updated for version 1.0.03

* Sun Jun 30 2002 Sam Trenholme <rpmbuild@samiam.org>
- MaraDNS rpm package updated for version 1.0.02

* Wed Jun 26 2002 Sam Trenholme <rpmbuild@samiam.org>
- MaraDNS rpm package updated for version 1.0.01

* Fri Jun 21 2002 Sam Trenholme <rpmbuild@samiam.org>
- MaraDNS rpm package updated for version 1.0.00

* Sat Jun 15 2002 Sam Trenholme <rpmbuild@samiam.org>
- MaraDNS rpm package updated for version 0.9.92

* Wed Jun 12 2002 Sam Trenholme <rpmbuild@samiam.org>
- MaraDNS rpm package updated for version 0.9.91

* Mon Jun 10 2002 Sam Trenholme <rpmbuild@samiam.org>
- MaraDNS rpm package updated for version 0.9.39

* Sat Jun  8 2002 Sam Trenholme <rpmbuild@samiam.org>
- MaraDNS rpm package updated for version 0.9.38

* Fri Jun  7 2002 Sam Trenholme <rpmbuild@samiam.org>
- MaraDNS rpm package updated for version 0.9.37

* Wed Jun  5 2002 Sam Trenholme <rpmbuild@samiam.org>
- MaraDNS rpm package updated for version 0.9.36

* Fri May 31 2002 Sam Trenholme <rpmbuild@samiam.org>
- MaraDNS rpm package updated for version 0.9.34

* Tue May 21 2002 Sam Trenholme <rpmbuild@samiam.org>
- MaraDNS rpm package updated for version 0.9.33

* Sat May 18 2002 Sam Trenholme <rpmbuild@samiam.org>
- MaraDNS rpm package updated for version 0.9.31

* Fri May 17 2002 Sam Trenholme <rpmbuild@samiam.org>
- MaraDNS rpm package updated for version 0.9.30

* Wed May 15 2002 Sam Trenholme <rpmbuild@samiam.org>
- MaraDNS rpm package updated for version 0.9.29

* Mon May 13 2002 Sam Trenholme <rpmbuild@samiam.org>
- MaraDNS rpm package updated for version 0.9.28

* Thu May 9 2002 Sam Trenholme <rpmbuild@samiam.org>
- MaraDNS rpm package updated for version 0.9.26

* Wed May 8 2002 Sam Trenholme <rpmbuild@samiam.org>
- MaraDNS rpm package updated for version 0.9.24

* Sun May 5 2002 Sam Trenholme <rpmbuild@samiam.org>
- MaraDNS rpm package updated for version 0.9.23

* Mon Feb 11 2002 Sam Trenholme <rpmbuild@samiam.org>
- MaraDNS rpm package updated for version 0.9.11

* Mon Feb 11 2002 Sam Trenholme <rpmbuild@samiam.org>
- MaraDNS rpm package updated for version 0.9.10

* Sun Jan 27 2002 Sam Trenholme <rpmbuild@samiam.org>
- MaraDNS rpm package updated for version 0.9.09

* Fri Jan 25 2002 Sam Trenholme <rpmbuild@samiam.org>
- MaraDNS rpm package updated for version 0.9.08

* Thu Jan 10 2002 Sam Trenholme <rpmbuild@maradns.org>
- MaraDNS rpm package updated to version 0.5.31

* Mon Sep 24 2001 Sam Trenholme <rpmbuild@maradns.org>
- MaraDNS rpm package updated to version 0.5.30

* Fri Aug 10 2001 Sam Trenholme <rpmbuild@maradns.org>
- MaraDNS rpm package updated to version 0.5.29

* Wed Jul 18 2001 Sam Trenholme <rpmbuild@maradns.org>
- MaraDNS rpm package updated to version 0.5.28

* Sun Jul 15 2001 Sam Trenholme <rpmbuild@maradns.org>
- MaraDNS rpm package updated to version 0.5.27

* Sun Jul 8 2001 Sam Trenholme <rpmbuild@maradns.org>
- MaraDNS rpm package updated to version 0.5.26

* Thu May 31 2001 Sam Trenholme <rpmbuild@maradns.org>
- MaraDNS rpm package updated to version 0.5.25

* Mon May 21 2001 Sam Trenholme <rpmbuild@maradns.org>
- MaraDNS rpm package updated to version 0.5.24

* Sat May 19 2001 Sam Trenholme <rpmbuild@maradns.org>
- MaraDNS rpm package updated to version 0.5.23

* Thu May 10 2001 Sam Trenholme <rpmbuild@maradns.org>
- MaraDNS rpm package updatd to version 0.5.22

* Mon May 7 2001 Sam Trenholme <rpmbuild@maradns.org> 
- MaraDNS rpm package updated to version 0.5.21

* Sun May 6 2001 Sam Trenholme <rpmbuild@maradns.org>
- MaraDNS rpm package updated to version 0.5.20

* Thu May 3 2001 Sam Trenholme <rpmbuild@maradns.org>
- MaraDNS rpm package updated to version 0.5.18.

* Mon Apr 30 2001 Sam Trehnolme <rpmbuild@maradns.org>
- MaraDNS rpm package upped to version 0.5.17.

* Sun Apr 22 2001 Sam Trenholme <rpmbuild@maradns.org>
- MaraDNS rpm package upped to version 0.5.13.  More info
  at http://www.maradns.org/changelog.html

* Sun Apr 22 2001 Sam Trenholme <rpmbuild@maradns.org>
- MaraDNS rpm package upped to version 0.5.12.  More info
  at http://www.maradns.org/changelog.html

* Fri Apr 20 2001 Sam Trenholme <rpmbuild@maradns.org>
- MaraDNS rpm package upped to version 0.5.10.  Details at
  http://www.maradns.org/changelog.html

* Fri Apr 20 2001 Sam Trenholme <rpmbuild@maradns,org>
- MaraDNS RPM package upped to version 0.5.09.  Go to www.maradns.org for
  full changelog.

* Thu Apr 19 2001 Sam Trenholme <rpmbuild@maradns.org>
- Initial RPM package of MaraDNS
      
