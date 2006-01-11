%define apache_ver    2.2.0
%define apache_prefix /usr/local/apache2-%{apache_ver}
%define mysql_ver     5.0.18

Name: apache2
Version: %{apache_ver}
Release: 7
Summary: The Apache webserver
Copyright: BSD-like
Group: Applications/Internet
BuildRoot: %{_tmppath}/%{name}-root
Source0: httpd-%{version}.tar.bz2
Source1: http://apache.webthing.com/database/apr_dbd_mysql.c
Patch0: httpd-2.2.0-buildoutput.patch
Patch1: httpd-2.2.0-util_ldap.patch
Patch2: httpd-ldap_firsttarget.patch
Patch3: httpd-2.2.0-pldmysql.patch
Provides: webserver
Requires: perl openssl gdbm expat db4
BuildRequires: perl openssl sqlite-devel mysql5-devel = %{mysql_ver} openldap-devel >= 2.3 make db4-devel >= 4.2
BuildConflicts: apache2 apache apache2-devel apache-devel

%description
Apache is a powerful web server.  Install this package if you want to
use Apache.  

This package includes mod_ssl support.


%package devel
Summary: Apache include files, etc.
Group: Applications/Internet
Requires: %{name} = %{version}

%description devel
This package consists of the Apache include files.


%package doc
Summary: Apache documentation
Group: Documentation
Requires: apache2
Requires: %{name} = %{version}

%description doc
This package consists of the Apache documentation.

%prep
%setup -q -n httpd-%{apache_ver}
# Throw in the GPL sauce
cp %{SOURCE1} srclib/apr-util/dbd
cd srclib/apr-util
%patch0
cd ../..

cd modules/ldap
%patch1
%patch2
cd ../..

cd srclib/apr-util/dbd
%patch3 -p1
cd ../../..

%build
LDFLAGS="-L/usr/local/ssl/lib -R/usr/local/ssl/lib -L/usr/local/lib -R/usr/local/lib -L/usr/local/mysql-%{mysql_ver}/lib -R/usr/local/mysql-%{mysql_ver}/lib"
export LDFLAGS

# CPPFLAGS for MySQL is TOTALLY BOGUS but apache/autoconf is dumb
# (or maybe we're not using it right)

CC='/opt/SUNWspro/bin/cc' CXX='/opt/SUNWspro/bin/CC' \
CPPFLAGS='-I/usr/local/ssl/include -I/usr/local/include -I/usr/local/mysql-%{mysql_ver}/include -DLDAP_DEPRECATED' \
CFLAGS='-g -xs' CXXFLAGS='-g -xs' \
./configure --prefix=/usr/local/apache2-%{version} \
        --with-mpm=prefork \
        --with-ldap=ldap_r --enable-ldap --enable-authnz-ldap \
        --enable-cache --enable-disk-cache --enable-mem-cache \
        --enable-ssl --with-ssl \
        --enable-deflate --enable-cgid \
        --enable-proxy --enable-proxy-connect \
        --enable-proxy-http --enable-proxy-ftp --enable-modules=all \
	--enable-mods-shared=all --with-mysql=/usr/local/mysql-%{mysql_ver} \
	--with-sqlite3=/usr/local

gmake -j3

%install
rm -Rf %{buildroot}
mkdir -p %{buildroot}/usr/local/apache2-%{version}

gmake install DESTDIR=%{buildroot} 
cd %{buildroot}/usr/local 
ln -s apache2-%{version} apache2

rm -f %{buildroot}%{apache_prefix}/lib/*.a
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
%defattr(-, root, other)
#%{apache_prefix}
%{apache_prefix}/bin
%{apache_prefix}/build
%{apache_prefix}/cgi-bin
%config(noreplace)%{apache_prefix}/conf
%{apache_prefix}/error
%{apache_prefix}/icons
%{apache_prefix}/lib
%{apache_prefix}/logs
%{apache_prefix}/modules
%config(noreplace) /usr/local/apache2

%files doc
%defattr(-, root, other)
%{apache_prefix}/htdocs
%{apache_prefix}/man
%{apache_prefix}/manual

%files devel
%defattr(-, root, other)
%{apache_prefix}/include


%changelog
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
