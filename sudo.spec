Name: sudo
Version: 1.6.7p5
Copyright: Courtesan Consulting
Group: System Environment/Base
Summary: executable and config files need to run sudo
Release: 1
Source: %{name}-%{version}.tar.gz
BuildRoot: /var/tmp/%{name}-root

%description
Sudo (superuser do) allows a system administrator to give certain users
(or groups of users) the ability to run some (or all) commands as root
or another user while logging the commands and arguments.

This package contains sudo, sudoers (a config file) and visudo (an editor
that must/should be used edit sudoers).

%prep
%setup -q

%build
./configure --prefix=/usr/local/  \
            --exec-prefix=/usr/local \
            --sysconfdir=/usr/local/etc \
            --with-pam --with-insults --with-all-insults \
            --disable-root-sudo --disable-path-info \
            --with-secure-path=/usr/local/sbin:/usr/sbin:/sbin:/usr/local/bin:/usr/bin:/bin:/usr/ucb:/usr/ccs/bin:/usr/local/gnu/bin 
make 

%install
make install DESTDIR=%{buildroot}
cp sudoers %{buildroot}/usr/local/etc

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%attr(4611,root,root) /usr/local/bin/sudo
%attr(0440,root,root) /usr/local/etc/sudoers
/usr/local/sbin/visudo
/usr/local/man/man1m/sudo.1m
/usr/local/man/man1m/visudo.1m
/usr/local/man/man4/sudoers.4
