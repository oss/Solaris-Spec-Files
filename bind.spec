%define real_version 9.6-ESV-R8
Summary:        Berkeley name server
Name:		bind
Version:	9.6.8
Release:	6.ESV.R8
License:	BSD
Group:		Applications/Internet
Distribution:	RU-Solaris
Vendor:		NBCS-OSS
Packager:	Naveen Gavini <ngavini@nbcs.rutgers.edu>
URL:            http://www.isc.org/software/bind
Source0:	http://ftp.isc.org/isc/bind9/9.6-ESV/%{name}-%{real_version}.tar.gz
Source1:	bind-ru.tar.gz
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildRequires:	openssl >= 0.9.8l 
Requires:	openssl >= 0.9.8l, bind-dnstools = %{version}-%{release}
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
%setup -q -n %{name}-%{real_version} -a 1

%build
LD_LIBRARY_PATH="/usr/local/:/usr/local/ssl/lib:/usr/local/ssl/include" \
LD_CONFIG_PATH="/usr/local/:/usr/local/ssl/lib" \
CFLAGS="-m32 -O2" \
export CFLAGS LD_CONFIG_PATH LD_LIBRARY_PATH

%configure \
	--with-openssl=/usr/local/ssl \
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
* Wed Oct 10 2012 Kenny Kostenbader <svensken@nbcs.rutgers.edu> - 9.6.8-6.ESV-R8
- Version bump
* Tue Sep 18 2012 Kaitlin Poskaitis <katiepru@nbcs.rutgers.edu> - 9.6.8-6.ESV-R7-P3
- Version bump back to production
* Thu Aug 16 2012 Kaitlin Poskaitis <katiepru@nbcs.rutgers.edu> - 9.6.8-5.ESV-R8-B1
- Changed hard coding real version to a variable
* Mon Aug 13 2012 Kaitlin Poskaitis <katiepru@nbcs.rutgers.edu> - 9.6.8-4.ESV-R8-B1
- Fixed NVR
* Mon Aug 13 2012 Kaitlin Poskaitis <katiepru@nbcs.rutgers.edu> - 9.6.8-3.ESV-R8-B1
- Version bump to beta
* Thu Aug 09 2012 Kenny Kostenbader <svensken@nbcs.rutgers.edu> - 9.6.8-3.ESV-R7-P2
- Version bump
* Tue Apr 17 2012 Josh Matthews <jam761@nbcs.rutgers.edu> - 9.6.8-1.ESV-R6-P1
- bumped to 9.6.8-1.ESV-R6-P1
* Mon Nov 28 2011 Jarek Sedlacek <jarek@nbcs.rutgers.edu> - 9.6.7-1.ESV-R5-P1
- bumped to 9.6.7-1.ESV-R5-P1
* Wed Sep 07 2011 Phillip Quiza <pquiza@nbcs.rutgers.edu> - 9.6.7-1.ESV
- bumped to 9.6-ESV-R5
* Tue Dec 07 2010 Daiyan Alamgir <daiyan@nbcs.rutgers.edu> - 9.6.5-1.ESV
- bumped to 9.6-ESV-R3. 
* Tue Oct 05 2010 Orcan Ogetbil <orcan@nbcs.rutgers.edu> - 9.6.4-1.ESV
- bumped to 9.6-ESV-R2. Note the hack in the versioning.
* Mon Aug 02 2010 Orcan Ogetbil <orcan@nbcs.rutgers.edu> - 9.6.3-1.ESV
- bumped to 9.6-ESV-R1. Note the hack in the versioning.
* Mon Apr 05 2010 Orcan Ogetbil <orcan@nbcs.rutgers.edu> - 9.6.2-1.ESV
- bumped to 9.6-ESV. Note the hack in the versioning.
* Tue Jan 26 2010 Jarek Sedlacek <jarek@nbcs.rutgers.edu> - 9.6.1-P3
- bumped to 9.6.1-P3
* Wed Jul 29 2009 Naveen Gavini <ngavini@nbcs.rutgers.edu> - 9.6.1-P1
- bumped to 9.6.1-P1
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

