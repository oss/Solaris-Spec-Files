Name: libmcrypt 
Version: 2.5.7
Release: 1
Copyright: GPL 
Group: Applications/Internet
Summary: libMCrypt is a replacement for the old crypt().
Source: libmcrypt-%{version}.tar.gz
BuildRoot: /var/tmp/%{name}-root

%description
libmcrypt allows developers to use a wide range of encryption 
functions, without making drastic changes to their code

%prep
%setup -q

%build
CC='/opt/SUNWspro/bin/cc' CXX='/opt/SUNWSpro/bin/CC' ./configure --disable-posix-threads --prefix=/usr/local
make

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/local
make install prefix=$RPM_BUILD_ROOT/usr/local

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,bin,bin)
/usr/local/lib/libmcrypt
/usr/local/lib/libmcrypt.so.4.4.7
/usr/local/lib/libmcrypt.so.4
/usr/local/lib/libmcrypt.so
/usr/local/lib/libmcrypt.la
/usr/local/bin/libmcrypt-config
/usr/local/include/mcrypt.h
/usr/local/share/aclocal/libmcrypt.m4
/usr/local/man/man3/mcrypt.3

