Summary: The ejabberd jabber server
Name: ejabberd
Version: 0.7.5
Release: 8
License: GPL
Group: Applications/Internet
Source: %{name}-%{version}.tar.gz
Source1: ejabberd_pam_auth.c
Source2: ejabberd-init.d-ejabberd
Patch: ejabberd-0.7.5.diff
Requires: erlang, expat >= 1.95, openssl >= 0.9.6
BuildRequires: erlang, make, expat >= 1.95, openssl >= 0.9.6
BuildRoot: /var/tmp/%{name}-root

%description
The ejabberd jabber server

%prep
%setup -q
%patch -p1

%build
#I need to set both CFLAGS and CPPFLAGS here because the autotools use CPPFLAGS for test in ./configure but the ejabberd people use CFLAGS and not CPPFLAGS in some important places
PATH=/opt/SUNWspro/bin:/usr/local/gnu/bin:/usr/ccs/bin:$PATH
CC="gcc"
CPPFLAGS="-I/usr/local/include -I/usr/local/ssl/include"
CFLAGS="-I/usr/local/include -I/usr/local/ssl/include"
LDFLAGS="-L/usr/local/lib -R/usr/local/lib -L/usr/local/ssl/lib -R/usr/local/ssl/lib"
export PATH CC CPPFLAGS CFLAGS LDFLAGS

cd src
./configure
gmake

cc -o ejabberd_pam_auth -lpam %{SOURCE1}

%install
cd src
gmake install DESTDIR=%{buildroot}
cp ../tools/ejabberdctl %{buildroot}/var/lib/ejabberd/ebin/

mkdir %{buildroot}/etc/init.d
cp %{SOURCE2} %{buildroot}/etc/init.d/ejabberd

mkdir %{buildroot}/var/lib/ejabberd/bin
cp ejabberd_pam_auth %{buildroot}/var/lib/ejabberd/bin/

%clean
rm -rf %{buildroot}

%files
%defattr(-, root, root)
%config(noreplace) /etc/init.d/ejabberd
%config(noreplace) /etc/ejabberd/ejabberd.cfg*
/var/lib/ejabberd/bin/ejabberd_pam_auth
/var/lib/ejabberd/ebin/*
/var/lib/ejabberd/priv/lib/*
/var/lib/ejabberd/priv/msgs/*
