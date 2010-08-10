Name:		sudo
Version:	1.7.4p1
Release:	1
License:	ISC-style
Group:		System Environment/Base
Summary:	executable and config files need to run sudo
URL:            http://www.sudo.ws/
Source:		http://www.sudo.ws/sudo/dist/sudo-%{version}.tar.gz
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

%description
Sudo (superuser do) allows a system administrator to give certain users
(or groups of users) the ability to run some (or all) commands as root
or another user while logging the commands and arguments.

This package contains sudo, sudoers (a config file) and visudo (an editor
that must/should be used to edit sudoers).

%prep
%setup -q

%build
%configure \
            --with-pam --with-insults --with-all-insults \
            --disable-root-sudo --disable-path-info \
            --with-secure-path=/usr/local/sbin:/usr/sbin:/sbin:/usr/local/bin:/usr/bin:/bin:/usr/ucb:/usr/ccs/bin:/usr/local/gnu/bin 
gmake -j3

%install
gmake install DESTDIR=%{buildroot}
cp sudoers %{buildroot}/usr/local/etc

#Get rid of evil .la
rm -f %{buildroot}/usr/local/libexec/sudo_noexec.la
rm -fr %{buildroot}/usr/local/share/doc/sudo/

# hardlink badness GO AWAY
cd %{buildroot}/usr/local
/usr/local/bin/unhardlinkify.py ./

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc README* HISTORY ChangeLog INSTALL* PORTING UPGRADE TROUBLESHOOTING LICENSE TROUBLESHOOTING WHATSNEW sample*

%attr(4711,root,root) /usr/local/bin/sudo
%config(noreplace) %attr(0440,root,root) /usr/local/etc/sudoers
/usr/local/bin/sudoreplay
/usr/local/sbin/visudo
%attr(4711,root,root) /usr/local/bin/sudoedit
/usr/local/libexec/sudo_noexec.so
/usr/local/share/man/*/*

%changelog
* Fri Aug 06 2010 Orcan Ogetbil <orcan@nbcs.rutgers.edu> - 1.7.4p1-1
- update to latest
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
