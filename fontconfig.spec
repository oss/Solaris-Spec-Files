Summary:	Font configuration and customization library
Name:		fontconfig
Version:	2.4.2
Release:	1
License:	MIT
Group:		System Environment/Libraries
Source:		http://www.fontconfig.org/release/fontconfig-%{version}.tar.gz
Distribution:	RU-Solaris
Packager:	David Lee Halik <dhalik@nbcs.rutgers.edu>
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
Requires:	%{name} = %{version}
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
	--disable-docs 

gmake


%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/local $RPM_BUILD_ROOT/usr/local/share/fonts

gmake install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post

echo -----------------------------------------------
echo NOTE: fonts.cache is not created automagically!
echo       If you so choose to create/update it you
echo       must do so with /usr/local/bin/fc-cache
echo -----------------------------------------------

%files
%defattr(-,root,other)
/usr/local/bin/*
/usr/local/etc/fonts/*
/usr/local/lib/libfontconfig.so*
/usr/local/share/fonts

%files devel
%defattr(-,root,other)
/usr/local/include/fontconfig/fcfreetype.h
/usr/local/include/fontconfig/fcprivate.h
/usr/local/include/fontconfig/fontconfig.h
/usr/local/lib/pkgconfig/fontconfig.pc
/usr/local/lib/libfontconfig.a
/usr/local/lib/libfontconfig.la

%changelog
* Tue May 29 2007 David Lee Halik <dhalik@nbcs.rutgers.edu> - 2.4.2-1
- Bumping back to 2.4.2 now that freetype is fixed
* Wed May 16 2007 David Lee Halik <dhalik@nbcs.rutgers.edu> - 2.3.95-4
- Matching whats in stable due to bugs
* Wed May 16 2007 David Lee Halik <dhalik@nbcs.rutgers.edu> - 2.4.2-1
- Bumped to 2.4.2
- Spun against new freetype

