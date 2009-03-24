Name:		sudo
Version:	1.7.0
License:	ISC-style
Group:		System Environment/Base
Summary:	executable and config files need to run sudo
Release:	1
Source:		%{name}-%{version}.tar.gz
BuildRoot:	%{_tmppath}/%{name}-root

%description
Sudo (superuser do) allows a system administrator to give certain users
(or groups of users) the ability to run some (or all) commands as root
or another user while logging the commands and arguments.

This package contains sudo, sudoers (a config file) and visudo (an editor
that must/should be used to edit sudoers).

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
	    --mandir=/usr/local/man \
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
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc README* HISTORY ChangeLog INSTALL* PORTING UPGRADE TROUBLESHOOTING LICENSE TROUBLESHOOTING WHATSNEW

%attr(4711,root,root) /usr/local/bin/sudo
%config(noreplace) %attr(0440,root,root) /usr/local/etc/sudoers
/usr/local/sbin/visudo
%attr(4711,root,root) /usr/local/bin/sudoedit
/usr/local/libexec/sudo_noexec.so
/usr/local/man/*

%changelog
* Mon Mar 23 2009 Naveen Gavini <ngavini@nbcs.rutgers.edu> - 1.7.0
- bumped to 1.7.0
* Thu Oct 9 2008 David Diffenbaugh <davediff@nbcs.rutgers.edu> - 1.7.0rc2-1
- bumped to 1.7.0, changed %attr from 4611 to 4711 for sudo/sudoedit
* Wed Oct 1 2008 David Diffenbaugh <davediff@nbcs.rutgers.edu> - 1.6.9p17-3
- changed %attr to sudoedit instead of sudo
* Thu Sep 11 2008 David Diffenbaugh <davediff@nbcs.rutgers.edu> - 1.6.9p17-2
- respun due to bad rpm archive
* Fri Aug 22 2008 Brian Schubert <schubert@nbcs.rutgers.edu> - 1.6.9p17-1
- Updated to version 1.6.9p17
- Fixed man path, added docs
* Tue Jan 8 2008 Naveen Gavini <ngavini@nbcs.rutgers.edu> - 1.6.9p11-1
- Bumped to latest version
* Fri Aug 10 2007 David Lee Halik <dhalik@nbcs.rutgers.edu> - 1.6.9p3-1
- Bumped to latest version
