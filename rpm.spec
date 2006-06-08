%define with_lua_subpackage     1
%define with_lua_version	5.1
%define	with_python_subpackage	1
%define	with_python_version	2.4
%define	with_perl_subpackage	1
%define	with_bzip2		1
%define	with_apidocs		0

# XXX legacy requires './' payload prefix to be omitted from rpm packages.
%define	_noPayloadPrefix	1



Summary: The RPM package management system.
Name: rpm
%define overallversion 4.4.6
Version: %{overallversion}
#%define release 1
Release: 1
Group: System Environment/Base
Source: ftp://wraptastic.org/pub/rpm-4.4.x/rpm-%{version}.tar.gz
License: GPL
Conflicts: patch < 2.5
Obsoletes: rpm-perl < %{version}
# These are the studsys public keys, I think
# Source2: rpm-4.1-pubkeys
# The documentation about gpg keys
# Source3: rpm-4.1-gpgdoc
##Patch0: rpm-%{version}-rutgers.patch
##Patch1: rpm-%{version}-sun-clean2.patch
##Patch3: rpm-%{version}-reqgpg.patch
###Patch5: rpm-%{version}-all.patch
BuildRequires: beecrypt-devel >= 4.1.2
BuildRequires: neon-devel
BuildRequires: bzip2-devel >= 0.9.0c-2
Requires: beecrypt >= 4.1.2
Requires: popt = 1.10.6
%if %{with_python_subpackage}
# python has no -devel package currently
BuildRequires: python >= %{with_python_version}
Requires: python = %{with_python_version}
%endif
BuildRoot: %{_tmppath}/%{name}-root

%description
The RPM Package Manager (RPM) is a powerful command line driven
package management system capable of installing, uninstalling,
verifying, querying, and updating software packages. Each software
package consists of an archive of files along with information about
the package like its version, a description, etc.


################
### rpm-libs ###
################
%package libs
Summary:  Libraries for manipulating RPM packages.
Group: Development/Libraries

%description libs
This package contains the RPM shared libraries.

#################
### rpm-devel ###
#################
%package devel
Summary:  Development files for manipulating RPM packages.
Group: Development/Libraries
Requires: rpm = %{version}-release
Requires: rpm-libs = %{overallversion}-%{release}
Requires: beecrypt >= 4.1.2
Requires: neon-devel

%description devel
This package contains the RPM C library and header files. These
development files will simplify the process of writing programs that
manipulate RPM packages and databases. These files are intended to
simplify the process of creating graphical package managers or any
other tools that need an intimate knowledge of RPM packages in order
to function.

#################
### rpm-build ###
#################
%package build
Summary: Scripts and executable programs used to build packages.
Group: Development/Tools
Requires: rpm = %{overallversion}-%{release}, patch >= 2.5, file

%description build
The rpm-build package contains the scripts and executable programs
that are used to build packages using the RPM Package Manager.

##################
### rpm-python ###
##################
%if %{with_python_subpackage}
%package python
Summary: Python bindings for apps which will manipulate RPM packages.
Group: Development/Libraries
Requires: rpm = %{overallversion}-%{release}
Requires: rpm-libs = %{overallversion}-%{release}
Requires: python >= %{with_python_version}

%description python
The rpm-python package contains a module that permits applications
written in the Python programming language to use the interface
supplied by RPM Package Manager libraries.

This package should be installed if you want to develop Python
programs that will manipulate RPM packages and databases.
%endif

################
### rpm-perl ###
################
%if %{with_perl_subpackage}
%package perl
Summary: Perl bindings for apps which will manipulate RPM packages.
Group: Development/Libraries
BuildRequires: perl-module-ExtUtils-MakeMaker >= 6.17
Requires: rpm = %{overallversion}-%{release}
Requires: rpm-libs = %{overallversion}-%{release}
Obsoletes: perl-RPM, perl-RPM2
Conflicts: perl-RPM, perl-RPM2

%description perl
The rpm-perl package contains a module that permits applications
written in the Perl programming language to use the interface
supplied by RPM Package Manager libraries.

This package should be installed if you want to develop Perl
programs that will manipulate RPM packages and databases.

(Note: rpm-perl is forked from perl-RPM2-0.66, and will obsolete existing perl-RPM packages)
%endif

