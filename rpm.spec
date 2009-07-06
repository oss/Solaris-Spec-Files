%define with_python_version     2.4
%define rpm_version		4.4.2.3
%define popt_version		1.10.9

%define rpmhome	%{_libdir}/rpm

Name:		rpm
Version:	%{rpm_version}
Release:	5
Group:		System Environment/Base
License:        GPLv2+
URL:		http://www.rpm.org

Source0:	http://rpm.org/releases/rpm-4.4.x/%{name}-%{rpm_version}.tar.gz
Source1:	rpm-pubkeys.tar.gz
Source2:	rpm-gpgdoc

Patch0:		rpm-4.4.2.3-ru_solaris.patch
Patch1:		rpm-4.4.2.3-macros.patch
Patch2:		rpm-4.4.2.3-sun.patch
Patch3:		rpm-4.4.2.3-rc1-sparc-mcpu.patch
Patch4:		rpm-4.4.2.3-magic.patch

# Use external lua to match what apt uses
Patch5:		rpm-4.4.2.3-extlua.patch

# Add explicit path to check-files script
Patch6:         rpm-4.4.2.3-checkfiles.patch

# Improve the dependency resolution in find-requires
Patch7:		rpm-4.4.2.3-findrequires.patch

BuildRoot:      %{_tmppath}/%{name}-%{rpm_version}-%{release}-root

Requires:	popt = %{popt_version}-%{release}

BuildRequires:	autoconf automake libtool-devel
BuildRequires:	zlib-devel bzip2-devel
BuildRequires:	readline5-devel beecrypt-devel
BuildRequires:	gettext-devel ncurses-devel lua-devel
BuildRequires:	python >= %{with_python_version}

BuildConflicts:	neon-devel

Summary:        The RPM package management system

%description
The RPM Package Manager (RPM) is a powerful command line driven
package management system capable of installing, uninstalling,
verifying, querying, and updating software packages. Each software
package consists of an archive of files along with information about
the package like its version, a description, etc.

%package libs
Group:		Development/Libraries
License:	GPLv2+ and LGPLv2+ with exceptions

Requires:	rpm = %{rpm_version}-%{release}

Summary:        Libraries for manipulating RPM packages

%description libs
This package contains the RPM shared libraries.

%package devel
Group:		Development/Libraries
License:	GPLv2+ and LGPLv2+ with exceptions

Requires:	rpm = %{rpm_version}-%{release}
Requires:	popt-devel = %{popt_version}-%{release}

Summary:        Development files for manipulating RPM packages

%description devel
This package contains the RPM C library and header files. These
development files will simplify the process of writing programs that
manipulate RPM packages and databases. These files are intended to
simplify the process of creating graphical package managers or any
other tools that need an intimate knowledge of RPM packages in order
to function.

This package should be installed if you want to develop programs that
will manipulate RPM packages and databases.

%package build
Group:		Development/Tools

Requires:	rpm = %{rpm_version}-%{release}
Requires:	findutils sed grep gawk diffutils file patch >= 2.5
Requires:	gzip bzip2 cpio

Summary:        Scripts and executable programs used to build packages

%description build
The rpm-build package contains the scripts and executable programs
that are used to build packages using the RPM Package Manager.

%package	python
Group:		Development/Libraries

Requires:	rpm = %{rpm_version}-%{release}

Summary:        Python bindings for apps which will manipulate RPM packages

%description python
The rpm-python package contains a module that permits applications
written in the Python programming language to use the interface
supplied by RPM Package Manager libraries.

This package should be installed if you want to develop Python
programs that will manipulate RPM packages and databases.

%package -n popt
Version:        %{popt_version}
Group:		Development/Libraries

Summary:        A C library for parsing command line parameters.

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

%package -n	popt-devel
Version:        %{popt_version}
Group:		Development/Libraries

Requires:	popt = %{popt_version}-%{release}

Summary:        Development files for the popt library

%description -n popt-devel
The popt-devel package includes header files and libraries necessary
for developing programs which use the popt C library.

%prep
%setup -q -n rpm-%{rpm_version} -a 1

%patch0 -p1
%patch1 -p1 
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1
%patch7 -p1

autoreconf

%build
PATH="/opt/SUNWspro/bin:/usr/ccs/bin:${PATH}"
CC="cc" CFLAGS="-g -xs" CXX="CC" 
CPPFLAGS="-I/usr/local/include"
LD="/usr/ccs/bin/ld"
LDFLAGS="-L/usr/local/lib -R/usr/local/lib -Bdirect -zdefs"
LIBS="-lm"
export PATH CC CFLAGS CXX CPPFLAGS LD LDFLAGS LIBS

