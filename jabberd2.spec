Summary: Jabber IM Server (PAM authentication, MySQL storage)
Name: jabberd
Version: 2.0s2
%define jcrversion 0.2.2
%define mucversion 0.6.0
Release: 5
Group: Applications/Internet
License: GPL
Source: %{name}-%{version}.tar.gz
Source1: jabberd2-init.d-jabberd
Source2: jcr-%{jcrversion}.tar.gz
Source3: mu-conference-%{mucversion}.tar.gz
Patch: jabberd2-ssl-only.diff
Patch2: jcr-%{jcrversion}.diff
BuildRoot: /var/tmp/%{name}-root
Requires: mysql, openssl >= 0.9.6b, glib2
BuildRequires: mysql-devel, openssl >= 0.9.6b, make, glib2-devel
Provides: jabberd2

%description
This is the server for the Jabber Instant Messaging system. It has been built
with support for PAM as it's authentication system, to use MySQL as it's
storage method, and has been built with debugging enabled.

%prep
%setup -q -D -T -b 2 -n jcr-0.2.2
%patch2 -p1
%setup -q -D -T -a 3 -n jcr-0.2.2
%setup -q -D
%patch -p1

%build
CC="cc"
LD="ld"
PATH=/opt/SUNWspro/bin:/usr/ccs/bin:/usr/local/gnu/bin:$PATH
export PATH
export CC
export LD

CPPFLAGS="-I/usr/local/include -I/usr/local/ssl/include -I/usr/local/mysql/include/mysql" LDFLAGS="-L/usr/local/lib -R/usr/local/lib -L/usr/local/ssl/lib -R/usr/local/ssl/lib -L/usr/local/mysql/lib/mysql -R/usr/local/mysql/lib/mysql" ./configure --enable-authreg=pam --enable-storage=mysql --prefix=/usr/local/jabberd --enable-debug
gmake

cd ../jcr-%{jcrversion}/
make
cp src/jcomp.mk src/main.c mu-conference-%{mucversion}/src
cd mu-conference-%{mucversion}/src/
# I wish I could just trust pkg-config to give me the -R flags, but it seems like it won't
sed -e 's/\(^LDFLAGS.*\)/\1-R\/usr\/local\/lib/' jcomp.mk > jcomp.mk.ru
CFLAGS="-lnsl -lsocket -lpthread" gmake -f jcomp.mk.ru

%install
gmake install DESTDIR=%{buildroot}

mkdir -p %{buildroot}/etc/init.d
cp %{SOURCE1} %{buildroot}/etc/init.d/jabberd
chmod 744 %{buildroot}/etc/init.d/jabberd

cp ../jcr-%{jcrversion}/mu-conference-%{mucversion}/src/mu-conference %{buildroot}/usr/local/jabberd/bin/
cp ../jcr-%{jcrversion}/mu-conference-%{mucversion}/muc-jcr.xml %{buildroot}/usr/local/jabberd/etc/jabberd/

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)

/usr/local/jabberd/bin/*
/usr/local/jabberd/man/man8/*
%attr(-,jabberd,jabberd) /usr/local/jabberd/etc/jabberd/*
%config(noreplace) /etc/init.d/jabberd
