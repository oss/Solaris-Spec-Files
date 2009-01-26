Name:           glpk
Version:        4.35
Release:        1
Summary:        GNU Linear Programming Kit

Group:          System Environment/Libraries
License:        GPLv3
URL:            http://www.gnu.org/software/glpk/glpk.html
Source:        ftp://ftp.gnu.org/gnu/glpk/%{name}-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

%description
The GLPK (GNU Linear Programming Kit) package is intended for solving
large-scale linear programming (LP), mixed integer programming (MIP),
and other related problems. It is a set of routines written in ANSI C
and organized in the form of a callable library.

GLPK supports the GNU MathProg language, which is a subset of the AMPL
language.

The GLPK package includes the following main components:

 * Revised simplex method.
 * Primal-dual interior point method.
 * Branch-and-bound method.
 * Translator for GNU MathProg.
 * Application program interface (API).
 * Stand-alone LP/MIP solver. 


%package devel
Summary:        Development headers and files for GLPK
Group:          Development/Libraries
Requires:       %{name} = %{version}-%{release}

%description devel
The glpk-devel package contains libraries and headers for developing
applications which use GLPK (GNU Linear Programming Kit).


%package utils
Summary:        GLPK-related utilities and examples
Group:          Development/Libraries
Requires:       %{name} = %{version}-%{release}

%description utils
The glpk-utils package contains the standalone solver programs glpksol
and tspsol that use GLPK (GNU Linear Programming Kit).


%package static
Summary:        Static version of GLPK libraries
Group:          Development/Libraries
Requires:       %{name}-devel = %{version}-%{release}

%description static
The glpk-static package contains the statically linkable version of
the GLPK (GNU Linear Programming Kit) libraries.


%prep
%setup -q

%build
PATH="/opt/SUNWspro/bin:${PATH}"
CC="cc" CXX="CC" CPPFLAGS="-I/usr/local/include"
LD="/usr/ccs/bin/ld" 
LDFLAGS="-L/usr/local/lib -R/usr/local/lib"
LIBS=-ldl
export PATH CC CXX CPPFLAGS LD LDFLAGS LIBS
./configure --prefix=%{_prefix}
gmake -j3

%install
rm -rf $RPM_BUILD_ROOT
gmake install prefix=$RPM_BUILD_ROOT%{_prefix} \
	bindir=$RPM_BUILD_ROOT%{_bindir} libdir=$RPM_BUILD_ROOT%{_libdir} \
	includedir=$RPM_BUILD_ROOT%{_includedir}/%name
## Clean up directories that are included in docs
gmake clean
rm -Rf examples/.deps examples/Makefile* doc/*.dvi doc/*.latex

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc AUTHORS ChangeLog COPYING NEWS README doc
%{_libdir}/*.so*

%files devel
%defattr(-,root,root)
%doc AUTHORS ChangeLog COPYING NEWS README doc
%{_includedir}/glpk

%files utils
%defattr(-,root,root)
%doc COPYING examples
%{_bindir}/*

%files static
%defattr(-,root,root)
%{_libdir}/*.a
%exclude %{_libdir}/*.la


%changelog
* Fri Jan 23 2009 Brian Schubert <schubert@nbcs.rutgers.edu> - 4.35-1
- Initial RU-Solaris build
