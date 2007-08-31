#%include perl-header.spec
%define name net-snmp
%define version 5.4.1
%define release 1

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:	A Simple Network Management Protocol implementation
Group:		System Environment/Daemons
URL:		http://net-snmp.sourceforge.net/
License:	BSDish
Distribution:   RU-Solaris
Vendor:         NBCS-OSS
Packager:       David Lee Halik <dhalik@nbcs.rutgers.edu>
Source:		%{name}-%{version}.tar.gz
Prereq:		openssl
BuildRequires:	coreutils
Requires:	openssl, popt, rpm, zlib
BuildRoot:	%{_tmppath}/%{name}-root
Obsoletes:	cmu-snmp ucd-snmp ucd-snmp-utils
Provides:	net-snmp, net-snmp-utils

%description

Net-SNMP provides tools and libraries relating to the Simple Network
Management Protocol including: An extensible agent, An SNMP library,
tools to request or set information from SNMP agents, tools to
generate and handle SNMP traps, etc.  Using SNMP you can check the
status of a network of computers, routers, switches, servers, ... to
evaluate the state of your network.

%package devel
Group:		Development/Libraries
Summary:	The includes and static libraries from the Net-SNMP package.
AutoReqProv:	no
Requires:	%{name} = %{version}
Obsoletes:	cmu-snmp-devel ucd-snmp-devel

%description devel
The net-snmp-devel package contains headers and libraries which are
useful for building SNMP applications, agents, and sub-agents.

%prep
%setup -q

%build
rm -rf %{buildroot}

PATH="/opt/SUNWspro/bin:${PATH}" \
CC="cc" CXX="CC" CPPFLAGS="-I/usr/local/include" \
LD="/usr/ccs/bin/ld" \
LDFLAGS="-L/usr/local/lib -R/usr/local/lib" \
CFLAGS="-I/usr/local/include"
export PATH CC CXX CPPFLAGS LD LDFLAGS CFLAGS

./configure \
	--with-defaults \
	--with-sys-contact="Unknown" \
        --with-mib-modules="host disman/event-mib smux" \
        --with-sysconfdir="%{_prefix}/etc/net-snmp" \
        --enable-shared \
	--with-mibdirs="/usr/local/share/snmp/mibs" \
	--without-perl-modules \
	--disable-embedded-perl \
	--prefix="%{buildroot}%{_prefix}"

make
#make test

%install
rm -rf $RPM_BUILD_ROOT

mkdir -p $RPM_BUILD_ROOT%{_prefix}/etc
mkdir -p $RPM_BUILD_ROOT%{_prefix}/bin
mkdir -p $RPM_BUILD_ROOT%{_prefix}/sbin
mkdir -p $RPM_BUILD_ROOT%{_prefix}/man/man1
mkdir -p $RPM_BUILD_ROOT%{_prefix}/man/man3
mkdir -p $RPM_BUILD_ROOT%{_prefix}/man/man5
mkdir -p $RPM_BUILD_ROOT%{_prefix}/man/man8
mkdir -p $RPM_BUILD_ROOT%{_prefix}/lib
mkdir -p $RPM_BUILD_ROOT%{_prefix}/include
mkdir -p $RPM_BUILD_ROOT%{_prefix}/share/snmp
mkdir -p $RPM_BUILD_ROOT/etc/init.d

make \
	ucdincludedir=$RPM_BUILD_ROOT%{_prefix}/include/ucd-snmp \
	includedir=$RPM_BUILD_ROOT%{_prefix}/include/net-snmp \
	install

# Deal with the rc script by hand
install -m 755 dist/snmpd-init.d $RPM_BUILD_ROOT/etc/init.d/net-snmpd

rm -rf $RPM_BUILD_ROOT%{_libdir}/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,bin)
%{_bindir}
%{_sbindir}
%{_mandir}/man1/*
%{_mandir}/man3/[^A-Z]*
%{_mandir}/man5/*
%{_mandir}/man8/*
%{_prefix}/lib/*.so*
%dir %{_prefix}/share/snmp
%{_prefix}/share/snmp/*
%config(noreplace) /etc/init.d/net-snmpd

%files devel
%defattr(-,root,bin)
%{_includedir}
%{_libdir}/*.a

%changelog
* Thu Aug 30 2007 David Lee Halik <dhalik@nbcs.rutgers.edu> - 5.4.1-1
- Bump to 5.4.1
* Thu May 10 2007 David Lee Halik <dhalik@nbcs.rutgers.edu> - 5.4-1
- Upgraded to 5.4
* Tue May 08 2007 David Lee Halik <dhalik@nbcs.rutgers.edu> - 5.1.3.1-3
- Fixed net-snmp to find MiBs in /usr/local/share by default

