%define apache_ver    1.3.26
%define mod_ssl_ver   2.8.9
%define mm_ver        1.1.3
%define apache_prefix /usr/local/apache-%{apache_ver}

%define mod_ssl_dir   mod_ssl-%{mod_ssl_ver}-%{apache_ver}
%define apache_dir    apache_%{apache_ver}

Name: apache
Version: %{apache_ver}
Release: 2
Summary: The Apache webserver
Copyright: BSD-like
Group: Applications/Internet
BuildRoot: %{_tmppath}/%{name}-root
Source0: apache_%{version}.tar.gz
Source1: mod_ssl-%{mod_ssl_ver}-%{apache_ver}.tar.gz
Provides: webserver
Requires: perl openssl mm = %{mm_ver}
BuildRequires: perl openssl mm-devel mm flex make

%description
Apache is a powerful web server.  Install this package if you want to
use Apache.  

This package includes mod_ssl support.

%package devel
Summary: Apache include files, etc.
Group: Applications/Internet
Requires: apache

%description devel
This package consists of the Apache include files.

%package doc
Summary: Apache documentation
Group: Documentation

%description doc
This package consists of the Apache documentation.



%prep
%setup -c -n apache -T

%setup -q -D -n apache -T -a 0
%setup -q -D -n apache -T -a 1


%build
TOPDIR=`pwd`
SSL_BASE="/usr/local/ssl"
EAPI_MM="/usr/local"
LDFLAGS="-L/usr/local/lib -R/usr/local/lib"

export SSL_BASE EAPI_MM LDFLAGS

cd $TOPDIR/%{mod_ssl_dir}
./configure --with-apache=$TOPDIR/%{apache_dir}

cd $TOPDIR/%{apache_dir}
./configure --with-layout=Apache --enable-suexec  --enable-module=ssl \
  --enable-shared=ssl --suexec-caller=www --enable-module=so \
  --prefix=%{apache_prefix} --runtimedir=/tmp/\
  --enable-module=access --enable-shared=access \
  --enable-module=actions --enable-shared=actions \
  --enable-module=alias --enable-shared=alias \
  --enable-module=asis --enable-shared=asis \
  --enable-module=auth  --enable-shared=auth \
  --enable-module=auth_anon   --enable-shared=auth_anon  \
  --enable-module=auth_db   --enable-shared=auth_db  \
  --enable-module=auth_dbm   --enable-shared=auth_dbm  \
  --enable-module=autoindex   --enable-shared=autoindex  \
  --enable-module=cern_meta   --enable-shared=cern_meta  \
  --enable-module=cgi   --enable-shared=cgi  \
  --enable-module=dir   --enable-shared=dir  \
  --enable-module=env   --enable-shared=env  \
  --enable-module=expires   --enable-shared=expires  \
  --enable-module=headers   --enable-shared=headers  \
  --enable-module=imap   --enable-shared=imap  \
#  --enable-module=imap-ssl   --enable-shared=imap-ssl  \
  --enable-module=include   --enable-shared=include  \
  --enable-module=info   --enable-shared=info  \
  --enable-module=log_agent   --enable-shared=log_agent  \
  --enable-module=log_config   --enable-shared=log_config  \
  --enable-module=log_referer   --enable-shared=log_referer  \
  --enable-module=mime   --enable-shared=mime  \
  --enable-module=mime_magic   --enable-shared=mime_magic  \
  --enable-module=negotiation   --enable-shared=negotiation  \
  --enable-module=proxy   --enable-shared=proxy  \
  --enable-module=rewrite   --enable-shared=rewrite  \
  --enable-module=setenvif   --enable-shared=setenvif  \
  --enable-module=speling   --enable-shared=speling  \
  --enable-module=status   --enable-shared=status  \
  --enable-module=unique_id   --enable-shared=unique_id  \
  --enable-module=userdir   --enable-shared=userdir  \
  --enable-module=usertrack   --enable-shared=usertrack  \
  --enable-module=vhost_alias   --enable-shared=vhost_alias 

#  --enable-module=auth_digest   --enable-shared=auth_digest 

make
make certificate TYPE=dummy


%install
TOPDIR=`pwd`

rm -rf %{buildroot}
mkdir -p %{buildroot}

cd $TOPDIR/%{apache_dir}
make install root=%{buildroot}
#for i in %{buildroot}%{apache_prefix}/conf/*.conf ; do
#    [ -d $i ] || mv $i $i.rpm
#done

#Make config not say build user / server
sed "s/ServerAdmin.*rutgers.edu/ServerAdmin root@localhost/" %{buildroot}/usr/local/apache-%{apache_ver}/conf/httpd.conf > %{buildroot}/usr/local/apache-%{apache_ver}/conf/httpd.conf2

sed "s/ServerName.*rutgers.edu/ServerName localhost/" %{buildroot}/usr/local/apache-%{apache_ver}/conf/httpd.conf2 > %{buildroot}/usr/local/apache-%{apache_ver}/conf/httpd.conf

rm %{buildroot}/usr/local/apache-%{apache_ver}/conf/httpd.conf2 


%clean
rm -rf %{buildroot}

%post
cat <<EOF
You must configure Apache before use (%{apache_prefix}/conf)
If upgrading from previous package revision (but same Apache version)
your configuration was left alone.

To utilize OpenSSL, you must replace the sample certificates that are
in %{apache_prefix}/conf/ssl*.

For instructions on how to make your very own certificate, see:
http://www.modssl.org/docs/2.8/ssl_faq.html#ToC28
EOF

%files
%defattr(-, root, other)
%{apache_prefix}/bin
%{apache_prefix}/libexec
%{apache_prefix}/man
%config(noreplace)%{apache_prefix}/conf
%{apache_prefix}/icons
%{apache_prefix}/cgi-bin
%{apache_prefix}/logs
%attr(0755, nobody, nobody) %{apache_prefix}/proxy

%files doc
%defattr(-, root, other)
%{apache_prefix}/htdocs

%files devel
%defattr(-, root, other)
%{apache_prefix}/include


%changelog
* Mon Feb 4 2002 Christopher Suleski <chrisjs@nbcs.rutgers.edu>
- Updated Apache to 1.3.22, modssl 2.8.6

* Thu Dec 20 2001 Samuel Isaacson <sbi@nbcs.rutgers.edu>
- Upgraded to Apache 1.3.22
- Added mod_ssl support
