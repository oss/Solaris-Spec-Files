Name: pango
Version: 1.8.0
Release: 1
Copyright: LGPL
Group: System Environment/Libraries
Source: %{name}-%{version}.tar.bz2
Distribution: RU-Solaris
Vendor: NBCS-OSS
Packager: Christopher J. Suleski <chrisjs@nbcs.rutgers.edu>
Summary: System for layout and rendering of internationalized text.
BuildRoot: %{_tmppath}/%{name}-root
# -assuming system has necessary X libraries pre-installed
Requires: glib2 >= 2.6.4
Requires: freetype2 >= 2.1.4 xft2 >= 2.1.2
BuildRequires: libtool >= 1.4.3
BuildRequires: glib2-devel >= 2.6.4
BuildRequires: pkgconfig >= 0.15.0
BuildRequires: freetype2-devel >= 2.1.4
BuildRequires: xft2-devel >= 2.1.2
BuildRequires: fontconfig-devel >= 2.2.0

%description
Pango is a system for layout and rendering of internationalized text.

%package devel
Summary: System for layout and rendering of internationalized text.
Requires: %{name} = %{version}
Requires: glib2-devel >= 2.6.4
Requires: freetype2-devel >= 2.1.4
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
LDFLAGS="-L/usr/local/lib -R/usr/local/lib -L/usr/sfw/lib -R/usr/sfw/lib"
LD_LIBRARY_PATH="/usr/local/lib:/usr/sfw/lib"
LD_RUN_PATH="/usr/local/lib:/usr/sfw/lib"
CC="gcc"
PATH="/usr/local/lib:/usr/sfw/bin:$PATH"
export CPPFLAGS LDFLAGS LD_LIBRARY_PATH LD_RUN_PATH CC PATH

./configure --prefix=/usr/local --disable-nls --disable-rebuilds --enable-freetype
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
/usr/local/man/man1/pango-querymodules.1

%files devel
%defattr(-,root,other)
/usr/local/include/pango-1.0/pango/*
/usr/local/lib/pkgconfig/

%files doc
%defattr(-,root,other)
/usr/local/share/gtk-doc/html/pango/*

%changelog
* Wed May 20 2005 Jonathan Kaczynski - <jmkacz@nbcs.rutgers.edu>
- Upgraded to latest release