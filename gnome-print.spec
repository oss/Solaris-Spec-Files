Summary: Gnome Print - Printing libraries for GNOME.
Name: 		gnome-print
Version: 	0.20
Release: 3
Copyright: 	LGPL
Group: 		System Environment/Base
Source: gnome-print-%{version}.tar.gz
BuildRoot: 	/var/tmp/gnome-print-root
Requires: 	gnome-libs >= 1.0
Requires:       gs-fonts >= 4.03
BuildRequires:  gnome-libs-devel

%description
GNOME (GNU Network Object Model Environment) is a user-friendly set of
applications and desktop tools to be used in conjunction with a window
manager for the X Window System.  GNOME is similar in purpose and scope
to CDE and KDE, but GNOME is based completely on free software.
The gnome-print package contains libraries and fonts that are needed by
GNOME applications wanting to print.

You should install the gnome-print package if you intend on using any of
the GNOME applications that can print. If you would like to develop GNOME
applications that can print you will also need to install the gnome-print
devel package.

%package devel
Summary: Libraries and include files for developing GNOME applications.
Group: 		Development/Libraries

%description devel
GNOME (GNU Network Object Model Environment) is a user-friendly set of
applications and desktop tools to be used in conjunction with a window
manager for the X Window System.  GNOME is similar in purpose and scope
to CDE and KDE, but GNOME is based completely on free software.
The gnome-print-devel package includes the libraries and include files that
you will need when developing applications that use the GNOME printing 
facilities.

You should install the gnome-print-devel package if you would like to 
develop GNOME applications that will use the GNOME printing facilities.
You don't need to install the gnome-print-devel package if you just want 
to use the GNOME desktop enviornment.

%prep
%setup -q

%build
LD="/usr/ccs/bin/ld -L/usr/local/lib -R/usr/local/lib" \
 LDFLAGS="-L/usr/local/lib -R/usr/local/lib" CPPFLAGS="-I/usr/local/include" \
 ./configure
make

%install
rm -rf $RPM_BUILD_ROOT

make prefix=$RPM_BUILD_ROOT/usr/local install
# This is ugly
#
cd fonts
install -c *.font $RPM_BUILD_ROOT/usr/local/share/fonts

%clean
rm -rf $RPM_BUILD_ROOT

%post
/usr/local/bin/gnome-font-install --system --scan --no-copy \
        --afm-path=/usr/local/share/fonts/afms \
        --pfb-path=/usr/local/share/fonts/pfbs \
        --pfb-assignment=ghostscript,/usr/local/share/ghostscript/fonts \
        --afm-assignment=ghostscript,/usr/local/share/ghostscript/fonts \
        --pfb-assignment=ghostscript,/usr/local/share/fonts/default/Type1 \
        --afm-assignment=ghostscript,/usr/local/share/fonts/default/Type1 \
        /usr/local/share/fonts/
chmod 644 /usr/local/share/fonts/fontmap

%files
%defattr(-, bin, bin)

%doc AUTHORS COPYING ChangeLog NEWS README
/usr/local/lib/lib*.so.*
/usr/local/bin/*
/usr/local/lib/locale/*/*/*
/usr/local/share/fonts/afms/adobe/*
/usr/local/share/fonts/*.font
%config /usr/local/share/gnome-print/profiles/Postscript.profile

%files devel
%defattr(-, root, root)

/usr/local/lib/lib*.so
/usr/local/lib/*.a
/usr/local/lib/*.la
/usr/local/lib/*.sh
/usr/local/include/*/*
