Name: pango
Version: 1.10.3
Release: 1
Copyright: LGPL
Group: System Environment/Libraries
Source: %{name}-%{version}.tar.bz2
Distribution: RU-Solaris
Vendor: NBCS-OSS
Packager: Leo Zhadanovsky <leozh@nbcs.rutgers.edu>
Summary: System for layout and rendering of internationalized text.
BuildRoot: %{_tmppath}/%{name}-root
# -assuming system has necessary X libraries pre-installed
Requires: glib2 >= 2.8.6
Requires: fontconfig >= 2.2.0
Requires: freetype2 >= 2.1.10 xft2 >= 2.1.7
BuildRequires: libtool >= 1.4.3
BuildRequires: glib2-devel >= 2.8.6
BuildRequires: pkgconfig >= 0.15.0
BuildRequires: freetype2-devel >= 2.1.10
BuildRequires: xft2-devel >= 2.1.7
BuildRequires: fontconfig-devel >= 2.2.0

%description
Pango is a system for layout and rendering of internationalized text.

%package devel
Summary: System for layout and rendering of internationalized text.
Requires: %{name} = %{version}
Requires: glib2-devel >= 2.8.6
Requires: freetype2-devel >= 2.1.10
Requires: fontconfig-devel >= 2.2.0
Group: Development/Libraries
%description devel
The pango-devel package includes the header files and
developer docs for the pango package.

%package doc
Summary: %{name} extra documentation
Requires: %{name}
Group: Documentation
%description doc
%{name} extra documentation

%prep
%setup -q -n %{name}-%{version}

%build
#LDFLAGS="-L/usr/local/lib -R/usr/local/lib -L/usr/sfw/lib -R/usr/sfw/lib"
#LD_LIBRARY_PATH="/usr/local/lib:/usr/sfw/lib"
#LD_RUN_PATH="/usr/local/lib:/usr/sfw/lib"
#CC="gcc"
#PATH="/usr/local/bin:/usr/ccs/bin:/usr/sfw/bin:$PATH"
#export CPPFLAGS LDFLAGS LD_LIBRARY_PATH LD_RUN_PATH CC PATH

PATH="/opt/SUNWspro/bin:${PATH}" \
CC="cc" CXX="CC" CPPFLAGS="-I/usr/local/include" \
LD="/usr/ccs/bin/ld" \
LDFLAGS="-L/usr/local/lib -R/usr/local/lib" \
export PATH CC CXX CPPFLAGS LD LDFLAGS

# --diable-gtk-doc just copies over existing documentation files, instead of creating new ones
./configure --prefix=/usr/local --disable-nls --disable-rebuilds --disable-gtk-doc
make

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/local
make install DESTDIR=$RPM_BUILD_ROOT
/usr/ccs/bin/strip $RPM_BUILD_ROOT/usr/local/bin/* \
$RPM_BUILD_ROOT/usr/local/lib/*.so*
# Remove files that should not be packaged
rm $RPM_BUILD_ROOT/usr/local/lib/pango/1.4.0/modules/*.la
rm $RPM_BUILD_ROOT/usr/local/lib/*.la

%post
echo Running pango-querymodules...
/usr/local/bin/pango-querymodules > /usr/local/etc/pango/pango.modules

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,other)
/usr/local/etc/pango/pangox.aliases
/usr/local/bin/pango-querymodules
/usr/local/lib/libpango*.so*
/usr/local/lib/pango/1.4.0/modules/*
/usr/local/man/man1/pango-querymodules.1

%files devel
%defattr(-,root,other)
/usr/local/include/pango-1.0/pango/*
/usr/local/lib/pkgconfig/*

%files doc
%defattr(-,root,other)
/usr/local/share/gtk-doc/html/pango/*

%changelog
* Wed Jun 29 2005 Jonathan Kaczynski <jmkacz@nbcs.rutgers.edu> - 1.9.0-6
- Changed /usr/local/lib to /usr/local/bin in the PATH

* Fri Jun 24 2005 Jonathan Kaczynski <jmkacz@nbcs.rutgers.edu> - 1.9.0-5
- Added a line to the %files section to include some unpackaged files

* Wed Jun 22 2005 Jonathan Kaczynski <jmkacz@nbcs.rutgers.edu> - 1.9.0-4
- switched back to gcc; see glib2.spec for the reason

* Mon Jun 06 2005 Jonathan Kaczynski <jmkacz@nbcs.rutgers.edu> - 1.9.0-3
- changed gcc to cc

* Wed May 20 2005 Jonathan Kaczynski - <jmkacz@nbcs.rutgers.edu> - 1.9.0-1
- Upgraded to latest release
