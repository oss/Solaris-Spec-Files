%define php4_version 4.4.8

Summary: 	eAccelerator for php4
Name: 		eAccelerator-php4
Version: 	0.9.5.3
Release: 	2
Group: 		Applications/Internet
Source: 	eaccelerator-%{version}.tar.bz2
Copyright: 	GPL
BuildRoot: 	%{_tmppath}/%{name}-root
Requires: apache
Requires: apache-module-php = %{php4_version}
Requires: php-common = %{php4_version}
BuildRequires: php-devel = %{php4_version}
BuildRequires: php-common = %{php4_version}

%description
eAccelerator is a further development of the mmcache PHP accelerator and
encoder. It increases the performance of PHP scripts by caching them in a
compiled state, so that the overhead of compiling is almost completely
eliminated.

%package doc
Summary: docs for eAccelerator-php4 
Group: Applications/Internet

%description doc
documents package for eAccelerator-php4

%prep
%setup -qn eaccelerator-%{version}

%build

#php4 build
PHP_PREFIX="/usr/local/"
CC="/opt/SUNWspro/bin/cc"
CXX="/opt/SUNWspro/bin/CC"
CFLAGS="-g -xs"
CPPFLAGS="-I/usr/local/include" 
LD="/usr/ccs/bin/ld"
LDFLAGS="-L/usr/local/lib -R/usr/local/lib"
PATH="/usr/local/gnu/bin:/usr/local/bin:/usr/ccs/bin:/opt/SUNWspro/bin:/usr/openwin/bin:/usr/bin:/usr/sbin:/sbin:$PATH"
export PHP_PREFIX CC CXX CFLAGS CPPFLAGS LD LDFLAGS PATH

$PHP_PREFIX/bin/phpize

./configure \
--enable-eaccelerator=shared \
--with-php-config=$PHP_PREFIX/bin/php-config \
--with-eaccelerator-userid=www --disable-nls
gmake
gmake test

%install
sed "s/$(INSTALL_ROOT)/$(DESTDIR)$(INSTALL_ROOT)/" Makefile > Makefile.2
mv Makefile.2 Makefile
gmake install DESTDIR=%{buildroot}
mkdir -p %{buildroot}/usr/local/libexec/php4
mv `find %{buildroot} -name eaccelerator.so` %{buildroot}/usr/local/libexec/php4

%clean
rm -rf %{buildroot}

%post
cat << EOF

WARNING: To use sysvipc semaphores, eAccelerator must run as uid "www"
EOF
echo "You need to edit your /usr/local/etc/php.ini file."
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
/usr/local/libexec/php4/eaccelerator.so

%files doc
%doc AUTHORS COPYING ChangeLog README NEWS

%changelog
* Wed Jul 30 2008 David Diffenbaugh <davediff@nbcs.rutgers.edu> - 0.9.5.3-2
- uncommented defattr line

* Mon Jun 16 2008 David Diffenbaugh <davediff@nbcs.rutgers.edu> - 0.9.5.3-1
- bumped to 0.9.5.3
- created eAccelerator-php4.spec since php4 and php5 installations can no longer co-exist

* Wed Apr 09 2008 David Diffenbaugh <davediff@nbcs.rutgers.edu> - 0.9.5.2-4
- changed path from /usr/local/libexec/php to /usr/local/libexec/php5

* Thu Feb 28 2008 David Diffenbaugh <davediff@nbcs.rutgers.edu> - 0.9.5.2-2
- broke into subpackages for php4, php5, and doc

* Thu Nov 15 2007 Naveen Gavini <ngavini@nbcs.rutgers.edu> - 0.9.5.2-1
- Updated to the latest version and disabled NLS.

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
