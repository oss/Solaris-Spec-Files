# This spec file assumes that Sun Studio 12 is installed in /opt/sunstudio12

Name:		octave
Version:	3.0.5
Release:        1
License:	GPL
Group:		Applications/Math
Source:		%{name}-%{version}.tar.gz
Patch0:		octave-3.0.3-is_dir_sep.patch
Patch1:		octave-3.0.5-glpk.patch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root

Requires:       gnuplot
Requires:       vpkg-SPROpls vpkg-SPROl90s vpkg-SPROsunms

BuildRequires:	bison, flex, gperf, texinfo, tetex, sed
BuildRequires:	pcre-devel, readline5-devel, ncurses-devel 
BuildRequires:	fftw-devel, suitesparse-devel, glpk-devel, qhull-devel

Summary:        A high-level language, primarily intended for numerical computations

%description
GNU Octave is a high-level language, primarily intended for numerical 
computations. It provides a convenient command line interface for 
solving linear and nonlinear problems numerically, and for performing 
other numerical experiments using a language that is mostly compatible 
with Matlab. It may also be used as a batch-oriented language.

Octave has extensive tools for solving common numerical linear algebra 
problems, finding the roots of nonlinear equations, integrating ordinary 
functions, manipulating polynomials, and integrating ordinary 
differential and differential-algebraic equations. It is easily 
extensible and customizable via user-defined functions written in 
Octave's own language, or using dynamically loaded modules written in 
C++, C, Fortran, or other languages.

%package devel 
Summary: Octave development files.
Group: Development/Libraries
Requires: octave = %{version}-%{release}
Requires: readline5-devel

%description devel
The octave-devel package contains files needed for developing
applications which use GNU Octave.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
PATH="/opt/sunstudio12/SUNWspro/bin:/usr/ccs/bin:/usr/local/teTeX/bin:${PATH}"
CC="cc" CFLAGS="-KPIC -g -xs"
CXX="CC" CXXFLAGS="${CFLAGS}"
F77="f90" FFLAGS="-f77 -ftrap=%none"
CPPFLAGS="-I/opt/sunstudio12/SUNWspro/prod/include/CC/std \
	  -I/opt/sunstudio12/SUNWspro/prod/include/cc \
	  -I/usr/local/include/readline \
	  -I/usr/local/include/ncursesw \
	  -I/usr/local/include"
LDFLAGS="-L/opt/sunstudio12/SUNWspro/lib -R/opt/SUNWspro/lib \
	 -L/usr/local/lib -R/usr/local/lib \
	 -Bdirect -z defs"
LD_LIBRARY_PATH="/opt/sunstudio12/SUNWspro/lib:/usr/local/lib"
LIBS="-lsunmath"	
 
export PATH CC CFLAGS CXX CXXFLAGS F77 FFLAGS CPPFLAGS LDFLAGS LD_LIBRARY_PATH LIBS

./configure --prefix=%{_prefix} \
	    --mandir=%{_mandir} \
	    --infodir=%{_infodir} \
	    --enable-shared \
	    --disable-static \
	    --with-blas=sunperf \
	    --with-lapack=sunperf \
            --without-zlib	

gmake -j3

%install
rm -rf %{buildroot}
gmake install DESTDIR=%{buildroot}

rm -f %{buildroot}%{_infodir}/dir

# Remove buildroot path from ls-R
cd %{buildroot}%{_libexecdir}/octave
%{__sed} -i "s:%{buildroot}::g" ls-R
cd %{buildroot}%{_datadir}/octave
%{__sed} -i "s:%{buildroot}::g" ls-R

%clean
rm -rf %{buildroot}

%post
if [ -x %{_bindir}/install-info ]; then
	%{_bindir}/install-info --info-dir=%{_infodir} \
		%{_infodir}/octave.info
fi

%preun
if [ -x %{_bindir}/install-info ]; then
	%{_bindir}/install-info --delete --info-dir=%{_infodir} \
		%{_infodir}/octave.info
fi

%files
%defattr(-,root,bin)
%doc COPYING NEWS* PROJECTS README README.kpathsea
%doc SENDING-PATCHES THANKS emacs examples ROADMAP
%doc doc/faq doc/interpreter doc/refcard
%{_bindir}/octave*
%{_libdir}/octave*
%{_datadir}/octave
%{_libexecdir}/octave
%{_mandir}/man1/octave*.1
%{_infodir}/octave.info*

%files devel
%defattr(-,root,bin)
%doc doc/liboctave
%{_bindir}/mkoctfile*
%{_includedir}/octave-%{version}
%{_mandir}/man1/mkoctfile.1

%changelog
* Fri Jan 23 2009 Brian Schubert <schubert@nbcs.rutgers.edu> - 3.0.3-1
- Initial build

