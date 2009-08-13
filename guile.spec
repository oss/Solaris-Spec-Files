Name:		guile
Version:	1.8.7
Release:        1
Group:		Development/Languages
License:	GPL
URL:		www.gnu.org/software/guile
Source:		ftp://ftp.gnu.org/gnu/guile/guile-%{version}.tar.gz
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires:	gmp-devel libtool-devel

Summary:	Scheme interpreter	

%description
Guile is a Scheme interpreter that you can link into your programs
to make them more customizable, in the spirit of Emacs.  If you are
writing a program that requires a lot of configuring, consider using
Guile instead of an ad-hoc configuration language.

%package devel
Group:		Development/Languages
Requires:	guile = %{version}-%{release}
Summary:        Guile header files and development tools

%description devel
This package contains header files and utilities for the development
of applications that use Guile.

%prep
%setup -q

%build
PATH="/opt/SUNWspro/bin:/usr/ccs/bin:${PATH}"
CC="cc" CXX="CC" 
CPPFLAGS="-I/usr/local/include/gmp32 -I/usr/local/include"
LDFLAGS="-L/usr/local/lib -R/usr/local/lib"
export PATH CC CXX CPPFLAGS LDFLAGS

./configure \
	--prefix=%{_prefix}		\
	--infodir=%{_infodir}		\
	--mandir=%{_mandir}		\
	--enable-dynamic-linking 	\
	--disable-static		\
	--disable-nls 			

gmake -j3

%install
rm -rf %{buildroot}

gmake install DESTDIR=%{buildroot}

rm -f %{buildroot}%{_libdir}/*.la
rm -f %{buildroot}%{_infodir}/dir

%clean
rm -rf %{buildroot}

%post
if [ -x %{_bindir}/install-info ] ; then
	%{_bindir}/install-info --info-dir=%{_infodir} %{_infodir}/guile.info
fi

%preun
if [ -x %{_bindir}/install-info ] ; then
        %{_bindir}/install-info --info-dir=%{_infodir} --delete %{_infodir}/guile.info
fi

%files
%defattr(-, root, root)
%doc README NEWS AUTHORS THANKS COPYING.LESSER
%doc ChangeLog* GUILE-VERSION LICENSE
%{_bindir}/guile
%{_bindir}/guile-tools
%{_libdir}/*.so*
%{_datadir}/guile/
%{_datadir}/emacs/site-lisp
%{_infodir}/*.info*
%{_mandir}/man1/*

%files devel
%defattr(-, root, root)
%{_bindir}/guile-config
%{_bindir}/guile-snarf
%{_includedir}/*
%{_datadir}/aclocal/*.m4
%{_libdir}/pkgconfig/*.pc

%changelog
* Wed Aug 12 2009 Brian Schubert <schubert@nbcs.rutgers.edu> - 1.8.7-1
- Updated to version 1.8.7
- No longer build static libraries
- Added post and preun scriptlets

* Fri Jan 23 2009 Brian Schubert <schubert@nbcs.rutgers.edu> - 1.8.6-1
- Added devel, static packages and bumped to 1.8.6

* Fri May 23 2008 David Diffenbaugh <davediff@nbcs.rutgers.edu> - 1.8.5-1
- bumped to 1.8.5, patch no longer needed, bug was upstreamed

* Fri Feb 08 2008 David Diffenbaugh <davediff@nbcs.rutgers.edu> - 1.8.3-4
- corrected files section, removed info/dir

* Wed Feb 06 2008 David Diffenbaugh <davediff@nbcs.rutgers.edu> - 1.8.3-3
- updated patch to include read.c and strings.c, added /usr/local/share to files section

* Mon Feb 04 2008 David Diffenbaugh <davediff@nbcs.rutgers.edu> - 1.8.3-2
- added patch from guile developers added libtool-devel buildrequires added --disable-nls

* Sat Oct 20 2007 David Lee Halik <dhalik@nbcs.rutgers.edu> - 1.8.3-1
- Bump tp 1.8.3
- De-gcc-ify
