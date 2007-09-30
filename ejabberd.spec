Summary:	The ejabberd jabber server
Name:		ejabberd
Version:	1.1.3
Release:	1
License:	GPL
Group:		Applications/Internet
Source:		%{name}-%{version}.tar.gz
Source1:	ejabberd-init.d-ejabberd
Source2:	ejabberd_mnesia_update.erl
Source3:	muc_room_dumper.erl
#Patch:		ejabberd-ru.diff
#Patch1: ejabberdctl-addroster.diff
Requires:	erlang = R11B4-1, expat >= 1.95.8-1, openssl >= 0.9.8
BuildRequires:	erlang = R11B4-1, make, expat >= 1.95.8, openssl >= 0.9.8
BuildRoot:	/var/tmp/%{name}-root

%description
The ejabberd jabber server

%prep
%setup -q
#%patch -p1

%build
#I need to set both CFLAGS and CPPFLAGS here because the autotools use CPPFLAGS for test in ./configure but the ejabberd people use CFLAGS internally
#PATH=/opt/SUNWspro/bin:/usr/local/bin/sparcv9:/usr/ccs/bin:/usr/local/gnu/bin:$PATH
#CC="/usr/local/bin/sparcv9/gcc"
#CPPFLAGS="-mcpu=v9 -m64 -I/usr/local/include -I/usr/local/ssl/include"
#CFLAGS="-g -mcpu=v9 -m64 -I/usr/local/include -I/usr/local/ssl/include"
#LDFLAGS="-L/usr/local/lib/sparcv9 -R/usr/local/lib/sparcv9 -L/usr/local/ssl/lib/sparcv9 -R/usr/local/ssl/lib/sparcv9 -L/usr/local/lib"
#export PATH CC CPPFLAGS CFLAGS LDFLAGS

#PATH=/opt/SUNWspro/bin:/usr/local/bin/sparcv9:/usr/ccs/bin:/usr/local/gnu/bin:$PATH
#CC="gcc"
#CPPFLAGS="-mcpu=v9 -m64 -I/usr/local/include -I/usr/local/ssl/include"
#CFLAGS="-g -mcpu=v9 -m64 -I/usr/local/include -I/usr/local/ssl/include"
#LDFLAGS="-L/usr/local/lib/sparcv9 -R/usr/local/lib/sparcv9 -L/usr/local/ssl/lib/sparcv9 -R/usr/local/ssl/lib/sparcv9 -L/usr/local/lib"
#export PATH CC CPPFLAGS CFLAGS LDFLAGS

PATH=/opt/SUNWspro/bin:/usr/local/bin/sparcv9:/usr/ccs/bin:/usr/local/gnu/bin:$PATH
CC="/usr/local/bin/sparcv9/gcc"
CPPFLAGS="-I/usr/local/include -I/usr/local/ssl/include"
#CFLAGS="-mcpu=v9 -m64"
LD="/usr/local/gnu/bin/ld"
LDFLAGS="-L/usr/local/lib -R/usr/local/lib -L/usr/local/lib/sparcv9 -R/usr/local/lib/sparcv9 -L/usr/local/ssl/lib/sparcv9 -R/usr/local/ssl/lib/sparcv9"
export PATH CC CPPFLAGS CFLAGS LD LDFLAGS

cd src/
# Let's generate the configure script here, that way I can just make changes to
# configure.ac and not worry about propagating them to configure in the diff
autoconf
./configure --enable-pam
gmake

erlc %{SOURCE2}
erlc %{SOURCE3}

%install

cd src
gmake install DESTDIR=%{buildroot}
cp ../tools/ejabberdctl %{buildroot}/var/lib/ejabberd/ebin/

mkdir %{buildroot}/etc/init.d
cp %{SOURCE1} %{buildroot}/etc/init.d/ejabberd

mkdir %{buildroot}/var/lib/ejabberd/priv/ebin
cp ejabberd_mnesia_update.beam %{buildroot}/var/lib/ejabberd/priv/ebin/

%clean
rm -rf %{buildroot}

%post
echo "IF YOU ARE UPGRADING FROM A VERSION PRE 1.0.0-5 THEN THIS VERSION OF THE PACKAGE HAS INCOMPATIBLE CHANGES IN ONE OF THE DATABASE STRUCTURES, THE INCLUDED ejabberd_mnesia_update TOOL MUST BE USED BEFORE STARTING THIS VERSION OF THE SERVER."

%files
%defattr(-, root, root)
%config(noreplace) /etc/init.d/ejabberd
%config(noreplace) /etc/ejabberd/ejabberd.cfg*
/var/lib/ejabberd/ebin/*
/var/lib/ejabberd/priv/lib/*
/var/lib/ejabberd/priv/msgs/*
/var/lib/ejabberd/priv/ebin/ejabberd_mnesia_update.beam

%changelog
* Fri Jul 27 2007 David Lee Halik <dhalik@nbcs.rutgers.edu> - 1.1.3-1
- Bump to 1.1.3
* Thu May 10 2007 David Lee Halik <dhalik@nbcs.rutgers.edu> - 1.1.1-4
- Fixed erlang require so that it doesn't break rpm version script

