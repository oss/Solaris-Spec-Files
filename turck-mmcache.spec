Summary: Turck MMCache is a free open source PHP accelerator, optimizer, encoder and dynamic content cache for PHP. 
Name: turck-mmcache 
Version: 2.4.6 
Release: 3
Group: System Environment/Base
Copyright: GPL
Source: turck-mmcache-%{version}.tar.gz
BuildRoot: /var/tmp/%{name}-root
Requires: php-common php-devel
BuildRequires: php-common php-devel

%description
Turck MMCache is a free open source PHP accelerator, optimizer, encoder and dynamic content cache for PHP. It increases performance of PHP scripts by caching them in compiled state, so that the overhead of compiling is almost completely eliminated. Also it uses some optimizations to speed up execution of PHP scripts. Turck MMCache typically reduces server load and increases the speed of your PHP code by 1-10 times. Turck MMCache stores compiled PHP scripts in shared memory and execute code directly from it. Turck MMCache contains a PHP encoder and loader. You can encode PHP scripts using encoder.php in order to distribute them without sources. Encoded files can be run on any site which runs PHP with Turck MMCache 2.3.10 or above. The sources of encoded scripts can't be restored because they are stored in a compiled form and the encoded version doesn't contain the source. Of course, some internals of the scripts can be restored with different reverse engineering tools (disassemblers, debuggers, etc), but it is not trivial.

%prep

%setup -q 
/usr/local/php-4.3.4/bin/phpize
./configure --with-php-config=/usr/local/php-4.3.4/bin/php-config
%build
gmake

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/local/php-modules
mkdir -p $RPM_BUILD_ROOT/usr/local/doc/turck-mmcache
cp modules/*.so $RPM_BUILD_ROOT/usr/local/php-modules 
cp README $RPM_BUILD_ROOT/usr/local/doc/turck-mmcache
cp CREDITS $RPM_BUILD_ROOT/usr/local/doc/turck-mmcache
cp EXPERIMENTAL $RPM_BUILD_ROOT/usr/local/doc/turck-mmcache
cp LICENSE $RPM_BUILD_ROOT/usr/local/doc/turck-mmcache
cp *.php $RPM_BUILD_ROOT/usr/local/doc/turck-mmcache
cp *.ini $RPM_BUILD_ROOT/usr/local/doc/turck-mmcache

%post
cat <<EOF

Turck-MMCache modules are now installed in /usr/local/php-modules
Documentation and sample files are located in /usr/local/doc/turck-mmcache

To configure, do the following:

- Add the following code to php.ini
  [To install as a ZEND extension]
  [NOTE: If you use a thread safe build of PHP, use "zend_extension_ts" instead of
         "zend_extension"]

    zend_extension="/usr/local/php-modules/mmcache.so"
    mmcache.shm_size="16"
    mmcache.cache_dir="/tmp/mmcache"
    mmcache.enable="1"
    mmcache.optimizer="1"
    mmcache.check_mtime="1"
    mmcache.debug="0"
    mmcache.filter=""
    mmcache.shm_max="0"
    mmcache.shm_ttl="0"
    mmcache.shm_prune_period="0"
    mmcache.shm_only="0"
    mmcache.compress="1"

  [To install as a PHP extension]
    
    extension="/usr/local/php-modules/mmcache.so"
    mmcache.shm_size="16"
    mmcache.cache_dir="/var/local/tmp/mmcache"
    mmcache.enable="1"
    mmcache.optimizer="1"
    mmcache.check_mtime="1"
    mmcache.debug="0"
    mmcache.filter=""
    mmcache.shm_max="0"
    mmcache.shm_ttl="0"
    mmcache.shm_prune_period="0"
    mmcache.shm_only="0"
    mmcache.compress="1"

- Then, create the cache directory

    mkdir /var/local/tmp/mmcache
    chmod 0777 /var/local/tmp/mmcache

    


EOF


%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,bin,bin)
/usr/local/php-modules/mmcache.so
/usr/local/doc/turck-mmcache/*
