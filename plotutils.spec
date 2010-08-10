Summary:       GNU plot utils
Name:          plotutils
Version:       2.6
Release:       1
Group:         Applications/Engineering
License:       GPL
URL:           http://ftp.gnu.org/gnu/plotutils/
Source0:       http://ftp.gnu.org/gnu/plotutils/plotutils-%{version}.tar.gz
Patch0:        plotutils-solaris-compile.patch
BuildRoot:     %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildRequires: libpng3-devel

%description
Not to be confused with gnuplot (which is -not- a GNU program), the
GNU plotutils consist of spline, double, ode, plot, tek2plot,
plotfont, graph, pic2plot, libplot and libplotter.

%package devel
Summary: GNU plotutils headers and static libraries
Group: Development/Libraries
Requires: plotutils = %{version}

%description devel
Plotutils-devel contains the static libraries and headers for
plotutils.

%prep
%setup -q
%patch0 -p1

%build
CXXFLAGS="-fpermissive"
%configure --with-xpm --enable-libplotter
gmake

%check
gmake check

%install
rm -rf $RPM_BUILD_ROOT
gmake install DESTDIR=$RPM_BUILD_ROOT

# We don't like static libraries
rm -f $RPM_BUILD_ROOT/usr/local/lib/*a

rm -f $RPM_BUILD_ROOT/usr/local/share/info/dir

%clean
rm -rf $RPM_BUILD_ROOT

%post
if [ -x /usr/local/bin/install-info ] ; then
	/usr/local/bin/install-info --info-dir=/usr/local/share/info \
		 /usr/local/share/info/plotutils.info
fi

%preun
if [ -x /usr/local/bin/install-info ] ; then
	/usr/local/bin/install-info --delete --info-dir=/usr/local/share/info \
		 /usr/local/share/info/plotutils.info
fi

%files
%defattr(-,root,root,-)
%doc AUTHORS COPYING NEWS README
/usr/local/bin/*
/usr/local/share/ode/*
/usr/local/share/tek2plot/*
/usr/local/share/pic2plot/*
/usr/local/share/libplot/*
/usr/local/lib/lib*.so.*
/usr/local/share/info/plotutils.info
%{_mandir}/man1/*.1

%files devel
%defattr(-,root,root,-)
%doc KNOWN_BUGS TODO THANKS ONEWS 
/usr/local/lib/lib*.so
/usr/local/include/*

%changelog
* Fri Aug 06 2010 Orcan Ogetbil <orcan@nbcs.rutgers.edu> - 2.6-1
- Update to the latest version
