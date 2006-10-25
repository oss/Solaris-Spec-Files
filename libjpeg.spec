Name: libjpeg
Version: 6b
Copyright: freely distributable
Group: Development/Libraries
Summary: Jpeg libraries
Release: 14
Provides: %{name} libjpeg62 libjpeg62-devel libjpeg.so libjpeg.so.62.0.0 libjpeg.so.62
Obsoletes: libjpeg62 libjpeg62-devel
Source: jpegsrc.v6b.tar.gz
BuildRoot: /var/tmp/%{name}-root

%description
Libjpeg is a library for manipulating jpeg images.  Install this package
if you are writing software that uses jpegs, or compiling software that
uses libjpeg.

%package devel
Summary: Libraries, includes to develop applications with %{name}.
Group: Applications/Libraries
Requires: %{name} = %{version}

%description devel
The %{name}-devel package contains the header files and static libraries
for building applications which use %{name}.

%prep
%setup -q -n jpeg-6b

%build
PATH="/opt/SUNWspro/bin:${PATH}" \
CC="cc" CXX="CC" CPPFLAGS="-I/usr/local/include" \
LD="/usr/ccs/bin/ld" \
LDFLAGS="-L/usr/local/lib -R/usr/local/lib" \
export PATH CC CXX CPPFLAGS LD LDFLAGS

./configure --prefix=/usr/local --enable-shared
sed -e "s%%^CC=\"/.*\"%%CC=\"$CC\"%%" `which libtool` > libtool
chmod a+x libtool
make

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/local/include
mkdir -p $RPM_BUILD_ROOT/usr/local/lib
mkdir -p $RPM_BUILD_ROOT/usr/local/bin
mkdir -p $RPM_BUILD_ROOT/usr/local/man/man1
make install prefix=$RPM_BUILD_ROOT/usr/local
cd $RPM_BUILD_ROOT/usr/local/lib/
#ln -s libjpeg.so.62.0.0 libjpeg.so.62
#ln -s libjpeg.so.62.0.0 libjpeg.so 

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc README
/usr/local/bin/*
/usr/local/man/man1/*
/usr/local/lib/*.so*

%files devel
%defattr(-,root,root)
/usr/local/include/*

%changelog
* Wed Aug 16 2006 Leo Zhadanovsky <leozh@nbcs.rutgers.edu> - 6b-12
- Cleaned up spec file, switched to Sun CC, got rid of 64 bit version
