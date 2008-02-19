Summary:	Small and fast DNS server for serving blacklist zones.
Name:		rbldnsd
Version:	0.996a
Release:        1
Copyright:	GPL
Group:		Applications/DNS
Distribution:   RU-Solaris
Vendor:         NBCS-OSS
Packager:       Naveen Gavini <ngavini@nbcs.rutgers.edu>
Url:		http://www.corpit.ru/mjt/software.html
Source:		%{name}_%{version}.tar.gz
BuildRoot:	/var/tmp/%{name}_%{version}-root

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
LIBXML_LIBS="-lxml2"
export PATH CC CXX CPPFLAGS LD LDFLAGS LIBXML_LIBS CFLAGS

./configure

gmake

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}
install -Dp -m0555 rbldnsd %{buildroot}%{_sbindir}/rbldnsd
install -Dp -m0444 rbldnsd.8 %{buildroot}%{_mandir}/man8/rbldnsd.8
install -Dp -m0664 debian/rbldnsd.default %{buildroot}%{_sysconfdir}/sysconfig/rbldnsd
install -Dp -m0555 debian/rbldnsd.init %{buildroot}%{_initrddir}/rbldnsd

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,bin,bin)
/usr/local/etc/sysconfig/rbldnsd
/usr/local/man/man8/rbldnsd.8
/usr/local/sbin/rbldnsd

%changelog
* Tue Feb 19 2008 Naveen Gavini <ngavini@nbcs.rutgers.edu> - 1.0.7-1
- Initial Build
