Summary: High-performance and highly configurable RADIUS server
URL: http://www.freeradius.org/
Name: freeradius
Version: 1.1.5
Release: 0
License: GPL
Group: Networking/Daemons
Packager: FreeRADIUS.org
Source0: %{name}-%{version}.tar.gz
BuildPreReq: sed heimdal-devel
# FIXME: snmpwalk, snmpget and rusers POSSIBLY needed by checkrad
Provides: radiusd
Conflicts: cistron-radius
BuildRoot: %{_tmppath}/%{name}-root

%description
The FreeRADIUS Server Project is a high-performance and highly
configurable GPL'd RADIUS server. It is somewhat similar to the
Livingston 2.0 RADIUS server, but has many more features, and is much
more configurable.

While the FreeRADIUS package is designed as a server, we only need the
test clients. This package is somewhat limited as a result, intentionally.

%prep
%setup

%build
# heh heh heh
#ls src/modules
#mv src/modules/rlm_always src/modules/rlm_example .
#rm -Rf src/modules/rlm_*
#mv rlm_* src/modules
#ls src/modules
#sleep 5

echo always > src/modules/stable
echo example >> src/modules/stable

cd src/main
sed s/-pie//g Makefile.in > MF
mv MF Makefile.in
cd ../..

# This thing doesn't seem to respect CPPFLAGS?
# obsolete int types. too dirty.
CC=/opt/SUNWspro/bin/cc 
CXX=/opt/SUNWspro/bin/CC 
#CPPFLAGS='-I/usr/local/include -I/usr/local/ssl/include -I/usr/local/include/heimdal -Du_int32_t=uint32_t'
#LDFLAGS='-L/usr/local/lib -R/usr/local/lib -L/usr/local/ssl/lib -R/usr/local/ssl/lib'
#CFLAGS="$CPPFLAGS $LDFLAGS"
export CC CXX CPPFLAGS LDFLAGS CFLAGS
./configure --prefix=%{_prefix} \
	--localstatedir=%{_localstatedir} \
	--sysconfdir=%{_sysconfdir} \
	--mandir=%{_mandir} \
	--with-docdir=%{_datadir}/doc/%{name}-%{version} \
	--with-large-files --with-udpfromto --with-edir \
	CC=/opt/SUNWspro/bin/cc CXX=/opt/SUNWspro/bin/CC # CPPFLAGS="$CPPFLAGS" \
	# LDFLAGS="$LDFLAGS" CFLAGS="$CPPFLAGS $LDFLAGS"
gmake -j3

%install
[ "$RPM_BUILD_ROOT" != "/" ] && rm -rf $RPM_BUILD_ROOT

gmake install R=$RPM_BUILD_ROOT

RADDB=$RPM_BUILD_ROOT/etc/raddb
# set radiusd as default user/group
perl -i -pe 's/^#user =.*$/user = radiusd/' $RADDB/radiusd.conf
perl -i -pe 's/^#group =.*$/group = radiusd/' $RADDB/radiusd.conf
# shadow password file MUST be defined on Linux
perl -i -pe 's/#	shadow =/shadow =/' $RADDB/radiusd.conf

# remove unneeded stuff
rm -f $RPM_BUILD_ROOT%{_mandir}/man8/builddbm.8
rm -f $RPM_BUILD_ROOT%{_prefix}/sbin/rc.radiusd

# more files go to /usr/share/doc/freeradius-%{version}
install -m 0644 CREDITS $RPM_BUILD_ROOT%{_datadir}/doc/%{name}-%{version}
install -m 0644 COPYRIGHT $RPM_BUILD_ROOT%{_datadir}/doc/%{name}-%{version}
install -m 0644 LICENSE $RPM_BUILD_ROOT%{_datadir}/doc/%{name}-%{version}

mkdir -p $RPM_BUILD_ROOT/etc/init.d
cd redhat
install -m 755 rc.radiusd-redhat $RPM_BUILD_ROOT/etc/init.d/radiusd
cd ..

%post
echo "You may need to make a radiusd user."

%clean
[ "$RPM_BUILD_ROOT" != "/" ] && rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc %{_datadir}/doc/%{name}-%{version}
%{_bindir}/*
%{_datadir}/%{name}
%{_libdir}/*
%{_mandir}/*/*
%{_sbindir}/*

%changelog
* Thu Dec 15 2004 Alan DeKok
- update for 1.1.0

* Mon May 31 2004 Paul Hampson
- update for 1.0.0 release

* Fri May 23 2003 Marko Myllynen
- update for 0.9

* Wed Sep  4 2002 Marko Myllynen
- fix libtool issues for good

* Thu Aug 22 2002 Marko Myllynen
- update for 0.7/0.8

* Tue Jun 18 2002 Marko Myllynen
- run as radiusd user instead of root
- added some options for configure

* Thu Jun  6 2002 Marko Myllynen
- set noreplace for non-dictionary files in /etc/raddb

* Sun May 26 2002 Frank Cusack <frank@google.com>
- move /var dirs from %%post to %%files

* Thu Feb 14 2002 Marko Myllynen
- use dir name macros in all configure options
- libtool is required only when building the package
- misc clean ups

* Wed Feb 13 2002 Marko Myllynen
- use %%{_mandir} instead of /usr/man
- rename %%postin as %%post
- clean up name/version

* Fri Jan 18 2002 Frank Cusack <frank@google.com>
- remove (noreplace) for /etc/raddb/* (due to rpm bugs)

* Fri Sep 07 2001 Ivan F. Martinez <ivanfm@ecodigit.com.br>
- changes to make compatible with default config file shipped
- adjusts log files are on /var/log/radius instead of /var/log
- /etc/raddb changed to config(noreplace) to don't override
-   user configs

* Fri Sep 22 2000 Bruno Lopes F. Cabral <bruno@openline.com.br>
- spec file clear accordling to the libltdl fix and minor updates

* Wed Sep 12 2000 Bruno Lopes F. Cabral <bruno@openline.com.br>
- Updated to snapshot-12-Sep-00

* Fri Jun 16 2000 Bruno Lopes F. Cabral <bruno@openline.com.br>
- Initial release
