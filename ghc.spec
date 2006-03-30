Summary: The Glasgow Haskell Compiler
Name: ghc
Version: 6.4.1
Release: 7
License: Other
Group: Development/Languages/Haskell
URL: http://www.haskell.org/ghc/
Source: http://www.haskell.org/ghc/dist/%{version}/ghc-%{version}-src.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-root
BuildRequires: readline5-devel, ghc >= 6.4, gmp, sed, bzip2, make
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

./configure --prefix=/usr/local
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
