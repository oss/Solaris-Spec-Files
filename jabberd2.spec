Summary: Jabber IM Server (PAM authentication, MySQL storage)
Name: jabberd
Version: 2.0s2
Release: 1
Group: Applications/Internet
License: GPL
Source: %{name}-%{version}.tar.gz
Source1: jabberd2-init.d-jabberd
Patch: jabberd2-ssl-only.diff
BuildRoot: /var/tmp/%{name}-root
Requires: mysql, openssl >= 0.9.6b
BuildRequires: mysql-devel, openssl >= 0.9.6b
Provides: jabberd2

%description
This is the server for the Jabber Instant Messaging system. It has been built
with support for PAM as it's authentication system, to use MySQL as it's
storage method, and has been built with debugging enabled.

%prep
%setup -q

%patch -p1

%build
PATH=/opt/SUNWspro/bin:/usr/ccs/bin:$PATH
export PATH
CC="cc" LD="ld" CPPFLAGS="-I/usr/local/include -I/usr/local/ssl/include -I/usr/local/mysql/include/mysql" LDFLAGS="-L/usr/local/lib -R/usr/local/lib -L/usr/local/ssl/lib -R/usr/local/ssl/lib -L/usr/local/mysql/lib/mysql -R/usr/local/mysql/lib/mysql" ./configure --enable-authreg=pam --enable-storage=mysql --enable-debug
gmake

%install
gmake install DESTDIR=%{buildroot}

mkdir -p %{buildroot}/etc/init.d
cp %{SOURCE1} %{buildroot}/etc/init.d/jabberd
chmod 744 %{buildroot}/etc/init.d/jabberd

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)

/usr/local/bin/*
/usr/local/man/man8/*
%attr(-,jabber,jabber) /usr/local/etc/jabberd/*
