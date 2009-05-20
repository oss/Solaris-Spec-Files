Name:		dnstop
Version:	20090128
Release:	1
Group:		Applications/Network
License:	BSD
Source:		http://dns.measurement-factory.com/tools/dnstop/src/dnstop-%{version}.tar.gz
URL:		http://dns.measurement-factory.com/tools/dnstop
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires:	libpcap-devel

Summary:	libpcap application that displays DNS traffic tables

%description
dnstop is a libpcap  application (ala tcpdump) that displays various tables of DNS traffic 
on your network.

%prep
%setup -q

%build
PATH="/opt/SUNWspro/bin:/usr/ccs/bin:${PATH}"
CC="cc" CFLAGS="-I/usr/local/include -g -xs"
LDFLAGS="-L/usr/local/lib -R/usr/local/lib"
LIBS="-lresolv -lnsl -lsocket -lcurses -lpcap"
export PATH CC CFLAGS LDFLAGS LIBS

./configure --disable-ipv6
gmake

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_mandir}/man8

%{__install} -m 0755 dnstop %{buildroot}%{_bindir}
%{__install} -m 0644 dnstop.8 %{buildroot}%{_mandir}/man8

%files
%defattr(-, root, root)
%doc LICENSE CHANGES
%{_bindir}/dnstop
%{_mandir}/man8/dnstop.8

%changelog
* Wed May 20 2009 Brian Schubert <schubert@nbcs.rutgers.edu> - 20090128-1
- Initial build
