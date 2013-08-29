### Unfortunately, version 2.13 requires <complex.h> which is provided starting in Solaris 10.
### So 2.12 is the highest we can do. No more upgrades past 2.12.
%global ver 2.12.2
%global rprefix /usr/local/R-%{ver}

%global _mandir /usr/local/man

Name:	 	R	
Version:	%{ver}
Release:	1
Group:		Applications/Math
License:	GPL
URL:		http://www.r-project.org
Source:		http://cran.r-project.org/src/base/R-2/R-%{version}.tar.gz
Patch:		R-2.9.0-solaris_bash_fix.patch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root

Requires:       vpkg-SPROl90s vpkg-SPROsunms
Requires:	acroread8

BuildRequires:	tcl-tk libpng3-devel libjpeg-devel libiconv-devel sed
BuildRequires:	perl >= 2.8.0
BuildRequires:  teTeX
BuildRequires:  xz-devel

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

# Why Neo, 
sed -i -e 's|\(@RBLAS_LDFLAGS@\)|\1 -lc|' -e 's|@BUILD_CYGWIN_TRUE@||' src/extra/blas/Makefile.in
sed -i -e 's|(LIBR)|(LIBR) -R/opt/SUNWspro/lib -L/opt/SUNWspro/lib -R%{rprefix}/lib/R/lib/ -L%{rprefix}/lib/R/lib/ -lm -lc -lsunmath -lfsu|' \
    -e 's|\(@RLAPACK_LDFLAGS@\)|\1 -R/opt/SUNWspro/lib -L/opt/SUNWspro/lib -R%{rprefix}/lib/R/lib/ -L%{rprefix}/lib/R/lib/ -lm -lc -lsunmath -lfsu|' \
    src/modules/lapack/Makefile.in

%build
# Couldn't build with proper LDFLAGS: -Bdirect -zdefs
PATH="/opt/SUNWspro/bin:/usr/ccs/bin:/usr/local/teTeX/bin/:${PATH}"
CC="cc" CXX="CC" F77="f77"
CFLAGS="-I/usr/local/include -g -xs"
CPPFLAGS="-I/usr/local/include"
LDFLAGS="-L/usr/local/lib -R/usr/local/lib"
PERL="/usr/local/perl5/bin/perl"
R_SHELL="/bin/bash"
MAIN_LDFLAGS="-L/usr/local/lib -R/usr/local/lib -B direct -z lazyload -z ignore -z defs"
SHLIB_LDFLAGS="-L/usr/local/lib -R/usr/local/lib -z text -B direct -z lazyload -z combreloc -z ignore"
export PATH CC CXX F77 CFLAGS CPPFLAGS LDFLAGS PERL R_SHELL SHLIB_LDFLAGS MAIN_LDFLAGS

### do NOT use the rpmmacros configure, we need MAIN_LDFLAGS and SHLIB_LDFLAGS different

### DO NOT EVER USE THIS METHOD. richton 16-Aug-2011
/usr/local/bin/sed --in-place=RU s/-zdefs//g configure
/usr/local/bin/sed --in-place=RU s/-zdefs//g m4/libtool.m4

./configure --host=%{_host} --build=%{_build} \
  --target=%{_target_platform} \
  --prefix=%{rprefix} \
  --mandir=%{_mandir} \
  --infodir=%{_infodir} \
  --disable-nls --with-tcltk=%{_libdir} --with-tk-config=%{_libdir} --with-tcl-config=%{_libdir}

gmake -j3

%install
rm -rf %{buildroot}

PERL="/usr/local/perl5/bin/perl"
export PERL

gmake install DESTDIR=%{buildroot}

# Create symlink
ln -s R-%{ver} %{buildroot}%{_prefix}/R

# Change default pdf viewer to acroread. Hopefully, R doesn't complain.
cd %{buildroot}%{rprefix}/lib/R/etc
sed "s|^R_PDFVIEWER=.*|R_PDFVIEWER=${R_PDFVIEWER-'acroread'}|" Renviron > Renviron.2
sed "s|^PAGER=.*|PAGER=${PAGER-'/usr/bin/less'}|" Renviron.2 > Renviron
sed "s|^R_BROWSER=.*|R_BROWSER=${R_BROWSER-''}|" Renviron > Renviron.2
mv Renviron.2 Renviron

# The following is borrowed from the debian rules file for r-base-2.1.1-1
# link $R_HOME/bin/R to real one, and set R_HOME_DIR env.var. 
perl -p -i -e 's|^R_HOME_DIR=.*|R_HOME_DIR=%{rprefix}/lib/R|' %{buildroot}%{rprefix}/bin/R
# fix permissions (Lintian)
chmod a+x %{buildroot}%{rprefix}/lib/R/share/sh/echo.sh

%post
echo "Please edit %{rprefix}/lib/R/etc/Renviron, to make sure"
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
%{_prefix}/R
%{rprefix}/bin/R*
%{rprefix}/lib/R/
%{_mandir}/man1/R*

%changelog
* Tue Aug 16 2011 Aaron Richton <richton@nbcs.rutgers.edu> - 2.12.2-1
- bump to 2.12.2

* Tue Aug 17 2010 Orcan Ogetbil <orcan@nbcs.rutgers.edu> - 2.11.1-2
- Change R prefix to /usr/local/R/

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
