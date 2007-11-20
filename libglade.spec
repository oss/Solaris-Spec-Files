Name: libglade
Version: 2.6.2
Release: 1
Copyright: LGPL
Group: System Environment/Libraries
Source: %{name}-%{version}.tar.bz2
Distribution: RU-Solaris
Vendor: NBCS-OSS
Packager: Naveen Gavini <ngavini@nbcs.rutgers.edu>
Summary: Library for GLADE user interface builder
BuildRoot: %{_tmppath}/%{name}-root
# -assuming system has necessary X libraries pre-installed
Requires: glib2 >= 2.8.6
Requires: fontconfig >= 2.2.0
Requires: freetype2 >= 2.1.10 xft2 >= 2.1.7
Requires: gtk2 >= 2.8.12
BuildRequires: libtool >= 1.4.3
BuildRequires: glib2-devel >= 2.8.6
BuildRequires: pkgconfig >= 0.15.0
BuildRequires: freetype2-devel >= 2.1.10
BuildRequires: xft2-devel >= 2.1.7
BuildRequires: fontconfig-devel >= 2.2.0
BuildRequires: gtk2 >= 2.8.12

%description
Libglade is a library that performs a similar job to the C source output 
routines in the GLADE user interface builder. Whereas GLADE's output 
routines create C source code that must be compiled, libglade builds the 
interface from an XML file (GLADE's save format) at runtime. This can 
allow modifying the user interface without recompiling.

%package devel 
Summary: Library for GLADE user interface builder
Requires: %{name} = %{version}
Requires: glib2-devel >= 2.8.6
Requires: freetype2-devel >= 2.1.10
Requires: fontconfig-devel >= 2.2.0
Group: Development/Libraries
%description devel
The %{name}-devel package includes the header files and
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

PATH="/opt/SUNWspro/bin:${PATH}" \
CC="cc" CXX="CC" CPPFLAGS="-I/usr/local/include" \
LD="/usr/ccs/bin/ld" \
LDFLAGS="-L/usr/local/lib -R/usr/local/lib" \
export PATH CC CXX CPPFLAGS LD LDFLAGS

# --diable-gtk-doc just copies over existing documentation files, instead of creating new ones
./configure --prefix=/usr/local --disable-nls --disable-rebuilds --disable-gtk-doc
gmake

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/local
gmake install DESTDIR=$RPM_BUILD_ROOT
# Remove files that should not be packaged
rm $RPM_BUILD_ROOT/usr/local/lib/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,other)
/usr/local/bin/*
/usr/local/lib/*so*
/usr/local/lib/libglade-2.0.a
/usr/local/share/xml/*

%files devel
%defattr(-,root,other)
/usr/local/include/*
/usr/local/lib/pkgconfig/*

%files doc
%defattr(-,root,other)
/usr/local/share/gtk-doc/*

%changelog
* Mon Nov 19 2007 Dasvid Lee Halik <dhalik@nbcs.rutgers.edu> - 2.6.2
- Disabled NLS
* Tue Jun 26 2007 Naveen Gavini <ngavini@nbcs.rutgers.edu> - 2.6.1-2
- Updated to 2.6.1
* Sun Feb 26 2006 Leo Zhadanovsky <leozh@nbcs.rutgers.edu> - 2.5.1-1
- Initial Rutgers release
