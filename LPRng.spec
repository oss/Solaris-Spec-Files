%define name LPRng
%define version 3.8.9
%define release 3
%define prefix /usr/local

Summary: New generation of submitting print requests
Name: %name
Version: %version
Release: %release
Copyright: Artistic License
Group: Console/Printing
Source0: ftp://ftp.astart.com/pub/LPRng/LPRng/%{name}-%{version}.tgz
BuildRoot: /var/local/tmp/%{name}-root
Provides: lprng

%description
LPRng is the Next Generation in LPR software.

%prep
%setup

%build
./configure --disable-setuid  --libexecdir=/usr/local/etc 
make

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{prefix}/etc
mkdir -p $RPM_BUILD_ROOT/etc/init.d


make libexecdir=/usr/local/etc DESTDIR=$RPM_BUILD_ROOT POSTINSTALL="NO" install

install src/monitor $RPM_BUILD_ROOT/usr/local/bin

install init.solaris $RPM_BUILD_ROOT/etc/init.d/lprng
install lpd.conf $RPM_BUILD_ROOT%{prefix}/etc/lpd.conf
install printcap $RPM_BUILD_ROOT%{prefix}/etc/printcap
install lpd.perms $RPM_BUILD_ROOT%{prefix}/etc/lpd.perms

%post 
cat <<EOF
Config: /usr/local/etc/(lpd.conf|lpd.perms|printcap)
EOF
#The print services startup file (lprng) is in /etc/init.d
#Also to use the lpd.conf, lpd.perms, and printcap files change there extensions!
#cd /usr/local/etc
#mv lpd.conf.rpm lpd.conf
#mv lpd.perms.rpm lpd.perms
#mv printcap.rpm printcap


%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-, root, root)
%doc README LICENSE COPYRIGHT CHANGES HOWTO
%attr(0744, root, sys)/etc/init.d/lprng
%config(noreplace) %attr(0644, root, sysprog)%{prefix}/etc/lpd.conf
%config(noreplace) %attr(0644, root, sysprog)%{prefix}/etc/lpd.perms
%config(noreplace) %attr(0644, root, sysprog)%{prefix}/etc/printcap
%{prefix}/lib/*
%attr(4711, root, other)%{prefix}/bin/lpq
%attr(4711, root, other)%{prefix}/bin/lprm
%attr(4711, root, other)%{prefix}/bin/lpr

%attr(-, root, other)%{prefix}/bin/monitor
%attr(-, root, other)%{prefix}/bin/cancel

%attr(-, root, other)%{prefix}/bin/lpstat
%attr(-, root, other)%{prefix}/bin/lp
%attr(4711, root, other)%{prefix}/sbin/lpc
%attr(-, root, other)%{prefix}/sbin/lpd
%attr(-, root, other)%{prefix}/sbin/checkpc
%{prefix}/etc/filters/*
%{prefix}/man/man1/*
%{prefix}/man/man5/*
%{prefix}/man/man8/*





