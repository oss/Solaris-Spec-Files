Summary: Translates an RPM database and dependency information into HTML.
Name: rpm2html 
%define version 1.7
Version: %{version}
Release: 1
Group: Applications/System
Source0: rpm2html-%{version}.tar.gz
Source1: rpm-4.0.3-BETA.tar.gz
URL: http://rufus.w3.org/linux/rpm2html/
Copyright: W3C Copyright (BSD like).
BuildRoot: %{_tmppath}/%{name}-root
BuildRequires: libxml2-devel
Requires: libxml2

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
%setup -q -D -T -a 1 

%build
CWD=`pwd`
# first build RPM 4.0.3 libs, etc.
cd $CWD/rpm-4.0.3
LD="/usr/ccs/bin/ld -L/usr/local/lib -R/usr/local/lib" \
LDFLAGS="-L/usr/local/lib -R/usr/local/lib" \
CFLAGS="-L/usr/local/lib -R/usr/local/lib" \
CPPFLAGS="-I/usr/local/lib" ./configure --prefix=/usr/local \
--sysconfdir=/etc
gmake CCLD="/usr/local/bin/gcc -L/usr/local/lib -R/usr/local/lib"

# install results
cd $CWD
mkdir include
cp rpm-4.0.3/rpmio/*h rpm-4.0.3/lib/*h rpm-4.0.3/build/*h rpm-4.0.3/misc/*h \
   include
mkdir rpmlib
find rpm-4.0.3 -name '*.a' | xargs -i'{}' cp '{}' rpmlib

# build rpm2html
cd $CWD
ed rpmopen.c <<EOF
    1,\$s/headerTagTableEntry_s/headerTagTableEntry/g
    w
    q
EOF
LIBS="-lnsl -lsocket -lbz2 -lrpm -lrpmio" \
CFLAGS="-L$CWD/rpmlib -L/usr/local/lib -R/usr/local/lib" \
CPPFLAGS="-I$CWD/include -I/usr/local/include" ./configure
make INCL="-I/usr/local/include/libxml -I. -I$CWD/include -I/usr/local/include"

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

install -m 0644 rpm2html.config  %{buildroot}/usr/local/etc/rpm2html.config.rpm
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
/usr/local/etc/rpm2html.config.rpm
