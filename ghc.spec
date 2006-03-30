Summary: The Glasgow Haskell Compiler
Name: ghc
Version: 6.4.1
Release: 7
License: Other
Group: Development/Languages/Haskell
URL: http://www.haskell.org/ghc/
Source: http://www.haskell.org/ghc/dist/%{version}/ghc-%{version}-src.tar.bz2
Source1: ghc-%{version}-sparc-sun-solaris2.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-root
BuildRequires: readline5-devel, ghc >= 6.4, gmp, sed, bzip2
Requires: readline5, gmp

%description
The Glasgow Haskell Compiler is a robust, fully-featured, optimising
compiler for the functional programming language Haskell. GHC compiles
Haskell to either native code or C. It implements numerous experimental
language extensions to Haskell for example concurrency, a foreign language
interface, several type-system extensions, exceptions, and so on. GHC comes
with a generational garbage collector, a space and time profiler, and a
comprehensive set of libraries. 

%prep
%setup -q

%build
PATH=/opt/SUNWspro/bin:/usr/ccs/bin:/usr/local/bin:/usr/local/gnu/bin:$PATH
EXTRA_LD_OPTS="-L/usr/local/lib -optl-R/usr/local/lib"
export PATH EXTRA_LD_OPTS

CURDIR=`pwd`

# Extract and ready bootstrapping ghc binaries
###cd %{_tmppath}
###bzip2 -dc %{SOURCE1} | tar -xf -
###cd ghc-%{version}
###./configure
###gmake in-place

# Begin horrible hack to work around the fact that the provided ghc binaries requires ncurses and we don't want ours to do so.

###cd ..
#### Use -p here so that if the directory happens to exist the build doesn't die
###mkdir -p ghc-ncurses-hack
###cd ghc-ncurses-hack
###TEMPCURDIR=`pwd`
###wget ftp://rpm.rutgers.edu/solaris/solaris9-sparc64/unstable/RPMS.main/ncurses-5.4-4.solaris2.9-sparc64.rpm
###rpm2cpio ncurses-5.4-4.solaris2.9-sparc64.rpm | cpio -id ./usr/local/lib/\*

# End horrible hack

###cd $CURDIR
#### Build our ghc
###PATH=%{_tmppath}/%{name}-%{version}/bin/sparc-sun-solaris2:$PATH
###export PATH

# For some reason the ghc binary tarball includes a file which defines HAVE_STDINT_H despite solaris seeming not to have stdint.h so I comment that define out.
###sed -e 's|#define HAVE_STDINT_H 1|/*#define HAVE_STDINT_H 1 */|' /var/local/tmp/ghc-6.4.1/lib/sparc-sun-solaris2/include/ghcautoconf.h > /tmp/ghc-stupid-temp
###mv /var/local/tmp/ghc-6.4.1/lib/sparc-sun-solaris2/include/ghcautoconf.h /var/local/tmp/ghc-6.4.1/lib/sparc-sun-solaris2/include/ghcautoconf.h.orig
###mv /tmp/ghc-stupid-temp /var/local/tmp/ghc-6.4.1/lib/sparc-sun-solaris2/include/ghcautoconf.h

./configure --prefix=/usr/local

# In order to not have configure pick up ncurses I can't set the LD_LIBRARY_PATH until later, but that means that configure can't get the version of ghc I am using correctly either. So I need to sed the values in where they belong.
###cp mk/config.mk mk/config.mk.orig
###sed -e 's/^GhcVersion.*/GhcVersion      = 6.4.1/' mk/config.mk > mk/config.mk.ru.4
###sed -e 's/^GhcMajVersion.*/GhcMajVersion   = 6/' mk/config.mk.ru.4 > mk/config.mk.ru.3
###sed -e 's/^GhcMinVersion.*/GhcMinVersion   = 4/' mk/config.mk.ru.3 > mk/config.mk.ru.1
###sed -e 's/^GhcPatchLevel.*/GhcPatchLevel   = 1/' mk/config.mk.ru.1 > mk/config.mk.ru
###mv mk/config.mk.ru mk/config.mk

# The stupid ghc build seems not to let me specify an rpath so one of the
# utils it builds doesn't work because it can't find libgmp.so.3 at run time.
###LD_LIBRARY_PATH="/usr/local/lib:$LD_LIBRARY_PATH"
###export LD_LIBRARY_PATH

# Begin horrible hack part 2
# I do this here so that configure doesn't see ncurses

###LD_LIBRARY_PATH="$TEMPCURDIR/usr/local/lib:$LD_LIBRARY_PATH"
###export LD_LIBRARY_PATH

# End horrible hack part 2

gmake

%install
gmake install prefix=%{buildroot}/usr/local

#dir=`pwd`
#cd ${RPM_BUILD_ROOT}
#libdir=`echo /usr/local/lib | sed 's|^/||'`
#find $libdir ! -type d !  -name '*.p_hi' !   -name '*_p.a'    -print | sed 's|^|/|' > $dir/rpm-noprof-lib-files
#find $libdir ! -type d \( -name '*.p_hi' -or -name '*_p.a' \) -print | sed 's|^|/|' > $dir/rpm-prof-lib-files
#for x in usr/local/bin/ghc*; do sed 's|/var/local/tmp/ghc-6.4.1-root/usr/local|/usr/local|' ${x} > ${x}.out; mv ${x}.out ${x}; chmod 755 ${x}; done
#cd $dir

%clean
#rm -rf %{_tmppath}/ghc-%{version}
#rm -rf %{_tmppath}/ghc-ncurses-hack
#rm -rf %{_tmppath}/ncurses*rpm
rm -rf %{buildroot}

#%post
#/sbin/ldconfig 2>/dev/null
#
#%postun
#/sbin/ldconfig 2>/dev/null

%files
%defattr(-, root, root, 0755)
%doc README docs
%{_bindir}/*
%{_libdir}/*

%changelog
* Mon Mar 27 2006 Etan Reisner <deryni@jla.rutgers.edu>
- -7 builds using our bootstrapped ghc, so as to not require upstream binaries and not need such awful specfile hacks
* Tue Mar 07 2006 Etan Reisner <deryni@jla.rutgers.edu>
- Bootstrapped ghc from upstream binaries
* Mon Oct 25 2005 Rob Zinkov <rzinkov@nbcs.rutgers.edu>
- Fixed bugs in make install
* Fri Oct 21 2005 Rob Zinkov <rzinkov@nbcs.rutgers.edu>
- Initial release
