%define apache_ver    1.3.22
%define mod_ssl_ver   2.8.5

%define apache_prefix /usr/local/apache-%{apache_ver}

%define mod_ssl_dir   mod_ssl-%{mod_ssl_ver}-%{apache_ver}
%define apache_dir    apache_%{apache_ver}

Name: apache
Version: %{apache_ver}
Release: 1
Summary: The Apache webserver
Copyright: BSD-like
Group: Applications/Internet
BuildRoot: %{_tmppath}/%{name}-root
Source0: apache_%{version}.tar.gz
Source1: mod_ssl-%{mod_ssl_ver}-%{apache_ver}.tar.gz

Requires: perl openssl mm
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
  --prefix=%{apache_prefix}
make
make certificate TYPE=dummy

%install
TOPDIR=`pwd`

rm -rf %{buildroot}
mkdir -p %{buildroot}

cd $TOPDIR/%{apache_dir}
make install root=%{buildroot}
for i in %{buildroot}%{apache_prefix}/conf/*.conf ; do
    [ -d $i ] || mv $i $i.rpm
done

%clean
rm -rf %{buildroot}

%post
cat <<EOF
You need to manually configure Apache: edit and move the files named
*.rpm in %{apache_prefix}/conf.  

If you are using SSL, replace the certificates in
%{apache_prefix}/conf/ssl*.
EOF

%files
%defattr(-, root, other)
%{apache_prefix}/bin
%{apache_prefix}/libexec
%{apache_prefix}/man
%{apache_prefix}/conf
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
* Thu Dec 20 2001 Samuel Isaacson <sbi@nbcs.rutgers.edu>
- Upgraded to Apache 1.3.22
- Added mod_ssl support
