%define name       pure-ftpd
%define version    1.0.4
%define release    1
%define builddir   $RPM_BUILD_DIR/%{name}-%{version}
%define no_install_post_compress_docs    1
%define con_pam    0
%define prefixdef  /usr/local
%define sysconfdef /etc

#rpm -ba|--rebuild --define 'with_pam 1'
%{?with_pam:%define con_pam 1}

#If you don't like the prefix '/usr/local' you can override it like this:
#rpm -ba|--rebuild --define 'prefix /usr'
%{?!prefix:%define prefix %{prefixdef}}

#If you don't like the sysconfdir '/etc' you can override it like this:
#rpm -ba|--rebuild --define 'sysconfdir /usr/local/etc'
%{?!sysconfdir:%define sysconfdir %{sysconfdef}}


Name:              %{name}
Version:           %{version}
Release:           %{release}
Vendor:            Rutgers
URL:               http://www.pureftpd.org
Source:            ftp://download.sourceforge.net/pub/sourceforge/pureftpd/%{name}-%{version}.tar.gz
Group:             System/Servers
Copyright:         GPL
Provides:     	   ftp-server
BuildRoot:         %{_tmppath}/%{name}-%{version}
Summary:           Lightweight, fast and secure FTP server
Conflicts:         wu-ftpd proftpd ftpd in.ftpd anonftp publicfile wuftpd ftpd-BSD ftpd-ru

%description
Pure-FTPd is a fast, production-quality, standard-comformant FTP server,
based upon Troll-FTPd. Unlike other popular FTP servers, it has no known
security flaw, it is really trivial to set up and it is especially designed
for modern Linux and FreeBSD kernels (setfsuid, sendfile, capabilities) .
Features include PAM support, IPv6, chroot()ed home directories, virtual
domains, built-in LS, anti-warez system, bandwidth throttling, FXP, bounded
ports for passive downloads, UL/DL ratios, native LDAP and SQL support,
Apache log files and more.

%prep
%setup 	           -n %{name}-%{version} 


%build
if [ ! -f configure ]; then
  ./autogen.sh --prefix=%{prefix} \
%if %{con_pam}
  --with-pam \
%endif  
  --with-paranoidmsg --with-everything --without-capabilities \
  --mandir=%{_mandir} --sysconfdir=%{sysconfdir}
else
  ./configure --prefix=%{prefix} \
%if %{con_pam}
  --with-pam \
%endif  
  --with-paranoidmsg --with-everything --without-capabilities \
  --mandir=%{_mandir} --sysconfdir=%{sysconfdir}
fi
if [ "$SMP" != "" ]; then
  (make "MAKE=make -k -j $SMP"; exit 0)
  make
else
  make
fi

%install
[ -n "$RPM_BUILD_ROOT" -a "$RPM_BUILD_ROOT" != / ] && rm -rf "$RPM_BUILD_ROOT"
make DESTDIR="$RPM_BUILD_ROOT" install-strip

if [ ! -d $RPM_BUILD_ROOT%{prefix}/sbin ]; then
  mkdir -p $RPM_BUILD_ROOT%{prefix}/sbin
fi
if [ ! -d $RPM_BUILD_ROOT%{prefix}/bin ]; then
  mkdir -p $RPM_BUILD_ROOT%{prefix}/bin
fi
if [ ! -d $RPM_BUILD_ROOT%{sysconfdir} ]; then
  mkdir -p $RPM_BUILD_ROOT%{sysconfdir}
fi
if [ ! -d $RPM_BUILD_ROOT%{sysconfdir}/rc.d/init.d ]; then
  mkdir -p $RPM_BUILD_ROOT%{sysconfdir}/rc.d/init.d
fi
if [ ! -d $RPM_BUILD_ROOT%{sysconfdir}/sysconfig ]; then
  mkdir -p $RPM_BUILD_ROOT%{sysconfdir}/sysconfig
