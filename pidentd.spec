Summary: IDENT daemon
Name: pidentd
Version: 3.0.11
Release: 2
Group: Applications/Internet
Copyright: BSD-type
Source: %{name}-%{version}.tar.gz
BuildRoot: /var/tmp/%{name}-root

%description
This daemon implements the IDENT protocol as specified in RFC1413 (see
the file rfc1413.txt in the doc subdirectory). It can be used to
identify the user who initiated a TCP/IP connection. It should
probably *NOT* be used for general authentication purposes.

%prep
%setup -q

%build
CC="/opt/SUNWspro/bin/cc" ./configure --prefix=/usr/local
make

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/local
make install prefix=$RPM_BUILD_ROOT/usr/local

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,bin,bin)
%doc README
/usr/local/sbin/*
/usr/local/man/man8/identd.8
