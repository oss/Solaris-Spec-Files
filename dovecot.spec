Name:		dovecot2
Version:	2.0.13
Release:       	1
License:	GPL
Group:		System Environment/Daemons
URL:		http://www.dovecot.org
Source0:	http://dovecot.org/releases/1.2/dovecot-%{version}.tar.gz
Source1:	dovecot.init
Source2:	imap.ru

# OSS patches
# Handle badness with the uidlist on NFS:
#equivilent patch was upstreamed in 1.2.11
#Patch8:         dovecot-uidlist-nfs.patch
BuildRoot:	%{_tmppath}/dovecot-%{version}-%{release}-root

BuildRequires:  openssl openldap-devel >= 2.4

Requires:       openldap-lib >= 2.4

Summary:        DOVECOT - Secure IMAP Servers

%description
Dovecot is an open source IMAP and POP3 server for Linux/UNIX-like 
systems, written with security primarily in mind. Dovecot is an 
excellent choice for both small and large installations. It's fast, 
simple to set up, requires no special administration and it uses very 
little memory

%prep
%setup -q -n dovecot-%{version}
#%patch8 -p1 -b .uidlist


%build
PATH="/opt/SUNWspro/bin:/usr/ccs/bin:${PATH}"
CC="cc" CFLAGS="-g -xs -D_POSIX_PTHREAD_SEMANTICS" CXX="CC" 
CPPFLAGS="-I/usr/local/ssl/include -I/usr/local/include -D_POSIX_PTHREAD_SEMANTICS" 
LDFLAGS="-L/usr/local/lib -R/usr/local/lib"
export CC CFLAGS CXX CPPFLAGS LDFLAGS


./configure 					\
	--prefix=%{_prefix} 			\
	--with-ssl=openssl 			\
	--disable-static

gmake -j3

%install
rm -rf %{buildroot}
gmake install DESTDIR=%{buildroot}

rm -rf %{buildroot}%{_datadir}

%{__install} -D -m 755 %{SOURCE1} %{buildroot}/etc/init.d/dovecot

# Install dovecot launcher script dealie
mv %{buildroot}%{_libexecdir}/dovecot/imap %{buildroot}%{_libexecdir}/dovecot/imap.REAL
%{__install} -m 755 %{SOURCE2} %{buildroot}%{_libexecdir}/dovecot/imap

find %{buildroot} -name '*.la' -exec rm -f '{}' \;

%clean
rm -rf %{buildroot}

