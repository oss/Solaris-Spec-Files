Summary: GNU plot utils
Name: plotutils
Version: 2.4.1
Release: 3
Group: Applications/Engineering
Copyright: GPL
Source: plotutils-2.4.1.tar.gz
BuildRoot: /var/tmp/%{name}-root

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

%build
CXX="c++ -fpermissive" \
  LD="/usr/ccs/bin/ld -L/usr/local/lib -R/usr/local/lib" \
  LDFLAGS="-L/usr/local/lib -R/usr/local/lib" \
  CFLAGS="-I/usr/local/include" ./configure --with-xpm --enable-libplotter
make
make check

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/local
make install prefix=$RPM_BUILD_ROOT/usr/local

%clean
rm -rf $RPM_BUILD_ROOT

%post
if [ -x /usr/local/bin/install-info ] ; then
	/usr/local/bin/install-info --info-dir=/usr/local/info \
		 /usr/local/info/plotutils.info
fi

%preun
if [ -x /usr/local/bin/install-info ] ; then
	/usr/local/bin/install-info --delete --info-dir=/usr/local/info \
		 /usr/local/info/plotutils.info
fi

%files
%defattr(-,bin,bin)
/usr/local/bin/*
/usr/local/share/ode/*
/usr/local/share/tek2plot/*
/usr/local/share/pic2plot/*
/usr/local/share/libplot/*
/usr/local/lib/lib*.so*
/usr/local/info/plotutils.info
/usr/local/man/man1/*.1

%files devel
%defattr(-,bin,bin)
/usr/local/lib/*a
/usr/local/include/*
