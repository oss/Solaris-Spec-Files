%define mysql_ver  3.23.46
%define apache_ver 1.3.22
%define php_ver    4.1.0

%define mysql_prefix  /usr/local/mysql-%{mysql_ver}
%define apache_prefix /usr/local/apache-%{apache_ver}
%define php_prefix    /usr/local/php-%{php_ver}

Summary: The PHP scripting language
Name: php
Version: %{php_ver}
Release: 1
License: PHP License
Group: Development/Languages
Source0: php-%{version}.tar.gz
Source1: php_c-client-%{version}.tar.gz
Patch: php-%{version}.patch
BuildRoot: %{_tmppath}/%{name}-root

Requires: apache = %{apache_ver}
Requires: mysql = %{mysql_ver}
Requires: mm openssl gdbm libru.so
BuildRequires: patch make gdbm libru.so
BuildRequires: mysql-devel = %{mysql_ver}
BuildRequires: apache-devel = %{apache_ver}

%description
PHP is a popular scripting language used for CGI programming.  This
package contains an Apache module as well as a standalone executable.

%prep
%setup -q
%setup -q -D -T -b 1
%patch -p1

%build
SSL_BASE="/usr/local/ssl"
EAPI_MM="/usr/local"
LDFLAGS="-L/usr/local/lib -R/usr/local/lib -L%{mysql_prefix}/lib -R%{mysql_prefix}/lib"
CPPFLAGS="-I/usr/local/include"
LIBS="-lru"
export SSL_BASE EAPI_MM LDFLAGS CPPFLAGS LIBS

TOPDIR=`pwd`

./configure --prefix=%{php_prefix} --enable-track-vars \
  --enable-force-cgi-redirect --with-gettext --with-ndbm --enable-ftp \
  --with-apxs=%{apache_prefix}/bin/apxs --with-mysql=/%{mysql_prefix} \
  --with-openssl=/usr/local/ssl --with-imap=$TOPDIR/c-client --enable-shared \
  --enable-sysvshm --enable-sysvsem

make

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}

TOPDIR=`pwd`

/bin/sh $TOPDIR/libtool --silent --silent --mode=install cp libphp4.la \
  $TOPDIR/libs/libphp4.la >/dev/null 2>&1
mkdir -p %{buildroot}%{php_prefix}/bin
mkdir -p %{buildroot}%{php_prefix}/libexec

install -m 0755 $TOPDIR/.libs/libphp4.so \
  %{buildroot}%{php_prefix}/libexec/libphp4.so

mkdir -p %{buildroot}%{apache_prefix}/libexec

# /usr/local/apache-1.3.22/bin/apxs -S LIBEXECDIR="/usr/local/apache-1.3.22/libexec" -i -a -n php4 libs/libphp4.so

cd $TOPDIR/pear && make install prefix=%{buildroot}%{php_prefix}

%post
cat <<EOF
You have to install libphp4.so with apxs(8).  Run

%{apache_prefix}/bin/apxs -S LIBEXECDIR="%{apache_prefix}/libexec" \
  -i -a -n php4 %{php_prefix}/libs/libphp4.so

as root.
EOF

%clean
rm -rf %{buildroot}

%files
%defattr(-, root, other)
%doc TODO CODING_STANDARDS CREDITS LICENSE 
%{php_prefix}

%changelog
* Fri Dec 21 2001 Samuel Isaacson <sbi@nbcs.rutgers.edu>
- Upgraded to PHP 4.1.0 against Apache 1.3.22, MySQL 3.23.46
- Changed build to match TINT package
