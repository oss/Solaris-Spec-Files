Name: logrotate
Version: 3.6.5
Release: 3
Group: System Environment/Base
Copyright: GPL
Packager: Douglas M. Motto <dmotto@cs.rutgers.edu>
Source: logrotate-%{version}.tar.gz
Patch: logrotate-%{version}-solaris.patch
BuildRoot: /var/tmp/%{name}-root
#BuildRequires: rpm-devel
Summary: GNU 
Requires: gzip, vpkg-SUNWcsu
%description
The logrotate utility is designed to simplify the administration of
log files on a system which generates a lot of log files.  Logrotate
allows for the automatic rotation compression, removal and mailing of
log files.  Logrotate can be set to handle a log file daily, weekly,
monthly or when the log file gets to a certain size.  Normally,
logrotate runs as a daily cron job.

Install the logrotate package if you need a utility to deal with the
log files on your system.

This is logrotate straight off the RedHat 8.0 distribution ported
for solaris8.

%prep
%setup -q
%patch -p 1

%build
make RPM_OPT_FLAGS=-O2 BINDIR=%{_exec_prefix}

%install
rm -rf $RPM_BUILD_ROOT
make PREFIX=$RPM_BUILD_ROOT MANDIR=%{_mandir} install
mkdir -p $RPM_BUILD_ROOT/usr/local/etc/logrotate.d
mkdir -p $RPM_BUILD_ROOT/usr/local/etc/cron.daily
mkdir -p $RPM_BUILD_ROOT/usr/local/var/lib

install -m 644 examples/logrotate-default $RPM_BUILD_ROOT/usr/local/etc/logrotate.conf
install -m 755 examples/logrotate.cron $RPM_BUILD_ROOT/usr/local/etc/cron.daily/logrotate
touch $RPM_BUILD_ROOT/usr/local/var/lib/logrotate.status



%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root)
%doc CHANGES COPYING README.HPUX README.SOLARIS
%attr(0755, root, root) %{_sbindir}/logrotate
%attr(0644, root, root) %{_mandir}/man8/logrotate.8*
%attr(0755, root, root) %{_sysconfdir}/cron.daily/logrotate
%attr(0644, root, root) %config(noreplace) %{_sysconfdir}/logrotate.conf
%attr(0755, root, root) %dir %{_sysconfdir}/logrotate.d
%attr(0644, root, root) %verify(not size md5 mtime) %config(noreplace) %{_localstatedir}/lib/logrotate.status








