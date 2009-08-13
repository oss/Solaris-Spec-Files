Name:           glpk
Version:        4.39
Release:        1
Group:          System Environment/Libraries
License:        GPLv3
URL:            http://www.gnu.org/software/glpk
Source:		ftp://ftp.gnu.org/gnu/glpk/glpk-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root

Summary:        GNU Linear Programming Kit

%description
The GLPK (GNU Linear Programming Kit) package is intended for solving
large-scale linear programming (LP), mixed integer programming (MIP),
and other related problems. It is a set of routines written in ANSI C
and organized in the form of a callable library.

GLPK supports the GNU MathProg language, which is a subset of the AMPL
language.

%package devel
Group:          Development/Libraries
Requires:       glpk = %{version}-%{release}
Summary:        Development headers and files for GLPK

%description devel
The glpk-devel package contains libraries and headers for developing
applications which use GLPK (GNU Linear Programming Kit).

%package utils
Group:          Development/Libraries
Requires:       glpk = %{version}-%{release}
Summary:        GLPK-related utilities and examples

%description utils
The glpk-utils package contains the standalone solver programs glpksol
and tspsol that use GLPK (GNU Linear Programming Kit).

%package static
Group:          Development/Libraries
Requires:       glpk-devel = %{version}-%{release}
Summary:        Static version of GLPK libraries

%description static
The glpk-static package contains the statically linkable version of
the GLPK (GNU Linear Programming Kit) libraries.

%prep
%setup -q

%build
PATH="/opt/SUNWspro/bin:/usr/ccs/bin:${PATH}"
CC="cc" CXX="CC" CPPFLAGS="-I/usr/local/include"
LDFLAGS="-L/usr/local/lib -R/usr/local/lib"
export PATH CC CXX CPPFLAGS LDFLAGS

./configure --prefix=%{_prefix}

gmake -j3

%install
rm -rf %{buildroot}

gmake install DESTDIR=%{buildroot}

## Clean up directories that are included in docs
gmake clean
rm -Rf examples/.deps examples/Makefile* doc/*.dvi doc/*.latex

rm -f %{buildroot}%{_libdir}/*.la

%clean
rm -rf %{buildroot}

%files
%defattr(-, root, root)
%doc AUTHORS ChangeLog COPYING NEWS README doc
%{_libdir}/*.so*

%files devel
%defattr(-, root, root)
%{_includedir}/*

%files utils
%defattr(-, root, root)
%doc examples
%{_bindir}/*

%files static
%defattr(-, root, root)
%{_libdir}/*.a

%changelog
* Wed Aug 12 2009 Brian Schubert <schubert@nbcs.rutgers.edu> - 4.39-1
- Updated to version 4.39
- Made some packaging modifications

* Fri Jan 23 2009 Brian Schubert <schubert@nbcs.rutgers.edu> - 4.35-1
- Initial RU-Solaris build
