
%define fullver 2.0.3

Summary:	High-performance and highly configurable RADIUS server
URL:		http://www.freeradius.org/
Name:		freeradius
Version:	%{fullver}
Release:	1
License:	GPL
Group:		Networking/Daemons
Distribution: 	RU-Solaris
Vendor: 	NBCS-OSS
Packager:       David Diffenbaugh <davediff@nbcs.rutgers.edu>	
Source0:	%{name}-server-%{fullver}.tar.bz2
Source1:	radiusd-init
Patch:          freeradius-2.0.0-int.patch
Provides:	radiusd
Conflicts:	cistron-radius
BuildRequires:	openssl libtool-devel
Requires:	openssl openldap-lib
BuildRoot:	%{_tmppath}/%{name}-%{version}-root

%description
The FreeRADIUS Server Project is a high-performance and highly
configurable GPL'd RADIUS server. It is somewhat similar to the
Livingston 2.0 RADIUS server, but has many more features, and is much
more configurable.

%package devel
Summary:	Freeradius development files
Group:		Networking/Daemons
Requires:	%{name} = %{version}

%description devel
Freeradius development package containg all the pesky .a files

%prep
%setup -q -n %{name}-server-%{fullver}
%patch -p1

%build

#echo always > src/modules/stable
#echo example >> src/modules/stable

cd src/main
sed s/-pie//g Makefile.in > MF
mv MF Makefile.in
cd ../..

cd src/modules
sed s/rlm_krb5//g stable > stable.1
sed s/rlm_otp//g stable.1 > stable.2
mv stable.2 stable
cd ../..

PATH="/opt/SUNWspro/bin:${PATH}" \
CC="cc" CXX="CC" CPPFLAGS="-I/usr/local/include -I/usr/local/ssl/include" \
LD="/usr/ccs/bin/ld" \
LDFLAGS="-L/usr/local/lib -R/usr/local/lib \
	-L/usr/local/ssl/lib -R/usr/local/ssl/lib" \
CFLAGS="-I/usr/local/include -I/usr/local/ssl/include" \
LD_OPTIONS="-L/usr/local/lib -R/usr/local/lib -L/usr/local/ssl/lib -R/usr/local/ssl/lib" \
export PATH CC CXX CPPFLAGS LD LDFLAGS CFLAGS LD_OPTIONS


%configure \
	--prefix=/usr/local/%{name} \
	--localstatedir=%{_localstatedir} \
	--libdir=/usr/local/lib/%{name} \
	--sysconfdir=%{_sysconfdir} \
	--mandir=%{_mandir} \
	--with-docdir=%{_datadir}/doc/%{name} \
	--with-large-files \
	--without-udpfromto \
	--with-edir \
	--with-ldap \
	--with-modules="rlm_ldap" \
	--with-rlm-ldap-lib-dir=/usr/local/lib \
	--with-rlm-ldap-include-dir=/usr/local/include \
	--with-openssl-includes=/usr/local/ssl/include \
	--with-openssl-libraries=/usr/local/ssl/lib \
	

gmake

%install
[ "$RPM_BUILD_ROOT" != "/" ] && rm -rf $RPM_BUILD_ROOT

mkdir -p $RPM_BUILD_ROOT/usr/local/etc/raddb/

gmake install R=$RPM_BUILD_ROOT

RADDB=$RPM_BUILD_ROOT/usr/local/etc/raddb
# set radiusd as default user/group
perl -i -pe 's/^#user =.*$/user = radiusd/' $RADDB/radiusd.conf
perl -i -pe 's/^#group =.*$/group = radiusd/' $RADDB/radiusd.conf
# shadow password file MUST be defined on Linux
perl -i -pe 's/#	shadow =/shadow =/' $RADDB/radiusd.conf

# remove unneeded stuff
rm -f $RPM_BUILD_ROOT%{_mandir}/man8/builddbm.8
rm -f $RPM_BUILD_ROOT%{_prefix}/sbin/rc.radiusd

# more files go to /usr/share/doc/freeradius-%{version}
install -m 0644 CREDITS $RPM_BUILD_ROOT%{_datadir}/doc/%{name}
install -m 0644 COPYRIGHT $RPM_BUILD_ROOT%{_datadir}/doc/%{name}
install -m 0644 LICENSE $RPM_BUILD_ROOT%{_datadir}/doc/%{name}

# install init.d script
mkdir -p $RPM_BUILD_ROOT/etc/init.d
install -m 755 %{SOURCE1} $RPM_BUILD_ROOT/etc/init.d/radiusd

cd redhat
install -m 644 radiusd-logrotate $RPM_BUILD_ROOT/usr/local/etc/raddb/
install -m 644 radiusd-pam       $RPM_BUILD_ROOT/usr/local/etc/raddb/
cd ..

# Put down proper dictionary path
cd $RPM_BUILD_ROOT/usr/local/etc/raddb
sed 's/local\/freeradius\//local\//g' dictionary > dictionary.1
mv dictionary.1 dictionary

# Get rid of evil .la files!
rm -rf $RPM_BUILD_ROOT%{_prefix}/lib/%{name}/*.la

%clean
[ "$RPM_BUILD_ROOT" != "/" ] && rm -rf $RPM_BUILD_ROOT

%post
cat << END
==========================NOTICE========================
You will need to create a radiusd user and group. Confs
are located in /usr/local/etc/raddb/ and an init script
is thrown down in /etc/init.d/
========================================================
END

%files
%defattr(-,root,root)
%config (noreplace) /usr/local/etc/raddb/*
%doc %{_datadir}/doc/%{name}
%{_bindir}/*
%{_datadir}/%{name}
/usr/local/lib/%{name}/*.so
%{_mandir}/*/*
%{_sbindir}/*
/etc/init.d/radiusd

%files devel
%defattr(-,root,root)
/usr/local/lib/%{name}/*.a
/usr/local/include/%{name}/*

%changelog
* Wed Apr 23 2008 David Diffenbaugh <davediff@nbcs.rutgers.edu> - 2.0.3-1
- bumped to 2.0.3
* Fri Jan 18 2008 David Diffenbaugh <davediff@nbcs.rutgers.edu> - 2.0.0-1
- Bumped to 2.0.0, patched to change u_int to uint
* Fri Aug 31 2007 David Lee Halik <dhalik@nbcs.rutgers.edu> - 2.0.0pre2-1
- Bump to pre2
* Wed Aug 01 2007 David Lee Halik <dhalik@nbcs.rutgers.edu> - 2.0.0-pre1-6
- Fixed openldap-lib as a dependency
* Tue Jul 31 2007 David Lee Halik <dhalik@nbcs.rutgers.edu> - 2.0.0-pre1-5
- Updated init script
* Wed Jul 25 2007 David Lee Halik <dhalik@nbcs.rutgers.edu> - 2.0.0-pre1-4
- Fixed versioning in paths
- Updated init script
* Tue Jul 17 2007 David Lee Halik <dhalik@nbcs.rutgers.edu> - 2.0.0-pre1-3
- Turned off udpfromto
* Mon Jul 16 2007 David Lee Halik <dhalik@nbcs.rutgers.edu> - 2.0.0-pre1-1
- The hell with stable, this actually compiles
* Mon Jul 16 2007 David Lee Halik <dhalik@nbcs.rutgers.edu> - 1.1.6-3
- Working out some more daemon issues
* Wed Jun 27 2007 David Lee Halik <dhalik@nbcs.rutgers.edu> - 1.1.6-2
- Some bug fixes.
* Mon Jun 25 2007 David Lee Halik <dhalik@nbcs.rutgers.edu> - 1.1.6-1
- Initial Build.
