Name:		guile
Version:	1.8.6
License:	GPL
Group:		Development/Languages
Summary:	An extensible scripting language
Release:	1
Source:		%{name}-%{version}.tar.gz
BuildRoot:	/var/tmp/%{name}-%{version}-%{release}-root
BuildRequires:	gmp-devel >= 4.1 libtool-devel >= 1.5.26

%description
Guile is a Scheme interpreter that you can link into your programs
to make them more customizable, in the spirit of Emacs.  If you are
writing a program that requires a lot of configuring, consider using
Guile instead of an ad-hoc configuration language.

%package devel
Summary:	Guile header files and development tools
Group:		Development/Languages
Requires:	guile = %{version}-%{release}

%description devel
This package contains header files and utilities for the development
of applications that use Guile.

%package static
Summary:	Guile static libraries
Group:		Development/Languages
Requires:	guile-devel = %{version}-%{release}

%description static
This package contains libraries needed to develop staticly-linked
applications that use guile.

%prep
%setup -q

%build
PATH="/opt/SUNWspro/bin:${PATH}"
CC="cc" CXX="CC" CPPFLAGS="-I/usr/local/include -I/usr/local/include/gmp32"
LD="/usr/ccs/bin/ld"
LDFLAGS="-L/usr/local/lib -R/usr/local/lib"
export PATH CC CXX CPPFLAGS LD LDFLAGS


./configure \
	--prefix=%{_prefix} \
	--enable-dynamic-linking \
	--disable-nls \
	--mandir=%{_mandir} \
	--infodir=%{_infodir}
gmake

%install
rm -rf %{buildroot}
gmake install DESTDIR=%{buildroot}
rm -f %{buildroot}%{_libdir}/*.la
rm -f %{buildroot}%{_infodir}/dir

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc README NEW AUTHORS THANKS COPYING.LESSER
%doc ChangeLog* FAQ GUILE-VERSION LICENSE
%{_bindir}/guile
%{_bindir}/guile-tools
%{_libdir}/*.so*
%{_datadir}/guile
%{_datadir}/emacs/site-lisp
%{_infodir}/*
%{_mandir}/man1/*

%files devel
%defattr(-,root,root)
%{_bindir}/guile-config
%{_bindir}/guile-snarf
%{_includedir}/*
%{_datadir}/aclocal/guile.m4
%{_libdir}/pkgconfig/guile-1.8.pc

%files static
%defattr(-,root,root)
%{_libdir}/*.a

%changelog
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
