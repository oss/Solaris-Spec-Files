%define name pam_radius_auth
%define version 1.3.15
%define release 0

Name: %{name}
Summary: PAM Module for RADIUS Authentication
Version: %{version}
Release: %{release}
Source: ftp://ftp.freeradius.org/pub/radius/pam_radius_auth-%{version}.tar
URL: http://www.freeradius.org/pam_radius_auth/
Group: System Environment/Libraries
BuildRoot: %{_tmppath}/%{name}-buildroot
License: BSD-like or GNU GPL

%description
This is the PAM to RADIUS authentication module. It allows any PAM-capable
machine to become a RADIUS client for authentication and accounting
requests. You will need a RADIUS server to perform the actual
authentication.

%prep
%setup -q -n pam_radius-%{version}

%build
make CC=/opt/SUNWspro/bin/cc CFLAGS='-KPIC -O -DCONF_FILE=\"/usr/local/etc/raddb/server\"' 
# stupid linuxism
/usr/ccs/bin/ld -G pam_radius_auth.o md5.o -lpam -lsocket -lnsl -o pam_radius_auth.so

%install
mkdir -p %{buildroot}/usr/lib/security
cp -p pam_radius_auth.so %{buildroot}/usr/lib/security
mkdir -p %{buildroot}/usr/local/etc/raddb
[ -f %{buildroot}/usr/local/etc/raddb/server ] || cp -p pam_radius_auth.conf %{buildroot}/usr/local/etc/raddb/server
#chown root %{buildroot}/usr/local/etc/raddb/server
#chgrp root %{buildroot}/usr/local/etc/raddb/server
chmod 0600 %{buildroot}/usr/local/etc/raddb/server

%clean
[ "$RPM_BUILD_ROOT" != "/" ] && rm -rf $RPM_BUILD_ROOT

%postun
rmdir /usr/local/etc/raddb || true

%files
%defattr(-,root,root,0755)
%doc README INSTALL USAGE Changelog
%config /usr/local/etc/raddb/server
/usr/lib/security/pam_radius_auth.so

%changelog
* Mon Jun 03 2002 Richie Laager <rlaager@wiktel.com> 1.3.15-0
- Inital RPM Version
