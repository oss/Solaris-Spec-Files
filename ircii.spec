Summary: IRC client
Name: ircii
Version: 4.4X
Release: 3
Group: Applications/Internet
Copyright: Freely redistributable
Source: ircii-4.4X.tar.bz2
BuildRoot: /var/tmp/%{name}-root

%description
IrcII is a popular Unix IRC client.

%prep
%setup -q

%build
LD="/usr/ccs/bin/ld -L/usr/local/lib -R/usr/local/lib" \
 LDFLAGS="-L/usr/local/lib -R/usr/local/lib" CPPFLAGS="-I/usr/local/include" \
 ./configure --prefix=/usr/local --sysconfdir=/etc
make

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/local
make install prefix=$RPM_BUILD_ROOT/usr/local sysconfdir=$RPM_BUILD_ROOT/etc

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,bin,bin)
%doc ChangeLog README NEWS
/usr/local/share/irc
/usr/local/bin/*
/usr/local/man/man1/*
