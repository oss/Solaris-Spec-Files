Name: gnuplot
Version: 3.7.1
Copyright: GPL-like
Group: Applications/Engineering
Summary: Command-line plotting software
Release: 2
Source: gnuplot-%{version}.tar.gz
Requires: libpng
BuildRequires: libpng
BuildRoot: /var/tmp/%{name}-root

%description
Gnuplot is a command-line-driven plotting program that is unrelated to
the GNU project.  It can make graphs in a variety of formats, such as
LaTeX, ps, and png.  It also can send its output to an X11 window.


%prep
%setup -q

%build
./configure --prefix=/usr/local
make  LIBS=" -lm  -R/usr/local/lib "

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
