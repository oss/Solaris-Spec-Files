AutoReqProv: no

%define	_noPayloadPrefix	1
%define poptversion 1.8.1
%define rpmversion 4.2.1
%define release 1

Summary: The Red Hat package management system.
Name: rpm
Version: %{rpmversion}
Release: %{release}
Group: System Environment/Base
Source0: rpm-4.2.1-0.30.src.rpm
#Source: rpm-%{version}.tar.gz
#Source1: beecrypt-3.0.1.tar
#Source2: rpm-4.1-pubkeys
#Source3: rpm-4.1-gpgdoc
Patch: rpmfc.c-string.patch
#Patch1: print.c.cjs
Patch2: rpm-4.2.1-sun-fts.c.patch
#Patch3: rpm-4.1-reqgpg.patch
Copyright: GPL
Conflicts: patch < 2.5
Provides: beecrypt
Requires: bzip2 zlib popt = %{poptversion}-rpm%{rpmversion}_%{release}
#BuildRequires: zlib make bzip2 patch autoconf libtool gettext
BuildRoot: /var/tmp/%{name}-root

%description
The RPM Package Manager (RPM) is a powerful command line driven
package management system capable of installing, uninstalling,
verifying, querying, and updating software packages.  Each software
package consists of an archive of files along with information about
the package like its version, a description, etc.

%package devel
Summary: Development files for applications which will manipulate RPM packages.
Group: Development/Libraries
Requires: rpm = %{version}
Provides: beecrypt-devel

%description devel
This package contains the RPM C library and header files.  These
development files will simplify the process of writing programs which
manipulate RPM packages and databases. These files are intended to
simplify the process of creating graphical package managers or any
other tools that need an intimate knowledge of RPM packages in order
to function.

This package should be installed if you want to develop programs that
will manipulate RPM packages and databases.

#%package -n popt
#Summary: A C library for parsing command line parameters.
#Group: Development/Libraries
#Version: %{poptversion}
#Release: rpm%{rpmversion}_%{release}

#%description -n popt
#Popt is a C library for parsing command line parameters.  Popt was
#heavily influenced by the getopt() and getopt_long() functions, but it
#improves on them by allowing more powerful argument expansion.  Popt
#can parse arbitrary argv[] style arrays and automatically set
#variables based on command line arguments.  Popt allows command line
#arguments to be aliased via configuration files and includes utility
#functions for parsing arbitrary strings into argv[] arrays using
#shell-like rules.

#Install popt if you're a C programmer and you'd like to use its
#capabilities.



%prep
%setup -T -c
rpm2cpio %{SOURCE0} | cpio -id --
( cd .. && gzcat rpm-4.2.1/rpm-4.2.1.tar.gz | tar -xvf - )

#%setup -q
#%setup  -q -D -n rpm-%{rpmversion} -T -a 1
pwd
%patch0 -p1
#%patch1 -p1
%patch2 -p0

#leave this out until repository is all signed
#%patch3 -p1


%build

# rename beecrypt so rpm sees it
#mv beecrypt-3.0.1 beecrypt

# This test checks to see if beecrypt is internal, yet seems to
# return true even if the condition is false. I don't want to 
# debug this so I'm just cutting it out for now.
cd rpmio
cp Makefile.in Makefile.in.orig
sed -e "s:if test X:#if test X:" Makefile.in.orig > Makefile.in
rm Makefile.in.orig
cd ..

# fix problem where ltmain.sh isn't created
#(cd beecrypt && ln -sf /usr/local/bin/libtool ltmain.sh)

# For some reason configure wants to call LD with such nonsense
# as "-R../zlib" also, for some reason, this is only for Solaris
mv configure configure.orig
sed -e "s:\-R\$l\ ::" configure.orig > configure
chmod u+x configure
rm configure.orig

