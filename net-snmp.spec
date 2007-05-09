%include perl-header.spec

Name:		net-snmp
Version:	5.1.3.1
Release:	3
Summary:	A Simple Network Management Protocol implementation
Group:		System Environment/Daemons
URL:		http://net-snmp.sourceforge.net/
License:	BSDish
Distribution:   RU-Solaris
Vendor:         NBCS-OSS
Packager:       David Lee Halik <dhalik@nbcs.rutgers.edu>
Source:		net-snmp-%{version}.tar.gz
Prereq:		openssl
BuildRequires:	perl coreutils
BuildRoot:	/var/tmp/%{name}-root
Obsoletes:	cmu-snmp

%description

Net-SNMP provides tools and libraries relating to the Simple Network
Management Protocol including: An extensible agent, An SNMP library,
tools to request or set information from SNMP agents, tools to
generate and handle SNMP traps, etc.  Using SNMP you can check the
status of a network of computers, routers, switches, servers, ... to
evaluate the state of your network.

%package devel
Group: Development/Libraries
Summary: The includes and static libraries from the Net-SNMP package.
AutoReqProv: no
Requires: net-snmp = %{version}
Obsoletes: cmu-snmp-devel

%description devel
The net-snmp-devel package contains headers and libraries which are
useful for building SNMP applications, agents, and sub-agents.

%prep
PATH="/usr/local/bin:/usr/local/sbin:/opt/SUNWspro/bin:/usr/ccs/bin"
PATH="${PATH}:/bin:/sbin:/usr/bin:/usr/sbin"
export PATH

%setup -q

%build
PATH="/usr/local/bin:/usr/local/sbin:/opt/SUNWspro/bin:/usr/ccs/bin"
PATH="${PATH}:/bin:/sbin:/usr/bin:/usr/sbin"
CC="cc"
CXX="CC"
CFLAGS="-I/usr/local/include"
CXXFLAGS=""
CPPFLAGS="-I/usr/local/include"
LDFLAGS="-L/usr/local/lib -R/usr/local/lib"
export PATH CC CXX CFLAGS CXXFLAGS CPPFLAGS LDFLAGS

./configure --prefix=$RPM_BUILD_ROOT/usr/local \
        --with-defaults --with-sys-contact="Unknown" \
        --with-mib-modules="host disman/event-mib smux" \
        --with-sysconfdir="%{_prefix}/etc/net-snmp" \
        --enable-shared \
	--with-mibdirs="/usr/local/share/snmp/mibs"
make
make test

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

make install ucdincludedir=$RPM_BUILD_ROOT%{_prefix}/include/ucd-snmp \
             includedir=$RPM_BUILD_ROOT%{_prefix}/include/net-snmp \
             DESTDIR=$RPM_BUILD_ROOT

# Deal with the rc script by hand
install -m 755 dist/snmpd-init.d $RPM_BUILD_ROOT/etc/init.d/net-snmpd

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
#%dir %{_prefix}/share/snmp/mibs
#%dir %{_prefix}/share/snmp/snmpconf-data
%{_prefix}/share/snmp/*
#%{_prefix}/share/snmp/mibs/*
#%{_prefix}/share/snmp/snmpconf-data/*
%config(noreplace) /etc/init.d/net-snmpd

%files devel
%defattr(-,root,bin)
%{_includedir}
%{_libdir}/*.a
%{_libdir}/*.la

%changelog
* Tue May 08 2007 David Lee Halik <dhalik@nbcs.rutgers.edu> - 5.1.3.1-3
- Fixed net-snmp to find MiBs in /usr/local/share by default

