Summary:	File Alteration Monitor
Name:		fam
Version:	2.7.0
Release:        1
Copyright:	GPL
Group:		Applications/System
Source:		%{name}-%{version}.tar.gz
Distribution: 	RU-Solaris
Vendor: 	NBCS-OSS
Packager: 	Leo Zhadanovsky <leozh@nbcs.rutgers.edu>
BuildRoot:	/var/tmp/%{name}-%{version}-root

%description
GUI tools should not mislead the user; they should display the current 
state of the system, even when changes to the system originate from 
outside of the tools themselves. FAM helps make GUI tools more usable by 
notifying them when the files they're interested in are created, 
modified, executed, and removed.

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
#CPPFLAGS="-I/usr/local/include -I/usr/sfw/include"
#LDFLAGS="-lsocket -lnsl -L/usr/local/lib -R/usr/local/lib -L/usr/sfw/lib -R/usr/sfw/lib"
#LD_LIBRARY_PATH="/usr/local/lib:/usr/sfw/lib"
#LD_RUN_PATH="/usr/local/lib:/usr/sfw/lib"
#CC="gcc"
#export CPPFLAGS LDFLAGS LD_LIBRARY_PATH LD_RUN_PATH CC

PATH="/opt/SUNWspro/bin:${PATH}" \
CC="cc" CXX="CC" CPPFLAGS="-I/usr/local/include" \
LD="/usr/ccs/bin/ld" \
LDFLAGS="-L/usr/local/lib -R/usr/local/lib -lintl" \
export PATH CC CXX CPPFLAGS LD LDFLAGS

./configure --prefix=/usr/local

make

%install
rm -rf $RPM_BUID_ROOT

make install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,bin,bin)
/usr/local/libexec/*
/usr/local/lib/*so
/usr/local/lib/*so*
/usr/local/lib/python2.4/site-packages/*.so
/usr/local/lib/python2.4/site-packages/*.py
/usr/local/lib/pkgconfig/*

%files devel
%defattr(-,root,root)
/usr/local/include/*

%changelog
* Tue Aug 29 2006 Leo Zhadanovsky <leozh@nbcs.rutgers.edu> - 2.7.0-1
- Initial Rutgers release