%files
%defattr(-, root, root,-)
%doc README NEWS COPYING* AUTHORS ChangeLog
%doc doc/wiki/
%{_bindir}/*
%{_sbindir}/*
%{_libdir}/*
%{_libexecdir}/*
%{_sysconfdir}/*
/etc/init.d/dovecot

%changelog
* Fri Jul 08 2011 Steven Lu <sjlu@nbcs.rutgers.edu> 2.0.13-2
- seperating from dovecot1 and dovecot2

* Fri Jul 08 2011 Steven Lu <sjlu@nbcs.rutgers.edu> 2.0.13-1
- bump to 2.0.13

* Fri Apr 22 2011 Steven Lu <sjlu@nbcs.rutgers.edu> - 2.0.12-2
- added ulimits to init script from request

* Thu Apr 14 2011 Jarek Sedlacek <jarek@nbcs.rutgers.edu> - 2.0.12-1
- bump to 2.0.12
* Tue Apr 05 2011 Steven Lu <sjlu@nbcs.rutgers.edu> - 2.0.11-4
- actual commit of changes

* Wed Mar 23 2011 Steven Lu <sjlu@nbcs.rutgers.edu> - 2.0.11-3
- updated dovecot.init with the requested changes, spec file updated

* Wed Mar 23 2011 Steven Lu <sjlu@nbcs.rutgers.edu> - 2.0.11-2
- doveconf was not included since bindir was not added to files section

* Tue Mar 22 2011 Phillip Quiza	<pquiza@nbcs.rutgers.edu> - 2.0.11-1
- Updated to version 2.0.11-1

* Tue Mar 09 2010 Jarek Sedlacek <jarek@nbcs.rutgers.edu> - 1.2.11-1
- bump to version 1.2.11
- removed uidlist nfs patch, upstream release has equivilant fix

* Mon Jan 25 2010 Orcan Ogetbil <orcan@nbcs.rutgers.edu> - 1.2.10-2
- Build with uidlist-nfs patch

* Mon Jan 25 2010 Orcan Ogetbil <orcan@nbcs.rutgers.edu> - 1.2.10-1
- Updated to version 1.2.10

* Wed Dec 23 2009 Naveen Gavini <ngavini@nbcs.rutgers.edu> - 1.2.9-2
- Added cmd-list patch and maildir-uid patch

* Mon Dec 21 2009 Brian Schubert <schubert@nbcs.rutgers.edu> - 1.2.9-1
- Updated to version 1.2.9

* Mon Nov 23 2009 Jarek Sedlacek <jarek@nbcs.rutgers.edu> - 1.2.7-1
- Updated to version 1.2.8

* Tue Nov 10 2009 Jarek Sedlacek <jarek@nbcs.rutgers.edu> - 1.2.7-1
- Updated to version 1.2.7

* Tue Oct 06 2009 Jarek Sedlacek <jarek@nbcs.rutgers.edu> - 1.2.6-1
- Updated to version 1.2.6

* Wed Sep 16 2009 Brian Schubert <schubert@nbcs.rutgers.edu> - 1.2.5-1
- Updated to version 1.2.5
- Added launcher script trickery

* Wed Sep 02 2009 Brian Schubert <schubert@nbcs.rutgers.edu> - 1.2.4-1
- Updated to version 1.2.4

* Wed Aug 12 2009 Brian Schubert <schubert@nbcs.rutgers.edu> - 1.2.3-2
- Removed -Bdirect and -zdefs from LDFLAGS

* Tue Aug 11 2009 Brian Schubert <schubert@nbcs.rutgers.edu> - 1.2.3-1
- Updated to version 1.2.3
- Removed modifications made for previous build

* Thu Jul 30 2009 Brian Schubert <schubert@nbcs.rutgers.edu> - 1.2.2-1
- Updated to version 1.2.2
- Defined the GLOB_BRACE macro since it does not exist on Solaris
- Added "-lsocket -lnsl" to LD_FLAGS

* Mon Jul 20 2009 Brian Schubert <schubert@nbcs.rutgers.edu> - 1.2.1-1
- Updated to version 1.2.1

* Wed Jul 08 2009 Brian Schubert <schubert@nbcs.rutgers.edu> - 1.2.0-2
- Modified init script

* Thu Jul 02 2009 Brian Schubert <schubert@nbcs.rutgers.edu> - 1.2.0-1
- Updated to 1.2.0

* Mon May 18 2009 Naveen Gavini <ngavini@nbcs.rutgers.edu> - 1.2.rc4-1
- Updated to rc4

* Mon Apr 20 2009 David Diffenbaugh <davediff@nbcs.rutgers.edu> - 1.2.rc3-1
- Updated to rc3
- removed dovecot-1.2.rc2-quotafs.patch

* Mon Apr 13 2009 Brian Schubert <schubert@nbcs.rutgers.edu> - 1.2.rc2-1
- Updated to rc2
- Removed dovecot-1.2.rc1-rquota_x.patch
- Added dovecot-1.2.rc2-quotafs.patch

* Fri Apr 10 2009 Brian Schubert <schubert@nbcs.rutgers.edu> - 1.2.rc1-1
- Updated to 1.2.rc1
- Added dovecot-1.2.rc1-rquota_x.patch

* Mon Mar 23 2009 David Diffenbaugh <davediff@nbcs.rutgers.edu> - 1.2.beta3
- updated to version 1.2.beta3

* Mon Mar 16 2009 David Diffenbaugh <davediff@nbcs.rutgers.edu> - 1.1.12-1
- updated to version 1.1.12

* Mon Feb 09 2009 David Diffenbaugh <davediff@nbcs.rutgers.edu> - 1.1.11-1
- updated to version 1.1.11

* Mon Feb 02 2009 Brian Schubert <schubert@nbcs.rutgers.edu> - 1.1.10-1
- Updated to version 1.1.10

* Mon Dec 01 2008 Brian Schubert <schubert@nbcs.rutgers.edu> - 1.1.7-2
- Added init script

* Mon Nov 24 2008 Brian Schubert <schubert@nbcs.rutgers.edu> - 1.1.7-1
- Updated to version 1.1.7

* Tue Oct 21 2008 Brian Schubert <schubert@nbcs.rutgers.edu> - 1.1.4-1
- Built against openldap 2.4, updated to version 1.1.4
- Static libraries are no longer built (they were just deleted anyway)

* Fri Sep 12 2008 David Diffenbaugh <davediff@nbcs.rutgers.edu> - 1.1.3-1
- updated to 1.1.3

* Tue Aug 5 2008 David Diffenbaugh <davediff@nbcs.rutgers.edu> - 1.1.2-1
- bumped to latest

* Tue Jul 15 2008 Brian Schubert <schubert@nbcs.rutgers.edu> - 1.1.1-2
- Added CFLAGS for debugging, added %doc directive

* Tue Jun 24 2008 Brian Schubert <schubert@nbcs.rutgers.edu> - 1.1.1-1
- Updated to version 1.1.1

* Thu Jun 19 2008 David Diffenbaugh <davediff@nbcs.rutgers.edu> - 1.1.rc11-1
- updated to 1.1.rc11

* Fri Jan 4 2008 Naveen Gavini <ngavini@nbcs.rutgers.edu> - 1.0.10-1
- Updated to 1.0.10-1

* Tue Nov 6 2007 Naveen Gavini <ngavini@nbcs.rutgers.edu> - 1.0.7-1
- Updated to 1.0.7-1
