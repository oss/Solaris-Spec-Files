Summary: Trace the route ip packets going to a host
Name: traceroute
Version: 1.4a5
Release: 2
License: BSD
Group: Applications/Internet
Source: traceroute.tar.Z
Patch: traceroute.patch
BuildRoot: /var/tmp/%{name}-root
BuildRequires: autoconf 
BuildRequires: bison
BuildRequires: bash

%description
Attempt to trace the route an ip packet would follow to some internet
host.  We find out intermediate hops by launching probe packets with a
small ttl (time to live) then listening for an icmp "time exceeded"
reply from a gateway.  We start our probes with a ttl of one and
increase by one until we get an icmp "port unreachable" (which means
we got to "host") or hit a max (which defaults to 30 hops & can be
changed with the -m flag).  Three probes (change with -q flag) are
sent at each ttl setting and a line is printed showing the ttl,
address of the gateway and round trip time of each probe.  If the
probe answers come from different gateways, the address of each
responding system will be printed.  If there is no response within a 5
sec. timeout interval (changed with the -w flag), a "*" is printed for
that probe.

  [from traceroute.c]

%prep 
%setup -q
%patch -p1

# The patch changes configure.in so it does not define CANT_HACK_CHECKSUM
# on Solaris.

%build
autoconf
bash configure
make

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/local/sbin
mkdir -p $RPM_BUILD_ROOT/usr/local/man/man8
install traceroute $RPM_BUILD_ROOT/usr/local/sbin/traceroute
install traceroute.8 $RPM_BUILD_ROOT/usr/local/man/man8/traceroute.8

%clean
rm -rf $RPM_BUILD_ROOT

%post
cat <<EOF
Traceroute was installed setuid root.
EOF

%files
%defattr(-,bin,bin)
%doc VERSION CHANGES README traceroute.c
%attr(4555,root,other) /usr/local/sbin/traceroute
%attr(0444,bin,bin) /usr/local/man/man8/traceroute.8


