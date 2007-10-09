Summary:	a system-independent interface for user-level packet capture
Name:		libpcap
Version:	0.9.8
Release:        1
Copyright:	GPL
Group:		System Environment/Libraries
Source:		%{name}-%{version}.tar.gz
Distribution: 	RU-Solaris
Vendor: 	NBCS-OSS
Packager: 	David Lee Halik <dhalik@nbcs.rutgers.edu>
BuildRoot:	/var/tmp/%{name}-%{version}-root

%description
libpcap is a system-independent interface for user-level packet 
capture. libpcap provides a portable framework for low-level network 
monitoring. Applications include network statistics collection, 
security monitoring, network debugging, etc.

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
PATH="/opt/SUNWspro/bin:${PATH}" \
CC="cc" CXX="CC" CPPFLAGS="-I/usr/local/include" \
LD="/usr/ccs/bin/ld" \
LDFLAGS="-L/usr/local/lib -R/usr/local/lib" \
export PATH CC CXX CPPFLAGS LD LDFLAGS

./configure --prefix=/usr/local 

#mv Makefile Makefile.wrong
#sed -e 's/ld -shared/ld -Bdynamic -G -dy/g' Makefile.wrong > Makefile

gmake -j3

%install
rm -rf $RPM_BUID_ROOT

gmake install DESTDIR=$RPM_BUILD_ROOT
#make install-shared DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,bin,bin)
/usr/local/lib/*
/usr/local/share/man/*

%files devel
%defattr(-,root,root)
/usr/local/include/*

%changelog
* Sat Oct 06 2007 David Lee Halik <dhalik@nbcs.rutgers.edu> - 0.9.8-1
- Bump to 0.9.8
* Tue Dec 19 2006 Leo Zhadanovsky <leozh@nbcs.rutgers.edu> - 0.9.5-1
- Updated to 0.9.5, modernized spec file
