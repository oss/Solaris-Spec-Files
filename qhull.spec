Summary: General dimension convex hull programs
Name: qhull
Version: 2003.1
Release: 1
License:  Distributable
Group: System Environment/Libraries
Source: http://www.qhull.org/download/qhull-%{version}.tar.gz

URL: http://www.qhull.org
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root

%description
Qhull is a general dimension convex hull program that reads a set
of points from stdin, and outputs the smallest convex set that contains
the points to stdout.  It also generates Delaunay triangulations, Voronoi
diagrams, furthest-site Voronoi diagrams, and halfspace intersections
about a point.

%package devel
Group: Development/Libraries
Summary: Development files for qhull
Requires: %{name} = %{version}-%{release}

%description devel
Qhull is a general dimension convex hull program that reads a set
of points from stdin, and outputs the smallest convex set that contains
the points to stdout.  It also generates Delaunay triangulations, Voronoi
diagrams, furthest-site Voronoi diagrams, and halfspace intersections
about a point.

%prep
%setup -q -n %{name}-%{version}
sed -i -e "s,\"../html/,\"html/,g" src/*.htm

%build
PATH="/opt/SUNWspro:${PATH}"
CC="cc" CXX="CC" CPPFLAGS="-I/usr/local/include"
LD="/usr/ccs/bin/ld" LDFLAGS="-L/usr/local/lib -R/usr/local/lib"
export PATH CC CXX CPPFLAGS LD LDFLAGS

./configure --disable-static
gmake

%install
rm -rf $RPM_BUILD_ROOT
gmake DESTDIR=$RPM_BUILD_ROOT \
  docdir=%{_docdir}/%{name}-%{version} install
rm -f ${RPM_BUILD_ROOT}/%{_libdir}/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc %{_docdir}/%{name}-%{version}
%_bindir/*
%_libdir/*.so.*
%_mandir/man1/*

%files devel
%defattr(-,root,root)
%_libdir/*.so
%_includedir/*

%changelog
* Tue Jan 20 2008 Brian Schubert <schubert@nbcs.rutgers.edu> - 2003.1-1
- Initial RU-Solaris build
