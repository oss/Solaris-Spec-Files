Summary: The Red Hat package management system.
Name: rpm
%define version 3.0.6
Version: %{version}
Release: 3
Group: System Environment/Base
Source: rpm-%{version}.tar.gz
Patch: rpm-%{version}.patch
Copyright: GPL
Conflicts: patch < 2.5
BuildRequires: bzip2 db zlib-devel autoconf automake patch make libtool gettext
Requires: db zlib bzip2
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
Requires: rpm = %{version}, popt

%description devel
This package contains the RPM C library and header files.  These
development files will simplify the process of writing programs which
manipulate RPM packages and databases. These files are intended to
simplify the process of creating graphical package managers or any
other tools that need an intimate knowledge of RPM packages in order
to function.

This package should be installed if you want to develop programs that
will manipulate RPM packages and databases.

%package -n popt
Summary: A C library for parsing command line parameters.
Group: Development/Libraries
Version: 1.5

%description -n popt
Popt is a C library for parsing command line parameters.  Popt was
heavily influenced by the getopt() and getopt_long() functions, but it
improves on them by allowing more powerful argument expansion.  Popt
can parse arbitrary argv[] style arrays and automatically set
variables based on command line arguments.  Popt allows command line
arguments to be aliased via configuration files and includes utility
functions for parsing arbitrary strings into argv[] arrays using
shell-like rules.

Install popt if you're a C programmer and you'd like to use its
capabilities.

%prep
%setup -q
%patch -p1

%build
autoconf
automake
LD="/usr/ccs/bin/ld -L/usr/local/lib -R/usr/local/lib" \
CPPFLAGS="-I/usr/local/include" \
LDFLAGS="-L/usr/local/lib -R/usr/local/lib" \
CFLAGS="-L/usr/local/lib -R/usr/local/lib" \
./configure --prefix=/usr/local
gmake CCLD="/usr/local/bin/gcc -L/usr/local/lib -R/usr/local/lib"

%install
rm -rf $RPM_BUILD_ROOT

gmake DESTDIR="$RPM_BUILD_ROOT" install
mv $RPM_BUILD_ROOT/usr/local/src/redhat \
   $RPM_BUILD_ROOT/usr/local/src/rpm-packages

{ cd $RPM_BUILD_ROOT
  strip ./usr/local/bin/rpm
  strip ./usr/local/bin/rpm2cpio
  strip ./usr/local/lib/rpm/rpmputtext ./usr/local/lib/rpm/rpmgettext
}

%clean
rm -rf $RPM_BUILD_ROOT

%post
/usr/local/bin/rpm --initdb

