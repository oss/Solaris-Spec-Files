%include machine-header.spec

Summary: GTK+ binding for librep Lisp environment
Name: rep-gtk
Version: 0.15
Release: 6
Group: Development/Languages
Copyright: GPL
Source: rep-gtk-%{version}.tar.gz
BuildRoot: /var/tmp/%{name}-root
Requires: librep >= 0.12.4, gtk+ >= 1.2, gnome-libs >= 1.2.3, libglade
Requires: db
BuildRequires: librep-devel gtk+-devel libglade-devel db

%description
This is a binding of GTK+ for the librep Lisp interpreter. It is based
on Marius Vollmer's guile-gtk package (initially version 0.15, updated
to 0.17), with a new glue-code generator.

%prep
%setup -q

%build
LD="/usr/ccs/bin/ld -L/usr/local/lib -R/usr/local/lib -R/usr/ucblib" \
    LDFLAGS="-L/usr/local/lib -R/usr/local/lib -R/usr/ucblib" \
    CPPFLAGS="-I/usr/local/include" ./configure --with-rep=/usr/local/ \
    --with-gnome --with-libglade-config=/usr/local/bin/libglade-config \
    --with-gdk-pixbuf-prefix=/usr/local --with-gtk-prefix=/usr/local
make 'rep_DL_LD=$(rep_LIBTOOL) --mode=link $(CC) -avoid-version -module -rpath $(rpath_repcommonexecdir)'


%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/local
make install installdir=$RPM_BUILD_ROOT/usr/local/libexec/rep/%{sparc_arch}
cd $RPM_BUILD_ROOT/usr/local/libexec/rep/%{sparc_arch}/gui
ln -s gnome/ui.so gnome.so
ln -s gnome/ui.la gnome.la
ln -s gtk/gtk.so gtk.so
ln -s gtk/gtk.la gtk.la

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,bin,bin)
/usr/local/libexec/rep/%{sparc_arch}/*