./configure \
	--prefix=%{_prefix}			\
	--sysconfdir=%{_sysconfdir}		\
	--localstatedir=%{_var}			\
	--infodir=%{_infodir}			\
	--mandir=%{_mandir}			\
	--with-python=%{with_python_version}	\
	--without-selinux			\
	--without-libelf			\
	--with-lua				\
	--disable-nls				\
	--disable-dependency-tracking

gmake -j3

%install
rm -rf %{buildroot}

gmake install DESTDIR=%{buildroot}

cp %{SOURCE2} RPM-GPG-README

mv %{buildroot}%{_prefix}/src/sun %{buildroot}%{_topdir}

# Clean up useless symlinks
for i in rpme rpmi rpmu; do
    rm -f %{buildroot}%{_bindir}/$i
done

mkdir -p %{buildroot}%{_dbpath}
for dbi in \
        Basenames Conflictname Dirnames Group Installtid Name Packages \
        Providename Provideversion Requirename Requireversion Triggername \
        Filemd5s Pubkeys Sha1header Sigmd5 \
        __db.001 __db.002 __db.003 __db.004 __db.005 __db.006 __db.007 \
        __db.008 __db.009
do
    touch %{buildroot}%{_dbpath}/$dbi
done

# copy db and file/libmagic license info to distinct names
cp -p db/LICENSE LICENSE-bdb
cp -p file/LEGAL.NOTICE LEGAL.NOTICE-file
#cp -p lua/COPYRIGHT COPYRIGHT-lua

# Get rid of unpackaged files
find %{buildroot} -name '*.a' -exec rm -f '{}' \;
find %{buildroot} -name '*.la' -exec rm -f '{}' \;

cd %{buildroot}
rm -f .%{rpmhome}/Specfile.pm
rm -f .%{rpmhome}/cpanflute
rm -f .%{rpmhome}/cpanflute2
rm -f .%{rpmhome}/rpmdiff
rm -f .%{rpmhome}/rpmdiff.cgi
rm -f .%{rpmhome}/sql.prov
rm -f .%{rpmhome}/sql.req
rm -f .%{rpmhome}/tcl.req
rm -f .%{rpmhome}/rpm.*
rm -rf .%{_mandir}/fr
rm -rf .%{_mandir}/ko
rm -rf .%{_mandir}/pl
rm -rf .%{_mandir}/ru
rm -rf .%{_mandir}/sk
rm -rf .%{_mandir}/ja

%clean
rm -rf %{buildroot}

%post
# Detect (and remove) incompatible dbenv files during upgrade.
# Removing dbenv files in %%post opens a lock race window, a tolerable
# risk compared to the support issues involved with upgrading Berkeley DB.
[ -w %{_dbpath}/__db.001 ] &&
%{rpmhome}/rpmdb_stat -CA -h %{_dbpath} > /dev/null 2>&1 || rm -f %{_dbpath}/__db*

cat << EOF

If you are installing rpm for the first time you
must create an rpm user and group. Also, ensure that
you chown rpm:rpm /var/local/lib/rpm/[A-Z]* Also,
be sure to initialize the database by running:

        /usr/local/bin/rpm --initdb

as root

If you are upgrading from an older rpm database you
must run /usr/local/bin/rpm --rebuilddb after an upgrade.

