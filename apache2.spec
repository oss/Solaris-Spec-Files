%define apache_ver    2.2.13
%define apache_prefix /usr/local/apache2-%{apache_ver}

Name:		apache2
Version:	%{apache_ver}
Release:	2
Summary:	The Apache webserver
License:	BSD-like
Group:		Applications/Internet
BuildRoot:	%{_tmppath}/%{name}-root
Source0:	httpd-%{version}.tar.gz
#Source1:	http://apache.webthing.com/database/apr_dbd_mysql.c
Patch0:		httpd-2.2.0-buildoutput.patch
#Patch1:	httpd-2.2.0-util_ldap.patch
Patch2:		httpd-ldap_firsttarget.patch
#Patch3:	httpd-2.2.0-pldmysql.patch
Patch4:		httpd-2.2.0-longlongttl.patch
Patch5:		httpd-2.2.0-util_ldap_time.patch
Provides:	webserver
Requires:	perl openssl >= 0.9.8 gdbm expat db4 >= 4.7 openldap >= 2.4
BuildRequires:	perl openssl >= 0.9.8 openldap-devel >= 2.4 make db4-devel >= 4.7
BuildConflicts:	apache2 apache apache2-devel apache-devel apr apr-util

%description
Apache is a powerful web server.  Install this package if you want to
use Apache.  

This package includes mod_ssl support.


%package devel
Summary: Apache include files, etc.
Group: Applications/Internet
Requires: %{name} = %{version}-%{release}

%description devel
This package consists of the Apache include files.


%package utils
Summary: Apache utilities
Group: Applications/Internet
Requires: %{name} = %{version}-%{release}

%description utils
Utilities from Apache that make sense to live outside of webservers.

%package doc
Summary: Apache documentation
Group: Documentation
Requires: %{name} = %{version}-%{release}

%description doc
This package consists of the Apache documentation.

%prep
%setup -q -n httpd-%{apache_ver}

cd modules/ldap
#%patch1
%patch2
%patch5
cd ../..


%patch4 -p1

%build
LDFLAGS="-L/usr/local/ssl/lib -R/usr/local/ssl/lib -L/usr/local/lib -R/usr/local/lib"
export LDFLAGS
LD=/usr/ccs/bin/ld
export LD
SH_LIBTOOL=/usr/local/bin/libtool
export SH_LIBTOOL

# CPPFLAGS for MySQL is TOTALLY BOGUS but apache/autoconf is dumb
# (or maybe we're not using it right)

CC='/opt/SUNWspro/bin/cc' CXX='/opt/SUNWspro/bin/CC' \
CPPFLAGS='-I/usr/local/ssl/include -I/usr/local/include -DLDAP_DEPRECATED' \
CFLAGS='-g -xs' CXXFLAGS='-g -xs' \
./configure --prefix=/usr/local/apache2-%{version} \
        --with-mpm=prefork \
	--with-perl=/usr/bin/perl \
	--with-apr-included \
	--with-apr-util-included \
        --with-ldap=ldap_r --enable-ldap --enable-authnz-ldap \
        --enable-cache --enable-disk-cache --enable-mem-cache \
        --enable-ssl --with-ssl \
        --enable-deflate --enable-cgid \
        --enable-proxy --enable-proxy-connect \
        --enable-proxy-http --enable-proxy-ftp --enable-modules=all \
	--enable-mods-shared=all \

gmake -j3

%install
rm -Rf %{buildroot}
mkdir -p %{buildroot}/usr/local/apache2-%{version}

gmake install DESTDIR=%{buildroot} 
cd %{buildroot}/usr/local 
ln -s apache2-%{version} apache2

