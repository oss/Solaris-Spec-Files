Summary: Analyzes and Reports on system logs
Name: logwatch
Version: 5.2.2
Release: 2
Vendor: Kirk Bauer <kirk@kaybee.org>
License: MIT
Group: Utilities/System
URL: http://www.logwatch.org
#BuildArch: noarch
Source: ftp://ftp.kaybee.org/pub/linux/logwatch-5.2.2.tar.gz
Requires: perl,textutils,sh-utils,grep
BuildRoot: %{_tmppath}/logwatchbuild/

%description
Logwatch is a customizable, pluggable log-monitoring system.  It will go
through your logs for a given period of time and make a report in the areas
that you wish with the detail that you wish.  Easy to use - works right out
of the package on many systems.


%prep
%setup

%build


%install
install -m 0755 -d %{buildroot}%{_sysconfdir}/log.d/conf/logfiles
install -m 0755 -d %{buildroot}%{_sysconfdir}/log.d/conf/services
install -m 0755 -d %{buildroot}%{_sysconfdir}/log.d/scripts/services
install -m 0755 -d %{buildroot}%{_sysconfdir}/log.d/scripts/shared
install -m 0755 -d %{buildroot}%{_sysconfdir}/log.d/lib


echo %{buildroot}
echo %{_sysconfdir}
echo %{buildroot}%{_sysconfdir}

install -m 755 scripts/logwatch.pl %{buildroot}%{_sysconfdir}/log.d/scripts/logwatch.pl

echo no paren error yet

for i in scripts/logfiles/* ; do
   if [ `ls $i | wc -l` -ne 0 ] ; then
      install -m 0755 -d %{buildroot}%{_sysconfdir}/log.d/$i
      install -m 0755 $i/* %{buildroot}%{_sysconfdir}/log.d/$i
   fi
done
install -m 0755 scripts/services/* %{buildroot}%{_sysconfdir}/log.d/scripts/services
install -m 0755 scripts/shared/* %{buildroot}%{_sysconfdir}/log.d/scripts/shared
install -m 0755 lib/* %{buildroot}%{_sysconfdir}/log.d/lib

install -m 0644 conf/logwatch.conf %{buildroot}%{_sysconfdir}/log.d/conf/logwatch.conf
install -m 0644 conf/logfiles/* %{buildroot}%{_sysconfdir}/log.d/conf/logfiles
install -m 0644 conf/services/* %{buildroot}%{_sysconfdir}/log.d/conf/services

install -m 0755 -d %{buildroot}%{_mandir}/man8
install -m 0644 logwatch.8 %{buildroot}%{_mandir}/man8

rm -f %{buildroot}%{_sysconfdir}/log.d/logwatch \
   %{buildroot}%{_sysconfdir}/log.d/logwatch.conf \
   %{buildroot}%{_sysconfdir}/cron.daily/logwatch \
   %{buildroot}%{_sbindir}/logwatch

ln -s scripts/logwatch.pl %{buildroot}%{_sysconfdir}/log.d/logwatch
ln -s conf/logwatch.conf %{buildroot}%{_sysconfdir}/log.d/logwatch.conf
install -m 0755 -d %{buildroot}%{_sysconfdir}/cron.daily
ln -s ../log.d/scripts/logwatch.pl %{buildroot}%{_sysconfdir}/cron.daily/0logwatch
install -m 0755 -d %{buildroot}%{_sbindir}
ln -s ../..%{_sysconfdir}/log.d/scripts/logwatch.pl %{buildroot}%{_sbindir}/logwatch


%clean
rm -rf %{buildroot}

%post


%pre


%preun


%postun


%files
%defattr(-,root,root)
%doc README HOWTO-Make-Filter
%dir %{_sysconfdir}/log.d
%dir %{_sysconfdir}/log.d/conf
%dir %{_sysconfdir}/log.d/scripts
%dir %{_sysconfdir}/log.d/conf/logfiles
%dir %{_sysconfdir}/log.d/conf/services
%dir %{_sysconfdir}/log.d/scripts/logfiles
%dir %{_sysconfdir}/log.d/scripts/services
%dir %{_sysconfdir}/log.d/scripts/shared
%dir %{_sysconfdir}/log.d/scripts/logfiles/*
%dir %{_sysconfdir}/log.d/lib
%config %{_sysconfdir}/log.d/conf/logwatch.conf
%config %{_sysconfdir}/log.d/conf/services/*
%config %{_sysconfdir}/log.d/conf/logfiles/*
%{_sysconfdir}/log.d/scripts/logwatch.pl
%{_sbindir}/logwatch
%{_sysconfdir}/log.d/scripts/shared/*
%{_sysconfdir}/log.d/scripts/services/*
%{_sysconfdir}/log.d/scripts/logfiles/*/*
%{_sysconfdir}/log.d/logwatch
%{_sysconfdir}/log.d/lib/Logwatch.pm
%{_sysconfdir}/log.d/logwatch.conf
%{_sysconfdir}/cron.daily/0logwatch
%doc %{_mandir}/man8/logwatch.8*

%doc License project/CHANGES project/TODO

%changelog
* Mon Nov 03 2003 Kirk Bauer <kirk@kaybee.org> pre5.0-1
- Now can build without change as non-root user

* Thu Feb 27 2003 Erik Ogan <erik@ogan.net> 4.3.2
- Added libdir & lib/Logwatch.pm
	
* Sun Oct 13 2002 Kirk Bauer <kirk@kaybee.org> pre4.0-14
- Changed the 'logwatch' cron.daily job to '0logwatch' to run before logrotate

* Thu Oct 10 2002 Kirk Bauer <kirk@kaybee.org> pre4.0-1
- Cronjob is now just named logwatch and not 00-logwatch

* Wed May 01 2002 Kirk Bauer <kirk@kaybee.org> 3.0-6
- up2date packaged... finally!

* Wed May 01 2002 Kirk Bauer <kirk@kaybee.org> 3.0-5
- Hopefully now properly included the up2date filter!

* Mon Apr 29 2002 Kirk Bauer <kirk@kaybee.org> pre3.0-1
- Now properly includes logfile-specific scripts

* Tue Apr 09 2002 Kirk Bauer <kirk@kaybee.org> 2.8-2
- Made man page entry in files list backwards compatible

* Thu Mar 28 2002 Kirk Bauer <kirk@kaybee.org> 2.5-2
- Updated new changes from Red Hat's rawhide packaging

* Wed Nov 18 1998 Kirk Bauer <kirk@kaybee.org>
- Modified to comply with RHCN standards

* Sun Feb 23 1998 Kirk Bauer <kirk@kaybee.org>
- Minor changes and addition of man-page

* Sun Feb 22 1998 Kirk Bauer <kirk@kaybee.org>
- initial release

