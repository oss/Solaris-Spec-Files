Summary: 	Expat is an XML 1.0 parser written in C.
Name: 		expat
Version: 	2.0.0
Release: 	1
License: 	MIT/X
Group: 		Utilities/parsers
URL: 		http://expat.sourceforge.net/
Source: 	http://download.sourceforge.net/expat/expat-%{version}.tar.gz
BuildRoot: 	/var/tmp/%{name}-root

%description
Expat is an XML 1.0 parser written in C by James Clark.  It aims to be
fully conforming. It is currently not a validating XML parser.

%package devel  
Summary: Libraries, includes to develop applications with %{name}.
Group: Applications/Libraries
Requires: %{name} = %{version}

%description devel
The %{name}-devel package contains the header files and static libraries
for building applications which use %{name}.

%prep
%setup -q

%build
LD_RUN_PATH="/usr/local/lib" \
PATH="/opt/SUNWspro/bin:${PATH}" \
CC="cc" CXX="CC" CPPFLAGS="-I/usr/local/include" \
LDFLAGS="-L/usr/local/lib -R/usr/local/lib" \
export LD_RUN_PATH PATH CC CXX CPPFLAGS LDFLAGS

./configure --prefix=/usr/local
make

cd .libs
ln -s libexpat.so.1.5.0 libexpat.so.0
ln -s libexpat.so.1.5.0 libexpat.so.0.5.0
cd .. 

rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/local/bin
mkdir -p $RPM_BUILD_ROOT/usr/local/lib
mkdir -p $RPM_BUILD_ROOT/usr/local/include
make install prefix=$RPM_BUILD_ROOT/usr/local

cp .libs/libexpat.so.0** $RPM_BUILD_ROOT/usr/local/lib

%ifarch sparc64
LD_RUN_PATH="/usr/local/lib/sparcv9" \
CC="cc -xtarget=ultra -xarch=v9" CXX="CC -xtarget=ultra -xarch=v9" \
CPPFLAGS="-I/usr/local/include/sparcv9" \
LDFLAGS="-L/usr/local/lib/sparcv9 -R/usr/local/lib/sparcv9" \
export LD_RUN_PATH CC CXX CPPFLAGS LDFLAGS
make clean
./configure --prefix=/usr/local
make

cd .libs
ln -s libexpat.so.1.5.0 libexpat.so.0
ln -s libexpat.so.1.5.0 libexpat.so.0.5.0
cd ..

mkdir sparcv9
mkdir sparcv9/bin
mkdir sparcv9/lib

mv xmlwf/.libs/xmlwf sparcv9/bin/
mv .libs/libexpat.so* sparcv9/lib/

gmake clean
%endif

%install
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
/usr/local/man/man1/xmlwf.1

%files devel
%defattr(-,root,root)
/usr/local/include/*

%changelog
* Tue Aug 22 2006 Leo Zhadanovsky <leozh@nbcs.rutgers.edu> - 2.0.0-1
- Fixed up spec file, switched to Sun CC, enabled backwards compatibility with 1.95
