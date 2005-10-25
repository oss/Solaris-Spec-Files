Summary: The Glasgow Haskell Compiler
Name: ghc
Version: 6.4.1
Release: 2
License: Other
Group: Development/Languages
URL: http://www.haskell.org/ghc/

Source: http://www.haskell.org/ghc/dist/%{version}/ghc-%{version}-sparc-sun-solaris2.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}--root
BuildRequires: readline5
Requires: readline5

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
# GHC configuration does not support differing host/target (i.e., cross-compiling)
./configure --prefix=/usr/local
gmake in-place

%install
rm -rf %{buildroot}
gmake install prefix=%{buildroot}/usr/local
dir=`pwd`
cd ${RPM_BUILD_ROOT}
libdir=`echo %{prefix}/lib | sed 's|^/||'`
find $libdir ! -type d !  -name '*.p_hi' !   -name '*_p.a'    -print | sed 's|^|/|' > $dir/rpm-noprof-lib-files
find $libdir ! -type d \( -name '*.p_hi' -or -name '*_p.a' \) -print | sed 's|^|/|' > $dir/rpm-prof-lib-files
cd $dir

%clean
rm -rf %{buildroot}

%post
/sbin/ldconfig 2>/dev/null

%postun
/sbin/ldconfig 2>/dev/null

%files
%defattr(-, root, root, 0755)
%doc README docs
%{_bindir}/*
%{_libdir}/*

%changelog
* Fri Oct 21 2005 Rob Zinkov <rzinkov@nbcs.rutgers.edu>
- Initial release

