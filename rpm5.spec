%define	with_python_version	2.4
%define overallversion 5.0b2

Summary:	The RPM package management system.
Name:		rpm
Version:	%{overallversion}
Release:	1
Group:		System Environment/Base
Source0:	ftp://wraptastic.org/pub/rpm-4.4.x/rpm-%{version}.tar.gz
Patch0:		rpm-5.0b1-linkage.patch
Patch1:		rpm-5.0a3-dbfix.patch
Patch2:		rpm-5.0a3-buildfix.patch
Source1:	rpm-4.4.9-macros.patch
Source2:	rpm-4.4.9-provides.patch
License:	GPL
Requires:	beecrypt >= 4.1.3, neon >= 0.26, popt >= 1.10.9
Requires:	rpm-libs = %{overallversion}-%{release}
BuildRequires:	bzip2-devel >= 1.0.4-6, perl
BuildRequires:	python >= %{with_python_version}, libtool-devel >= 1.5.24
BuildRequires:	neon-devel >= 0.26, beecrypt-devel >= 4.1.2, expat, perl-module-ExtUtils-MakeMaker >= 6.31
BuildRoot:	%{_tmppath}/%{name}-root
BuildArch:	sparc64

# These are the studsys public keys, I think
# Source2: rpm-4.1-pubkeys
# The documentation about gpg keys
# Source3: rpm-4.1-gpgdoc
# Patch5: rpm-%{version}-reqgpg.patch
#BuildRequires: beecrypt-devel >= 4.1.2

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
Requires: rpm = %{overallversion}-%{release}
Requires: rpm-libs = %{overallversion}-%{release}
Requires: beecrypt >= 4.1.3
Requires: neon-devel < 0.27

%description devel
This package contains the RPM C library and header files. These
development files will simplify the process of writing programs that
manipulate RPM packages and databases. These files are intended to
simplify the process of creating graphical package managers or any
other tools that need an intimate knowledge of RPM packages in order
to function.

##################
### rpm-static ###
##################
%package static
Summary:  Static development files for manipulating RPM packages.
Group: Development/Libraries
Requires: rpm = %{overallversion}-%{release}
Requires: rpm-libs = %{overallversion}-%{release}
Requires: rpm-devel = %{overallversion}-%{release}

%description static
This package contains the static rpm libraries. These
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


################
### rpm-perl ###
################
%package perl
Summary: Perl bindings for apps which will manipulate RPM packages.
Group: Development/Libraries
BuildRequires: perl-module-ExtUtils-MakeMaker >= 6.31
Requires: rpm = %{overallversion}-%{release}
Requires: rpm-libs = %{overallversion}-%{release}

%description perl
The rpm-perl package contains a module that permits applications
written in the Perl programming language to use the interface
supplied by RPM Package Manager libraries.

This package should be installed if you want to develop Perl
programs that will manipulate RPM packages and databases.

#(Note: rpm-perl is forked from perl-RPM2-0.66, and will obsolete existing perl-RPM packages)

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1

%build
CPPFLAGS="-I/usr/local/include -I/usr/local/include/python%{with_python_version} \
	-I/usr/local/include/beecrypt -I/usr/local/ssl/include"
LDFLAGS="-L/usr/local/lib -R/usr/local/lib -L/usr/local/ssl/lib -R/usr/local/ssl/lib"
CC="cc"
CXX="CC"
CFLAGS="-g -xs -DWITH_DB"
PATH="/opt/SUNWspro/bin:/usr/local/gnu/bin:$PATH"
PERL5LIB="/usr/perl5/5.6.1/:$PERL5LIB"
LD="/usr/ccs/bin/ld"
export CPPFLAGS LDFLAGS CC CXX PATH CFLAGS PERL5LIB LD

./configure \
	--srcdir=`pwd` \
	--with-python=%{with_python_version} \
	--with-perl \
	--sysconfdir="/usr/local/etc" \
	--prefix="/usr/local" \
	--with-lua \
	--without-selinux \
	--without-libelf \
	--disable-nls \
	--without-pcre \
	--with-db=internal \
	--with-dbapi=db \
	--with-db-largefile \
	--without-sqlite \
	--with-zlib=internal \
	--with-neon=external \
	--with-bzip2 \
	--with-path-database="/var/local/lib/rpm" \
	--with-path-sources="/usr/local/src/rpm-packages"

