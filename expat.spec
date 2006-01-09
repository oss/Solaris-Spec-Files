%define version 1.95.8
%define release 0 

Summary: Expat is an XML 1.0 parser written in C.
Name: expat
Version: %{version}
Release: %{release}
Copyright: MIT/X
Group: Utilities/parsers
URL: http://expat.sourceforge.net/
Source: http://download.sourceforge.net/expat/expat-%{version}.tar.gz
BuildRoot: /var/tmp/%{name}-buildroot

%description
Expat is an XML 1.0 parser written in C by James Clark.  It aims to be
fully conforming. It is currently not a validating XML parser.

%prep
%setup -q

%build
./configure --prefix=/usr/local \
CC=gcc CPPFLAGS="-I/usr/local/include" \
LDFLAGS="-R/usr/local/lib -L/usr/local/lib"
gmake 

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/local/bin
mkdir -p $RPM_BUILD_ROOT/usr/local/lib
mkdir -p $RPM_BUILD_ROOT/usr/local/include
gmake install prefix=$RPM_BUILD_ROOT/usr/local

%files
%defattr(-,root,bin)
%doc COPYING Changes MANIFEST README doc/reference.html doc/style.css
/usr/local/bin/xmlwf
/usr/local/lib/*.so*
/usr/local/lib/*.a
/usr/local/include/*.h
/usr/local/man/man1/xmlwf.1

