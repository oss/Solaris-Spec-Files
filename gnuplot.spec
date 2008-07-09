Name: gnuplot
Version: 4.2.3
Copyright: GPL-like
Group: Applications/Engineering
Summary: Command-line plotting software
Release: 1
Source: gnuplot-%{version}.tar.gz
Requires: libpng3 libjpeg
BuildRequires: libpng3-devel libjpeg-devel
BuildRoot: %{_tmppath}/%{name}-root

%description
Gnuplot is a command-line-driven plotting program that is unrelated to
the GNU project.  It can make graphs in a variety of formats, such as
LaTeX, ps, and png.  It also can send its output to an X11 window.

%prep
%setup -q

%build
PATH="/opt/SUNWspro/bin:${PATH}" \
CC="cc" CXX="CC" CPPFLAGS="-I/usr/local/include" \
LD="/usr/ccs/bin/ld" \
LDFLAGS="-L/usr/local/lib -R/usr/local/lib" \
export PATH CC CXX CPPFLAGS LD LDFLAGS

./configure \
	--prefix=/usr/local \
	--mandir=/usr/local/share/man \
	--infodir=/usr/local/share/info
gmake

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/local
gmake install DESTDIR=%{buildroot}
rm -f %{buildroot}/usr/local/share/info/dir

%clean
rm -rf %{buildroot}

%post
if [ -x /usr/local/bin/install-info ]; then
	/usr/local/bin/install-info --info-dir=/usr/local/share/info \
		/usr/local/share/info/gnuplot.info
fi

%preun
if [ -x /usr/local/bin/install-info ]; then
	/usr/local/bin/install-info --delete --info-dir=/usr/local/share/info \
		/usr/local/share/info/gnuplot.info
fi

%files
%defattr(-,root,root)
%doc README FAQ NEWS Copyright ChangeLog
%doc /usr/local/share/info/gnuplot.info
%doc /usr/local/share/man/man1/gnuplot.1
/usr/local/bin/gnuplot
/usr/local/lib/X11/app-defaults/Gnuplot
/usr/local/libexec/gnuplot/4.2/gnuplot_x11
/usr/local/share/gnuplot/4.2/*
/usr/local/share/emacs/site-lisp/*

%changelog
* Tue Jul 08 2008 Brian Schubert <schubert@nbcs.rutgers.edu> - 4.2.3-1
- Added changelog and updated to version 4.2.3

