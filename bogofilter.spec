%define name    bogofilter
%define ver     1.2.1
%define rel     1

Summary:	Bogofilter: Fast anti-spam filtering by Bayesian statistical analysis
Name: 		%{name}
Version: 	%{ver} 
Release: 	%{rel}
License: 	GPL
Group:          Networking/Mail
URL:            http://bogofilter.sourceforge.net
Source0:        %{name}-%{ver}.tar.bz2
Distribution: 	RU-Solaris
Vendor: 	NBCS-OSS
Packager:       Brian Schubert <schubert@nbcs.rutgers.edu>
Requires: 	db4 >= 4.7
BuildRequires: 	db4-devel >= 4.7
BuildRoot: 	%{_tmppath}/%{name}-root
Patch0: 	bogoNFS.patch

%description
Bogofilter is a Bayesian spam filter.  In its normal mode of
operation, it takes an email message or other text on standard input,
does a statistical check against lists of "good" and "bad" words, and
returns a status code indicating whether or not the message is spam.
Bogofilter is designed with fast algorithms (including Berkeley DB system),
coded directly in C, and tuned for speed, so it can be used for production
by sites that process a lot of mail.


%prep
%setup -q
%patch -p1

%build
autoconf
CC="gcc" CFLAGS="-I/usr/local/include -I/usr/local/include/db4" \
LDFLAGS="-R/usr/local/lib -L/usr/local/lib" \
  ./configure --prefix=/usr/local --mandir=/usr/local/man --with-libdb-prefix=/usr/local/lib
gmake

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}
gmake install DESTDIR=%{buildroot}

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)

%doc AUTHORS COPYING INSTALL
%doc GETTING.STARTED
%doc NEWS README* RELEASE.NOTES TODO
%doc doc/bogofilter-tuning.HOWTO.html
%doc doc/bogofilter-SA-2002-01
%doc doc/integrating*
%doc doc/programmer
%doc doc/README.*db doc/rpm.notes.BerkeleyDB

%{_sysconfdir}/bogofilter.cf.example

%{_bindir}/bogofilter
%{_bindir}/bogolexer
%{_bindir}/bogotune
%{_bindir}/bogoutil
%{_bindir}/bogoupgrade
%{_bindir}/bf_copy
%{_bindir}/bf_compact
%{_bindir}/bf_tar

%{_mandir}/man1/bogofilter.1*
%{_mandir}/man1/bogolexer.1*
%{_mandir}/man1/bogotune.1*
%{_mandir}/man1/bogoutil.1*
%{_mandir}/man1/bogoupgrade.1*
%{_mandir}/man1/bf_compact.1*
%{_mandir}/man1/bf_copy.1*
%{_mandir}/man1/bf_tar.1*

%changelog 
* Thu Jan 07 2010 Russ Frank <rfranknj@nbcs.rutgers.edu> - 1.2.1-1
- Respin against BDB 4.8; update to 1.2.1
* Mon Oct 20 2008 Brian Schubert <schubert@nbcs.rutgers.edu> - 1.1.7-3
- Respin against BDB 4.7
* Tue Apr 06 2008 David Diffenbaugh <davediff@nbcs.rutgers.edu> - 1.1.7-1
- bumped
* Thu Jan 17 2008 Kevin Mulvey <kmulvey at nbcs dot rutgers dot edu> - 1.1.6-1
- Updated to 1.1.6
* Tue Jul 17 2007 Kevin Mulvey <kmulvey at nbcs dot rutgers dot edu> - 1.1.5-2
- added patch for NFS compatability
* Mon Apr 30 2007 Kevin Mulvey <kmulvey at nbcs dot rutgers dot edu> - 1.1.5-1
- Updated to 1.1.5
