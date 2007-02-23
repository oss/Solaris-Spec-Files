%include perl-header.spec

Summary: Rutgers Account Tools and Services (RATS)
Name: rats
Version: 3.0beta
Release: 1
Group: System Admin
Copyright: Rutgers University
# force perl at least 5.6.1.
Requires: perl > 5.6
#Requires: perl-module-CGI   # provided as part of perl 5.6 it seems
Requires: perl-module-Quota perl-module-RATSdes perl-module-TermReadKey perl-module-DBI
Source: %{name}-%{version}.tar
BuildRoot: /var/tmp/%{name}-root
BuildRequires: perl swig cpdir perl-module-DBI

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
PATH="/usr/local/bin/" sed  -e 's/@@@RPMVERSION@@@/\"%{version}\"/' etc/rats_internal.conf > temp
mv temp etc/rats_internal.conf

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/local/accounts
cp -Rp . $RPM_BUILD_ROOT/usr/local/accounts

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(0700, root, other)

%dir /usr/local/accounts

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
%attr(0600, root, other) /usr/local/accounts/etc/rats_internal.conf
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
%attr(0700, root, other) /usr/local/accounts/sbin/ratsd

%dir /usr/local/accounts/scripts

%dir /usr/local/accounts/user_cgi
%attr(0700, root, other) /usr/local/accounts/user_cgi/.htaccess.example
%attr(4700, root, other) /usr/local/accounts/user_cgi/user_chggcos.cgi
%attr(4700, root, other) /usr/local/accounts/user_cgi/user_chgpass.cgi
%attr(4700, root, other) /usr/local/accounts/user_cgi/user_chgshell.cgi

