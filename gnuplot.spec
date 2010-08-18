Name:          gnuplot
Version:       4.4.0
Release:       2
# Modifications are to be distributed as patches to the released version.
# aglfn.txt has license: MIT
License:       gnuplot and MIT
Group:         Applications/Engineering
Summary:       Command-line plotting software
Source:        http://downloads.sourceforge.net/gnuplot/gnuplot-%{version}.tar.gz
URL:           http://www.gnuplot.info/
BuildRequires: libpng3-devel libjpeg-devel
BuildRoot:     %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

%description
Gnuplot is a command-line-driven plotting program that is unrelated to
the GNU project.  It can make graphs in a variety of formats, such as
LaTeX, ps, and png.  It also can send its output to an X11 window.

%prep
%setup -q

%build
%configure

gmake

%install
rm -rf %{buildroot}
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
%defattr(-,root,root, -)
%doc README FAQ NEWS Copyright ChangeLog
%{_infodir}/gnuplot.info
%{_mandir}/man1/gnuplot.1
/usr/local/bin/gnuplot
/usr/local/libexec/gnuplot/
/usr/local/share/gnuplot/
/usr/local/share/emacs/site-lisp/*


%changelog
* Mon Aug 16 2010 Orcan Ogetbil <orcan#nbcs.rutgers.edu> - 4.4.0-2
- Rebuild. For some reason the info file turned into zero size
- Fix license

* Wed Aug 04 2010 Orcan Ogetbil <orcan#nbcs.rutgers.edu> - 4.4.0-1
- Update to 4.4.0

* Tue Jul 08 2008 Brian Schubert <schubert@nbcs.rutgers.edu> - 4.2.3-1
- Added changelog and updated to version 4.2.3

