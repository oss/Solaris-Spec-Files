#
# To checkout rpm2html from CVS:
# cvs -z3 -d :pserver:anoncvs@sources.redhat.com:/cvs/rpm2html login
#  {enter "anoncvs" as the password}
# cvs -z3 -d :pserver:anoncvs@sources.redhat.com:/cvs/rpm2html co rpm2html
# There is also an 'rpmfind' module we don't checkout for this package
#
%define cvsdate 20030428
%define mysql_version 5.0.67

Summary:	Translates an RPM database and dependency information into HTML.
Name:		rpm2html
Version:	1.10.0
Release:	2
Group:		Applications/System
Source:   	rpm2html-%{version}.tar.gz
# We don't want to use the reserved word "Release" in mysql syntax
Patch0:         rpm2html-sql.patch
URL:		http://rufus.w3.org/linux/rpm2html/
License:	W3C Copyright (BSD like).
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root
BuildRequires:	libxml2-devel >= 2.5.4 mysql5-devel = %{mysql_version} 
BuildRequires:	autoconf automake rpm-devel
Requires:	libxml2 >= 2.5.4 mysql5 = %{mysql_version}

%description
The rpm2html utility automatically generates web pages that describe a
set of RPM packages.  The goals of rpm2html are to identify the
dependencies between various packages, and to find the package(s) that
will provide the resources needed to install a given package.
Rpm2html analyzes the provides and requires of the given set of RPMs,
and then shows the dependency cross-references using hypertext links.
Rpm2html can now dump the metadata associated with RPM files into
standard RDF files.

Install rpm2html if you want a utility for translating information
from an RPM database into HTML.

%prep
%setup -q
%patch0 -p0

%build
PATH="/opt/SUNWspro/bin:${PATH}"
CC="cc" CXX="CC" 
CPPFLAGS="-I/usr/local/mysql-%{mysql_version}/include \
          -I/usr/local/include/rpm -I/usr/local/include"
LD="/usr/ccs/bin/ld" 
LDFLAGS="-L/usr/local/lib -R/usr/local/lib \
         -L/usr/local/mysql-%{mysql_version}/lib \
         -R/usr/local/mysql-%{mysql_version}/lib \
         -L/usr/local/lib/rpm -R/usr/local/lib/rpm"

export PATH CC CXX CPPFLAGS LD LDFLAGS

autoreconf -i
./configure --with-sql
gmake

%install
rm -rf %{buildroot}
install -d %{buildroot}%{_bindir}
install -d %{buildroot}%{_sysconfdir}
install -d %{buildroot}%{_datadir}/rpm2html
install -d %{buildroot}%{_mandir}/man1

install -m 0755 -s rpm2html %{buildroot}%{_bindir}/rpm2html

for i in msg.*
do
  install -m 0644 $i %{buildroot}%{_datadir}/rpm2html/$i
done

install -m 0644 rpm2html.config %{buildroot}%{_sysconfdir}/rpm2html.config
install -m 0644 rpm2html.1 %{buildroot}%{_mandir}/man1/rpm2html.1

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,bin)
%doc CHANGES BUGS Copyright PRINCIPLES README TODO 
%doc rpm2html-cdrom.config rpm2html-en.config rpm2html-rdf.config
%{_bindir}/rpm2html
%{_datadir}/rpm2html/
%{_mandir}/man1/*
%config(noreplace)%{_sysconfdir}/rpm2html.config

%changelog
* Fri Dec 04 2009 Orcan Ogetbil <orcan@nbcs.rutgers.edu> - 1.10.0-2
- Fix occurences of Packages.Release in MySQO queries

* Fri May 08 2009 Brian Schubert <schubert@nbcs.rutgers.edu> - 1.10.0-1
- Update to version 1.10.0

* Fri May 1 2009 Naveen Gavini <ngavini@nbcs.rutgers.edu> - 1.8.1-5
- Fixed stuff for database.
