Summary:	Small and fast DNS server for serving blacklist zones.
Name:		rbldnsd
Version:	0.996b
Release:        1
License:	GPL
Group:		Applications/DNS
Distribution:   RU-Solaris
Vendor:         NBCS-OSS
Packager:       Naveen Gavini <ngavini@nbcs.rutgers.edu>
Url:		http://www.corpit.ru/mjt/software.html
Source:		%{name}_%{version}.tar.gz
Source1:	sync_lists.sh
Source2:	test.ru
Source3:	rbldnsd.sh
BuildRoot:	/var/tmp/%{name}_%{version}-root
Requires:	rsync

%description
rbldnsd is a small and fast DNS daemon which is especially made to serve
DNSBL zones. This daemon was inspired by Dan J. Bernstein's rbldns program
found in the djbdns package.

rbldnsd is extremely fast - it outperforms both bind and djbdns greatly. It
has very small memory footprint.

The daemon can serve both IP-based (ordb.org, dsbl.org etc) and name-based
(rfc-ignorant.org) blocklists. Unlike DJB's rbldns, it has ability to specify
individual values for every entry, can serve as many zones on a single IP
address as you wish, and, finally, it is a real nameserver: it can reply
to DNS metadata requests. The daemon keeps all zones in memory for faster
operations, but its memory usage is very efficient, especially for repeated
TXT values which are stored only once.


%prep
%setup -q

%build
PATH="/opt/SUNWspro/bin:${PATH}" \
CC="cc" CXX="CC" CPPFLAGS="-I/usr/local/include" \
CFLAGS="-D__unix__" \
LD="/usr/ccs/bin/ld" \
LDFLAGS="-L/usr/local/lib -R/usr/local/lib" \
LIBXML_LIBS="-lxml2" \
export PATH CC CXX CPPFLAGS LD LDFLAGS LIBXML_LIBS CFLAGS 

./configure

gmake

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}
/usr/local/gnu/bin/install -Dp -m0555 rbldnsd %{buildroot}%{_sbindir}/rbldnsd
/usr/local/gnu/bin/install -Dp -m0444 rbldnsd.8 %{buildroot}%{_mandir}/man8/rbldnsd.8
#/usr/local/gnu/bin/install -Dp -m0664 debian/rbldnsd.default %{buildroot}%{_sysconfdir}/sysconfig/rbldnsd
#/usr/local/gnu/bin/install -Dp -m0555 debian/rbldnsd.init %{buildroot}%{_initrddir}/rbldnsd
/usr/local/gnu/bin/install -Dp -m0744 %{SOURCE1} %{buildroot}/usr/local/etc/rbldnsd/sync_lists.sh
/usr/local/gnu/bin/install -Dp -m0644 %{SOURCE2} %{buildroot}/usr/local/etc/rbldnsd/test.ru
/usr/local/gnu/bin/install -Dp -m0744 %{SOURCE3} %{buildroot}/usr/local/etc/rbldnsd/rbldnsd.sh

%clean
rm -rf $RPM_BUILD_ROOT

%files
%doc
%defattr(-,bin,bin)
#/usr/local/etc/sysconfig/rbldnsd
/usr/local/man/man8/rbldnsd.8
/usr/local/sbin/rbldnsd
/usr/local/etc/rbldnsd/sync_lists.sh
/usr/local/etc/rbldnsd/test.ru
/usr/local/etc/rbldnsd/rbldnsd.sh

%changelog
* Tue Dec 08 2009 Jarek Sedlacek <jarek@nbcs.rutgers.edu> - 0.996b-1
- Updated to version .996b
- changed %install to use /usr/local/gnu/bin/install instead of /usr/ucb/install
* Tue Feb 19 2008 Naveen Gavini <ngavini@nbcs.rutgers.edu> - 1.0.7-1
- Initial Build
