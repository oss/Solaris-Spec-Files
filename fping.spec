Summary: fping
Name: fping	
Version: 2.4b2_to
Release: 1
Group: System/Libraries
Copyright: BSD-Like
Source: fping-%{version}.tar.gz
BuildRoot: /var/tmp/%{name}-root

%description
fping is a ping(1) like program which uses the Internet Control Message
Protocol (ICMP) echo request to determine if a host is up. fping is
different from ping in that you can specify any number of hosts on the
command line, or specify a file containing the lists of hosts to ping.
Instead of trying one host until it timeouts or replies, fping will send
out a ping packet and move on to the next host in a round-robin fashion.
If a host replies, it is noted and removed from the list of hosts to
check. If a host does not respond within a certain time limit and/or retry
limit it will be considered unreachable.

Unlike ping, fping is meant to be used in scripts and its output is easy
to parse.

%prep
%setup -q

%build
./configure
make

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,bin,bin)
/usr/*
