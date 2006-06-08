Summary: Expat is an XML 1.0 parser written in C.
Name: expat
#Version: 2.0.0
Version: 1.95.8
Release: 1
License: MIT/X
Group: Utilities/parsers
URL: http://expat.sourceforge.net/
Source: http://download.sourceforge.net/expat/expat-%{version}.tar.gz
BuildRoot: /var/tmp/%{name}-root

%description
Expat is an XML 1.0 parser written in C by James Clark.  It aims to be
fully conforming. It is currently not a validating XML parser.

%prep
%setup -q

%build
CPPFLAGS="-I/usr/local/include"
export CPPFLAGS

%ifarch sparc64
CC=/usr/local/bin/sparcv9/gcc
CFLAGS="-mcpu=v9 -m64"
LDFLAGS="-L/usr/local/lib/sparcv9 -R/usr/local/lib/sparcv9 -L/usr/local/ssl/lib/sparcv9 -R/usr/local/ssl/lib/sparcv9"
export CC CFLAGS LDFLAGS

./configure
gmake

mkdir sparcv9
mkdir sparcv9/bin
mkdir sparcv9/lib

mv xmlwf/.libs/xmlwf sparcv9/bin/
mv .libs/libexpat.so* sparcv9/lib/

gmake clean

%endif

CC=/usr/local/bin/gcc
CFLAGS=""
LDFLAGS="-L/usr/local/lib -R/usr/local/lib"
export CC CFLAGS LDFLAGS
./configure
gmake 

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/local/bin
mkdir -p $RPM_BUILD_ROOT/usr/local/lib
mkdir -p $RPM_BUILD_ROOT/usr/local/include
gmake install prefix=$RPM_BUILD_ROOT/usr/local

%ifarch sparc64
umask 022
mkdir $RPM_BUILD_ROOT/usr/local/bin/sparcv9
mkdir $RPM_BUILD_ROOT/usr/local/lib/sparcv9

cp sparcv9/bin/* $RPM_BUILD_ROOT/usr/local/bin/sparcv9/
cp sparcv9/lib/libexpat.so* $RPM_BUILD_ROOT/usr/local/lib/sparcv9/
%endif

%files
%defattr(-,root,bin)
%doc COPYING Changes MANIFEST README doc/reference.html doc/style.css
/usr/local/bin/xmlwf
/usr/local/lib/*.so*
%ifarch sparc64
/usr/local/bin/sparcv9/xmlwf
/usr/local/lib/sparcv9/*.so*
%endif
/usr/local/lib/*.a
/usr/local/include/*.h
/usr/local/man/man1/xmlwf.1