rm  %{buildroot}%{apache_prefix}/lib/*.a
rm -f %{buildroot}%{apache_prefix}/lib/*.la
rm -f %{buildroot}%{apache_prefix}/modules/*.a
rm -f %{buildroot}%{apache_prefix}/modules/*.la

%clean
rm -rf %{buildroot}

%post
cat <<EOF
You must configure Apache before use (%{apache_prefix}/conf)
If upgrading from previous package revision (but same Apache version)
your configuration was left alone.

Apache 1.3/2.0 modules may not be compatible with this release.

THERE ARE NO EXAMPLE SSL CERTIFICATES DISTRIBUTED WITH THIS RELEASE
IN ORDER TO USE SSL YOU MUST CREATE SSL CERTIFICATES, read here:
   http://httpd.apache.org/docs-2.0/ssl/ssl_faq.html#realcert
EOF

%files
%defattr(-, root, root)
%dir %{apache_prefix}
%{apache_prefix}/build
%{apache_prefix}/cgi-bin
%config(noreplace)%{apache_prefix}/conf
%{apache_prefix}/error
%{apache_prefix}/icons
%{apache_prefix}/lib
%{apache_prefix}/logs
%{apache_prefix}/modules
%config(noreplace) /usr/local/apache2
%{apache_prefix}/bin/ab
%{apache_prefix}/bin/apachectl
%{apache_prefix}/bin/apr-1-config
%{apache_prefix}/bin/apu-1-config
%{apache_prefix}/bin/apxs
%{apache_prefix}/bin/checkgid
%{apache_prefix}/bin/envvars
%{apache_prefix}/bin/envvars-std
%{apache_prefix}/bin/htcacheclean
%{apache_prefix}/bin/htdbm
%{apache_prefix}/bin/httpd
%{apache_prefix}/bin/httxt2dbm
%{apache_prefix}/bin/logresolve
%{apache_prefix}/bin/rotatelogs


%files doc
%defattr(-, root, root)
%docdir %{apache_prefix}/htdocs
%docdir %{apache_prefix}/manual
%{apache_prefix}/htdocs
%{apache_prefix}/manual
%{apache_prefix}/man

%files devel
%defattr(-, root, root)
%{apache_prefix}/include

%files utils
%defattr(-, root, root)
%{apache_prefix}/man/man1
%{apache_prefix}/bin/dbmmanage
%{apache_prefix}/bin/htdigest
%{apache_prefix}/bin/htpasswd


%changelog
* Fri Jan 08 2010 Russ Frank <rfranknj@nbcs.rutgers.edu> - 2.2.11-2
- Respin against BDB4.8

* Mon Jan 5 2009 David Diffenbaugh <davediff@nbcs.rutgers.edu> - 2.2.11-1
- bumped to 2.2.11

* Tue Oct 21 2008 Brian Schubert <schubert@nbcs.rutgers.edu> - 2.2.10-1
- Built against openldap 2.4 and db4 4.7, updated to version 2.2.10

* Mon Jun 16 2008 David Diffenbaugh <davediff@nbcs.rutgers.edu> 2.2.9-1
- bumped to 2.2.9

* Mon Jan 21 2008 Naveen Gavini <ngavini@nbcs.rutgers.edu> 2.2.8-0
- Bump to 2.2.8

* Thu Sep 13 2007 David Lee Halik <dhalik@nbcs.rutgers.edu> 2.2.6-0
- Bump to 2.2.6

* Thu Dec 14 2006 Leo Zhadanovsky <leozh@nbcs.rutgers.edu> 2.2.3-3
- Changed for OpenSSL 0.9.8

* Tue Jul 12 2005 Jonathan Kaczynski <jmkacz@nbcs.rutgers.edu> 2.0.54-3
- Made sure all sub-packages had Requires: %{name} = %{version}

* Wed Jul 06 2005 Jonathan Kaczynski <jmkacz@nbcs.rutgers.edu> 2.0.54-2
- Removed evil *.a and *.la files
- Commented out section that fiddles with the *.conf files

* Wed Jul 06 2005 Jonathan Kaczynski <jmkacz@nbcs.rutgers.edu> 2.0.54-1
- Updated Apache to 2.0.54

* Wed Aug 25 2004 Jonathan Kaczynski <jmkacz@nbcs.rutgers.edu>
- Updated Apache to 2.0.50

* Tue Feb 4 2003 Christopher Suleski <chrisjs@nbcs.rutgers.edu>
- Apache2 build

* Mon Feb 4 2002 Christopher Suleski <chrisjs@nbcs.rutgers.edu>
- Updated Apache to 1.3.22, modssl 2.8.6

* Thu Dec 20 2001 Samuel Isaacson <sbi@nbcs.rutgers.edu>
- Upgraded to Apache 1.3.22
- Added mod_ssl support