###############
### rpm-lua ###
###############
%if %{with_lua_subpackage}
%package lua
Summary: Lua bindings for apps which will manipulate RPM packages.
Group: Development/Libraries
BuildRequires: lua >= %{with_lua_version}
Requires: rpm = %{overallversion}-%{release}
Requires: rpm-libs = %{overallversion}-%{release}

%description lua
...
%endif

############
### POPT ###
############
%package -n popt
Summary: A C library for parsing command line parameters.
Group: Development/Libraries
Version: 1.10.6
#Release: rpm%{overallversion}_%{release}

%description -n popt
Popt is a C library for parsing command line parameters. Popt was
heavily influenced by the getopt() and getopt_long() functions, but it
improves on them by allowing more powerful argument expansion. Popt
can parse arbitrary argv[] style arrays and automatically set
variables based on command line arguments. Popt allows command line
arguments to be aliased via configuration files and includes utility
functions for parsing arbitrary strings into argv[] arrays using
shell-like rules.

Install popt if you are a C programmer and you would like to use its
capabilities.


%prep
%setup -q
##%patch0 -p1
##%patch1 -p1
###%patch5 -p1

#leave this out until repository is all signed
#%patch3 -p1


%build
%if %{with_python_subpackage}
WITH_PYTHON="--with-python=%{with_python_version}"
%else
WITH_PYTHON="--without-python"
%endif

%if %{with_perl_subpackage}
WITH_PERL="--with-perl"
%else
WITH_PERL="--without-perl"
%endif

%if %{with_lua_subpackage}
WITH_LUA="--with-lua=%{with_lua_version}"
%else
WITH_LUA="--without-lua"
%endif

PERL5LIB="/usr/perl5/5.6.1/:$PERL5LIB"
export PERL5LIB
#LD_RUN_PATH="/usr/local/lib"
CPPFLAGS="-I/usr/local/include -I/usr/local/include/python%{with_python_version} -I/opt/SUNWspro/prod/include/"
LDFLAGS="-L/usr/local/lib -R/usr/local/lib -L/opt/SUNWspro/prod/lib/ -R/opt/SUNWspro/prod/lib/"
CC="gcc"
PATH="/usr/local/gnu/bin:/usr/local/bin:/usr/ccs/bin:/usr/bin:/opt/SUNWspro/bin:/usr/openwin/bin:/usr/sbin:/sbin:$PATH"
#export LD_RUN_PATH
export CPPFLAGS LDFLAGS CC PATH

## This only occurs once in the configure script causing lua bindings to
## be built, even if --without-lua is given
#sed "s/WITH_LUA_INCLUDE=\nwithval=yes/WITH_LUA_INCLUDE=\nwithval=no/" configure > configure.2
#mv configure.2 configure
#chmod +x configure
rm -rf sqlite/

./configure --disable-nls --srcdir=`pwd` $WITH_PYTHON $WITH_PERL $WITH_LUA \
--disable-dependency-tracking --sysconfdir=/usr/local/etc \
--prefix=/usr/local --without-javaglue

cp config.h config.h.backup
sed "s/\/etc\/rpm/\/usr\/local\/etc\/rpm\//" config.h > config.h.2
mv config.h.2 config.h

# Use the zlib built in the rpm directory, not the one on the system
sed "s/LIBS = -lz/LIBS = \/usr\/local\/src\/rpm-packages\/BUILD\/rpm-%{overallversion}\/zlib\/.libs\/libz.a/" file/src/Makefile > zzz
mv zzz file/src/Makefile

# No relative rpaths allowed
sed "s/top_builddir = ./top_builddir = \/usr\/local\/src\/rpm-packages\/BUILD\/rpm-%{overallversion}/" Makefile > zzz
mv zzz Makefile
sed "s/top_builddir = ../top_builddir = \/usr\/local\/src\/rpm-packages\/BUILD\/rpm-%{overallversion}/" lua/Makefile > zzz
mv zzz lua/Makefile
sed "s/top_builddir = ../top_builddir = \/usr\/local\/src\/rpm-packages\/BUILD\/rpm-%{overallversion}/" rpmio/Makefile > zzz
mv zzz rpmio/Makefile
sed "s/top_builddir = ../top_builddir = \/usr\/local\/src\/rpm-packages\/BUILD\/rpm-%{overallversion}/" python/Makefile > zzz
mv zzz python/Makefile
sed "s/top_builddir = ../top_builddir = \/usr\/local\/src\/rpm-packages\/BUILD\/rpm-%{overallversion}/" tools/Makefile > zzz
mv zzz tools/Makefile

