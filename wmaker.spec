Name: WindowMaker
Version: 0.80.0
Copyright: GPL
Group: User Interface/X
Summary: The WindowMaker window manager
Release: 4
Source: WindowMaker-%{version}.tar.bz2
BuildRoot: /var/tmp/%{name}-root
Requires: libPropList libpng3 libjpeg62 xpm libungif libtiff
BuildRequires: libPropList libpng3 libjpeg62-devel xpm libungif libtiff-devel

%description
WindowMaker is a window manager modeled on NeXT.  Install this package,
along with libPropList, libpng, and libjpeg, if you want to use
WindowMaker.

%prep
%setup -q

%build
LD="/usr/ccs/bin/ld -L/usr/local/lib -R/usr/local/lib" \
  LDFLAGS="-L/usr/local/lib -R/usr/local/lib" \
  CPPFLAGS="-I/usr/local/include" \
  ./configure --prefix=/usr/local --enable-gnome --enable-openlook
make

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/local
make install prefix=$RPM_BUILD_ROOT/usr/local
for i in $RPM_BUILD_ROOT/usr/local/etc/WindowMaker/* ; do
    mv $i $i.rpm
done

%post
cat <<EOF
To complete the WindowMaker installation you must copy the config files
in /usr/local/etc/WindowMaker.
EOF

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc COPYING
/usr/local/lib/lib*.so*
/usr/local/lib/lib*a
/usr/local/bin/*
/usr/local/include/*
/usr/local/share/WINGs/*
/usr/local/share/WindowMaker
/usr/local/etc/WindowMaker
/usr/local/GNUstep/Apps/WPrefs.app/*
/usr/local/man/man1/*