# there's a typo in the rpmio Makefile.in
#cd rpmio
#mv Makefile.in Makefile.in.orig
#sed -e s:WITH_BEECTYPT_SUBDIR:WITH_BEECRYPT_SUBDIR:g Makefile.in.orig > Makefile.in
#cd ..
 
# for some reason this doesn't get defined itself
#cd rpmio
#mv Makefile.in Makefile.in.orig
#sed -e "s:@WITH_BEECRYPT_SUBDIR@:beecrypt:g" Makefile.in.orig > Makefile.in
#rm Makefile.in.orig
#cd ..

# for some reason this doesn't get defined itself
#cd rpmio
#mv Makefile.in Makefile.in.orig
#sed -e "s:@WITH_BEECRYPT_INCLUDE@:-I../beecrypt:g" Makefile.in.orig > Makefile.in
#rm Makefile.in.orig
#cd ..


# Internal dependency check just crashes rpm, probably due to libelf
mv macros.in macros.in.orig
sed -e "s/%_use_internal_dependency_generator.*/%_use_internal_dependency_generator 0/" macros.in.orig > macros.in
rm macros.in.orig


# there's a typo in this file
mv rpmio/rpmio.h rpmio/rpmio.h.orig
sed -e "s:fdCLose:fdClose:g" rpmio/rpmio.h.orig > rpmio/rpmio.h
rm rpmio/rpmio.h.orig


# we rename the src/redhat dir to src/rpm-packages b/c we're not redhat
mv lib/rpmrc.c lib/rpmrc.c.orig
sed -e "s:src/redhat:src/rpm-packages:g" lib/rpmrc.c.orig > lib/rpmrc.c
rm lib/rpmrc.c.orig


# Apparently RedHat has a magical linker that can do absolute
# run-time linking to a relative path. That's magic we don't have.
# in RPMIO
#cd rpmio
#mv Makefile.in Makefile.in.orig
#sed -e s:top_builddir\ =\ ..:top_builddir\ =\ @top_srcdir@:g Makefile.in.orig > Makefile.in
#cd ..

# in TOOLS
#cd tools
#mv Makefile.in Makefile.in.orig
#sed -e s:top_builddir\ =\ ..:top_builddir\ =\ @top_srcdir@:g Makefile.in.orig > Makefile.in
#cd ..

# in "BASE"
#mv Makefile.in Makefile.in.orig
#sed -e s:top_builddir\ =\ .:top_builddir\ =\ @top_srcdir@:g Makefile.in.orig > Makefile.in

# Going to cut out "tools" as it now requires Linux-specific libelf
mv Makefile.in Makefile.in.orig
sed -e s:tools::g Makefile.in.orig > Makefile.in


# Re-enable fix perms/own and don't term build on unpackaged files 
sed -e "s/#%_fix/%_fix/" macros.in > macros.in.2
#mv macros.in macros.in.2
sed -e "s/terminate_build.*/terminate_build 0/" macros.in.2 > macros.in


# Now we get to ./configure
LD_LIBRARY_PATH="`pwd`/beecrypt/.libs"
CPPFLAGS="-I`pwd`/beecrypt"
LDFLAGS="-L/usr/local/lib -R/usr/local/lib -L`pwd`/beecrypt/.libs"
CC="gcc"
CPPFLAGS="-I/usr/local/include -I/usr/local/include/beecrypt"
export CC CPPFLAGS
./configure --disable-nls --srcdir=`pwd` --without-python \
--disable-dependency-tracking --sysconfdir=/usr/local/etc \
--prefix=/usr/local --disable-largefile --without-javaglue \
--disable-nls


# rpmdb won't build in default setup. it appears that db3
# is getting overlooked somewhere. setup and build it *first*
cd rpmdb
mv db.h db.h.broken
ln -s ../db3/db.h
cd ../db3
gmake -j4
cd ..


# workaround - something's "different" about redhat's beecrypt
#cd beecrypt && gmake && ls *.lo > listobjs


