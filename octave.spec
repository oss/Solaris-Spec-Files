Summary:	a high-level language, primarily intended for numerical computations
Name:		octave
Version:	2.1.73
Release:        1
Copyright:	GPL
Group:		Applications/Math
Source:		%{name}-%{version}.tar.bz2
Distribution: 	RU-Solaris
Vendor: 	NBCS-OSS
Packager: 	Leo Zhadanovsky <leozh@nbcs.rutgers.edu>
BuildRoot:	/var/tmp/%{name}-%{version}-root
Requires:	gcc-libs, gnuplot
BuildRequires:	gperf

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
Summary: Libraries, includes to develop applications with %{name}.
Group: Applications/Libraries
Requires: %{name} = %{version}

%description devel
The %{name}-devel package contains the header files and static libraries
for building applications which use %{name}.

%prep
%setup -q

%build
PATH=$PATH:/usr/sfw/bin:/usr/local/teTeX/bin
CPPFLAGS="-I/usr/local/include -I/usr/sfw/include"
LDFLAGS="-L/usr/local/lib -R/usr/local/lib -L/usr/sfw/lib -R/usr/sfw/lib"
LD_LIBRARY_PATH="/usr/local/lib:/usr/sfw/lib"
LD_RUN_PATH="/usr/local/lib:/usr/sfw/lib"
CC="gcc" 
export PATH CPPFLAGS LDFLAGS LD_LIBRARY_PATH LD_RUN_PATH CC

./configure --prefix=/usr/local --disable-nls --enable-shared --enable-dl

make

%install
rm -rf $RPM_BUID_ROOT

make install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,bin,bin)
/usr/local/bin/*
/usr/local/libexec/*
/usr/local/lib/%{name}-%{version}/*.so
/usr/local/lib/%{name}-%{version}/*so*
/usr/local/share/*
/usr/local/man/man1/*
/usr/local/info/octave.info
/usr/local/info/octave.info-1
/usr/local/info/octave.info-2
/usr/local/info/octave.info-3

%files devel
%defattr(-,root,root)
/usr/local/include/*

%changelog
* Mon May 15 2006 Leo Zhadanovsky <leozh@nbcs.rutgers.edu> - 2.1.73-1
- Initial Rutgers release