# We put all our configuration in /usr/local/etc
mv config.h config.h.backup
sed "s/\/etc\/rpm/\/usr\/local\/etc\/rpm/g" config.h.backup > config.h

# we rename the src/rpm dir to src/rpm-packages b/c that's our convention
sed -e "s:src/rpm:src/rpm-packages:g" lib/rpmrc.c > zzz
mv zzz lib/rpmrc.c

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

sed "s/#\!\/bin\/sh/#\!\/bin\/bash/g" scripts/rpm2cpio > zzz
mv zzz scripts/rpm2cpio

#patch -p0 < %{SOURCE1}
#patch -p0 < %{SOURCE2}

gmake -j4

%install
slide rm -rf %{buildroot}

PERL5LIB="/usr/perl5/5.6.1/:$PERL5LIB"
export PERL5LIB

# cp %{SOURCE3} RPM-GPG-README
gmake DESTDIR=%{buildroot} install
# mv %{buildroot}/usr/local/src/sun %{buildroot}/usr/local/src/rpm-packages
# cp %{SOURCE2} RPM-GPG-KEYS

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


cd %{buildroot}
/usr/local/gnu/bin/find ./usr/perl5 -type f -a \( -name perllocal.pod -o \
-name .packlist -o \( -name '*.bs' -a -empty \) \) -exec rm -f {} ';'

/usr/local/gnu/bin/find ./usr/perl5 -type d -depth -exec rmdir {} 2>/dev/null ';'

%clean
rm -rf %{buildroot}

%pre
if [ -f /var/lib/rpm/packages.rpm ]; then
    cat<<EOF

You have (unsupported) /var/lib/rpm/packages.rpm db1 format 
installed package headers. Please install at least rpm-4.0.4 first 
and do "rpm --rebuilddb" to convert your database from db1 to db3 
format. Also, it is importnat that you remove your macros.db1 file as well.
EOF

#    exit 1
fi

%post
cat<<EOF
====================================================
If you are installing rpm for the first time you
must create an rpm user and group. Also, ensure that
you chown rpm:rpm /var/local/lib/rpm/[A-Z]* Also,
be sure to initialize the database by running
/usr/local/bin/rpm --initdb as root

If you are upgrading from an older rpm database you 
must run /usr/local/bin/rpm --rebuilddb after an upgrade.

In order to use the rpm.rutgers.edu database you MUST 
have the OSS GPG keys installed and run:
/usr/local/bin/rpm --initdb as root
====================================================

EOF

