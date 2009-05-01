#
# To checkout rpm2html from CVS:
# cvs -z3 -d :pserver:anoncvs@sources.redhat.com:/cvs/rpm2html login
#  {enter "anoncvs" as the password}
# cvs -z3 -d :pserver:anoncvs@sources.redhat.com:/cvs/rpm2html co rpm2html
# There is also an 'rpmfind' module we don't checkout for this package
#
%define cvsdate 20030428
%define mysql_version 5.0.67

Summary: Translates an RPM database and dependency information into HTML.
Name: rpm2html
Version: 1.8.2.cvs%{cvsdate}
Release: 5
Group: Applications/System
Source: rpm2html-%{cvsdate}.tar.bz2
Patch: rpm2html-longfilessql.patch
URL: http://rufus.w3.org/linux/rpm2html/
License: W3C Copyright (BSD like).
BuildRoot: %{_tmppath}/%{name}-root
BuildRequires: libxml2-devel >= 2.5.4 mysql5-devel = %{mysql_version}
Requires: libxml2 >= 2.5.4 mysql5 = %{mysql_version}

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
%setup -q -n rpm2html
%patch -p1

%build
# build rpm2html
LD_LIBRARY_PATH="/usr/local/mysql-%{mysql_version}/lib/mysql:/usr/local/lib:/usr/local/lib/rpm"
LD_RUN_PATH="/usr/local/mysql-%{mysql_version}/lib/mysql:/usr/local/lib:/usr/local/lib/rpm"
CPPFLAGS="-I/usr/local/mysql-%{mysql_version}/include -I/usr/local/include -I/usr/local/include/rpm -L/usr/local/lib -R/usr/local/lib -lm -lsocket -lnsl"
export LD_LIBRARY_PATH LD_RUN_PATH CPPFLAGS
./configure --with-sql
LD_LIBRARY_PATH="/usr/local/mysql-%{mysql_version}/lib/mysql:/usr/local/lib:/usr/local/lib/rpm" \
LD_RUN_PATH="/usr/local/mysql-%{mysql_version}/lib/mysql:/usr/local/lib:/usr/local/lib/rpm" \
make

%install
rm -rf %{buildroot}
install -d %{buildroot}/usr/local/bin
install -d %{buildroot}/usr/local/etc
install -d %{buildroot}/usr/local/share/rpm2html
install -d %{buildroot}/usr/local/man/man1

install -m 0755 -s rpm2html %{buildroot}/usr/local/bin/rpm2html

for i in msg.*
do
  install -m 0644 $i %{buildroot}/usr/local/share/rpm2html/$i
done

install -m 0644 rpm2html.config  %{buildroot}/usr/local/etc/rpm2html.config
install -m 0644 rpm2html.1  %{buildroot}/usr/local/man/man1/rpm2html.1

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,bin)
%doc CHANGES BUGS Copyright PRINCIPLES README TODO 
%doc rpm2html-cdrom.config rpm2html-en.config
%doc rpm2html.config.mirrors rpm2html-fr.config
%doc rpm2html.config.resources rpm2html-rdf.config
/usr/local/bin/rpm2html
/usr/local/share/rpm2html/msg.*
/usr/local/man/man1/*
%config(noreplace)/usr/local/etc/rpm2html.config

%changelog
* Fri May 1 2009 Naveen Gavini <ngavini@nbcs.rutgers.edu> - 1.8.1-1
- Fixed stuff for database.