%files
%defattr(-,bin,bin)
%doc RPM-PGP-KEY CHANGES GROUPS doc/manual/*
/usr/local/bin/rpm
/usr/local/bin/rpm2cpio
/usr/local/bin/gendiff
/usr/local/lib/librpm.so.*
/usr/local/lib/librpmbuild.so.*

/usr/local/lib/rpm/brp-*
/usr/local/lib/rpm/config.guess
/usr/local/lib/rpm/config.sub
/usr/local/lib/rpm/convertrpmrc.sh
/usr/local/lib/rpm/find-prov.pl
/usr/local/lib/rpm/find-provides
/usr/local/lib/rpm/find-req.pl
/usr/local/lib/rpm/find-requires
/usr/local/lib/rpm/macros
/usr/local/lib/rpm/mkinstalldirs
/usr/local/lib/rpm/rpmpopt
/usr/local/lib/rpm/rpmrc
/usr/local/lib/rpm/vpkg-provides.sh
/usr/local/lib/rpm/vpkg-provides2.sh

%ifarch i386 i486 i586 i686
/usr/local/lib/rpm/i[3456]86*
%endif
%ifarch alpha
/usr/local/lib/rpm/alpha*
%endif
%ifarch sparc sparc64
/usr/local/lib/rpm/sparc*
%endif
%ifarch ia64
/usr/local/lib/rpm/ia64*
%endif
%ifarch powerpc ppc
/usr/local/lib/rpm/ppc*
%endif

%dir /usr/local/src/rpm-packages
%dir /usr/local/src/rpm-packages/BUILD
%dir /usr/local/src/rpm-packages/SPECS
%dir /usr/local/src/rpm-packages/SOURCES
%dir /usr/local/src/rpm-packages/SRPMS
%dir /usr/local/src/rpm-packages/RPMS
/usr/local/src/rpm-packages/RPMS/*
/usr/local/*/locale/*/LC_MESSAGES/rpm.mo
/usr/local/man/man[18]/*.[18]*
%lang(pl) /usr/local/man/pl/man[18]/*.[18]*
%lang(ru) /usr/local/man/ru/man[18]/*.[18]*
/usr/local/lib/rpm/check-prereqs
/usr/local/lib/rpm/cpanflute
/usr/local/lib/rpm/find-lang.sh
/usr/local/lib/rpm/find-provides.perl
/usr/local/lib/rpm/find-requires.perl
/usr/local/lib/rpm/get_magic.pl
/usr/local/lib/rpm/getpo.sh
/usr/local/lib/rpm/http.req
/usr/local/lib/rpm/magic.prov
/usr/local/lib/rpm/magic.req
/usr/local/lib/rpm/perl.prov
/usr/local/lib/rpm/perl.req
/usr/local/lib/rpm/rpmdiff
/usr/local/lib/rpm/rpmdiff.cgi
/usr/local/lib/rpm/rpmgettext
/usr/local/lib/rpm/rpmputtext
/usr/local/lib/rpm/u_pkg.sh

%files devel
%defattr(-,root,root)
/usr/local/include/rpm
/usr/local/lib/librpm.a
/usr/local/lib/librpm.la
/usr/local/lib/librpm.so
/usr/local/lib/librpmbuild.a
/usr/local/lib/librpmbuild.la
/usr/local/lib/librpmbuild.so

%files -n popt
%defattr(-,root,root)
/usr/local/lib/libpopt.so.*
/usr/local/*/locale/*/LC_MESSAGES/popt.mo
/usr/local/man/man3/popt.3*

# XXX These may end up in popt-devel but it hardly seems worth the effort now.
/usr/local/lib/libpopt.a
/usr/local/lib/libpopt.la
/usr/local/lib/libpopt.so
/usr/local/include/popt.h

%changelog
* Thu Jul 20 2000 Jeff Johnson <jbj@redhat.com>
- fix: Red Hat 6.0 (5.2?) glibc-2.1.1 fclose fails using libio.
- add /usr/kerberos/man to brp-compress.

* Sun Jul 16 2000 Jeff Johnson <jbj@redhat.com>
- remove (unused) RPMTAG_CAPABILITY.
- remove (legacy) use of RPMTAG_{OBSOLETES,PROVIDES} internally.
- remove (legacy) support for version 1 packaging.
- remove (legacy) support for converting gdbm databases.
- eliminate unused headerGz{Read,Write}.
- support for rpmlib(...) internal feature dependencies.
- display rpmlib provides when invoked with --showrc.
- fix: compare versions if doing --freshen.

* Tue Jul 11 2000 Jeff Johnson <jbj@redhat.com>
- identify package when install scriptlet fails (#12448).

* Sun Jul  9 2000 Jeff Johnson <jbj@redhat.com>
- fix: payload compression tag not nul terminated.

* Thu Jun 22 2000 Jeff Johnson <jbj@redhat.com>
- internalize --freshen (Gordon Messmer <yinyang@eburg.com>).
- support for separate source/binary compression policy.
- support for bzip payloads.

* Wed Jun 21 2000 Jeff Johnson <jbj@redhat.com>
- fix: don't expand macros in false branch of %if (kasal@suse.cz).
- fix: macro expansion problem and clean up (#11484) (kasal@suse.cz).
- uname on i370 has s390 as arch (#11456).
- python: initdb binding (Dan Burcaw <dburcaw@terraplex.com>).

* Tue Jun 20 2000 Jeff Johnson <jbj@redhat.com>
- handle version 4 packaging as input.
- builds against bzip2 1.0
- fix: resurrect symlink unique'ifying property of finger prints.
- fix: broken glob test with empty build directory (Geoff Keating).
- fix: create per-platform directories correctly.
- update brp-* scripts from rpm-4.0, enable in per-platform config.
- alpha: add -mieee to default optflags.
- add RPMTAG_OPTFLAGS, configured optflags when package was built.
- add RPMTAG_DISTURL for rpmfind-like tools (content unknown yet).
- teach brp-compress about /usr/info and /usr/share/info as well.
- update macros.in from rpm-4.0 (w/o dbi configuration).

* Thu Mar 15 2000 Jeff Johnson <jbj@redhat.com>
- portability: skip bzip2 if not available.
- portability: skip gzseek if not available (zlib-1.0.4).
- portability: skip personality if not available (linux).
- portability: always include arpa/inet.h (HP-UX).
- portability: don't use id -u (Brandon Allbery).
- portability: don't chown/chgrp -h w/o lchown.
- portability: splats in rpm.spec to find /usr/{share,local}/locale/*
- fix: better filter in linux.req to avoid ARM specific objdump output.
- fix: use glibc 2.1 glob/fnmatch everywhere.
- fix: noLibio = 0 on Red Hat 4.x and 5.x.
- fix: typo in autodeps/linux.req.

* Thu Mar  2 2000 Jeff Johnson <jbj@redhat.com>
- simpler hpux.prov script (Tim Mooney).

* Wed Mar  1 2000 Jeff Johnson <jbj@redhat.com>
- fix rpmmodule.so python bindings.

* Sun Feb 27 2000 Jeff Johnson <jbj@redhat.com>
- rpm-3.0.4 release candidate.

* Fri Feb 25 2000 Jeff Johnson <jbj@redhat.com>
- fix: filter excluded paths before adding install prefixes (#8709).
- add i18n lookaside to PO catalogue(s) for i18n strings.
- try for /etc/rpm/macros.specspo so that specspo autoconfigures rpm.
- per-platform configuration factored into /usr/lib/rpm subdir.

* Tue Feb 15 2000 Jeff Johnson <jbj@redhat.com>
- new rpm-build package to isolate rpm dependencies on perl/bash2.
- always remove duplicate identical package entries on --rebuilddb.
- add scripts for autogenerating CPAN dependencies.

* Wed Feb  9 2000 Jeff Johnson <jbj@redhat.com>
- brp-compress deals with hard links correctly.

* Mon Feb  7 2000 Jeff Johnson <jbj@redhat.com>
- brp-compress deals with symlinks correctly.

* Mon Jan 24 2000 Jeff Johnson <jbj@redhat.com>
- explicitly expand file lists in writeRPM for rpmputtext.
