
%define name 	nagios
%define version 3.0b5
%define release 1
%define prefix  /usr/local
%define nagpath %{prefix}/%{name}
%define _initrddir /etc/init.d

Summary:	Open Source host, service and network monitoring program
Name:		nagios
Version:	%{version}
Release:	%{release}
License:	GPL
Group:		Applications/System
URL:		http://www.nagios.org/
Packager:	David Lee Halik <dhalik@nbcs.rutgers.edu>
Distribution:   RU-Solaris
Vendor:         NBCS-OSS
Source0:	%{name}-%{version}.tar.gz
Source1:	imagepak-base.tar.gz
Patch0:		perl_ver_bug.patch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root
BuildRequires:	gd-devel > 1.8, zlib-devel, libpng3-devel, libjpeg-devel

%description
Nagios is an application, system and network monitoring application.
It can escalate problems by email, pager or any other medium. It is
also useful for incident or SLA reporting.

Nagios is written in C and is designed as a background process,
intermittently running checks on various services that you specify.

The actual service checks are performed by separate "plugin" programs
which return the status of the checks to Nagios. The plugins are
located in the nagios-plugins package.

%package devel
Summary: Header files, libraries and development documentation for %{name}
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}

%description devel
This package contains the header files, static libraries and development
documentation for %{name}. If you like to develop programs using %{name},
you will need to install %{name}-devel.

%prep
%setup -q
%patch0 -p1

%build
PATH="/opt/SUNWspro/bin:${PATH}" \
CC="cc" CXX="CC" CPPFLAGS="-I/usr/local/include -I/usr/sfw/include" \
CFLAGS=$CPPFLAGS \
LD="/usr/ccs/bin/ld" \
LDFLAGS="-L/usr/local/lib -R/usr/local/lib -L/usr/sfw/lib -R/usr/sfw/lib" \
export PATH CC CXX CPPFLAGS LD LDFLAGS CFLAGS

./configure \
	--bindir="%{prefix}/bin" \
	--datadir="%{_datadir}/%{name}" \
	--libexecdir="%{_libdir}/%{name}/plugins" \
	--localstatedir="/var/log/%{name}" \
	--sbindir="%{_libdir}/%{name}/cgi" \
	--sysconfdir="%{_sysconfdir}/%{name}" \
	--with-cgiurl="/%{name}/cgi-bin" \
	--with-command-user="www" \
	--with-command-group="nagiocmd" \
	--with-gd-lib="%{_libdir}" \
	--with-gd-inc="%{_includedir}" \
	--with-htmurl="/%{name}" \
	--with-init-dir="%{_initrddir}" \
	--with-lockfile="/var/run/%{name}.pid" \
	--with-mail="/bin/mailx" \
	--with-nagios-user="nagios" \
	--with-nagios-group="nagios" \
	--with-template-objects \
	--with-template-extinfo

gmake -j3 all
gmake -j3 -C contrib

%install

mkdir -p %{buildroot}/var/log/nagios

%{__rm} -rf %{buildroot}

gmake install install-init install-commandmode install-config \
        DESTDIR="%{buildroot}" \
        INSTALL_OPTS="" \
        COMMAND_OPTS="" \
        INIT_OPTS=""

gmake install -C contrib \
	DESTDIR="%{buildroot}" \
	INSTALL_OPTS=""

%{__install} -d -m0755 %{buildroot}%{_libdir}/nagios/plugins/eventhandlers/
%{__cp} -afpv contrib/eventhandlers/* %{buildroot}%{_libdir}/nagios/plugins/eventhandlers/

%{__install} -d -m0755 %{buildroot}%{_includedir}/nagios/
%{__install} -p -m0644 include/*.h %{buildroot}%{_includedir}/nagios/

%{__install} -Dp -m0644 sample-config/httpd.conf %{buildroot}%{_sysconfdir}/%{name}/nagios.conf

### Install logos
tar -xvz -C %{buildroot}%{_datadir}/nagios/images/logos -f %{SOURCE1}

%post

cat << END
==========================NOTICE========================

You need to create a nagios group/user and nagiocmd group
if you have not done so already.

You will also need to add nagios.conf to Apache or link
it as such:

Ex: ln -s /usr/local/etc/nagios/nagios.conf \
	/usr/local/apache2/conf/extra/nagios.conf

==========================NOTICE========================
END


%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changelog INSTALLING LICENSE README UPGRADING
%config(noreplace) %{_sysconfdir}/%{name}/nagios.conf
%config %{_initrddir}/nagios
%{_bindir}/convertcfg
%{_bindir}/nagios
%{_bindir}/nagiostats
%{_bindir}/mini_epn
%{_bindir}/new_mini_epn
%{_libdir}/nagios/
%{_datadir}/nagios/

%defattr(-, nagios, nagios, 0755)
%dir %{_sysconfdir}/nagios/
%{_sysconfdir}/nagios/objects
%config(noreplace) %{_sysconfdir}/nagios/*.cfg
/var/log/nagios/

%defattr(-, nagios, www, 2755)
/var/log/nagios/rw/

%files devel
%defattr(-, root, root, 0755)
%{_includedir}/nagios/

%changelog
* Thu Sep 27 2007 David Lee Halik <dhalik@nbcs.rutgers.edu> - 3.0b4-1
- Bump to 3.0b4
* Thu Aug 30 2007 David Lee Halik <dhalik@nbcs.rutgers.edu> - 3.0b2-1
- Upgrade to 3.0b2
* Wed Aug 01 2007 David Lee Halik <dhalik@nbcs.rutgers.edu> - 3.0b1-5
- Bump
* Tue May 29 2007 David Lee Halik <dhalik@nbcs.rutgers.edu> - 3.0a4-4
- Playing with proper paths
* Tue May 29 2007 David Lee Halik <dhalik@nbcs.rutgers.edu> - 3.0a4-3
- Removed useradd junk, not playing nice in bash
* Wed May 16 2007 David Lee Halik <dhalik@nbcs.rutgers.edu> - 3.0a4-2
- Fixing useradd issues
* Tue May 08 2007 David Lee Halik <dhalik@nbcs.rutgers.edu> - 3.0a4-1
- Version bump.
* Sat Apr 27 2007 David Lee Halik <dhalik@nbcs.rutgers.edu> - 3.0a3-1
- Initial Nagios 3 Build.

