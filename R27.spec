Summary:	R - Statistics Program
Name:	 	R	
Version:	2.7.1
Release:	1
License:	GPL
Group:		Applications/Math
URL:		http://www.r-project.org/
Source0:	%{name}-%{version}.tar.gz
Vendor:		NBCS-OSS
Distribution:	RU-Solaris
BuildRoot:	%{_tmppath}/%{name}-root
BuildRequires:	tcl-tk >= 8.4.16-1 libpng3-devel >= 1.2.8-3 
BuildRequires:	libjpeg-devel >= 6b-14 perl >= 2.8.0
Requires:	acroread7
Requires:	vpkg-SPROl90s vpkg-SUNWlibms vpkg-SPROsunms

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
PATH="/opt/SUNWspro/bin:${PATH}" \
CC="cc" CXX="CC" CPPFLAGS="-I/usr/local/include" \
LD="/usr/ccs/bin/ld" \
LDFLAGS="-L/usr/local/lib -R/usr/local/lib" F77="f77" \
PERL="/usr/local/perl5/bin/perl"
export PATH CC CXX CPPFLAGS LD LDFLAGS F77 PERL

./configure --prefix=%{rprefix} \
	--with-tcltk=/usr/local/lib \
	--with-tk-config=/usr/local/lib \
	--with-tcl-config=/usr/local/lib \
	--disable-nls

gmake

%install
PATH="/opt/SUNWspro/bin:${PATH}" \
CC="cc" CXX="CC" CPPFLAGS="-I/usr/local/include" \
LD="/usr/ccs/bin/ld" \
LDFLAGS="-L/usr/local/lib -R/usr/local/lib" F77="f77" \
PERL="/usr/local/perl5/bin/perl"
export PATH CC CXX CPPFLAGS LD LDFLAGS F77 PERL

rm -rf %{buildroot}
gmake install DESTDIR=%{buildroot}
cd %{buildroot}/usr/local
ln -s R-%{version} R

# Change default pdf viewer to acroread. Hopefully, R doesn't complain.
cd %{buildroot}%{rprefix}/lib/R/etc
sed "s|^R_PDFVIEWER=.*|R_PDFVIEWER=${R_PDFVIEWER-'acroread'}|" Renviron > Renviron.2
sed "s|^PAGER=.*|PAGER=${PAGER-'/usr/bin/less'}|" Renviron.2 > Renviron
sed "s|^R_BROWSER=.*|R_BROWSER=${R_BROWSER-''}|" Renviron > Renviron.2
mv Renviron.2 Renviron

# The following is borrowed from the debian rules file for r-base-2.1.1-1
# link $R_HOME/bin/R to real one, and set R_HOME_DIR env.var. 
cd %{buildroot}%{rprefix}/lib/R/bin
#ln -sf ../../../../bin/R R
cd ../../../bin
perl -p -i -e 's|^R_HOME_DIR=.*|R_HOME_DIR=/usr/local/R-%{version}/lib/R|' R
# fix permissions (Lintian)
chmod a+x	%{buildroot}%{rprefix}/lib/R/share/sh/echo.sh		\
		%{buildroot}%{rprefix}/lib/R/share/sh/help-links.sh	\
		%{buildroot}%{rprefix}/lib/R/share/sh/help-print.sh

%post
echo "Please edit /usr/local/R-%{version}/lib/R/etc/Renviron, to make sure"
echo "it matches what your system provides."
echo "For example:"
echo "If you want R to use gv to view pdfs, change R_PDFVIEWER to"
echo "    R_PDFVIEWER=${R_PDFVIEWER-'/usr/local/bin/gv'}"
echo "If you want R to use lynx to view html files, change R_BROWSER to"
echo "    R_BROWSER=${R_BROWSER-'/usr/local/bin/lynx'}"

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,bin)
/usr/local/%{name}-%{version}
/usr/local/%{name}

%changelog
* Thu Jul 31 2008 Brian Schubert <schubert@nbcs.rutgers.edu> - 2.7.1-1
- Updated to version 2.7.1
* Thu Jul 31 2008 Brian Schubert <schubert@nbcs.rutgers.edu> - 2.5.1-4
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
