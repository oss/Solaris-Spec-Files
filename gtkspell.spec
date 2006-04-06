Summary: gtkspell
Name: gtkspell
Version: 2.0.11
Release: 1
Copyright: GPL
Group: Applications/Spelling
Source: http://gtkspell.sourceforge.net/download/gtkspell-2.0.11.tar.gz
URL: http://gtkspell.sf.net
Distribution: RU-Solaris
Vendor: NBCS-OSS
Packager: Leo Zhadanovsky <leozh@nbcs.rutgers.edu>
BuildRoot: %{_tmppath}/%{name}-root
Requires: aspell gtk2
BuildRequires: aspell gtk2-devel

%description
GTK Spelling library

%package devel
Summary: Libraries, includes to develop applications with %{name}.
Group: Applications/Libraries
Requires: %{name} = %{version}

%description devel
The %{name}-devel package contains the header files and static libraries
for building applications which use {%name}.

%prep
%setup -q

%build
#PATH=`echo $PATH | sed "s/\/usr\/sfw\/bin//g"`
#export PATH
#LD_LIBRARY_PATH="/usr/local/lib" \
#LD_RUN_PATH="/usr/local/lib" \
#LDFLAGS="-L/usr/local/lib -R/usr/local/lib /usr/local/lib/libstdc++.so.2.10.0" \
#CPPFLAGS="-I/usr/local/include"  \
#CC="gcc" 
PATH="/opt/SUNWspro/bin:${PATH}" \
CC="cc" CXX="CC" CPPFLAGS="-I/usr/local/include" \
LD="/usr/ccs/bin/ld" \
LDFLAGS="-L/usr/local/lib -R/usr/local/lib" \
export PATH CC CXX CPPFLAGS LD LDFLAGS

./configure --prefix=/usr/local

make

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/local
make install prefix=$RPM_BUILD_ROOT/usr/local

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,other)
/usr/local/lib/*.so
/usr/local/lib/*.so*
/usr/local/share/*
/usr/local/lib/pkgconfig/*

%files devel
%defattr(-,root,root)
/usr/local/include/*

%changelog
* Thu Apr 06 2006 Leo Zhadanovsky <leozh@nbcs.rutgers.edu> - 2.0.11-1
- Fixed a lot of nastiness in old spec file, added devel package, switched to Sun cc