# No ncurses; only Sun curses
sed "s/-lncurses/-lcurses/" lua/Makefile > zzz
mv zzz lua/Makefile

# Solaris doesn't have stdint.h!
sed "s/#include <stdint.h>//" rpmdb/db.h > zzz
mv zzz rpmdb/db.h

# u_int32_t is undefined
# in db3.c
sed "s/u_int32_t/unsigned int/g" rpmdb/db3.c > zzz
mv zzz rpmdb/db3.c

# u_int32_t is undefined
# actual fix, check "__BIT_TYPES_DEFINED__" in db.h
sed "s/u_int32_t/unsigned int/g" rpmdb/db.h > zzz
mv zzz rpmdb/db.h

# u_int16_t is undefined
# actual fix, check "__BIT_TYPES_DEFINED__" in db.h
sed "s/u_int16_t/unsigned short/g" rpmdb/db.h > zzz
mv zzz rpmdb/db.h

# u_int8_t is undefined
# actual fix, check "__BIT_TYPES_DEFINED__" in db.h
sed "s/u_int8_t/unsigned char/g" rpmdb/db.h > zzz
mv zzz rpmdb/db.h

# u_int is undefined
# actual fix, check "__BIT_TYPES_DEFINED__" in db.h
sed "s/u_int/unsigned int/g" rpmdb/db.h > zzz
mv zzz rpmdb/db.h

# u_long is undefined
# actual fix, check "__BIT_TYPES_DEFINED__" in db.h
sed "s/u_long/unsigned long/g" rpmdb/db.h > zzz
mv zzz rpmdb/db.h

# rpmdb.c seems to have some stuff missing
# http://suse.osuosl.org/people/mmj/rpm-doxygen/html/rpmdb_8c-source.html
/usr/local/bin/sed "s@#include <sys/file.h>@#include <sys/file.h>\n#include <signal.h>\n#include <sys/signal.h>@" rpmdb/rpmdb.c > zzz
mv zzz rpmdb/rpmdb.c

# rpmio/rpmsq.h doesn't have sigset_t defined
/usr/local/bin/sed "s@#include <rpmsw.h>@#include <rpmsw.h>\n#include <signal.h>\n#include <sys/signal.h>@" rpmio/rpmsq.h > zzz
mv zzz rpmio/rpmsq.h

# What is __BEGIN_DECLS? __END_DECLS?
# header-py.h:27: error: syntax error before "hdrObject"
sed "s/__BEGIN_DECLS//" python/header-py.h > zzz
mv zzz python/header-py.h
sed "s/__END_DECLS//" python/header-py.h > zzz
mv zzz python/header-py.h

# What is __BEGIN_DECLS? __END_DECLS?
# rpmal-py.h:30: error: syntax error before "rpmalObject"
sed "s/__BEGIN_DECLS//" python/rpmal-py.h > zzz
mv zzz python/rpmal-py.h
sed "s/__END_DECLS//" python/rpmal-py.h > zzz
mv zzz python/rpmal-py.h

# What is __BEGIN_DECLS? __END_DECLS?
# rpmds-py.h:32: error: syntax error before "rpmds"
sed "s/__BEGIN_DECLS//" python/rpmds-py.h > zzz
mv zzz python/rpmds-py.h
sed "s/__END_DECLS//" python/rpmds-py.h > zzz
mv zzz python/rpmds-py.h

# What is __BEGIN_DECLS? __END_DECLS?
# rpmfd-py.h:29: error: syntax error before "rpmfdObject"
sed "s/__BEGIN_DECLS//" python/rpmfd-py.h > zzz
mv zzz python/rpmfd-py.h
sed "s/__END_DECLS//" python/rpmfd-py.h > zzz
mv zzz python/rpmfd-py.h

# What is __BEGIN_DECLS? __END_DECLS?
# rpmfi-py.h:32: error: syntax error before "rpmfi"
sed "s/__BEGIN_DECLS//" python/rpmfi-py.h > zzz
mv zzz python/rpmfi-py.h
sed "s/__END_DECLS//" python/rpmfi-py.h > zzz
mv zzz python/rpmfi-py.h