fi
if [ ! -d $RPM_BUILD_ROOT%{_mandir}/man8 ]; then
  mkdir -p $RPM_BUILD_ROOT%{_mandir}/man8
fi

gzip --best $RPM_BUILD_ROOT/%{_mandir}/man8/*.8

install -m 755 configuration-file/pure-config.pl $RPM_BUILD_ROOT%{prefix}/sbin/
install -m 644 configuration-file/pure-ftpd.conf $RPM_BUILD_ROOT%{sysconfdir}/
install -m 600 pureftpd-ldap.conf $RPM_BUILD_ROOT%{sysconfdir}/
install -m 600 pureftpd-mysql.conf $RPM_BUILD_ROOT%{sysconfdir}/
install -m 644 contrib/redhat.sysconfig $RPM_BUILD_ROOT/%{sysconfdir}/sysconfig/pure-ftpd

# replace some occurences of prefix and sysconfig:
sed "s|%{prefixdef}|%{prefix}|g; s|%{sysconfdef}/sysconfig|%{sysconfdir}/sysconfig|g" < contrib/redhat.init > contrib/redhat.init_replaced
install -m 755 contrib/redhat.init_replaced $RPM_BUILD_ROOT/%{sysconfdir}/rc.d/init.d/pure-ftpd
sed "s|\(\$prefix *= *['\"]\)%{prefixdef}|\1%{prefix}|g" < configuration-file/pure-config.pl > configuration-file/pure-config.pl_replaced
install -m 755 configuration-file/pure-config.pl_replaced $RPM_BUILD_ROOT%{prefix}/sbin/pure-config.pl


%if %{con_pam}
  install -d $RPM_BUILD_ROOT/%{sysconfdir}/pam.d/
  install -m 644 pam/pure-ftpd $RPM_BUILD_ROOT/%{sysconfdir}/pam.d/
%endif

%clean
[ -n "$RPM_BUILD_ROOT" -a "$RPM_BUILD_ROOT" != / ] && rm -rf "$RPM_BUILD_ROOT"

%files

%defattr(0755, root, root)
%{prefix}/sbin/pure-config.pl
%{prefix}/sbin/pure-ftpd
%{prefix}/sbin/pure-ftpwho
%{prefix}/sbin/pure-quotacheck
%{prefix}/sbin/pure-uploadscript
%{prefix}/sbin/pure-mrtginfo
%{prefix}/bin/pure-statsdecode
%{prefix}/bin/pure-pw
%{prefix}/bin/pure-pwconvert
%config(noreplace) %{sysconfdir}/rc.d/init.d/pure-ftpd

%defattr(0644, root, root)
%{_mandir}/man8/pure-ftpd.8.gz
%{_mandir}/man8/pure-ftpwho.8.gz
%{_mandir}/man8/pure-quotacheck.8.gz
%{_mandir}/man8/pure-pw.8.gz
%{_mandir}/man8/pure-pwconvert.8.gz
%{_mandir}/man8/pure-mrtginfo.8.gz
%{_mandir}/man8/pure-uploadscript.8.gz
%{_mandir}/man8/pure-statsdecode.8.gz

%doc FAQ THANKS README.Virtual-Users README.Debian README README.Contrib README.Configuration-File AUTHORS CONTACT HISTORY NEWS README.LDAP README.MySQL README.Netfilter pureftpd-ldap.conf pureftpd-mysql.conf

%config(noreplace) %{sysconfdir}/pure-ftpd.conf
%config(noreplace) %{sysconfdir}/pureftpd-ldap.conf
%config(noreplace) %{sysconfdir}/pureftpd-mysql.conf
%config(noreplace) %{sysconfdir}/sysconfig/pure-ftpd
%if %{con_pam}
%config(noreplace) %{sysconfdir}/pam.d/pure-ftpd
%endif

%changelog
* Mon Nov 21 2001 Frank DENIS <j@pureftpd.org>
- First RPM build of this package.