# We put all our configuration in /usr/local/etc
#mv config.h config.h.orig
#sed "s/\/etc\/rpm/\/usr\/local\/etc\/rpm\//" config.h.orig > config.h


# Actually build RPM!!
gmake -j4 || gmake

# What was the buildarchtranslate change for again?
# Fix another typo
%ifarch sparc
sed "s/buildarchtranslate\:\ sparcv9\:\ sparc64/buildarchtranslate\:\ sparcv9\:\ sparc/" rpmrc > rpmrc.2
sed "s/buildarchtranslate\:\ sun4u\:\ sparc64/buildarchtranslate\:\ sun4u\:\ sparc/" rpmrc.2 > rpmrc.3
sed "s/osps_canon/os_canon/" rpmrc.3 > rpmrc
%endif


%install
rm -rf $RPM_BUILD_ROOT

#cp %{SOURCE3} RPM-GPG-README
gmake DESTDIR="$RPM_BUILD_ROOT" install
#(cd beecrypt && gmake DESTDIR="$RPM_BUILD_ROOT" install)
mkdir -p $RPM_BUILD_ROOT/usr/local/etc/rpm
mv $RPM_BUILD_ROOT/usr/local/src/sun $RPM_BUILD_ROOT/usr/local/src/rpm-packages


#cp %{SOURCE2} RPM-GPG-KEYS

%clean
rm -rf $RPM_BUILD_ROOT

%post
if [ -f /var/local/lib/rpm/packages.rpm ]; then
    : # do nothing
elif [ -f /var/local/lib/rpm/Packages ]; then
    # undo db1 configuration
    rm -f /etc/rpm/macros.db1
else
    # initialize db3 database
    rm -f /etc/rpm/macros.db1
    /usr/local/bin/rpm --initdb
fi

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
/usr/local/bin/gendiff
/usr/local/bin/rpm
/usr/local/bin/rpm2cpio
/usr/local/bin/rpmbuild
/usr/local/bin/rpmdb
/usr/local/bin/rpme
/usr/local/bin/rpmi
/usr/local/bin/rpmquery
/usr/local/bin/rpmsign
/usr/local/bin/rpmu
/usr/local/bin/rpmverify
#/usr/local/lib/libbeecrypt.so
#/usr/local/lib/libbeecrypt.so.6
#/usr/local/lib/libbeecrypt.so.6.1.0
/usr/local/lib/librpm-4.2.so
/usr/local/lib/librpm.so
/usr/local/lib/librpmbuild-4.2.so
/usr/local/lib/librpmbuild.so
/usr/local/lib/librpmdb-4.2.so
/usr/local/lib/librpmdb.so
/usr/local/lib/librpmio-4.2.so
/usr/local/lib/librpmio.so
#/usr/local/lib/rpm/
#/usr/local/man/man*
#/usr/local/src/rpm-packages
#/var/local/lib/rpm

