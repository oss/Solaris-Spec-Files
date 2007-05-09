
%define name 	nagios
%define version 3.0a4
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
	--localstatedir="%{_localstatedir}/log/%{name}" \
	--sbindir="%{_libdir}/%{name}/cgi" \
	--sysconfdir="%{_sysconfdir}/%{name}" \
	--with-cgiurl="/%{name}/cgi-bin" \
	--with-command-user="www" \
	--with-command-group="nagiocmd" \
	--with-gd-lib="%{_libdir}" \
	--with-gd-inc="%{_includedir}" \
	--with-htmurl="/%{name}" \
	--with-init-dir="%{_initrddir}" \
	--with-lockfile="%{_localstatedir}/run/nagios.pid" \
	--with-mail="/bin/mailx" \
	--with-nagios-user="nagios" \
	--with-nagios-group="nagios" \
	--with-template-objects \
	--with-template-extinfo
%{__make} %{?_smp_mflags} all
%{__make} %{?_smp_mflags} -C contrib

%install
%{__rm} -rf %{buildroot}
%{__make} install install-init install-commandmode install-config \
        DESTDIR="%{buildroot}" \
        INSTALL_OPTS="" \
        COMMAND_OPTS="" \
        INIT_OPTS=""


#for file in %{buildroot}%{_sysconfdir}/%{name}/*.cfg-sample; do
#	%{__mv} -f $file ${file%%-*}
#done

%{__make} install -C contrib \
	DESTDIR="%{buildroot}" \
	INSTALL_OPTS=""

%{__install} -d -m0755 %{buildroot}%{_libdir}/nagios/plugins/eventhandlers/
%{__cp} -afpv contrib/eventhandlers/* %{buildroot}%{_libdir}/nagios/plugins/eventhandlers/

%{__install} -d -m0755 %{buildroot}%{_includedir}/nagios/
%{__install} -p -m0644 include/*.h %{buildroot}%{_includedir}/nagios/

%{__install} -Dp -m0644 sample-config/httpd.conf %{buildroot}%{_sysconfdir}/%{name}/nagios.conf

### Install logos
tar -xvz -C %{buildroot}%{_datadir}/nagios/images/logos -f %{SOURCE1}

%pre
if ! /usr/bin/id nagios &>/dev/null; then
	/usr/sbin/useradd -r -d %{_localstatedir}/log/nagios -s /bin/sh -c "nagios" nagios || \
		%logmsg "Unexpected error adding user \"nagios\". Aborting installation."
fi
if ! /usr/bin/getent group nagiocmd &>/dev/null; then
	/usr/sbin/groupadd nagiocmd &>/dev/null || \
		%logmsg "Unexpected error adding group \"nagiocmd\". Aborting installation."
fi

%post

if /usr/bin/id www &>/dev/null; then
	if ! /usr/bin/id -Gn apache 2>/dev/null | grep -q nagios ; then
		/usr/sbin/usermod -G nagios,nagiocmd www &>/dev/null
	fi
else
	%logmsg "User \"www\" does not exist and is not added to group \"nagios\". Sending commands to Nagios from the command CGI is not possible."
fi

if [ -f /usr/local/apache/conf/httpd.conf ]; then
	if ! grep -q "Include .*/nagios.conf" /usr/local/apache/conf/httpd.conf; then
		echo -e "\n# Include %{_sysconfdir}/%{name}/nagios.conf" >> /usr/local/apache/conf/httpd.conf; then
		/sbin/service httpd restart
	fi
fi

echo "================================"
echo "WARNING: THIS IS AN ALPHA BUILD."
echo "================================"

%preun
if [ $1 -eq 0 ]; then
	/etc/init.d/nagios stop &>/dev/null || :
fi

%postun
if [ $1 -eq 0 ]; then
	/usr/sbin/userdel nagios || %logmsg "User \"nagios\" could not be deleted."
	/usr/sbin/groupdel nagios || %logmsg "Group \"nagios\" could not be deleted."
fi

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
%config(noreplace) %{_sysconfdir}/nagios/*.cfg
%{_localstatedir}/log/nagios/

%defattr(-, nagios, www, 2755)
%{_localstatedir}/log/nagios/rw/

%files devel
%defattr(-, root, root, 0755)
%{_includedir}/nagios/

%changelog
* Tue May 08 2007 David Lee Halik <dhalik@nbcs.rutgers.edu> - 3.0a4-1
- Version bump.
* Sat Apr 27 2007 David Lee Halik <dhalik@nbcs.rutgers.edu> - 3.0a3-1
- Initial Nagios 3 Build.

