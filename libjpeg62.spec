Name: libjpeg62
Version: 6b
Copyright: freely distributable
Group: Development/Libraries
Summary: Jpeg libraries
Release: 1
#Provides: libjpeg.so libjpeg.so.62.0.0 libjpeg.so.62
Source: jpegsrc.v6b.tar.gz
BuildRoot: /var/tmp/%{name}-root
#Conflicts: vpkg-SFWjpg
Obsoletes: libjpeg
Provides: libjpeg

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

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc README
/usr/local/lib/lib*.so*
/usr/local/bin/*
/usr/local/man/man1/*

%files devel
%defattr(-,root,root)
/usr/local/lib/lib*.a
/usr/local/include/*
