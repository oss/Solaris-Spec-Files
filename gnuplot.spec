Name: gnuplot
Version: 3.7.1
Copyright: GPL-like
Group: Applications/Engineering
Summary: Command-line plotting software
Release: 3ru
Source: gnuplot-%{version}.tar.gz
Patch0: gnuplot-3.7.1-gd-1.8.patch
Requires: libpng libjpeg
BuildRequires: libpng
BuildRoot: /var/tmp/%{name}-root

%description
Gnuplot is a command-line-driven plotting program that is unrelated to
the GNU project.  It can make graphs in a variety of formats, such as
LaTeX, ps, and png.  It also can send its output to an X11 window.


%prep
%setup -q
%patch -p1 -b .gd-1.8

%build
LD_LIBRARY_PATH="/usr/local/lib:/usr/sfw/lib"
LD_RUN_PATH="/usr/local/lib:/usr/sfw/lib"
CPPFLAGS="-I/usr/sfw/include"
export LD_RUN_PATH LD_LIBRARY_PATH CPPFLAGS
./configure --prefix=/usr/local
make  LIBS=" -lm -ljpeg -R/usr/local/lib -R/usr/sfw/lib "

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/local
make install prefix=$RPM_BUILD_ROOT/usr/local

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc Copyright
/usr/local/bin/gnuplot
/usr/local/bin/gnuplot_x11
/usr/local/share/gnuplot.gih
/usr/local/man/man1/gnuplot.1
