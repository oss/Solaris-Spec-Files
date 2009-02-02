Summary:	Font configuration and customization library
Name:		fontconfig
Version:	2.6.0
Release:	3
License:	MIT
Group:		System Environment/Libraries
Source:		http://www.fontconfig.org/release/fontconfig-%{version}.tar.gz
Distribution:	RU-Solaris
Packager:	Brian Schubert <schubert@nbcs.rutgers.edu>
Vendor:		NBCS-OSS
BuildRoot:	%{_tmppath}/%{name}-root
Requires:	freetype2 >= 2.3.5
BuildRequires:	freetype2-devel >= 2.3.5, expat-devel

%description
Fontconfig is designed to locate fonts within the
system and select them according to requirements specified by
applications.

%package devel
Summary:	Font configuration and customization library
Group:		Development/Libraries 
Requires:	%{name} = %{version}-%{release}
Requires:	freetype2-devel >= 2.3.5

%description devel
The fontconfig-devel package includes the header files,
and developer docs for the fontconfig package.

Install fontconfig-devel if you want to develop programs which
will use fontconfig.

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
	--disable-nls \
	--enable-expat \
	--with-add-fonts=/usr/openwin/lib/X11/fonts \
	--disable-docs \
	--disable-static

gmake -j3


%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{_datadir}/fonts

gmake install DESTDIR=%{buildroot}

rm -f %{buildroot}%{_libdir}/libfontconfig.la


%clean
rm -rf %{buildroot}

%post

echo -----------------------------------------------
echo NOTE: fonts.cache is not created automagically!
echo       If you so choose to create/update it you
echo       must do so with /usr/local/bin/fc-cache
echo -----------------------------------------------

%files
%doc README NEWS AUTHORS COPYING ChangeLog
%defattr(-,root,other)
%{_bindir}/*
%{_sysconfdir}/fonts/*
%{_libdir}/libfontconfig.so*
%{_datadir}/fonts

%files devel
%defattr(-,root,other)
%{_includedir}/fontconfig
%{_libdir}/pkgconfig/fontconfig.pc

%changelog
* Mon Feb 02 2009 Brian Schubert <schubert@nbcs.rutgers.edu> - 2.6.0-3
- Removed libfontconfig.la again (causes problems when building some packages)
- No longer build static libraries
* Thu Aug 21 2008 Brian Schubert <schubert@nbcs.rutgers.edu> - 2.6.0-2
- Put back libfontconfig.la (seems to be needed)
* Fri Aug 15 2008 Brian Schubert <schubert@nbcs.rutgers.edu> - 2.6.0-1
- Added doc entry and updated to 2.6.0
* Tue May 27 2008 Brian Schubert <schubert@nbcs.rutgers.edu> - 2.5.93-1
- Updated to 2.5.93
* Tue Dec 11 2007 David Lee Halik <dhalik@nbcs.rutgers.edu> - 2.5.0-1
- Bump to 2.5
* Tue May 29 2007 David Lee Halik <dhalik@nbcs.rutgers.edu> - 2.4.2-1
- Bumping back to 2.4.2 now that freetype is fixed
* Wed May 16 2007 David Lee Halik <dhalik@nbcs.rutgers.edu> - 2.3.95-4
- Matching whats in stable due to bugs
* Wed May 16 2007 David Lee Halik <dhalik@nbcs.rutgers.edu> - 2.4.2-1
- Bumped to 2.4.2
- Spun against new freetype

