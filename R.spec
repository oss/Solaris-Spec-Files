Name:	 	R	
Version:	2.11.1
Release:	1
Group:		Applications/Math
License:	GPL
URL:		http://www.r-project.org
Source:		http://cran.r-project.org/src/base/R-2/R-%{version}.tar.gz
Patch:		R-2.9.0-solaris_bash_fix.patch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root

Requires:       vpkg-SPROl90s vpkg-SPROsunms
Requires:	acroread8

BuildRequires:	tcl-tk libpng3-devel libjpeg-devel libiconv-devel
BuildRequires:	perl >= 2.8.0
BuildRequires:  teTeX

Summary:        Statistical computing language and environment

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
%patch -p1

# Why Neo, why?
sed -i -e 's|\(@RBLAS_LDFLAGS@\)|\1 -lc|' -e 's|@BUILD_CYGWIN_TRUE@||' src/extra/blas/Makefile.in
sed -i -e 's|(LIBR)|(LIBR) -R/opt/SUNWspro/lib -L/opt/SUNWspro/lib -R%{_libdir}/R/lib/ -L %{_libdir}/R/lib/ -lm -lc -lsunmath -lfsu|' \
    -e 's|\(@RLAPACK_LDFLAGS@\)|\1 -R/opt/SUNWspro/lib -L/opt/SUNWspro/lib -R%{_libdir}/R/lib/ -L %{_libdir}/R/lib/ -lm -lc -lsunmath -lfsu|' \
    src/modules/lapack/Makefile.in

%build
# Couldn't build with proper LDFLAGS: -Bdirect -zdefs
PATH="/opt/SUNWspro/bin:/usr/ccs/bin:/usr/local/teTeX/bin/:${PATH}"
CC="cc" CXX="CC" F77="f77"
CFLAGS="-I/usr/local/include -g -xO2"
CPPFLAGS="-I/usr/local/include -g -xO2"
LDFLAGS="-L/usr/local/lib -R/usr/local/lib"
PERL="/usr/local/perl5/bin/perl"
R_SHELL="/bin/bash"
export PATH CC CXX F77 CFLAGS CPPFLAGS LDFLAGS PERL R_SHELL

./configure \
	--with-tcltk=%{_libdir}			\
	--with-tk-config=%{_libdir}		\
	--with-tcl-config=%{_libdir}		\
	--disable-nls

gmake -j3

%install
rm -rf %{buildroot}

PERL="/usr/local/perl5/bin/perl"
export PERL

gmake install DESTDIR=%{buildroot}

# Change default pdf viewer to acroread. Hopefully, R doesn't complain.
cd %{buildroot}%{_prefix}/lib/R/etc
sed "s|^R_PDFVIEWER=.*|R_PDFVIEWER=${R_PDFVIEWER-'acroread'}|" Renviron > Renviron.2
sed "s|^PAGER=.*|PAGER=${PAGER-'/usr/bin/less'}|" Renviron.2 > Renviron
sed "s|^R_BROWSER=.*|R_BROWSER=${R_BROWSER-''}|" Renviron > Renviron.2
mv Renviron.2 Renviron

# The following is borrowed from the debian rules file for r-base-2.1.1-1
# link $R_HOME/bin/R to real one, and set R_HOME_DIR env.var. 
perl -p -i -e 's|^R_HOME_DIR=.*|R_HOME_DIR=/usr/local/lib/R|' %{buildroot}%{_prefix}/bin/R
# fix permissions (Lintian)
chmod a+x %{buildroot}%{_prefix}/lib/R/share/sh/echo.sh

%post
echo "Please edit /usr/local/lib/R/etc/Renviron, to make sure"
echo "it matches what your system provides."
echo "For example:"
echo "If you want R to use gv to view pdfs, change R_PDFVIEWER to"
echo "    R_PDFVIEWER=${R_PDFVIEWER-'/usr/local/bin/gv'}"
echo "If you want R to use lynx to view html files, change R_BROWSER to"
echo "    R_BROWSER=${R_BROWSER-'/usr/local/bin/lynx'}"

%clean
rm -rf %{buildroot}

%files
%defattr(-, root, root, -)
%doc doc/*
%{_bindir}/R*
%{_libdir}/R/
%{_mandir}/man1/R*

%changelog
* Thu Aug 05 2010 Orcan Ogetbil <orcan@nbcs.rutgers.edu> - 2.11.1-1
- Update to 2.11.1
- Remove BR: gettext-devel

* Mon Jul 20 2009 Brian Schubert <schubert@nbcs.rutgers.edu> - 2.9.1-1
- Updated to version 2.9.1
- Added gettext-devel to BuildRequires

* Wed May 13 2009 Brian Schubert <schubert@nbcs.rutgers.edu> - 2.9.0-1
- Updated to version 2.9.0

* Thu Aug 28 2008 Brian Schubert <schubert@nbcs.rutgers.edu> - 2.7.1-2
- Now requires acroread8

* Fri Aug 08 2008 Brian Schubert <schubert@nbcs.rutgers.edu> - 2.7.1-1
- Updated to version 2.7.1
- Fixed dependency issues, switched to gmake, disabled nls

* Thu Aug 16 2007 David Lee Halik <dhalik@nbcs.rutgers.edu> - 2.5.1-3
- Fixed defines for dep issues

* Thu Aug 16 2007 David Lee Halik <dhalik@nbcs.rutgers.edu> - 2.5.1-2
- Added post message about sun studio requirement

* Mon Aug 13 2007 David Lee Halik <dhalik@nbcs.rutgers.edu> - 2.5.1-1
- Bump to 2.5.1

* Tue Aug 23 2005 Jonathan Kaczynski <jmkacz@nbcs.rutgers.edu> - 2.1.1-3
- Took a fix from the debian rules file from r-base-2.1.1-1, so that it will install correctly
- Changed the default pdf reader to acroread

* Fri Aug 19 2005 Jonathan Kaczynski <jmkacz@nbcs.rutgers.edu> - 2.1.1-2
- Upgraded to v2.1.1
- Built against tcl/tk

* Wed Jun 04 2003 Christopher Wawak <cwawak@nbcs.rutgers.edu> - 1.7.0-2
- Initial Rutgers RPM
