Summary: The PHP scripting language
Name: php
Version: 4.0.2
Release: 2
License: PHP License
Group: Development/Languages
Source0: php-%{version}.tar.gz
Source1: number4.tar.gz
Requires: mysql
Requires: apache
BuildRoot: /var/tmp/%{name}-root
BuildRequires: mysql-devel
BuildRequires: apache-devel

%description
PHP is a popular scripting language used for CGI programming.  This
package contains an Apache module as well as a standalone executable.

%prep
%setup -q
%setup -q -D -T -a 1

%build
LD="/usr/ccs/bin/ld -L/usr/local/lib -R/usr/local/lib" \
    LDFLAGS="-L/usr/local/lib -R/usr/local/lib" \
    CPPFLAGS="-I/usr/local/include" ./configure --with-mysql=/usr/local/mysql \
    --enable-bcmath --enable-safe-mode --enable-memory-limit \
    --with-exec-dir=/usr/local/apache/phpexec --with-readline \
    --enable-discard-path
make
mv php php.keepme
rm config.cache
LD="/usr/ccs/bin/ld -L/usr/local/lib -R/usr/local/lib" \
    LDFLAGS="-L/usr/local/lib -R/usr/local/lib" \
    CPPFLAGS="-I/usr/local/include" ./configure --with-mysql=/usr/local/mysql \
    --with-apxs=/usr/local/apache/bin/apxs --enable-bcmath --enable-safe-mode \
    --enable-memory-limit --with-exec-dir=/usr/local/apache/phpexec \
    --with-readline --enable-discard-path
make clean
make
mv php.keepme php

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/local/apache/libexec
mkdir $RPM_BUILD_ROOT/usr/local/bin
install -m 0755 .libs/libphp4.so $RPM_BUILD_ROOT/usr/local/apache/libexec/libphp4.so
install -m 0755 php $RPM_BUILD_ROOT/usr/local/bin/php

%post
cat <<EOF
You have to install libphp4.so with apxs(8).
EOF

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,other)
%doc TODO CODING_STANDARDS CREDITS LICENSE 
/usr/local/apache/libexec/libphp4.so
/usr/local/bin/php
