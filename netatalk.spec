Summary: Apple file and print sharing daemon
Name: netatalk
Version: 1.6.0
Release: 1
Group: System Enviroment/Daemons
Copyright: GPL
BuildRequires: db3.3 tcp_wrappers openssl
Requires: db3.3 tcp_wrappers openssl
Source: %{name}-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-root

%description
Netatalk is a freely-available, kernel level implementation of the AppleTalk
Protocol Suite, originally for BSD-derived systems. A *NIX/*BSD system running
netatalk is capable of serving many macintosh clients simultaneously as an
AppleTalk router, AppleShare file server, *NIX/*BSD print server, and for
accessing AppleTalk printers via Printer Access Protocol (PAP). Included are
a number of minor printing and debugging utilities. 

%prep
%setup -q

%build
LDFLAGS="-L/usr/local/lib -R/usr/local/lib" \
./configure --prefix=/usr/local --with-tcpwrappers


%install
rm -rf %{buildroot}
mkdir -p %{buildroot}
make install prefix=%{buildroot}/usr/local

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc COPYING 
%doc doc/FAQ
%doc doc/README.hidden-items
%doc doc/README.platforms
/usr/local/bin/*
/usr/local/etc/netatalk/
/usr/local/include/*
/usr/local/lib/*
/usr/local/sbin/*
/usr/local/share/*
/usr/local/man/*


