Summary: pango
Name: pango
Version: 1.2.1
Release: 3
Copyright: GPL
Group: Applications/Editors
Source: pango-1.2.1.tar.bz2
Distribution: RU-Solaris
Vendor: NBCS-OSS
Packager: Christopher J. Suleski <chrisjs@nbcs.rutgers.edu>
BuildRoot: %{_tmppath}/%{name}-root
Requires: glib2
BuildRequires: glib2-devel pkgconfig

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
CC="gcc" ./configure --prefix=/usr/local --disable-nls --disable-rebuilds
make

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/local
make install DESTDIR=$RPM_BUILD_ROOT

%post
echo Running pango-querymodules...
/usr/local/bin/pango-querymodules > /usr/local/etc/pango/pango.modules

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,other)
/usr/local/bin/pango-querymodules
/usr/local/etc/pango/pangox.aliases
/usr/local/lib/libpango-1.0.so
/usr/local/lib/libpango-1.0.so.0
/usr/local/lib/libpango-1.0.so.0.200.1
/usr/local/lib/libpangox-1.0.so
/usr/local/lib/libpangox-1.0.so.0
/usr/local/lib/libpangox-1.0.so.0.200.1
/usr/local/lib/pango/1.2.0
/usr/local/lib/pango/1.2.0/modules
/usr/local/lib/pango/1.2.0/modules/pango-*.so

%files devel
%defattr(-,root,other)
/usr/local/include/pango-1.0
/usr/local/lib/pkgconfig/pango.pc
/usr/local/lib/pkgconfig/pangox.pc

%files doc
%defattr(-,root,other)
/usr/local/share/gtk-doc/html/pango
