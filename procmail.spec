Name: procmail
Version: 3.21
Copyright: GPL/Artistic
Group: System Environment/Base
Summary: procmail mail filtering system
Release: 1
Source: procmail-%{version}.tar.gz
BuildRoot: /var/tmp/%{name}-root

%description
Procmail is a mail filtering program.  Install this package if you
want to filter your mail.

%prep
%setup -q

%build
make LOCKINGTEST="/var/tmp /tmp ." CC="gcc"

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/local
make install BASENAME=$RPM_BUILD_ROOT/usr/local

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc Artistic COPYING examples/*
%attr(644, bin, bin) /usr/local/man/man1/procmail.1
%attr(644, bin, bin) /usr/local/man/man1/formail.1
%attr(644, bin, bin) /usr/local/man/man1/lockfile.1
%attr(644, bin, bin) /usr/local/man/man5/procmailrc.5
%attr(644, bin, bin) /usr/local/man/man5/procmailsc.5
%attr(644, bin, bin) /usr/local/man/man5/procmailex.5
%attr(6755, root, mail) /usr/local/bin/procmail
%attr(2755, root, mail) /usr/local/bin/lockfile
/usr/local/bin/formail
/usr/local/bin/mailstat