# What is __BEGIN_DECLS? __END_DECLS?
# rpmdb-py.h:51: error: syntax error before "__END_DECLS"
sed "s/__BEGIN_DECLS//" python/rpmdb-py.h > zzz
mv zzz python/rpmdb-py.h
sed "s/__END_DECLS//" python/rpmdb-py.h > zzz
mv zzz python/rpmdb-py.h

# What is __BEGIN_DECLS? __END_DECLS?
# rpmmi-py.h:32: error: syntax error before "rpmmiObject"
sed "s/__BEGIN_DECLS//" python/rpmmi-py.h > zzz
mv zzz python/rpmmi-py.h
sed "s/__END_DECLS//" python/rpmmi-py.h > zzz
mv zzz python/rpmmi-py.h

# What is __BEGIN_DECLS? __END_DECLS?
# rpmte-py.h:30: error: syntax error before "rpmteObject"
sed "s/__BEGIN_DECLS//" python/rpmte-py.h > zzz
mv zzz python/rpmte-py.h
sed "s/__END_DECLS//" python/rpmte-py.h > zzz
mv zzz python/rpmte-py.h

# What is __BEGIN_DECLS? __END_DECLS?
# rpmps-py.h:33: error: syntax error before "rpmps"
sed "s/__BEGIN_DECLS//" python/rpmps-py.h > zzz
mv zzz python/rpmps-py.h
sed "s/__END_DECLS//" python/rpmps-py.h > zzz
mv zzz python/rpmps-py.h

# What is __BEGIN_DECLS? __END_DECLS?
# rpmts-py.h:41: error: syntax error before "rpmtsObject"
sed "s/__BEGIN_DECLS//" python/rpmts-py.h > zzz
mv zzz python/rpmts-py.h
sed "s/__END_DECLS//" python/rpmts-py.h > zzz
mv zzz python/rpmts-py.h

# What is __BEGIN_DECLS? __END_DECLS?
# spec-py.h:31: error: syntax error before "Spec"
sed "s/__BEGIN_DECLS//" python/spec-py.h > zzz
mv zzz python/spec-py.h
sed "s/__END_DECLS//" python/spec-py.h > zzz
mv zzz python/spec-py.h

# What is __BEGIN_DECLS? __END_DECLS?
# premptive rpmrc-py.h
sed "s/__BEGIN_DECLS//" python/rpmrc-py.h > zzz
mv zzz python/rpmrc-py.h
sed "s/__END_DECLS//" python/rpmrc-py.h > zzz
mv zzz python/rpmrc-py.h

# Levels are wrong in perl/RPM-0.66/Makefile
# /usr/include/rpm ... pointless?
sed "s@INC = -I../lib -I../rpmdb -I../rpmio -I../popt -I/usr/include/rpm@INC = -I../../lib -I../../rpmdb -I../../rpmio -I../../popt -I/usr/include/rpm@" perl/RPM-0.66/Makefile > zzz
mv zzz perl/RPM-0.66/Makefile

# Modify perl Makefiles to be the same as %{pmake_install}
# from perl-header.spec
sed "s@^PREFIX = .*\$@PREFIX = %{buildroot}/usr/perl5@" perl/Makefile > zzz
mv zzz perl/Makefile
sed "s@^INSTALLARCHLIB = .*\$@INSTALLARCHLIB = \$(PREFIX)/5.6.1/lib/sun4-solaris-64int@" perl/Makefile > zzz
mv zzz perl/Makefile
sed "s@^INSTALLSITEARCH = .*\$@INSTALLSITEARCH = \$(PREFIX)/site_perl/5.6.1/sun4-solaris-64int@" perl/Makefile > zzz
mv zzz perl/Makefile
sed "s@^INSTALLPRIVLIB = .*\$@INSTALLPRIVLIB = \$(PREFIX)/5.6.1@" perl/Makefile > zzz
mv zzz perl/Makefile
sed "s@^INSTALLSITELIB = .*\$@INSTALLSITELIB = \$(PREFIX)/site_perl/5.6.1@" perl/Makefile > zzz
mv zzz perl/Makefile
sed "s@^INSTALLBIN = .\$@INSTALLBIN = \$(PREFIX)/bin@" perl/Makefile > zzz
mv zzz perl/Makefile
sed "s@^INSTALLSCRIPT = .\$@INSTALLSCRIPT = \$(PREFIX)/bin@" perl/Makefile > zzz
mv zzz perl/Makefile
sed "s@^INSTALLMAN1DIR = .\$@INSTALLMAN1DIR = \$(PREFIX)/man/man1@" perl/Makefile > zzz
mv zzz perl/Makefile
sed "s@^INSTALLMAN3DIR = .\$@INSTALLMAN3DIR = \$(PREFIX)/man/man3@" perl/Makefile > zzz
mv zzz perl/Makefile

