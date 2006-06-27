%define php_version 4.4.2

Summary: eAccelerator
Name: eAccelerator
Version: 0.9.5_beta2
Release: 1
Group: Applications/Internet
Source: eaccelerator-0.9.5-beta2.tar.bz2
Copyright: GPL
Requires: apache2
Requires: apache2-module-php = %{php_version}
Requires: php-common = %{php_version}
# autoconf, automake, libtool, m4
# or apache >= 1.3 apache-module-php = 4.4.2 php-common = 4.4.2
BuildRequires: php-devel = %{php_version}
BuildRequires: php-common = %{php_version}
BuildRoot: %{_tmppath}/%{name}-root


%description
eAccelerator is a further development of the mmcache PHP accelerator and
encoder. It increases the performance of PHP scripts by caching them in a
compiled state, so that the overhead of compiling is almost completely
eliminated.


%prep
%setup -qn eaccelerator-0.9.5-beta2


%build
PHP_PREFIX="/usr/local/php-%{php_version}"
CC="/opt/SUNWspro/bin/cc"
CXX="/opt/SUNWspro/bin/CC"
CFLAGS="-g -xs"
CPPFLAGS="-I/usr/local/include -I/usr/local/php-%{php_version}/include"
LD="/usr/ccs/bin/ld"
LDFLAGS="-L/usr/local/lib -R/usr/local/lib"
PATH="/usr/local/gnu/bin:/usr/local/bin:/usr/ccs/bin:/opt/SUNWspro/bin:/usr/openwin/bin:/usr/bin:/usr/sbin:/sbin:$PATH"
export PHP_PREFIX CC CXX CFLAGS CPPFLAGS LD LDFLAGS PATH

$PHP_PREFIX/bin/phpize

./configure \
--enable-eaccelerator=shared \
--with-php-config=$PHP_PREFIX/bin/php-config \
--with-eaccelerator-userid=www
make


%install
sed "s/$(INSTALL_ROOT)/$(DESTDIR)$(INSTALL_ROOT)/" Makefile > Makefile.2
mv Makefile.2 Makefile
make install DESTDIR=%{buildroot}
mkdir -p %{buildroot}/usr/local/php-modules
mv %{buildroot}/usr/local/php-4.4.2/lib/php/extensions/no-debug-non-zts-20020429/eaccelerator.so %{buildroot}/usr/local/php-modules


%clean
rm -rf %{buildroot}


%post
cat << EOF

WARNING: To use sysvipc semaphores, eAccelerator must run as uid "www"
EOF
echo "You need to edit your /usr/local/php-%{php_version}/lib/php.ini file."
echo "You need to add the following lines to it:"
echo "  extension=\"eaccelerator.so\""
echo "  eaccelerator.shm_size=\"16\""
echo "  eaccelerator.cache_dir=\"/tmp/eaccelerator\""
echo "  eaccelerator.enable=\"1\""
echo "  eaccelerator.optimizer=\"1\""
echo "  eaccelerator.check_mtime=\"1\""
echo "  eaccelerator.debug=\"0\""
echo "  eaccelerator.filter=\"\""
echo "  eaccelerator.shm_max=\"0\""
echo "  eaccelerator.shm_ttl=\"0\""
echo "  eaccelerator.shm_prune_period=\"0\""
echo "  eaccelerator.shm_only=\"0\""
echo "  eaccelerator.compress=\"1\""
echo "  eaccelerator.compress_level=\"9\""
#mkdir /tmp/eaccelerator
#chmod 0777 /tmp/eaccelerator


%postun
#rm -rf /tmp/eaccelerator


%files
%defattr(-,bin,bin)
%doc AUTHORS COPYING ChangeLog README NEWS
/usr/local/php-modules/eaccelerator.so
#/usr/local/doc/turck-mmcache/*

%changelog
* Mon May 08 2006 Jonathan Kaczynski <jmkacz@nbcs.rutgers.edu> - 0.9.5-beta2
- Initial package.




#Step 1. Compiling eAccelerator
#  export PHP_PREFIX="/usr"
#  $PHP_PREFIX/bin/phpize 
#  ./configure \
#  --enable-eaccelerator=shared \
#  --with-php-config=$PHP_PREFIX/bin/php-config  
#  make
#  You must specify the real prefix where PHP is installed in the "export"
#  command. It may be "/usr" "/usr/local", or something else.

#Step 2. Installing eAccelerator
#  make install

#Step 3. Configuring eAccelerator
#eAccelerator can be installed both as Zend or PHP extension.
#For eaccelerator > 0.9.1, if you have /etc/php.d directory, you should copy
#eaccelerator.ini inside and modify default value if you need.
#If not, you need to edit your php.ini file (usually /etc/php.ini).
#To install as PHP extension:
#  extension="eaccelerator.so"
#  eaccelerator.shm_size="16"
#  eaccelerator.cache_dir="/tmp/eaccelerator"
#  eaccelerator.enable="1"
#  eaccelerator.optimizer="1"
#  eaccelerator.check_mtime="1"
#  eaccelerator.debug="0"
#  eaccelerator.filter=""
#  eaccelerator.shm_max="0"
#  eaccelerator.shm_ttl="0"
#  eaccelerator.shm_prune_period="0"
#  eaccelerator.shm_only="0"
#  eaccelerator.compress="1"
#  eaccelerator.compress_level="9"  

#Step 4. Creating cache directory
#  mkdir /tmp/eaccelerator
#  chmod 0777 /tmp/eaccelerator
