%define realver 9.5.0-P1

Summary:        Berkeley name server
Name:		bind
Version:	9.5.0P1
Release:	2
License:	BSD
Group:		Applications/Internet
Distribution:	RU-Solaris
Vendor:		NBCS-OSS
Packager:	Brian Schubert <schubert@nbcs.rutgers.edu>
Source0:	%{name}-%{realver}.tar.gz
Source1:	bind-ru.tar.gz
BuildRoot:	/var/tmp/%{name}-root
BuildRequires:	openssl >= 0.9.8
Requires:	openssl >= 0.9.8, bind-dnstools = %{version}

%description
BIND is the Internet Software Consortium's domain name server.

%package dnstools
Summary: Bind dnstools
Group: Applications/Internet

%description dnstools
The bind-dnstools are addr, dig, dnsquery, host, nslookup, and nsupdate.

%package devel
Summary: Bind header files and static libraries
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}

%description devel
This package contains the header files and static libraries for
bind. Install this package if you want to write or compile a
program that needs bind.

%prep
%setup -q -n %{name}-%{realver} -b 1

%build
PATH="/opt/SUNWspro/bin:${PATH}" \
CC="cc" CXX="CC" CPPFLAGS="-I/usr/local/include" \
LD="/usr/ccs/bin/ld" \
LDFLAGS="-L/usr/local/lib -R/usr/local/lib"
export PATH CC CXX CPPFLAGS LD LDFLAGS

./configure \
	--prefix=/usr/local \
	--with-openssl \
	--enable-threads \
	--enable-shared \
	--enable-static \
	--enable-largefile

gmake -j3

%install
rm -rf %{buildroot}
make install DESTDIR=%{buildroot}

install -d %{buildroot}/etc/init.d
install -d %{buildroot}/var/named

install $RPM_BUILD_DIR/ru-bind/etc/named.conf.sample.rpm %{buildroot}/etc
install $RPM_BUILD_DIR/ru-bind/etc/init.d/named.rpm %{buildroot}/etc/init.d
install $RPM_BUILD_DIR/ru-bind/var/named/root.hints.get.rpm %{buildroot}/var/named

# We need to remove hard links
cd %{buildroot}
/usr/local/bin/unhardlinkify.py ./

%clean
rm -rf %{buildroot}

%post
cat <<EOF
RPM installed these files on your system:

/etc/init.d/named.rpm
/etc/named.conf.sample.rpm
/var/named/root.hints.get.rpm

You should take the rpm extension off and customize them.  You also
should add directories /var/named/primary and /var/named/rutgers.

You may also need to disable BIND that comes with Solaris.
EOF

%files
%defattr(-,bin,bin)
%doc CHANGES COPYRIGHT README
%doc doc/*
%{_sbindir}/*
/etc/init.d/named.rpm
/etc/named.conf.sample.rpm
/var/named/root.hints.get.rpm
%{_datadir}/man/man5/*.5
%{_datadir}/man/man8/dnssec*.8
%{_datadir}/man/man8/lwresd.8
%{_datadir}/man/man8/named*.8
%{_datadir}/man/man8/rndc*.8

%files dnstools
%defattr(-,bin,bin)
%{_bindir}/dig
%{_bindir}/host
%{_bindir}/nslookup
%{_bindir}/nsupdate
%{_datadir}/man/man1/*.1
%{_datadir}/man/man8/nsupdate.8

%files devel
%defattr(-,bin,bin)
%{_bindir}/isc-config.sh
%{_includedir}/*
%{_libdir}/*.a
%{_datadir}/man/man3/*.3

%changelog
* Wed Jul 30 2008 Brian Schubert <schubert@nbcs.rutgers.edu> - 9.5.0P1-2
- Added dnstools and devel packages, removed S72bind.rpm symlink
* Thu Jul 10 2008 Brian Schubert <schubert@nbcs.rutgers.edu> - 9.5.0P1-1
- Updated to version 9.5.0-P1
* Tue Jun 3 2008 Brian Schubert <schubert@nbcs.rutgers.edu> - 9.5.0-1
- Updated to version 9.5.0
* Tue Sep 04 2007 David Lee Halik <dhalik@nbcs.rutgers.edu> - 9.4.1P1-1
- Bump to 9.4.1-P1
* Wed Aug 22 2007 Naveen Gavini <ngavini@nbcs.rutgers.edu> - 9.4.1-1
 - Updated to the latest version.

