Summary: ISC DHCP
Name: dhcp
Version: 3.1.1
Release: 8
Group: Applications/Internet
Copyright: Unique
Source0: dhcp-%{version}.tar.gz
Source1: dhcp-init.d
Source2: dhcpd.conf
BuildRoot: /var/tmp/%{name}-root

%description
ISC DHCP Server and Client.


%prep
%setup -q

%build
PATH="/opt/SUNWspro/bin:/usr/ccs/bin:/bin:/usr/bin" \
CC="cc" CFLAGS="-g -xs" \
export PATH CC CFLAGS

./configure

make

%install
rm -rf $RPM_BUILD_ROOT

make install DESTDIR=$RPM_BUILD_ROOT

mv $RPM_BUILD_ROOT/usr/share $RPM_BUILD_ROOT/usr/local
mv $RPM_BUILD_ROOT/usr/sbin $RPM_BUILD_ROOT/usr/local
mv $RPM_BUILD_ROOT/usr/bin $RPM_BUILD_ROOT/usr/local
mv $RPM_BUILD_ROOT/etc $RPM_BUILD_ROOT/usr/local
mv $RPM_BUILD_ROOT/sbin/* $RPM_BUILD_ROOT/usr/local/sbin

mkdir -p $RPM_BUILD_ROOT/etc/init.d/
cp %{SOURCE1} $RPM_BUILD_ROOT/etc/init.d/dhcpd
chmod 755 $RPM_BUILD_ROOT/etc/init.d/dhcpd
cp %{SOURCE2} $RPM_BUILD_ROOT/usr/local/etc/

%clean
rm -rf $RPM_BUILD_ROOT

%post
cat<<EOF

Link the startup script, /etc/init.d/dhcpd, to the correct rc directory for
dhcpd to start at runtime.

EOF

%files
%doc LICENSE README RELNOTES
%defattr(-,root,bin)
/usr/local/share/man/man4/*
/usr/local/share/man/man3/*
/usr/local/share/man/man1m/*
/usr/local/share/man/man1/*
/usr/local/lib/*
/usr/local/include/omapip/*
/usr/local/include/isc-dhcp/*
/usr/local/include/dhcpctl.h
/usr/local/sbin/dhcpd
/usr/local/sbin/dhcrelay
/usr/local/bin/omshell
/usr/local/sbin/dhclient
/usr/local/sbin/dhclient-script
%config(noreplace)/usr/local/etc/dhcpd.conf
%config(noreplace)/etc/init.d/dhcpd
%config(noreplace)/usr/local/etc/dhcpd.leases

%changelog
* Tue Aug 05 2008 David Diffenbaugh <davediff@nbcs.rutgers.edu> - 3.1.1-8
- some more changes to dhcpd init script
* Thu Jul 31 2008 David Diffenbaugh <davediff@nbcs.rutgers.edu> - 3.1.1-7
- switched dhcpd script to sh instead of bash
* Wed Jul 30 2008 David Diffenbaugh <davediff@nbcs.rutgers.edu> - 3.1.1-6
- final tweaks to dhcpd script
* Wed Jun 17 2008 David Diffenbaugh <davediff@nbcs.rutgers.edu> - 3.1.1-5
- more tweaks to dhcpd script
* Wed May 28 2008 David Diffenbaugh <davediff@nbcs.rutgers.edu> - 3.1.1-4
- tweaked dhcpd script
* Tue May 27 2008 David Diffenbaugh <davediff@nbcs.rutgers.edu> - 3.1.1-3
- updated to 3.1.1, changed to gmake, added new /etc/init.d/dhcpd script
- updated environment variables