gmake

#cp rpmrc rpmrc.backup
#%ifarch sparc
#sed "s/buildarchtranslate\:\ sparcv9\:\ sparc64/buildarchtranslate\:\ sparcv9\:\ sparc/" rpmrc > rpmrc.2
#sed "s/buildarchtranslate\:\ sun4u\:\ sparc64/buildarchtranslate\:\ sun4u\:\ sparc/" rpmrc.2 > rpmrc.3
#sed "s/osps_canon/os_canon/" rpmrc.3 > rpmrc
#%endif


%install
rm -rf %{buildroot}

# cp %{SOURCE3} RPM-GPG-README
gmake DESTDIR=%{buildroot} install
# mv %{buildroot}/usr/local/src/sun %{buildroot}/usr/local/src/rpm-packages
# cp %{SOURCE2} RPM-GPG-KEYS

mkdir -p %{buildroot}/etc/rpm
mkdir -p %{buildroot}/var/local/lib/rpm
for dbi in \
	Basenames Conflictname Dirnames Group Installtid Name Packages \
	Providename Provideversion Requirename Requireversion Triggername \
	Filemd5s Pubkeys Sha1header Sigmd5 \
	__db.001 __db.002 __db.003 __db.004 __db.005 __db.006 __db.007 \
	__db.008 __db.009
do
    touch %{buildroot}/var/local/lib/rpm/$dbi
done

