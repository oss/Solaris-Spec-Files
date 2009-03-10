Summary:        Internationalization Tools
Name:           gettext
Version:        0.17
Release:        6
License:	GPL
Group:          Development/Tools
Source:         %{name}-%{version}.tar.gz
Distribution:   RU-Solaris
Vendor:         NBCS-OSS
BuildRoot:      /var/tmp/%{name}-%{version}-root
Requires:	libiconv
BuildRequires:	libiconv-devel

%description
GNU gettext is a tool that helps programmers write programs that
are "portable" culturally: by marking strings in your program that
potentially should be in several languages and compiling with gettext,
you can add translations with minimum effort.  Install gettext if you
are developing software that potentially would be used by non-English
speakers or compiling software that requires it.

%package devel
Summary: Libraries, includes to develop applications with %{name}.
Group: Applications/Libraries
Requires: %{name} = %{version}-%{release}

%description devel
The %{name}-devel package contains the header files and static libraries
for building applications which use %{name}.

%prep
%setup -q

%build
PATH="/opt/SUNWspro/bin:${PATH}" \
CC="cc" CXX="CC" CPPFLAGS="-I/usr/local/include" \
LD="/usr/ccs/bin/ld" \
LDFLAGS="-L/usr/local/lib -R/usr/local/lib" \
export PATH CC CXX CPPFLAGS LD LDFLAGS

./configure \
	--prefix=%{_prefix}			\
	--with-libiconv-prefix=%{_prefix}	\
	--infodir=%{_infodir}			\
	--mandir=%{_mandir}			\
	--disable-openmp
	
gmake -j3

%install
rm -rf %{buildroot}
gmake install DESTDIR=%{buildroot}

rm -rf %{buildroot}%{_libdir}/*.la
rm -rf %{buildroot}%{_libdir}/charset.alias

%clean
rm -rf %{buildroot}

%post
if [ -x %{_bindir}/install-info ] ; then
	%{_bindir}/install-info --info-dir=%{_infodir} \
		 %{_infodir}/gettext.info
fi

%preun
if [ -x %{_bindir}/install-info ] ; then
	%{_bindir}/install-info --delete --info-dir=%{_infodir} \
		 %{_infodir}/gettext.info
fi

%files
%defattr(-,root,root)
%doc README NEWS COPYING ChangeLog*
%doc AUTHORS THANKS
%doc %{_datadir}/doc/*
%{_bindir}/*
%{_libdir}/*.so*
%{_libdir}/gettext
%{_datadir}/gettext
%{_datadir}/emacs/*
%{_datadir}/locale/*
%{_infodir}/*
%{_mandir}/man1/*

%files devel
%defattr(-,root,root)
%{_includedir}/*
%{_datadir}/aclocal/*
%{_libdir}/*.a
%{_mandir}/man3/*

%changelog
* Tue Mar 10 2009 Brian Schubert <schubert@nbcs.rutgers.edu> - 0.17-6
- Fixed man, info paths
- Miscellaneous small changes
* Mon Nov 26 2007 Naveen Gavini <ngavini@nbcs.rutgers.edu> - 0.17-5
- Removed conflicting file with emacs.
* Sun Nov 18 2007 David Lee Halik <dhalik@nbcs.rutgers.edu> - 0.17-4
- Disable openmp to get rid of libmtsk requirement
* Mon Nov 12 2007 David Lee Halik <dhalik@nbcs.rutgers.edu> - 0.17-1
- Bump to 0.17
* Wed Aug 15 2007 Naveen Gavini <ngavini@nbcs.rutgers.edu> - 0.16.1-3
- Updated to new version.
* Mon May 22 2006 Leo Zhadanovsky <leozh@nbcs.rutgers.edu> - 0.14.5-1
- Updated to new version, switched to Sun CC.
