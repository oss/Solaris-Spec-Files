Summary: DJB's DNS server
Name: djbdns
Version: 1.05
Release: 2
Group: Applications/Internet
Copyright: BSD-like
Requires: ucspi-tcp daemontools
BuildRequires: patch
Source: %{name}-%{version}.tar.gz
Patch: %{name}-%{version}.patch
BuildRoot: /var/tmp/%{name}-root
%description
djbdns is a collection of Domain Name System tools. It includes
several components:
  * The dnscache program is a local DNS cache. It accepts recursive
    DNS queries from local clients such as web browsers. It collects
    responses from remote DNS servers.
  * The tinydns program is a fast, UDP-only DNS server. It makes local
    DNS information available to the Internet. It supports load
    balancing and client differentiation.
  * The walldns program is a reverse DNS wall. It provides matching
    reverse and forward records while hiding local host information.
  * The rbldns program is an IP-address-listing DNS server. It uses
    DNS to publish a list of IP addresses, such as RBL or DUL.
  * The dns library handles outgoing and incoming DNS packets. It can
    be used by clients such as web browsers to look up host addresses,
    host names, MX records, etc. It supports asynchronous resolution.
  * The dnsfilter program is a parallel IP-address-to-host-name
    converter.
  * The dnsip, dnsipq, dnsname, dnstxt, and dnsmx programs are simple
    command-line interfaces to DNS.
  * The dnsq and dnstrace programs are DNS debugging tools.

 [ from the web page - http://cr.yp.to/djbdns.html ]

%prep
%setup -q
%patch -p1

%build
make

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/local $RPM_BUILD_ROOT/etc
make setup check
mv $RPM_BUILD_ROOT/etc/dnsroots.global $RPM_BUILD_ROOT/etc/dnsroots.global.rpm

%post
cat <<EOF
To complete the installation, copy /etc/dnsroots.global.rpm to 
/etc/dnsroots.global.
EOF

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc README
/usr/local/bin/*
/etc/dnsroots.global.rpm
