%define version 0.2.6

Name: scli
Version: %{version}
Release: 1
Summary: A collection of SNMP command line management tools
Copyright: GPL
Group: Applications/System
URL: http://www.ibr.cs.tu-bs.de/projects/scli/
Source: ftp://ftp.ibr.cs.tu-bs.de/local/scli/scli-%{version}.tar.gz
#Patch: scli-%{version}-missing.patch
Prefix: /usr
Requires: libxml2 readline
BuildRoot: /var/tmp/%{name}-%{version}
BuildRequires: readline-devel libxml2-devel

%description
The scli package contains small and efficient command line utilities to
monitor and configure network devices and host systems. It is based on the
Simple Network Management Protocol (SNMP).

%prep
%setup 
#%patch -p1

%build
./configure --prefix=/usr
make

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT
# Adjust info,man paths to /usr/share as recommende by Linux FSSTD
mkdir -p $RPM_BUILD_ROOT/usr/share/info
mv $RPM_BUILD_ROOT/usr/info/* $RPM_BUILD_ROOT/usr/share/info
mv $RPM_BUILD_ROOT/usr/man $RPM_BUILD_ROOT/usr/share/

%clean
rm -rf $RPM_BUILD_ROOT


%files 
%defattr (-,root,root)
/usr/bin/*
%doc /usr/share/info/*
%doc /usr/share/man/man1/*
%doc AUTHORS COPYING NEWS README TODO


%changelog
* Wed Dec 19 2001 Oliver Wellnitz <oliver@tecq.org>
- Update to 0.2.6

* Fri Dec 07 2001 Oliver Wellnitz <oliver@escape.de>
- Update to 0.2.5

* Thu Nov 22 2001 Oliver Wellnitz <oliver@escape.de>
- Update to 0.2.4

* Sun Sep 30 2001 Oliver Wellnitz <oliver@escape.de>
- Update to 0.2.3
- Removed old stools naming workaround

* Mon Sep 25 2001 Oliver Wellnitz <oliver@escape.de>
- Update to 0.2.2

* Mon Sep 10 2001 Oliver Wellnitz <oliver@escape.de>
- Update to 0.2.1
- Patched broken version 0.2.1

* Mon Aug 27 2001 Oliver Wellnitz <oliver@escape.de>
- Changed package name to scli
- Update to 0.2.0

* Thu Aug 23 2001 Oliver Wellnitz <oliver@escape.de>
- Update to 0.1.20

* Wed Jun 20 2001 Oliver Wellnitz <oliver@escape.de>
- Update to 0.1.19

* Tue Jun 12 2001 Oliver Wellnitz <oliver@escape.de>
- Update to 0.1.18

* Thu Apr 12 2001 Oliver Wellnitz <oliver@escape.de>
- Update to 0.1.17

* Tue Apr 10 2001 Oliver Wellnitz <oliver@escape.de>
- Update to 0.1.16

* Mon Mar 26 2001 Oliver Wellnitz <oliver@escape.de>
- Update to 0.1.15

* Thu Mar 15 2001 Oliver Wellnitz <oliver@escape.de>
- Update to 0.1.14

* Fri Mar 09 2001 Oliver Wellnitz <oliver@escape.de>
- Update to 0.1.13
- Put infos and man pages in /usr/share/{info,man}

* Thu Mar 01 2001 Oliver Wellnitz <oliver@escape.de>
- Update to 0.1.12

* Wed Feb 28 2001 Oliver Wellnitz <oliver@escape.de>
- Initial version (0.1.11)