APT checks for GPG signatures before installing packages.
Before initializing the database, you must import the
public GPG keys you trust into RPM using:

     rpm --import /usr/local/doc/rpm-%{rpm_version}/rpm-pubkeys/*

This directory contains the public keys of the NBCS package signers. You
may wish to validate this against: http://keyserver.rutgers.edu
More information is available in the RPM-GPG-README document.

EOF

%define rpmdbattr %attr(0644, root, root) %verify(not md5 size mtime) %ghost %config(missingok,noreplace)

%files
%defattr(-,root,root,-)
%doc CHANGES GROUPS COPYING LICENSE-bdb LEGAL.NOTICE-file CREDITS ChangeLog
%doc doc/manual/[a-z]*
%doc RPM-GPG-README rpm-pubkeys

%dir %{_dbpath}
%rpmdbattr %{_dbpath}/*
%dir %{rpmhome}

%{_bindir}/rpm
%{_bindir}/rpm2cpio
%{_bindir}/gendiff
%{_bindir}/rpmdb
%{_bindir}/rpmsign
%{_bindir}/rpmquery
%{_bindir}/rpmverify

%{rpmhome}/config.guess
%{rpmhome}/config.sub
%{rpmhome}/convertrpmrc.sh
%{rpmhome}/freshen.sh
%{rpmhome}/mkinstalldirs
%{rpmhome}/rpm2cpio.sh
%{rpmhome}/rpm[deiukqv]
%{rpmhome}/tgpg
%{rpmhome}/rpmdb_*
%{rpmhome}/rpmfile

%{rpmhome}/macros
%{rpmhome}/rpmpopt*
%{rpmhome}/rpmrc

%{rpmhome}/sparc*
%{rpmhome}/noarch*

%{_mandir}/man1/gendiff.1*
%{_mandir}/man8/rpm.8*
%{_mandir}/man8/rpm2cpio.8*

%files libs
%defattr(-,root,root)
%{_libdir}/librpm*-*.so

%files build
%defattr(-,root,root)
%attr(0775,root,studsys) %dir %{_topdir}
%attr(0775,root,studsys) %dir %{_builddir}
%attr(0775,root,studsys) %dir %{_specdir}
%attr(0775,root,studsys) %dir %{_sourcedir}
%attr(0775,root,studsys) %dir %{_srcrpmdir}
%attr(0775,root,studsys) %dir %{_rpmdir}
%attr(0775,root,studsys) %{_rpmdir}/*
%{_bindir}/rpmbuild
%{rpmhome}/brp-*
%{rpmhome}/check-buildroot
%{rpmhome}/check-files
%{rpmhome}/check-prereqs
%{rpmhome}/check-rpaths*
%{rpmhome}/cross-build
%{rpmhome}/find-debuginfo.sh
%{rpmhome}/find-lang.sh
%{rpmhome}/find-prov.pl
%{rpmhome}/find-provides
%{rpmhome}/find-provides.perl
%{rpmhome}/find-req.pl
%{rpmhome}/find-requires
%{rpmhome}/find-requires.perl
%{rpmhome}/get_magic.pl
%{rpmhome}/getpo.sh
%{rpmhome}/http.req
%{rpmhome}/javadeps
%{rpmhome}/magic.prov
%{rpmhome}/magic.req
%{rpmhome}/mono-find-provides
%{rpmhome}/mono-find-requires
%{rpmhome}/osgideps.pl
%{rpmhome}/perldeps.pl
%{rpmhome}/perl.prov
%{rpmhome}/perl.req
%{rpmhome}/pythondeps.sh
%{rpmhome}/rpm[bt]
%{rpmhome}/rpmdeps
%{rpmhome}/trpm
%{rpmhome}/u_pkg.sh
%{rpmhome}/vpkg-provides.sh
%{rpmhome}/vpkg-provides2.sh

%{rpmhome}/config.site
%{rpmhome}/magic
%{rpmhome}/magic.mgc
%{rpmhome}/magic.mime
%{rpmhome}/magic.mime.mgc

%{_mandir}/man8/rpmbuild.8*
%{_mandir}/man8/rpmdeps.8*

%files python
%defattr(-,root,root)
%{_libdir}/python%{with_python_version}/site-packages/rpm

%files devel
%defattr(-,root,root)
%{_includedir}/rpm
%{_libdir}/librp*[a-z].so
%{_mandir}/man8/rpmcache.8*
%{_mandir}/man8/rpmgraph.8*
%{rpmhome}/rpmcache
%{_bindir}/rpmgraph

%files -n popt
%defattr(-,root,root)
%{_libdir}/libpopt.so.*
%{_mandir}/man3/popt.3*

%files -n popt-devel
%defattr(-,root,root)
%{_includedir}/popt.h
%{_libdir}/libpopt.so

%changelog
* Mon Jul 06 2009 Brian Schubert <schubert@nbcs.rutgers.edu> - 4.4.2.3-5
- Remove neon support
- Put find-requires changes in patch
- Modified check-files patch

* Fri Jun 19 2009 Brian Schubert <schubert@nbcs.rutgers.edu> - 4.4.2.3-4
- Added improved find-requires script
- Fixed popt-devel permissions

* Tue Mar 31 2009 Brian Schubert <schubert@nbcs.rutgers.edu> - 4.4.2.3-3
- Patch that adds absolute GNU diff path to check-files script

* Tue Mar 10 2009 Brian Schubert <schubert@nbcs.rutgers.edu> - 4.4.2.3-2
- Incompatible dbenv files are now actually removed after installation

* Wed Feb 18 2009 Brian Schubert <schubert@nbcs.rutgers.edu> - 4.4.2.3-1
- Initial RPM 4.4 build.
