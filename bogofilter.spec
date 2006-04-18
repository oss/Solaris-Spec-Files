%define name    bogofilter 
%define ver     1.0.2
%define rel     1

Summary: Bogofilter: Fast anti-spam filtering by Bayesian statistical analysis
Name: %{name}
Version: %{ver} 
Release: %{rel}
Copyright: GPL
Group:          Networking/Mail
URL:            http://bogofilter.sourceforge.net
Source0:        %{name}-%{ver}.tar.gz
Distribution: RU-Solaris
Vendor: NBCS-OSS
Requires: db4
BuildRequires: db4
BuildRoot: %{_tmppath}/%{name}-root


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

%build
CC="gcc" CFLAGS="-I/usr/local/include" \
LDFLAGS="-R/usr/local/lib -L/usr/local/lib" \
  ./configure --prefix=/usr/local
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
