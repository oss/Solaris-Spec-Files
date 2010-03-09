#%include perl-header.spec

Summary: Rutgers Account Tools and Services (RATS)
Name: rats
Version: 4.1
Release: 4
Group: System Admin
License: Rutgers University
Requires: perl > 5.6
Requires: perl-module-Quota perl-module-RATSdes >= 3-1 perl-module-TermReadKey perl-module-DBI
Source: %{name}-%{version}.tar.bz2
BuildRoot: /var/tmp/%{name}-root
BuildRequires: perl 

%description
RATS stands for Rutgers Account Tools and Services. It is a suite of
daemons, clients, and tools that allow you to set up automated account
creation on your Unix machines running Solaris. It provides a means of
contacting a central repository of demographic information (the People
Data Base) about the population of Rutgers University for the purposes
of authentication and and access restriction with regards to account
creation.

%prep
%setup -q -n accounts

%build
# Perl script repackage; no compiling
# VERSION = @@@RPMVERSION@@@ to VERSION = %{version}
PATH="/usr/local/bin/" sed  -e 's/@@@RPMVERSION@@@/%{version}/' etc/rats_internal.conf > temp
mv temp etc/rats_internal.conf

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/local/accounts
cp -Rp . $RPM_BUILD_ROOT/usr/local/accounts
rm $RPM_BUILD_ROOT/usr/local/accounts/CHANGELOG
%clean
rm -rf $RPM_BUILD_ROOT

%post

%files
%doc CHANGELOG
%defattr(0700, root, other)

%dir /usr/local/accounts
%config /usr/local/accounts/etc/rats_internal.conf

%dir /usr/local/accounts/bin
%attr(0700, root, other) /usr/local/accounts/bin/fastcheck
%attr(0700, root, other) /usr/local/accounts/bin/rats_lock
%attr(0700, root, other) /usr/local/accounts/bin/ratscheck
%attr(0700, root, other) /usr/local/accounts/bin/ratsat
%attr(0700, root, other) /usr/local/accounts/bin/ratsadmin
%attr(0700, root, other) /usr/local/accounts/bin/ratsd
%attr(0700, root, other) /usr/local/accounts/bin/ratsfmt
%attr(0700, root, other) /usr/local/accounts/bin/ratsut
%attr(0700, root, other) /usr/local/accounts/bin/send
%attr(0700, root, other) /usr/local/accounts/bin/pwdcheck

%dir /usr/local/accounts/cgi
%attr(4700, root, other) /usr/local/accounts/cgi/kerbshell_change.cgi
%attr(4700, root, other) /usr/local/accounts/cgi/rats.cgi

%dir /usr/local/accounts/contrib
%dir /usr/local/accounts/contrib/bin
%attr(0700, root, other) /usr/local/accounts/contrib/bin/reiid

%dir /usr/local/accounts/doc

%dir /usr/local/accounts/etc
%attr(0600, root, other) /usr/local/accounts/etc/accounts.example
%attr(0600, root, other) /usr/local/accounts/etc/group.privs.example
%attr(0600, root, other) /usr/local/accounts/etc/rats.conf.example
#%attr(0600, root, other) /usr/local/accounts/etc/rats_internal.conf.example
%attr(0600, root, other) /usr/local/accounts/etc/reserve.example
%attr(0600, root, other) /usr/local/accounts/etc/reserveg.example

%dir /usr/local/accounts/lib
%attr(0600, root, other) /usr/local/accounts/lib/RatsClientLib.pm
%attr(0600, root, other) /usr/local/accounts/lib/RatsClientStyle.pm
%attr(0600, root, other) /usr/local/accounts/lib/RatsLib.pm

%dir /usr/local/accounts/log
%attr(0600, root, other) /usr/local/accounts/log/rats.log

