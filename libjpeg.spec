Name: libjpeg
Version: 6b
Copyright: freely distributable
Group: Development/Libraries
Summary: Jpeg libraries
Release: 11
Provides: %{name} libjpeg62 libjpeg62-devel libjpeg.so libjpeg.so.62.0.0 libjpeg.so.62
Obsoletes: libjpeg62 libjpeg62-devel
BuildRequires: gcc >= 3.3
Source: jpegsrc.v6b.tar.gz
BuildRoot: /var/tmp/%{name}-root
#Conflicts: vpkg-SFWjpg
%ifarch sparc64
Provides: %{name}-sparc64 %{name} libjpeg62 libjpeg62-devel
Obsoletes: libjpeg62 libjpeg62-devel
BuildRequires: gcc >= 3.3
%endif

%description
Libjpeg is a library for manipulating jpeg images.  Install this package
if you are writing software that uses jpegs, or compiling software that
uses libjpeg.

%prep
%setup -q -n jpeg-6b

%build

%ifarch sparc64
LD_LIBRARY_PATH="/usr/local/lib/sparcv9"
LD_RUN_PATH="/usr/local/lib/sparcv9"
LD=/usr/ccs/bin/ld 
CC="/usr/local/bin/gcc" \
./configure --prefix=/usr/local --enable-static --enable-shared
make LD=/usr/ccs/bin/ld CC="/usr/local/bin/gcc"
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
rm $RPM_BUILD_ROOT/usr/local/lib/libjpeg.la
%ifarch sparc64
mkdir -p $RPM_BUILD_ROOT/usr/local/lib/sparcv9
mv sparcv9/* $RPM_BUILD_ROOT/usr/local/lib/sparcv9/
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc README
/usr/local/bin/*
/usr/local/man/man1/*
/usr/local/lib/lib*.so*
/usr/local/lib/lib*a
/usr/local/include/*
%ifarch sparc64
/usr/local/lib/sparcv9/*
%endif
