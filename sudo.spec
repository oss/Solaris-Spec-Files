Name:		sudo
Version:	1.6.9p11
Copyright:	Courtesan Consulting
Group:		System Environment/Base
Summary:	executable and config files need to run sudo
Release:	2
Source:		%{name}-%{version}.tar.gz
BuildRoot:	/var/tmp/%{name}-root

%description
Sudo (superuser do) allows a system administrator to give certain users
(or groups of users) the ability to run some (or all) commands as root
or another user while logging the commands and arguments.

This package contains sudo, sudoers (a config file) and visudo (an editor
that must/should be used edit sudoers).

%prep
%setup -q

%build
PATH="/opt/SUNWspro/bin:${PATH}" \
CC="cc" CXX="CC" CPPFLAGS="-I/usr/local/include" \
CFLAGS="-D__unix__" \
LD="/usr/ccs/bin/ld" \
LDFLAGS="-L/usr/local/lib -R/usr/local/lib" \
export PATH CC CXX CPPFLAGS LD LDFLAGS  CFLAGS

./configure --prefix=/usr/local/  \
            --exec-prefix=/usr/local \
            --sysconfdir=/usr/local/etc \
            --with-pam --with-insults --with-all-insults \
            --disable-root-sudo --disable-path-info \
            --with-secure-path=/usr/local/sbin:/usr/sbin:/sbin:/usr/local/bin:/usr/bin:/bin:/usr/ucb:/usr/ccs/bin:/usr/local/gnu/bin 
gmake 

%install
gmake install DESTDIR=%{buildroot}
cp sudoers %{buildroot}/usr/local/etc

#Get rid of evil .la
rm -f %{buildroot}/usr/local/libexec/sudo_noexec.la

# hardlink badness GO AWAY
cd %{buildroot}/usr/local
/usr/local/bin/unhardlinkify.py ./


%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%attr(4611,root,root) /usr/local/bin/sudo
%config(noreplace) %attr(0440,root,root) /usr/local/etc/sudoers
/usr/local/sbin/visudo
/usr/local/bin/sudoedit
/usr/local/libexec/sudo_noexec.so
/usr/local/share/man/*

%changelog
* Tue Jan 8 2008 Naveen Gavini <ngavini@nbcs.rutgers.edu> - 1.6.9p11-1
- Bumped to latest version
* Fri Aug 10 2007 David Lee Halik <dhalik@nbcs.rutgers.edu> - 1.6.9p3-1
- Bumped to latest version