%dir /usr/local/accounts/priv_cgi
%attr(0700, root, other) /usr/local/accounts/priv_cgi/.htaccess.example
%attr(4700, root, other) /usr/local/accounts/priv_cgi/cgipw.cgi
%attr(4700, root, other) /usr/local/accounts/priv_cgi/lock.cgi
%attr(4700, root, other) /usr/local/accounts/priv_cgi/setkerb.cgi
%attr(0600, root, other) /usr/local/accounts/priv_cgi/users-example
%attr(4700, root, other) /usr/local/accounts/priv_cgi/vigr.cgi

%dir /usr/local/accounts/sample
%dir /usr/local/accounts/sample/css2
%attr(0600, root, other) /usr/local/accounts/sample/css2/RATS.css
%attr(0600, root, other) /usr/local/accounts/sample/css2/RATS_CLIENT.css
%dir /usr/local/accounts/sample/css3
%attr(0600, root, other) /usr/local/accounts/sample/css3/RATS.css
%attr(0600, root, other) /usr/local/accounts/sample/css3/RATS_CLIENT.css
%dir /usr/local/accounts/sample/images2
%attr(0600, root, other) /usr/local/accounts/sample/images2/menu_off.gif
%attr(0600, root, other) /usr/local/accounts/sample/images2/menu_on.gif
%attr(0600, root, other) /usr/local/accounts/sample/images2/navl.gif
%attr(0600, root, other) /usr/local/accounts/sample/images2/navlh.gif
%attr(0600, root, other) /usr/local/accounts/sample/images2/navr.gif
%attr(0600, root, other) /usr/local/accounts/sample/images2/navrh.gif
%attr(0600, root, other) /usr/local/accounts/sample/images2/slim_short_banner.jpg
%attr(0600, root, other) /usr/local/accounts/sample/images2/small_seal.gif

%dir /usr/local/accounts/sbin
%attr(0700, root, other) /usr/local/accounts/sbin/ratsd.linux
%attr(0700, root, other) /usr/local/accounts/sbin/ratsd.solaris


%dir /usr/local/accounts/scripts

%dir /usr/local/accounts/user_cgi
%attr(0700, root, other) /usr/local/accounts/user_cgi/.htaccess.example
%attr(4700, root, other) /usr/local/accounts/user_cgi/user_chggcos.cgi
%attr(4700, root, other) /usr/local/accounts/user_cgi/user_chgpass.cgi
%attr(4700, root, other) /usr/local/accounts/user_cgi/user_chgshell.cgi
%doc

%changelog
* Mon Mar 08 2010 Jarek Sedlacek <jarek@nbcs.rutgers.edu> - 4.1-4
- rats_internal.conf moved to %config section of files (so it doesn't everwrite, etc)

* Fri Mar 05 2010 Jarek Sedlacek <jarek@nbcs.rutgers.edu> - 4.1-1
- Bumped to 4.1
- only copy rats.conf.example to rats.conf if rats.conf DOES NOT exist (in postinstall)

* Wed Jan 27 2010 Jarek Sedlacek <jarek@nbcs.rutgers.edu> - 4.0-2
- Requires perl-module-RATSdes >= 3-1
- added CHANGELOG to %doc
* Mon Nov 02 2009 Jarek Sedlacek <jarek@nbcs.rutgers.edu> - 4.0-1
 - Updated to latest version
 - Added post install section (copy default config file into place)
* Tue Jul 21 2009 Naveen Gavini <ngavini@nbcs.rutgers.edu> - 3.0-11
 - Updated vigr.cgi to vigr.cgi.beta.
* Thu Jul 19 2007 Eric Rivas <kc2hmv@nbcs.rutgers.edu> - 3.0-9
 - Update to 2007-07-19 second version.
* Thu Jul 19 2007 Eric Rivas <kc2hmv@nbcs.rutgers.edu> - 3.0-8
 - Update to 2007-07-19 version.
* Thu Jul 19 2007 Eric Rivas <kc2hmv@nbcs.rutgers.edu> - 3.0-7
 - Remove unneeded dep.
* Wed Jul 18 2007 Eric Rivas <kc2hmv@nbcs.rutgers.edu> - 3.0-6
 - Update to 2007-07-18 version.

