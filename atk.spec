Summary: atk
Name: atk
Version: 1.2.0
Release: 2
Copyright: GPL
Group: Applications/Editors
Source: atk-1.2.0.tar.bz2
Distribution: RU-Solaris
Vendor: NBCS-OSS
Packager: Christopher J. Suleski <chrisjs@nbcs.rutgers.edu>
BuildRoot: %{_tmppath}/%{name}-root
Requires: glib2 pango
BuildRequires: glib2-devel pango-devel pkgconfig

%description
atk

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
PATH="/usr/local/bin:$PATH"
export LD_LIBRARY_PATH PATH
CC="gcc" ./configure --prefix=/usr/local --disable-nls


%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/local
make install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,other)
/usr/local/lib/libatk-1.0.so
/usr/local/lib/libatk-1.0.so.0
/usr/local/lib/libatk-1.0.so.0.200.0

%files devel
%defattr(-,root,other)
/usr/local/include/atk-1.0
/usr/local/include/atk-1.0/atk
/usr/local/include/atk-1.0/atk/atk-enum-types.h
/usr/local/include/atk-1.0/atk/atk.h
/usr/local/include/atk-1.0/atk/atkaction.h
/usr/local/include/atk-1.0/atk/atkcomponent.h
/usr/local/include/atk-1.0/atk/atkdocument.h
/usr/local/include/atk-1.0/atk/atkeditabletext.h
/usr/local/include/atk-1.0/atk/atkgobjectaccessible.h
/usr/local/include/atk-1.0/atk/atkhyperlink.h
/usr/local/include/atk-1.0/atk/atkhypertext.h
/usr/local/include/atk-1.0/atk/atkimage.h
/usr/local/include/atk-1.0/atk/atknoopobject.h
/usr/local/include/atk-1.0/atk/atknoopobjectfactory.h
/usr/local/include/atk-1.0/atk/atkobject.h
/usr/local/include/atk-1.0/atk/atkobjectfactory.h
/usr/local/include/atk-1.0/atk/atkregistry.h
/usr/local/include/atk-1.0/atk/atkrelation.h
/usr/local/include/atk-1.0/atk/atkrelationset.h
/usr/local/include/atk-1.0/atk/atkrelationtype.h
/usr/local/include/atk-1.0/atk/atkselection.h
/usr/local/include/atk-1.0/atk/atkstate.h
/usr/local/include/atk-1.0/atk/atkstateset.h
/usr/local/include/atk-1.0/atk/atkstreamablecontent.h
/usr/local/include/atk-1.0/atk/atktable.h
/usr/local/include/atk-1.0/atk/atktext.h
/usr/local/include/atk-1.0/atk/atkutil.h
/usr/local/include/atk-1.0/atk/atkvalue.h
/usr/local/lib/pkgconfig
/usr/local/lib/pkgconfig/atk.pc

%files doc
%defattr(-,root,other)
/usr/local/share/gtk-doc/html/atk
/usr/local/share/gtk-doc/html/atk/atk-atkaction.html
/usr/local/share/gtk-doc/html/atk/atk-atkcomponent.html
/usr/local/share/gtk-doc/html/atk/atk-atkdocument.html
/usr/local/share/gtk-doc/html/atk/atk-atkeditabletext.html
/usr/local/share/gtk-doc/html/atk/atk-atkhypertext.html
/usr/local/share/gtk-doc/html/atk/atk-atkimage.html
/usr/local/share/gtk-doc/html/atk/atk-atkselection.html
/usr/local/share/gtk-doc/html/atk/atk-atkstate.html
/usr/local/share/gtk-doc/html/atk/atk-atkstreamablecontent.html
/usr/local/share/gtk-doc/html/atk/atk-atktable.html
/usr/local/share/gtk-doc/html/atk/atk-atktext.html
/usr/local/share/gtk-doc/html/atk/atk-atkvalue.html
/usr/local/share/gtk-doc/html/atk/atk.html
/usr/local/share/gtk-doc/html/atk/atkgobjectaccessible.html
/usr/local/share/gtk-doc/html/atk/atkhyperlink.html
/usr/local/share/gtk-doc/html/atk/atknoopobject.html
/usr/local/share/gtk-doc/html/atk/atknoopobjectfactory.html
/usr/local/share/gtk-doc/html/atk/atkobject.html
/usr/local/share/gtk-doc/html/atk/atkobjectfactory.html
/usr/local/share/gtk-doc/html/atk/atkregistry.html
/usr/local/share/gtk-doc/html/atk/atkrelation.html
/usr/local/share/gtk-doc/html/atk/atkrelationset.html
/usr/local/share/gtk-doc/html/atk/atkstateset.html
/usr/local/share/gtk-doc/html/atk/atkutil.html
/usr/local/share/gtk-doc/html/atk/book1.html
/usr/local/share/gtk-doc/html/atk/index.sgml

