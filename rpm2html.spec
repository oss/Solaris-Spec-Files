Summary: Translates an RPM database and dependency information into HTML.
Name: rpm2html 
%define version 1.8.1
%define mysql_version 3.23.55
Version: %{version}
Release: 1
Group: Applications/System
Source: rpm2html-%{version}.tar.gz
Patch: rpm2html-sigfix.patch
URL: http://rufus.w3.org/linux/rpm2html/
Copyright: W3C Copyright (BSD like).
BuildRoot: %{_tmppath}/%{name}-root
BuildRequires: libxml2-devel
Requires: libxml2 mysql = 3.23.55

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
%patch -p1

%build
# build rpm2html
LD_LIBRARY_PATH="/usr/local/mysql-3.23.55/lib/mysql"
LD_RUN_PATH="/usr/local/mysql-3.23.55/lib/mysql"
CFLAGS="-I/usr/local/mysql-3.23.55/include -I/usr/local/include -I/usr/local/include/rpm"
export LD_LIBRARY_PATH LD_RUN_PATH
./configure --with-sql
./config.status
sed "s/aclocal-1.6/aclocal/" Makefile > Makefile1
sed "s/automake-1.6/automake/" Makefile1 > Makefile
sed "s/config.status $@ $(am__depfiles_maybe)/config.status/" Makefile > Makefile1
sed "s/config.status config.h/config.status/" Makefile1 > Makefile
make || make

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
/usr/local/etc/rpm2html.config