%files devel
%defattr(-,root,root)
/usr/local/include/*
/usr/local/lib/*.a

#%files -n popt
#%defattr(-,root,root)
#/usr/local/lib/libpopt.so
#/usr/local/lib/libpopt.so.0
#/usr/local/lib/libpopt.so.0.0.0


%changelog
* Tue Mar 13 2001 Jeff Johnson <jbj@redhat.com>
- map i686-like (i.e. w/o CMOV) platforms to better alternatives.

* Mon Mar 12 2001 Jeff Johnson <jbj@redhat.com>
- fix: adjust for libio breakage in Red Hat 5.x with glibc-2.0.7-29.4.

* Wed Mar  7 2001 Jeff Johnson <jbj@redhat.com>
- remove mozilla dependency white out, no longer needed.

* Fri Feb 23 2001 Jeff Johnson <jbj@redhat.com>
- (sparc) disable MD5 sum checks during install.
- (db1) plug largish memory leak in simulated interface for falloc.c.

* Thu Feb 22 2001 Jeff Johnson <jbj@redhat.com>
- portability changes from Joe Orton <jorton@redhat.com> et al.
- (alpha): rip out ALPHA_LOSSAGE now that gcc-2.96-76 has fix (#28509).
- (popt): use sprintf rather than snprintf for portability.

* Mon Feb 19 2001 Jeff Johnson <jbj@redhat.com>
- rpm-4.0.2 release candidate.

* Wed Feb 14 2001 Jeff Johnson <jbj@redhat.com>
- fix: permit packages to differ by 0 or 32 bytes (#26373).
- fix: permit HEADER_IMMUTABLE tag queries.
- split db configuration into separate file.

* Tue Feb 13 2001 Jeff Johnson <jbj@redhat.com>
- fix: remove fixed size buffer on output path (#26987,#26332).
- resurrect rpmErrorCode in the API for Perl-RPM.

* Sat Feb 10 2001 Jeff Johnson <jbj@redhat.com>
- fix: diddle exit code for attempted installs of non-packages (#26850).
- python binding diddles to reduce installer memory footprint by
  delayed loading of file info.

* Fri Feb  9 2001 Jeff Johnson <jbj@redhat.com>
- fix: make a copy of retrieved header before loading.

* Sun Jan 21 2001 Jeff Johnson <jbj@redhat.com>
- fix: check waitpid return code.

* Fri Jan 19 2001 Jeff Johnson <jbj@redhat.com>
- ewt's cpio.c hack.
- ewt's cpio.c hack reverted.
- rebuild with i18n from rpm-4_0 branch.
- rpmlint conformance.

* Thu Jan 18 2001 Matt Wilson <msw@redhat.com>
- fix: exit 0 at the end of %pre

* Thu Jan 18 2001 Jeff Johnson <jbj@redhat.com>
- fix: insure that %lang scopes over hard links correctly.
- fix: rpmCleanPath was nibbling at .. in macrofiles incorrectly.

* Wed Jan 17 2001 Jeff Johnson <jbj@redhat.com>
- 1st crack at Mandrake specific per-platform macros.

* Tue Jan 16 2001 Jeff Johnson <jbj@redhat.com>
- tsort prefers presentation order.

* Mon Jan 15 2001 Jeff Johnson <jbj@redhat.com>
- fix: extra newline in many error messages (#23947).
- fix: rpm -Va with db1 needs per-iterator, not per-index, offset.
- add install/remove transaction id tags.

* Sat Jan 13 2001 Jeff Johnson <jbj@redhat.com>
- fix the hack.

* Fri Jan 12 2001 Jeff Johnson <jbj@redhat.com>
- hack: permit installer to determine package ordering using 1000003 tag.

* Thu Jan 11 2001 Jeff Johnson <jbj@redhat.com>
- fix: don't hang on build error.
- fix: remove "error: " prefix from signature verification message.

* Wed Jan 10 2001 Jeff Johnson <jbj@redhat.com>
- successors from tsort are processed in presentation order.
- fix: find-requires.perl needed update (#23450).

* Tue Jan  9 2001 Jeff Johnson <jbj@redhat.com>
- fix: digests on input FD_t dinna work.
- fix: remove rebuilddb debugging leakage.

* Mon Jan  8 2001 Jeff Johnson <jbj@redhat.com>
- tsorted packages processed in successor count order.
- fix: resurrect --excludepath (#19666).

* Fri Jan  5 2001 Jeff Johnson <jbj@redhat.com>
- fix: 3 packages from Red Hat 5.2 had bogus %verifyscript tag.

* Wed Jan  3 2001 Jeff Johnson <jbj@redhat.com>
- fix: avoid locale issues with strcasecmp/strncasecmp (#23199).
- remove almost all explicit uses of stderr in rpmlib using rpmError().
- fix: pass scriptlet args, as in %post -p "/sbin/ldconfig -n /lib".
	(Rodrigo Barbosa)

* Tue Jan  2 2001 Jeff Johnson <jbj@redhat.com>
- fix apidocs.

* Mon Jan  1 2001 Jeff Johnson <jbj@redhat.com>
- use popt autohelp for rpm helper binaries.

* Sun Dec 31 2000 Jeff Johnson <jbj@redhat.com>
- (popt): fix float/double handling (#19701).
- (popt): non-linux needs <float.h> (#22732).
- (popt): add POPT_ARGFLAG_OPTIONAL for long options with optional arg.
- (popt): diddle auto-help to include type of arg expected.

* Sat Dec 30 2000 Jeff Johnson <jbj@redhat.com>
- (non-linux): move stubs.c to rpmio (#21132).
- (python): bind initdb (#20988).

* Fri Dec 29 2000 Jeff Johnson <jbj@redhat.com>
- fix: hack around alpha mis-compilation signature problems.
- rpmmodule.c(handleDbResult): return empty list when nothing matches.

* Thu Dec 28 2000 Jeff Johnson <jbj@redhat.com>
- fix: avoid FAT and other brain-dead file systems that have not inodes.

* Wed Dec 27 2000 Jeff Johnson <jbj@redhat.com>
- use malloc'ed buffer for large queries.

* Tue Dec 26 2000 Jeff Johnson <jbj@redhat.com>
- send query/verify output through rpmlog().
- resurrect rpmErrorSetCallback() and rpmErrorString().

* Thu Dec 21 2000 Jeff Johnson <jbj@redhat.com>
- immutable headers, once installed by rpm3, need to lose immutablity.
- fix: removed headers from db need a headerCopy().

* Wed Dec 20 2000 Jeff Johnson <jbj@redhat.com>
- whiteout mozilla loop for 7.1.

* Tue Dec 19 2000 Jeff Johnson <jbj@redhat.com>
- gendiff: generate ChangeLog patches more intelligently (#22356).
- identify install scriptlet failures with the name of the scriptlet.
- handle install chroot's identically throughout the install process.
- add rpmlib(HeaderLoadSortsTags) for tracking header regions "just in case".
- create _tmppath on the fly if not present.
- remove /etc/rpm/macros.db1 configuration file if db3 rebuilt.

* Wed Dec 13 2000 Jeff Johnson <jbj@redhat.com>
- bump popt version.
- fix: (transaction.c) assume file state normal if tag is missing.
- fix: failed signature read headerFree segfault.
- fix: revert ALPHA_LOSSAGE, breaks 6.2/i386.
- fix: segfault on build path, ignore deleted drips.
- fix: synthesized callbacks for removed packages have not a pkgkey.

* Tue Dec 12 2000 Jeff Johnson <jbj@redhat.com>
- bail on header regions.
- change dependency loop message to RPMMESS_WARNING to use stderr, not stdout.

* Sun Dec 10 2000 Jeff Johnson <jbj@redhat.com>
- handle added dirtoken tags (mostly) correctly with header regions.
- add FHS doc/man/info dirs, diddle autoconf goo.
- fix: headerUnload handles headers w/o regions correctly on rebuilddb.

* Thu Dec  7 2000 Jeff Johnson <jbj@redhat.com>
- add rpmtransGetKeys() to retrieve transaction keys in tsort'ed order.
- python bindings for rpmtransGetKeys().
- fix: include alignment in count when swabbing header region.

* Wed Dec  6 2000 Jeff Johnson <jbj@redhat.com>
- improved find-{requires,provides} for aix4/hpux/irix6/osf.
		Tim Mooney<mooney@dogbert.cc.ndsu.NoDak.edu>
- portability: remove use of GNU make subst in lib/Makefile (Joe Orton).
- python: bind package removal (#21274).
- autoconfigure building python bindings.
- autoconfigure generating rpm API doco rpm-devel package.
- fix: don't fdFree in rpmVerifyScript, rpmtransFree does already.
- unify rpmError and rpmMessge interfaces through rpmlog.
- collect and display rpm build error messages at end of build.
- use package version 3 if --nodirtokens is specified.
- add package names to problem sets early, don't save removed header.
- make sure that replaced tags in region are counted in headerSizeof().
- support for dmalloc debugging.
- filter region tags in headerNextIterator, exit throut headerReload.

* Thu Nov 30 2000 Jeff Johnson <jbj@redhat.com>
- add missing headerFree for legacy signature header.
- fix: removed packages leaked DIRINDEXES tag data.
- reload tags added during install when loading header from rpmdb.
- avoid brp-compress hang with both compressed/uncompressed man pages.

* Tue Nov 21 2000 Jeff Johnson <jbj@redhat.com>
- add brp-strip-shared script <rodrigob@conectiva.com.br>.
- better item/task progress bars <rodrigob@conectiva.com.br>.
- load headers as single contiguous region.
- add region marker as RPM_BIN_TYPE in packages and database.
- fix: don't headerCopy() relocateable packages if not relocating.
- merge signatures into header after reading from package.

* Mon Nov 20 2000 Jeff Johnson <jbj@redhat.com>
- add doxygen and lclint annotations most everywhere.
- consistent return for all signature verification.
- use enums for almost all rpmlib #define's.
- API: change rpmProblem typedef to pass by reference, not value.
- don't trim leading ./ in rpmCleanPath() (#14961).
- detect (still need to test) rdonly linux file systems.
- check available inodes as well as blocks on mounted file systems.
- pass rpmTransactionSet, not elements, to installBinaryPackage et al.
- add cscope/ctags (Rodrigo Barbosa<rodrigob@conectiva.com.br>).
- remove getMacroBody() from rpmio API.
- add support for unzip <rodrigob@conectiva.com.br>

* Thu Nov 16 2000 Jeff Johnson <jbj@redhat.com>
- don't verify src rpm MD5 sums (yet).
- md5 sums are little endian (no swap) so big endian needs the swap.

* Wed Nov 15 2000 Jeff Johnson <jbj@redhat.com>
- fix: segfault on exit of "rpm -qp --qf '%{#fsnames}' pkg" (#20595).
- hpux w/o -D_OPEN_SOURCE has not h_errno.
- verify MD5 sums of payload files when unpacking archive.
- hide libio lossage in prototype, not API.
- add support for SHA1 as well as MD5 message digests.

* Mon Nov 13 2000 Jeff Johnson <jbj@redhat.com>
- fix: work around for (mis-compilation?!) segfaults on signature paths.

* Sun Nov 12 2000 Jeff Johnson <jbj@redhat.com>
- fix: duplicate headerFree() on instalBinaryPackage() error return.

* Sat Nov 11 2000 Jeff Johnson <jbj@redhat.com>
- fix: runTriggers was not adding countCorrection.
- add rpmGetRpmlibProvides() to retrieve rpmlib(...) provides
	"Pawel A. Gajda" <mis@k2.net.pl>.
- syntax to specify source of Requires: (PreReq: now legacy).
- rip out rpm{get,put}text, use getpo.sh and specspo instead.
- fine-grained Requires, remove install PreReq's from Requires db.

* Wed Oct 11 2000 Jeff Johnson <jbj@redhat.com>
- fix: rpm2cpio error check wrong on non-libio platforms.

* Fri Sep 29 2000 Jeff Johnson <jbj@redhat.com>
- fix: more (possible) xstrdup side effects.

* Wed Sep 27 2000 Jeff Johnson <jbj@redhat.com>
- bump popt version to 1.6.1.

* Tue Sep 26 2000 Jeff Johnson <jbj@redhat.com>
- fix: avoid calling getpass twice as side effect of xstrdup macro (#17672).
- order packages using tsort, clipping PreReq:'s in dependency loops.
- handle possible db3 dependency on -lpthread more gracefully.

* Thu Sep 14 2000 Jeff Johnson <jbj@redhat.com>
- start rpm-4.0.1.
