# This package requires cdefs.h, I copied it from 
# /usr/local/src/rpm-packages/BUILD/bind-9.3.2/lib/bind/port/sunos/include/sys/cdefs.h 
# to /usr/include/sys/cdefs.h before building 

Summary:	D-BUS - a message bus system
Name:		dbus
Version:	0.61
Release:        3
Copyright:	GPL
Group:		System Environment/Libraries
Source:		%{name}-%{version}.tar.gz
Distribution: 	RU-Solaris
Vendor: 	NBCS-OSS
Packager: 	Leo Zhadanovsky <leozh@nbcs.rutgers.edu>
BuildRoot:	/var/tmp/%{name}-%{version}-root
Requires:	gtk2, python >= 2.4, Pyrex, libxml2

%description
D-BUS supplies both a system daemon (for events such as "new hardware 
device added" or "printer queue changed") and a per-user-login-session 
daemon (for general IPC needs among user applications). Also, the 
message bus is built on top of a general one-to-one message passing 
framework, which can be used by any two apps to communicate directly 
(without going through the message bus daemon). Currently the 
communicating applications are on one computer, but TCP/IP option is 
available and remote support planned.

%package devel
Summary: Libraries, includes to develop applications with %{name}.
Group: Applications/Libraries
Requires: %{name} = %{version} 

%description devel
The %{name}-devel package contains the header files and static libraries
for building applications which use %{name}.

%prep
%setup -q -n %{name}-%{version}

%build
PATH="/opt/SUNWspro/bin:${PATH}" \
CC="cc" CXX="CC" CPPFLAGS="-I/usr/local/include" \
LD="/usr/ccs/bin/ld" \
LDFLAGS="-L/usr/local/lib -R/usr/local/lib" \
export PATH CC CXX CPPFLAGS LD LDFLAGS

#CPPFLAGS="-I/usr/local/include -I/usr/sfw/include"
#LDFLAGS="-L/usr/local/lib -R/usr/local/lib -L/usr/sfw/lib -R/usr/sfw/lib"
#LD_LIBRARY_PATH="/usr/local/lib:/usr/sfw/lib"
#LD_RUN_PATH="/usr/local/lib:/usr/sfw/lib"
#CC="gcc" 

./configure --prefix=/usr/local --enable-gtk --enable-python --with-xml=expat

#mv glib/examples/statemachine/Makefile glib/examples/statemachine/Makefile.wrong
#sed -e 's/ -mt//g' glib/examples/statemachine/Makefile.wrong > glib/examples/statemachine/Makefile

#mv tools/Makefile tools/Makefile.wrong
#sed -e 's/ -mt//g' tools/Makefile.wrong > tools/Makefile

make

%install
rm -rf $RPM_BUID_ROOT

make install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,bin,bin)
/usr/local/bin/*
/usr/local/lib/*.so
/usr/local/lib/*so*
/usr/local/lib/python2.4/site-packages/dbus/*.so
/usr/local/lib/python2.4/site-packages/dbus/*.py
/usr/local/lib/python2.4/site-packages/dbus/*py*
/usr/local/lib/python2.4/site-packages/dbus.pth 
/usr/local/share/*
/usr/local/etc/*
/usr/local/man/man1/*
/usr/local/var/*

%files devel
%defattr(-,root,root)
/usr/local/include/*
/usr/local/lib/pkgconfig/*
/usr/local/lib/dbus-1.0/include/*

%changelog
* Thu May 04 2006 Leo Zhadanovsky <leozh@nbcs.rutgers.edu> - 0.61-2
- Deleted .la files from the package
* Tue Apr 04 2006 Leo Zhadanovsky <leozh@nbcs.rutgers.edu> - 0.61-1
- Initial Rutgers release