# Get rid of unpackaged files
{
  rm %{buildroot}/usr/local/lib/*.la
  rm -f %{buildroot}/usr/local/lib/rpm/{Specfile.pm,cpanflute,cpanflute2,rpmdiff,rpmdiff.cgi,sql.prov,sql.req,tcl.req}
  rm -rf %{buildroot}/usr/local/man/{fr,ja,ko,pl,ru,sk}
  rm -f %{buildroot}/usr/local/bin/rpm{e,i,u}
%if %{with_python_subpackage}
  rm -f %{buildroot}/usr/local/lib/python%{with_python_version}/site-packages/*.{a,la}
  rm -f %{buildroot}/usr/local/lib/python%{with_python_version}/site-packages/rpm/*.{a,la}
%endif
%if %{with_perl_subpackage}
  /usr/local/gnu/bin/find %{buildroot}/usr/perl5 -type f -a \( -name perllocal.pod -o -name .packlist \
    -o \( -name '*.bs' -a -empty \) \) -exec rm -f {} ';'
  /usr/local/gnu/bin/find %{buildroot}/usr/perl5 -type d -depth -exec rmdir {} 2>/dev/null ';'
%endif
}


%clean
#rm -rf %{buildroot}


%post
#if [ -f /var/local/lib/rpm/packages.rpm ]; then
#    : # do nothing
#elif [ -f /var/local/lib/rpm/Packages ]; then
#    # undo db1 configuration
#    rm -f /etc/rpm/macros.db1
#else
#    # initialize db3 database
#    rm -f /etc/rpm/macros.db1
#    /usr/local/bin/rpm --initdb
#fi

cat<<EOF 

Upgrading to RPM 4.1 REQUIRES intervention
APT now checks for GPG signatures before installing packages.
You must import the public GPG keys you trust into RPM using:
     rpm --import /usr/local/doc/rpm-4.1/RPM-GPG-KEYS
this file contains the NBCS package signers' public keys. You
may wish to validate this against: http://keyserver.rutgers.edu
More information is available in the RPM-GPG-README document.

EOF


%files
%defattr(-,root,root)
#%doc RPM-PGP-KEY RPM-GPG-KEY BETA-GPG-KEY CHANGES GROUPS doc/manual/[a-z]*
%attr(0755, rpm, rpm)	/usr/local/bin/rpm
%attr(0755, rpm, rpm)	/usr/local/bin/rpm2cpio
%attr(0755, rpm, rpm)	/usr/local/bin/gendiff
%attr(0755, rpm, rpm)	/usr/local/bin/rpmdb
%attr(0755, rpm, rpm)	/usr/local/bin/rpmsign
%attr(0755, rpm, rpm)	/usr/local/bin/rpmquery
%attr(0755, rpm, rpm)	/usr/local/bin/rpmverify
%attr(0755, rpm, rpm)	%dir /usr/local/lib/rpm
%attr(0755, rpm, rpm)	/usr/local/lib/rpm/config.guess
%attr(0755, rpm, rpm)	/usr/local/lib/rpm/config.sub
%attr(0755, rpm, rpm)	/usr/local/lib/rpm/convertrpmrc.sh
%attr(0755, rpm, rpm)	/usr/lcoal/lib/rpm/freshen.sh
%attr(0644, rpm, rpm)	/usr/local/lib/rpm/macros
%attr(0755, rpm, rpm)	/usr/local/lib/rpm/mkinstalldirs
%attr(0755, rpm, rpm)	/usr/local/lib/rpm/rpm.*
%attr(0755, rpm, rpm)	/usr/local/lib/rpm/rpm2cpio.sh
%attr(0755, rpm, rpm)	/usr/local/lib/rpm/rpm[deiukqv]
%attr(0755, rpm, rpm)	/usr/local/lib/rpm/tgpg
%attr(0644, rpm, rpm)	/usr/local/lib/rpm/rpmpopt*
%attr(0644, rpm, rpm)	/usr/local/lib/rpm/rpmrc
%attr(-, rpm, rpm)	/usr/local/lib/rpm/sparc*
%attr(-, rpm, rpm)	/usr/local/lib/rpm/noarch*
%attr(0755, rpm, rpm)	/usr/local/lib/rpm/rpmdb_*
%attr(0755, rpm, rpm)	/usr/local/lib/rpm/rpmfile
/usr/local/man/man8/rpm.8
/usr/local/man/man8/rpm2cpio.8

#/etc/cron.daily/rpm
#/etc/logrotate.d/rpm
#/etc/rpm
#/var/lib/rpm/Basenames
#/var/lib/rpm/Conflictname
#/var/lib/rpm/Dirnames
#/var/lib/rpm/Filemd5s
#/var/lib/rpm/Group
#/var/lib/rpm/Installtid
#/var/lib/rpm/Name
#/var/lib/rpm/Packages
#/var/lib/rpm/Providename
#/var/lib/rpm/Provideversion
#/var/lib/rpm/Pubkeys
#/var/lib/rpm/Requirename
#/var/lib/rpm/Requireversion
#/var/lib/rpm/Sha1header
#/var/lib/rpm/Sigmd5
#/var/lib/rpm/Triggername
#/var/lib/rpm/__db.001
#/var/lib/rpm/__db.002
#/var/lib/rpm/__db.003
#/var/lib/rpm/__db.004
#/var/lib/rpm/__db.005
#/var/lib/rpm/__db.006
#/var/lib/rpm/__db.007
#/var/lib/rpm/__db.008
#/var/lib/rpm/__db.009
#/var/spool/repackage


%files libs
%defattr(-,root,root)
/usr/local/lib/librpm-4.4.so
/usr/local/lib/librpmdb-4.4.so
/usr/local/lib/librpmio-4.4.so
/usr/local/lib/librpmbuild-4.4.so


%files build
%defattr(-,root,root)
%dir /usr/local/src/rpm
%attr(0777,root,root)   %dir /usr/local/src/rpm/BUILD
%attr(0777,root,root)   %dir /usr/local/src/rpm/SPECS
%attr(0777,root,root)   %dir /usr/local/src/rpm/SOURCES
%attr(0777,root,root)   %dir /usr/local/src/rpm/SRPMS
%attr(0777,root,root)   %dir /usr/local/src/rpm/RPMS
%attr(0777,root,root)   /usr/local/src/rpm/RPMS/*
%attr(0755, rpm, rpm)	/usr/local/bin/rpmbuild
%attr(0755, rpm, rpm)	/usr/local/lib/rpm/brp-*
%attr(0755, rpm, rpm)	/usr/local/lib/rpm/check-files
%attr(0755, rpm, rpm)	/usr/local/lib/rpm/check-prereqs
%attr(0755, rpm, rpm)	/usr/local/lib/rpm/config.site
%attr(0755, rpm, rpm)	/usr/local/lib/rpm/cross-build
#%attr(0755, rpm, rpm)	/usr/local/lib/rpm/debugedit
%attr(0755, rpm, rpm)	/usr/local/lib/rpm/find-*
%attr(0755, rpm, rpm)	/usr/local/lib/rpm/get_magic.pl
%attr(0755, rpm, rpm)	/usr/local/lib/rpm/getpo.sh
%attr(0755, rpm, rpm)	/usr/local/lib/rpm/http.req
%attr(0755, rpm, rpm)	/usr/local/lib/rpm/javadeps.sh
%attr(0755, rpm, rpm)	/usr/local/lib/rpm/javadeps
%attr(0755, rpm, rpm)	/usr/local/lib/rpm/magic
%attr(0755, rpm, rpm)	/usr/local/lib/rpm/magic.*
%attr(0755, rpm, rpm)	/usr/local/lib/rpm/executabledeps.sh
%attr(0755, rpm, rpm)	/usr/local/lib/rpm/libtooldeps.sh
%attr(0755, rpm, rpm)	/usr/local/lib/rpm/perldeps.pl
%attr(0755, rpm, rpm)	/usr/local/lib/rpm/perl.prov
%attr(0755, rpm, rpm)	/usr/local/lib/rpm/perl.req
%attr(0755, rpm, rpm)	/usr/local/lib/rpm/pkgconfigdeps.sh
%attr(0755, rpm, rpm)	/usr/local/lib/rpm/pythondeps.sh
%attr(0755, rpm, rpm)	/usr/local/lib/rpm/rpmdeps
%attr(0755, rpm, rpm)	/usr/local/lib/rpm/rpm[bt]
%attr(0755, rpm, rpm)	/usr/local/lib/rpm/trpm
%attr(0755, rpm, rpm)	/usr/local/lib/rpm/u_pkg.sh
%attr(0755, rpm, rpm)	/usr/local/lib/rpm/vpkg-provides.sh
%attr(0755, rpm, rpm)	/usr/local/lib/rpm/vpkg-provides2.sh
/usr/local/man/man1/gendiff.1
/usr/local/man/man8/rpmbuild.8
/usr/local/man/man8/rpmdeps.8


%if %{with_python_subpackage}
%files python
%defattr(-,root,root)
/usr/local/lib/python%{with_python_version}/site-packages/rpm
%endif


%if %{with_perl_subpackage}
%files perl
%defattr(-,root,root)
/usr/perl5/site_perl/sun4-solaris-64int/auto/auto/RPM
/usr/perl5/site_perl/sun4-solaris-64int/RPM.*
/usr/perl5/man/man3/RPM.*
%endif


%if %{with_lua_subpackage}
%files lua
%defattr(-,root,root)
%endif


%files devel
%defattr(-,root,root)
/usr/local/include/rpm
/usr/local/lib/librpm.a
/usr/local/lib/librpm.so
/usr/local/lib/librpmdb.a
/usr/local/lib/librpmdb.so
/usr/local/lib/librpmio.a
/usr/local/lib/librpmio.so
/usr/local/lib/librpmbuild.a
/usr/local/lib/librpmbuild.so
%attr(0755, rpm, rpm)	/usr/local/lib/rpm/rpmcache
%attr(0755, rpm, rpm)	/usr/local/bin/rpmgraph
/usr/local/man/man8/rpmcache.8
/usr/local/man/man8/rpmgraph.8


%files -n popt
%defattr(-,root,root)
/usr/local/lib/libpopt.so.*
/usr/local/man/man3/popt.3*
# XXX These may end up in popt-devel but it hardly seems worth the effort.
/usr/local/lib/libpopt.a
/usr/local/lib/libpopt.so
/usr/local/include/popt.h


%changelog
* Thu Jun 08 2006 Jonathan Kaczynski <jmkacz@nbcs.rutgers.edu> 4.4.6-1
 - Built latest version.