%files
%defattr(-,root,root)
%doc CHANGES CREDITS INSTALL README doc/manual/[a-z]*
%attr(0755, root, root)   %dir /var/local/lib/rpm
%attr(0644, root, root) %verify(not md5 size mtime) %ghost %config(missingok,noreplace) /var/local/lib/rpm/*
%attr(0755, root, root)	/usr/local/bin/rpm
%attr(0755, root, root)	/usr/local/bin/rpm2cpio
%attr(0755, root, root)	/usr/local/bin/gendiff
%attr(0755, root, root) /usr/local/bin/rpmconstant
%attr(0755, root, root)	%dir /usr/local/lib/rpm
%attr(0644, root, root)	/usr/local/lib/rpm/macros
%attr(0755, root, root)	/usr/local/lib/rpm/mkinstalldirs
%attr(0755, root, root)	/usr/local/lib/rpm/rpm.*
%attr(0755, root, root)	/usr/local/lib/rpm/tgpg
%attr(0644, root, root)	/usr/local/lib/rpm/rpmpopt*
%attr(0755, root, root)	/usr/local/lib/rpm/rpmdb_*
%attr(0755, root, root) /usr/local/lib/rpm/db_*
%attr(0755, root, root) /usr/local/lib/rpm/rpm2cpio
%attr(0755, root, root) /usr/local/lib/rpm/vcheck
/usr/local/share/man/man8/rpmconstant.8
/usr/local/share/man/man8/rpm.8
/usr/local/share/man/man8/rpm2cpio.8

%files libs
%defattr(-,root,root)
/usr/local/lib/librpm-5.0.so
/usr/local/lib/librpmdb-5.0.so
/usr/local/lib/librpmio-5.0.so
/usr/local/lib/librpmbuild-5.0.so
/usr/local/lib/librpmconstant-5.0.so
/usr/local/lib/librpmconstant.a
/usr/local/lib/librpmconstant.so
/usr/local/lib/librpmmisc-5.0.so
/usr/local/lib/librpmmisc.a
/usr/local/lib/librpmmisc.so

%files static
%defattr(-,root,root)
/usr/local/lib/*.la
/usr/local/lib/python%{with_python_version}/site-packages/rpm/*.a
/usr/local/lib/python%{with_python_version}/site-packages/rpm/*.la

%files build
%defattr(0775,root,studsys)
%dir /usr/local/src/rpm-packages
%dir /usr/local/src/rpm-packages/BUILD
%dir /usr/local/src/rpm-packages/SPECS
%dir /usr/local/src/rpm-packages/SOURCES
%dir /usr/local/src/rpm-packages/SRPMS
%dir /usr/local/src/rpm-packages/RPMS
%defattr(0755,root,root)
/usr/local/bin/rpmbuild
/usr/local/lib/rpm/brp-*
/usr/local/lib/rpm/check-files
/usr/local/lib/rpm/cross-build
/usr/local/lib/rpm/find-*
/usr/local/lib/rpm/getpo.sh
/usr/local/lib/rpm/http.req
/usr/local/lib/rpm/javadeps.sh
/usr/local/lib/rpm/magic
/usr/local/lib/rpm/magic.*
/usr/local/lib/rpm/executabledeps.sh
/usr/local/lib/rpm/libtooldeps.sh
/usr/local/lib/rpm/perldeps.pl
/usr/local/lib/rpm/perl.prov
/usr/local/lib/rpm/perl.req
/usr/local/lib/rpm/pkgconfigdeps.sh
/usr/local/lib/rpm/pythondeps.sh
/usr/local/lib/rpm/rpmdeps
/usr/local/lib/rpm/u_pkg.sh
/usr/local/lib/rpm/vpkg-provides.sh
/usr/local/lib/rpm/vpkg-provides2.sh
/usr/local/lib/rpm/php.prov
/usr/local/lib/rpm/php.req
/usr/local/share/man/man1/gendiff.1
/usr/local/share/man/man8/rpmbuild.8
/usr/local/share/man/man8/rpmdeps.8
/usr/local/lib/rpm/symclash.py
/usr/local/lib/rpm/symclash.sh
/usr/local/lib/rpm/install-sh
/usr/local/lib/rpm/mono-find-provides
/usr/local/lib/rpm/mono-find-requires
/usr/local/lib/rpm/osgideps.pl
/usr/local/lib/rpm/rpmcache
/usr/local/lib/rpm/rpmcmp
/usr/local/lib/rpm/rpmdigest

%files python
%defattr(-,root,root)
/usr/local/lib/python%{with_python_version}/site-packages/rpm/_rpmmodule.so
/usr/local/lib/python%{with_python_version}/site-packages/rpm/__init__.py

%files perl
%defattr(-,root,root)
/usr/perl5/5.6.1/man/man3/RPM*
/usr/perl5/site_perl/5.6.1/sun4-solaris-64int/*

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
/usr/local/share/man/man8/rpmcache.8
/usr/local/share/man/man8/rpmgraph.8
/usr/local/lib/pkgconfig/rpm.pc

%changelog
* Mon Dec 17 2007 David Lee Halik <dhalik@nbcs.rutgers.edu> 5.0b2-1
- First install beta, b2
* Thu Dec 13 2007 David Lee Halik <dhalik@nbcs.rutgers.edu> 5.0b1-1
- First beta build
* Fri Sep 21 2007 David Lee Halik <dhalik@nbcs.rutgers.edu> 4.4.9-6
- --without-libelf
* Thu Sep 20 2007 David Lee Halik <dhalik@nbcs.rutgers.edu> 4.4.9-5
- Added rpmevr.h bug fix
* Fri Sep 14 2007 David Lee Halik <dhalik@nbcs.rutgers.edu> 4.4.9-3
- Trying a build against neon 0.26 instead
* Thu Sep 13 2007 David Lee Halik <dhalik@nbcs.rutgers.edu> 4.4.9-2
- Respin against nongcc beecrypt
* Thu Sep 13 2007 David Lee Halik <dhalik@nbcs.rutgers.edu> 4.4.9-1
- First succesful build with SunCC
