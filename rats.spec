%include perl-header.spec

Summary: Rutgers Account Tools and Services (RATS)
Name: rats
Version: 2.13
Release: 1ru
Group: System Admin
Copyright: Rutgers University
# force perl at least 5.6.1.
Requires: perl > 5.6
#Requires: perl-module-CGI   # provided as part of perl 5.6 it seems
Requires: perl-module-Quota perl-module-RATSdes perl-module-TermReadKey perl-module-DBI
Source: %{name}-%{version}.tar.bz2
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

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/local/accounts
cpdir . $RPM_BUILD_ROOT/usr/local/accounts

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(0700, root, other)
%doc doc/*

%dir /usr/local/accounts

%dir /usr/local/accounts/bin
%attr(0700, root, other) /usr/local/accounts/bin/ratsadmin
%attr(0700, root, other) /usr/local/accounts/bin/ratsd
%attr(0700, root, other) /usr/local/accounts/bin/ratsut
%attr(0700, root, other) /usr/local/accounts/bin/fastcheck
%attr(0700, root, other) /usr/local/accounts/bin/ratscheck
%attr(0700, root, other) /usr/local/accounts/bin/rats_lock
%attr(0700, root, other) /usr/local/accounts/bin/ratsat
%attr(0700, root, other) /usr/local/accounts/bin/ratsfmt

%dir /usr/local/accounts/user_cgi
%attr(4700, root, other) /usr/local/accounts/user_cgi/user_chgshell.cgi
%attr(4700, root, other) /usr/local/accounts/user_cgi/user_chggcos.cgi
%attr(4700, root, other) /usr/local/accounts/user_cgi/user_chgpass.cgi
%attr(0700, root, other) /usr/local/accounts/user_cgi/.htaccess.example

%dir /usr/local/accounts/log

%dir /usr/local/accounts/doc

%dir /usr/local/accounts/scripts

%dir /usr/local/accounts/sbin
%attr(0700, root, other) /usr/local/accounts/sbin/ratsd

%dir /usr/local/accounts/etc
%attr(0600, root, other) /usr/local/accounts/etc/reserveg.example
%attr(0600, root, other) /usr/local/accounts/etc/reserve.example
%attr(0600, root, other) /usr/local/accounts/etc/rats_internal.conf
%attr(0600, root, other) /usr/local/accounts/etc/accounts.example
%attr(0600, root, other) /usr/local/accounts/etc/group.privs.example
%attr(0600, root, other) /usr/local/accounts/etc/rats.conf.example

%dir /usr/local/accounts/lib
%attr(0600, root, other) /usr/local/accounts/lib/RatsLib.pm
%attr(0600, root, other) /usr/local/accounts/lib/RatsClientLib.pm

# obsolete DES now in different package
#%attr(0755, root, other) /usr/local/accounts/lib/RUDes.pm
#%attr(0755, root, other) /usr/local/accounts/lib/des_safer.o
#%attr(0755, root, other) /usr/local/accounts/lib/makefile
#%attr(0755, root, other) /usr/local/accounts/lib/des_safer.c
#%attr(0755, root, other) /usr/local/accounts/lib/RUDes.so
#%attr(0755, root, other) /usr/local/accounts/lib/des_safer_wrap.c
#%attr(0755, root, other) /usr/local/accounts/lib/des_safer_wrap.o

%dir /usr/local/accounts/priv_cgi
%attr(4700, root, other) /usr/local/accounts/priv_cgi/vigr.cgi
%attr(4700, root, other) /usr/local/accounts/priv_cgi/setkerb.cgi
%attr(4700, root, other) /usr/local/accounts/priv_cgi/lock.cgi
%attr(0600, root, other) /usr/local/accounts/priv_cgi/users.example
%attr(0700, root, other) /usr/local/accounts/priv_cgi/.htaccess.example
%attr(4700, root, other) /usr/local/accounts/priv_cgi/cgipw.cgi

%dir /usr/local/accounts/cgi
%attr(4700, root, other) /usr/local/accounts/cgi/kerbshell_change.cgi
%attr(4700, root, other) /usr/local/accounts/cgi/rats.cgi

%dir /usr/local/accounts/contrib
%dir /usr/local/accounts/contrib/bin
%attr(0700, root, other) /usr/local/accounts/contrib/bin/reiid
