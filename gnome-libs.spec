Summary: The libraries needed to run the GNOME GUI desktop environment
Name: gnome-libs
Version: 1.2.8
Release: 3
Group: System Environment/Libraries
Copyright: LGPL/GPL
Source: gnome-libs-%{version}.tar.gz
Patch: gnome-libs.patch
# fixes db_185 problem
BuildRoot: /var/tmp/%{name}-root
Requires: zlib
Requires: libpng
Requires: libjpeg
Requires: esound >= 0.2.22
Requires: audiofile >= 0.1.9
BuildRequires: zlib-devel
BuildRequires: libpng
BuildRequires: libjpeg
BuildRequires: esound-devel >= 0.2.22
BuildRequires: audiofile-devel >= 0.1.9
BuildRequires: autoconf

%description
GNOME (GNU Network Object Model Environment) is a user-friendly set of
GUI applications and desktop tools to be used in conjunction with a
window manager for the X Window System.  The gnome-libs package
includes libraries that are needed to run GNOME.

%package devel
Summary: Libraries and include files for developing GNOME applications.
Group: Development/Libraries
Requires: gnome-libs = %{version}

%description devel
GNOME (GNU Network Object Model Environment) is a user-friendly set of
GUI applications and desktop tools to be used in conjunction with a
window manager for the X Window System. The gnome-libs-devel package
includes the libraries and include files that you will need to develop
GNOME applications.

You should install the gnome-libs-devel package if you would like to
develop GNOME applications.  You don't need to install gnome-libs-devel
if you just want to use the GNOME desktop environment.

%prep
%setup -q
%patch

%build
autoconf
LD="/usr/ccs/bin/ld -L/usr/local/lib -R/usr/local/lib" \
    LDFLAGS="-L/usr/local/lib -R/usr/local/lib" ./configure \
    --enable-shared --enable-static --with-gtk-prefix=/usr/local \
    --with-imlib-prefix=/usr/local --with-esd-prefix=/usr/local \
    --with-audiofile-prefix=/usr/local --sysconfdir=/etc
make

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/local/
mkdir -p $RPM_BUILD_ROOT/etc
make install prefix=$RPM_BUILD_ROOT/usr/local sysconfdir=$RPM_BUILD_ROOT/etc
for i in mime-magic mime-magic.dat paper.config sound/events/gnome.soundlist \
         sound/events/gtk-events.soundlist ; do
    mv $RPM_BUILD_ROOT/etc/$i $RPM_BUILD_ROOT/etc/$i.rpm
done

%clean
rm -rf $RPM_BUILD_ROOT

%post
cat <<EOF
You have to chmod 4755 /usr/local/sbin/gnome-pty-helper
to finish the installation.  You also have to edit and move:

  /etc/mime-magic.rpm
  /etc/mime-magic.dat.rpm
  /etc/paper.config.rpm
  /etc/sound/events/gnome.soundlist.rpm
  /etc/sound/events/gtk-events.soundlist.rpm

EOF

%files
%defattr(-,bin,bin)
%doc AUTHORS COPYING COPYING.LIB ChangeLog NEWS README
/usr/local/bin/dns-helper
/usr/local/bin/gnome-dump-metadata
/usr/local/bin/gnome-moz-remote
/usr/local/bin/gconfigger
/usr/local/bin/gnome-gen-mimedb
/usr/local/bin/gnome_segv
/usr/local/bin/loadshlib
/usr/local/bin/goad-browser
/usr/local/bin/gnome-name-service
/usr/local/bin/gnome-bug
%attr(0755,root,root) /usr/local/sbin/gnome-pty-helper
/usr/local/lib/locale/*/LC_MESSAGES/gnome-libs*
/usr/local/lib/lib*.so*
/usr/local/share/doc/gnome-doc.el
/usr/local/share/doc/gnome-doc
/usr/local/share/doc/mkstub
/usr/local/share/pixmaps/*
/usr/local/share/gtkrc*
/usr/local/share/idl/*
/usr/local/share/type-convert/gnome-make-postscript-mimes
/usr/local/share/type-convert/type.convert
/usr/local/share/type-convert/postscript.convert
/usr/local/share/mime-info/gnome.mime
/etc/*.rpm
/etc/sound/events/*
/usr/local/man/man1/*
/usr/local/man/man5/*

%files devel
%defattr(-,bin,bin)
%doc devel-docs
/usr/local/bin/gnome-config
/usr/local/bin/libart-config
/usr/local/lib/lib*a
/usr/local/lib/*sh
/usr/local/lib/gnome-libs
/usr/local/include/*
/usr/local/share/aclocal/*

