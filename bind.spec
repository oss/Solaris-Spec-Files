Summary:        Berkeley name server
Name:		bind
Version:	9.6.1
Release:	1
License:	BSD
Group:		Applications/Internet
Distribution:	RU-Solaris
Vendor:		NBCS-OSS
Packager:	Naveen Gavini <ngavini@nbcs.rutgers.edu>
Source0:	%{name}-%{version}.tar.gz
Source1:	bind-ru.tar.gz
BuildRoot:	/var/tmp/%{name}-root
BuildRequires:	openssl >= 0.9.8
Requires:	openssl >= 0.9.8, bind-dnstools = %{version}-%{release}
Obsoletes:	bind-doc

%description
BIND is the Internet Software Consortium's domain name server.

%package dnstools
Summary: Bind dnstools
Group: Applications/Internet
Conflicts: bind < %{version}-%{release} bind > %{version}-%{release}
Conflicts: bind-doc < %{version}-%{release} bind-doc > %{version}-%{release}

%description dnstools
The bind-dnstools are addr, dig, dnsquery, host, nslookup, and nsupdate.

%package devel
Summary: Bind header files and static libraries
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}
Conflicts: bind < %{version}-%{release} bind > %{version}-%{release}
COnflicts: bind-doc < %{version}-%{release} bind-doc > %{version}-%{release}

%description devel
This package contains the header files and static libraries for
bind. Install this package if you want to write or compile a
program that needs bind.

%prep
%setup -q -n %{name}-%{version} -a 1

%build
PATH="/opt/SUNWspro/bin:${PATH}" \
CC="cc" CXX="CC" CPPFLAGS="-I/usr/local/include" \
LD="/usr/ccs/bin/ld" \
LDFLAGS="-L/usr/local/lib -R/usr/local/lib"
export PATH CC CXX CPPFLAGS LD LDFLAGS

./configure \
	--prefix=%{_prefix} \
	--mandir=%{_mandir} \
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

install bind-ru/etc/named.conf.sample.rpm %{buildroot}/etc
install bind-ru/var/named/root.hints.get.rpm %{buildroot}/var/named
install bind-ru/etc/init.d/named %{buildroot}/etc/init.d

# We need to remove hard links
cd %{buildroot}
/usr/local/bin/unhardlinkify.py ./

%clean
rm -rf %{buildroot}

%post
cat << EOF
RPM installed these files on your system:

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
%attr(755,root,sys) /etc/init.d/named 
/etc/named.conf.sample.rpm
/var/named/root.hints.get.rpm
%{_mandir}/man5/*.5
%{_mandir}/man8/dnssec*.8
%{_mandir}/man8/lwresd.8
%{_mandir}/man8/named*.8
%{_mandir}/man8/rndc*.8

%files dnstools
%defattr(-,bin,bin)
%{_bindir}/dig
%{_bindir}/host
%{_bindir}/nslookup
%{_bindir}/nsupdate
%{_mandir}/man1/*.1

%files devel
%defattr(-,bin,bin)
%{_bindir}/isc-config.sh
%{_includedir}/*
%{_libdir}/*.a
%{_mandir}/man3/*.3

%changelog
* Tue Jul 14 2009 Naveen Gavini <ngavini@nbcs.rutgers.edu> - 9.6.1-1
- bumped to 9.6.1-1
* Wed Mar 25 2009 David Diffenbaugh <davediff@nbcs.rutgers.edu> - 9.6.1b1-1
- bumped to 9.6.1-b1
* Mon Jan 26 2009 Brian Schubert <schubert@nbcs.rutgers.edu> - 9.6.0P1-1
- Bumped to 9.6.0-P1
* Tue Dec 23 2008 Brian Schubert <schubert@nbcs.rutgers.edu> - 9.6.0-1
- Bumped to 9.6.0
* Thu Oct 09 2008 David Diffenbaugh <davediff@nbcs.rutgers.edu> - 9.6.0a1
- bump for unstable
* Fri Sep 12 2008 David Diffenbaugh <davediff@nbcs.rutgers.edu> - 9.5.1b1
- built 9.5.1b1 for unstable, removed patch, see above comments
* Thu Aug 14 2008 Brian Schubert <schubert@nbcs.rutgers.edu> - 9.5.0P2-2
- Added SEGV patch (rbtdb.c.diff)
* Tue Aug 05 2008 Brian Schubert <schubert@nbcs.rutgers.edu> - 9.5.0P2-1
- Removed /etc/init.d/named.rpm and added /etc/init.d/named
- Added Conflicts: bind-doc < %{version}-%{release} bind-doc > %{version}-%{release}
  to packages 'bind-dnstools' and 'bind-devel'
- Changed mandir to /usr/local/man
* Wed Jul 30 2008 Brian Schubert <schubert@nbcs.rutgers.edu> - 9.5.0P1-3
- Added Obsoletes: bind-doc to package 'bind' (docs are included)
- Added Requires: bind-dnstools = %{version}-%{release} to package 'bind'
- Added Conflicts: bind < %{version}-%{release} bind > %{version}-%{release}
  to packages 'bind-dnstools' and 'bind-devel'
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

