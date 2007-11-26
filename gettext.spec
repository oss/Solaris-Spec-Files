Summary:        Internationalization Tools
Name:           gettext
Version:        0.17
Release:        5
Copyright:      GPL
Group:          Development/Tools
Source:         %{name}-%{version}.tar.gz
Distribution:   RU-Solaris
Vendor:         NBCS-OSS
Packager:       Naveen Gavini <ngavini@nbcs.rutgers.edu>
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
Requires: %{name} = %{version}

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
	--prefix=/usr/local \
	--with-libiconv-prefix=/usr/local \
	--disable-openmp
	
gmake -j3

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/local
gmake install DESTDIR=$RPM_BUILD_ROOT

rm -rf %{buildroot}/usr/local/lib/*.la
rm -rf %{buildroot}/usr/local/lib/charset.alias

%clean
rm -rf $RPM_BUILD_ROOT

%post
if [ -x /usr/local/bin/install-info ] ; then
	/usr/local/bin/install-info --info-dir=/usr/local/info \
		 /usr/local/share/info/gettext.info
fi

%preun
if [ -x /usr/local/bin/install-info ] ; then
	/usr/local/bin/install-info --delete --info-dir=/usr/local/info \
		 /usr/local/share/info/gettext.info
fi

%files
%defattr(-,root,root)
%doc COPYING
/usr/local/bin/*
/usr/local/lib/*.so*
/usr/local/share/aclocal/*
/usr/local/share/doc/*
/usr/local/share/emacs/*
/usr/local/share/gettext/*
/usr/local/share/info/autosprintf.info
/usr/local/share/info/gettext.info
/usr/local/share/locale/*
/usr/local/share/man/*
/usr/local/lib/gettext/*
#/usr/local/lib/charset.alias

%files devel
%defattr(-,root,root)
/usr/local/include/*
/usr/local/lib/libintl.a
/usr/local/lib/libasprintf.a
/usr/local/lib/libgettextpo.a

%changelog
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
