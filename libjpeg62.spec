Name: libjpeg62
Version: 6b
Copyright: freely distributable
Group: Development/Libraries
Summary: Jpeg libraries
Release: 4
#Provides: libjpeg.so libjpeg.so.62.0.0 libjpeg.so.62
Source: jpegsrc.v6b.tar.gz
BuildRoot: /var/tmp/%{name}-root
#Conflicts: vpkg-SFWjpg
#Obsoletes: libjpeg
Provides: libjpeg libjpeg.so
%ifarch sparc64
Provides: %{name}-sparc64
BuildRequires: gcc3
%endif

%description
Libjpeg is a library for manipulating jpeg images.  Install this package
if you are writing software that uses jpegs, or compiling software that
uses libjpeg.

%package devel
Summary: %{name} include files, etc.
Requires: %{name}
Group: Development
%description devel
%{name} include files, etc.

%prep
%setup -q -n jpeg-6b

%build
%ifarch sparc64
LD_LIBRARY_PATH="/usr/local/lib/sparcv9"
LD_RUN_PATH="/usr/local/lib/sparcv9"
LD=/usr/ccs/bin/ld 
CC="/usr/local/gcc3/bin/gcc" \
./configure --prefix=/usr/local --enable-static --enable-shared
make LD=/usr/ccs/bin/ld CC="/usr/local/gcc3/bin/gcc"
mkdir sparcv9
mv .libs/libjpeg.so* sparcv9/
make clean
%endif

./configure --prefix=/usr/local --enable-static --enable-shared
make

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/local/include
mkdir -p $RPM_BUILD_ROOT/usr/local/man/man1
mkdir $RPM_BUILD_ROOT/usr/local/lib
mkdir $RPM_BUILD_ROOT/usr/local/bin
make install prefix=$RPM_BUILD_ROOT/usr/local
/usr/ccs/bin/strip $RPM_BUILD_ROOT/usr/local/bin/* $RPM_BUILD_ROOT/usr/local/lib/*.so*
%ifarch sparc64
mkdir -p $RPM_BUILD_ROOT/usr/local/lib/sparcv9
mv sparcv9/* $RPM_BUILD_ROOT/usr/local/lib/sparcv9/
%endif

%post
rm -f /usr/local/lib/libjpeg.so
ln -sf /usr/local/lib/libjpeg.so.62 /usr/local/lib/libjpeg.so
%ifarch sparc64
rm -f /usr/local/lib/sparcv9/libjpeg.so
ln -sf /usr/local/lib/sparcv9/libjpeg.so.62 /usr/local/lib/sparcv9/libjpeg.so
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc README
/usr/local/lib/lib*.so.*
/usr/local/bin/*
/usr/local/man/man1/*
%ifarch sparc64
/usr/local/lib/sparcv9/*.so.*
%endif

%files devel
%defattr(-,root,root)
/usr/local/lib/lib*.a
/usr/local/include/*
