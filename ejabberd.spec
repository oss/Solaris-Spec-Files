Summary:	The ejabberd jabber server
Name:		ejabberd
Version:	2.0.2
Release:	1
License:	GPL
Group:		Applications/Internet
Source:		%{name}-%{version}.tar.gz
Source1:	ejabberd-init.d-ejabberd
#Source2:	ejabberd_mnesia_update.erl
#Source3:	muc_room_dumper.erl
#Patch:		ejabberd-1.1.2-ru.patch
Requires:	erlang = R12B5-1, expat >= 2.0.1, openssl >= 0.9.8
BuildRequires:	erlang = R12B5-1, expat >= 2.0.1, expat-devel >= 2.0.1, openssl >= 0.9.8 zlib >= 1.2.3
BuildRoot:	/var/tmp/%{name}-root

%description
The ejabberd jabber server

%prep
%setup -q 
#%patch -p1

%build
PATH=/opt/SUNWspro/bin:/usr/ccs/bin:/usr/local/gnu/bin:$PATH
CC="gcc"
CXX="g++"
CPPFLAGS="-I/usr/local/include -I/usr/local/ssl/include"
CFLAGS="-mcpu=v9 -m64"
LD="/usr/ccs/bin/ld"
LDFLAGS="-Wl,-64 -L/usr/local/lib -R/usr/local/lib -L/usr/local/lib/sparcv9 -R/usr/local/lib/sparcv9 -L/usr/local/ssl/lib/sparcv9 -R/usr/local/ssl/lib/sparcv9"
export PATH CC CXX CPPFLAGS CFLAGS LD LDFLAGS

cd src/

# Let's generate the configure script here, that way I can just make changes to
# configure.ac and not worry about propagating them to configure in the diff

##commented out by davediff because this failed
#autoconf

./configure --enable-pam

##following added by davediff
#getting unresolved symbol compile errors, needs to know to use -lsocket and -lnsl
cd pam
sed -e 's/-lpam/-lpam -lsocket -lnsl/' Makefile > Makefile.good
mv Makefile.good Makefile
cd ..

gmake

##commented out by davediff
#erlc %{SOURCE2}
#erlc %{SOURCE3}

%install
PATH=/usr/local/gnu/bin:$PATH
export PATH

cd src
gmake install DESTDIR=%{buildroot}

##commented out by davediff for ejabber 2 not sure if we need it
#cp ../tools/ejabberdctl %{buildroot}/var/lib/ejabberd/ebin/

mkdir %{buildroot}/etc/init.d
cp %{SOURCE1} %{buildroot}/etc/init.d/ejabberd

##commented out by davediff for ejabberd 2
#mkdir %{buildroot}/var/lib/ejabberd/priv/ebin
#cp ejabberd_mnesia_update.beam %{buildroot}/var/lib/ejabberd/priv/ebin/

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
##added by davediff
#new files for ejabberd-2
%config(noreplace) /etc/ejabberd/ejabberdctl.cfg*
/etc/ejabberd/inetrc
/sbin/ejabberdctl
/var/lib/ejabberd/priv/bin/epam
##commented out by davediff
#/var/lib/ejabberd/priv/ebin/ejabberd_mnesia_update.beam

%changelog
* Tue Nov 11 2008 David Diffenbaugh <davediff@nbcs.rutgers.edu> - 2.0.2-1
- bumped to 2.0.2-1
- built against erlang-R12B5-1
* Wed Jun 11 2008 David Diffenbaugh <davediff@nbcs.rutgers.edu> - 2.0.1_2-1
- bumping to 2.0.1_2, removed patches for now, added -lsocket -lnsl
- built against latest erlang-R12B3-1
- updated file list for new files
* Tue Oct 30 2007 David Lee Halik <dhalik@nbcs.rutgers.edu> - 1.1.4-4
- Attempting a repatch by hand
* Thu Oct 25 2007 David Lee Halik <dhalik@nbcs.rutgers.edu> - 1.1.4-2
- Respin against R11B5 with 64bitiness
* Mon Oct 01 2007 David Lee Halik <dhalik@nbcs.rutgers.edu> - 1.1.4-1
- Bump to 1.1.4
* Thu May 10 2007 David Lee Halik <dhalik@nbcs.rutgers.edu> - 1.1.1-4
- Fixed erlang require so that it doesn't break rpm version script

