Summary:	R - Statistics Program
Name:	 	R	
Version:	2.1.1
Release:	4
Copyright:	GPL
Group:		Applications/Math
URL:		http://www.r-project.org/
Source0:	%{name}-%{version}.tar.gz
BuildRoot:	%{_tmppath}/%{name}-root
BuildRequires: tcl-tk >= 8.4
BuildRequires: libpng3-devel libjpeg62-devel
Requires: tcl-tk >= 8.4
Requires: libpng3 libjpeg62
Requires: acroread5 = 5.10-1

%define rprefix /usr/local/%{name}-%{version}

%description
The core of R is an interpreted computer language with a syntax
superficially similar to C, but which is actually a "functional
programming language" with capabilities similar to Scheme. The language
allows branching and looping as well as modular programming using
functions. Most of the user-visible functions in R are written in R,
calling upon a smaller set of internal primitives. It is possible for
the user to interface to procedures written in C or Fortran languages
for efficiency, and also to write additional primitives.

%prep
%setup -q 

%build
./configure --prefix=%{rprefix}              \
            --with-tcltk=/usr/local/lib      \
            --with-tk-config=/usr/local/lib  \
            --with-tcl-config=/usr/local/lib

make
make check

%install
rm -rf %{buildroot}
make prefix=%{buildroot}/%{rprefix} install
cd %{buildroot}/usr/local
ln -s R-%{version} R

# Change default pdf viewer to acroread. Hopefully, R doesn't complain.
cd %{buildroot}/%{rprefix}/lib/R/etc
sed "s|^R_PDFVIEWER=.*|R_PDFVIEWER=${R_PDFVIEWER-'acroread'}|" Renviron > Renviron.2
sed "s|^PAGER=.*|PAGER=${PAGER-'/usr/bin/less'}|" Renviron.2 > Renviron
sed "s|^R_BROWSER=.*|R_BROWSER=${R_BROWSER-''}|" Renviron > Renviron.2
mv Renviron.2 Renviron

# The following is borrowed from the debian rules file for r-base-2.1.1-1
# link $R_HOME/bin/R to real one, and set R_HOME_DIR env.var. 
cd %{buildroot}/%{rprefix}/lib/R/bin
ln -svf ../../../bin/R R
cd ../../../bin
perl -p -i -e 's|^R_HOME_DIR=.*|R_HOME_DIR=/usr/local/R-%{version}/lib/R|' R
# fix permissions (Lintian)
chmod a+x	%{buildroot}/%{rprefix}/lib/R/share/sh/echo.sh		\
		%{buildroot}/%{rprefix}/lib/R/share/sh/help-links.sh	\
		%{buildroot}/%{rprefix}/lib/R/share/sh/help-print.sh

%post
echo "Please edit /usr/local/R-2.1.1/lib/R/etc/Renviron, to make sure"
echo "it matches what your system provides."
echo "For example:"
echo "If you want R to use gv to view pdfs, change R_PDFVIEWER to"
echo "    R_PDFVIEWER=${R_PDFVIEWER-'/usr/local/bin/gv'}"
echo "If you want R to use lynx to view html files, change R_BROWSER to"
echo "    R_BROWSER=${R_BROWSER-'/usr/local/bin/lynx'}"

%clean
rm -rf %{buildroot}

%files
%defattr(-, root, root)
/usr/local/%{name}-%{version}
/usr/local/%{name}

%changelog
* Tue Aug 23 2005 Jonathan Kaczynski <jmkacz@nbcs.rutgers.edu> - 2.1.1-3
- Took a fix from the debian rules file from r-base-2.1.1-1, so that it will install correctly
- Changed the default pdf reader to acroread

* Fri Aug 19 2005 Jonathan Kaczynski <jmkacz@nbcs.rutgers.edu> - 2.1.1-2
- Upgraded to v2.1.1
- Built against tcl/tk

* Wed Jun 04 2003 Christopher Wawak <cwawak@nbcs.rutgers.edu> - 1.7.0-2
- Initial Rutgers RPM