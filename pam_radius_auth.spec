%define name pam_radius_auth
%define version 1.3.16
%define release 0

Name: %{name}
Summary: PAM Module for RADIUS Authentication
Version: %{version}
Release: %{release}
Source: ftp://ftp.freeradius.org/pub/radius/pam_radius-%{version}.tar
Patch0: pam_radius-1.3.16-Makefile.patch
Patch1: pam_radius-1.3.16-typedef.patch
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
%patch0 -p1
%patch1 -p1

%build
PATH="/opt/SUNWspro/bin:/usr/ccs/bin:${PATH}"
export PATH

%ifarch sparc64
mkdir sparcv9
gmake CFLAGS='-xarch=generic64 -xcode=pic32 -g -xs -KPIC -DCONF_FILE=\"/usr/local/etc/raddb/server\"'
mv pam_radius_auth.so sparcv9
gmake clean
%endif

gmake CFLAGS='-g -xs -KPIC -DCONF_FILE=\"/usr/local/etc/raddb/server\"' 

%install
mkdir -p %{buildroot}/usr/lib/security
mkdir -p %{buildroot}/usr/lib/security/sparcv9

cp -p pam_radius_auth.so %{buildroot}/usr/lib/security

%ifarch sparc64
cp -p sparcv9/pam_radius_auth.so %{buildroot}/usr/lib/security/sparcv9
%endif

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
%ifarch sparc64
/usr/lib/security/sparcv9/pam_radius_auth.so
%endif

%changelog
* Fri Nov 10 2006 Eric Rivas <kc2hmv@nbcs.rutgers.edu> 1.3.16-0
 - Update to latest and build 64-bit version.

