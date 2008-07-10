%define realver 9.5.0-P1

Name:		bind
Version:	9.5.0P1
Copyright:	BSD
Group:		Applications/Internet
Summary:	Berkeley name server
Release:	1
Source0:	%{name}-%{realver}.tar.gz
Source1:	bind-ru.tar.gz
BuildRoot:	/var/tmp/%{name}-root
BuildRequires:	openssl >= 0.9.8
Requires:	openssl >= 0.9.8

%description
BIND is the Internet Software Consortium's domain name server.

%prep
%setup -q -n %{name}-%{realver}

tar zxf %{SOURCE1}

%build
PATH="/opt/SUNWspro/bin:${PATH}" \
CC="cc" CXX="CC" CPPFLAGS="-I/usr/local/include" \
LD="/usr/ccs/bin/ld" \
LDFLAGS="-L/usr/local/lib -R/usr/local/lib"
export PATH CC CXX CPPFLAGS LD LDFLAGS

./configure \
	--prefix=/usr/local \
	--with-openssl \
	--enable-threads \
	--enable-shared \
	--enable-static \
	--enable-largefile

gmake -j3

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/local/bin
mkdir -p $RPM_BUILD_ROOT/usr/local/sbin
mkdir -p $RPM_BUILD_ROOT/usr/local/bind/lib
mkdir -p $RPM_BUILD_ROOT/usr/local/bind/include/arpa
mkdir -p $RPM_BUILD_ROOT/usr/local/bind/include/isc
mkdir -p $RPM_BUILD_ROOT/usr/local/bind/include/sys
mkdir -p $RPM_BUILD_ROOT/usr/local/lib
make install DESTDIR=$RPM_BUILD_ROOT
cd ru-bind
tar cf - etc var | (cd $RPM_BUILD_ROOT && tar xvf -)

# We need to remove hard links
cd $RPM_BUILD_ROOT
/usr/local/bin/unhardlinkify.py ./

%clean
rm -rf $RPM_BUILD_ROOT

%post
cat <<EOF
RPM installed these files on your system:

/etc/init.d/named.rpm
/etc/rc2.d/S72bind.rpm
/etc/named.conf.sample.rpm
/var/named/root.hints.get.rpm

You should take the rpm extension off and customize them.  You also
should add directories /var/named/primary and /var/named/rutgers.

You may also need to disable BIND that comes with Solaris.
EOF

%files
%defattr(-,root,root,0755)
%doc CHANGES COPYRIGHT README
%doc doc/
%doc /usr/local/share/man/man1/*
%doc /usr/local/share/man/man3/*
%doc /usr/local/share/man/man5/*
%doc /usr/local/share/man/man8/*
%defattr(-,bin,bin)
%dir /usr/local/include/bind9/
%dir /usr/local/include/isc/
%dir /usr/local/include/isccc/
%dir /usr/local/include/dns/
%dir /usr/local/include/dst/
%dir /usr/local/include/lwres/
%dir /usr/local/include/isccfg/
/usr/local/bind/*
/usr/local/sbin/*
/usr/local/bin/*
/usr/local/include/bind9/*
/usr/local/include/isc/*
/usr/local/include/isccc/*
/usr/local/include/dns/*
/usr/local/include/dst/*
/usr/local/include/lwres/*
/usr/local/include/isccfg/*
/usr/local/lib/*
/etc/init.d/named.rpm
/etc/rc2.d/S72bind.rpm
/etc/named.conf.sample.rpm
/var/named/root.hints.get.rpm

%changelog
* Thu Jul 10 2008 Brian Schubert <schubert@nbcs.rutgers.edu> - 9.5.0P1-1
- Updated to version 9.5.0-P1
* Tue Jun 3 2008 Brian Schubert <schubert@nbcs.rutgers.edu> - 9.5.0-1
- Updated to version 9.5.0
* Tue Sep 04 2007 David Lee Halik <dhalik@nbcs.rutgers.edu> - 9.4.1P1-1
- Bump to 9.4.1-P1
* Wed Aug 22 2007 Naveen Gavini <ngavini@nbcs.rutgers.edu> - 9.4.1-1
 - Updated to the latest version.

