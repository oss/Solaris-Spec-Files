Summary: pango
Name: pango
Version: 1.2.3
Release: 5
Copyright: GPL
Group: Applications/Editors
Source: pango-1.2.3.tar.bz2
Distribution: RU-Solaris
Vendor: NBCS-OSS
Packager: Christopher J. Suleski <chrisjs@nbcs.rutgers.edu>
BuildRoot: %{_tmppath}/%{name}-root
Requires: glib2 >= 2.2.2 freetype2 fontconfig
BuildRequires: glib2-devel pkgconfig freetype2 freetype2-devel fontconfig
%ifnos solaris2.7
Requires: xft2 >= 2.1.2-5
BuildRequires: xft2 >= 2.1.2-5
%endif

%description
pango

%package devel
Summary: %{name} include files, etc.
Requires: %{name}
Group: Development
%description devel
%{name} include files, etc.

%package doc
Summary: %{name} extra documentation
Requires: %{name}
Group: Documentation
%description doc
%{name} extra documentation

%prep
%setup -q

%build
LD_LIBRARY_PATH="/usr/local/lib"
LD_RUN_PATH="/usr/local/lib"
PATH="/usr/local/bin:$PATH"
export LD_LIBRARY_PATH PATH LD_RUN_PATH
CC="gcc" ./configure --prefix=/usr/local --disable-nls --disable-rebuilds --enable-freetype
make

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/local
make install DESTDIR=$RPM_BUILD_ROOT
/usr/ccs/bin/strip $RPM_BUILD_ROOT/usr/local/bin/* \
$RPM_BUILD_ROOT/usr/local/lib/*.so*

%post
echo Running pango-querymodules...
/usr/local/bin/pango-querymodules > /usr/local/etc/pango/pango.modules

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,other)
/usr/local/bin/pango-querymodules
/usr/local/etc/pango/pangox.aliases
/usr/local/lib/libpango*.so*
/usr/local/lib/pango/1.2.*/modules/pango-basic-x.so
%ifnos solaris2.7
/usr/local/lib/pango/1.2.*/modules/pango-basic-xft.so
%endif
/usr/local/lib/pango/1.2.*/modules/pango-basic-ft2.so

%files devel
%defattr(-,root,other)
/usr/local/include/pango-1.0
/usr/local/lib/pkgconfig/pango*

%files doc
%defattr(-,root,other)
/usr/local/share/gtk-doc/html/pango
