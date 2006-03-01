Summary: The ion window manager
Name: ion3
%define preversion ds-
Version: 20060107
Release: 1
License: LGPL
Group: User Interface/X11
Source: ion-3%{preversion}%{version}.tar.gz
Patch1: libextl-mkexports-fix-for-lua5.1.diff
Patch2: mkman-fix-for-lua5.1.diff
Packager: Etan Reisner <deryni@jla.rutgers.edu>
BuildRoot: /var/tmp/%{name}-root
BuildRequires: lua, gcc, make, libtool
Requires: lua

%description
%{summary}

%prep
%setup -q -n ion-3%{preversion}%{version}

%build
PATH=/usr/local/gnu/bin:/opt/SUNWspro/bin:/usr/ccs/bin:$PATH
#CC=cc
#LD=ld
EXTRA_INCLUDES="-I/usr/local/include"
EXTRA_LIBS="-L/usr/local/lib -R/usr/local/lib"
#export PATH CC LD EXTRA_INCLUDES EXTRA_LIBS
export PATH EXTRA_INCLUDES EXTRA_LIBS

cd libextl
patch -p0 < %{PATCH1}
cd ..

cd build
patch -p0 < %{PATCH2}
cd ..

sed -e 's#^PREFIX=/usr/local#PREFIX=%{buildroot}/usr/local#' system.mk > system.mk.ru.6
sed -e 's/^\(X11_PREFIX=.*\)/\#\1/' system.mk.ru.6 > system.mk.ru.5
sed -e 's/^#X11_PREFIX=\(.*\)/X11_PREFIX=\1/' system.mk.ru.5 > system.mk.ru.4
sed -e 's/-llualib//' system.mk.ru.4 > system.mk.ru.3
sed -e 's/^\(XINERAMA_LIBS=.*\)/\#\1/' system.mk.ru.3 > system.mk.ru.2
sed -e 's/^#\(DEFINES += -DCF_NO_XINERAMA\)/\1/' system.mk.ru.2 > system.mk.ru.1
sed -e 's/^\(EXPORT_DYNAMIC=.*\)/\#\1/' system.mk.ru.1 > system.mk.ru
cp system.mk system.mk.orig
cp system.mk.ru system.mk

sed -e 's/_loadlib/_package/' libextl/luaextl.c > libextl/luaextl.c.ru
cp libextl/luaextl.c libextl/luaextl.c.orig
cp libextl/luaextl.c.ru libextl/luaextl.c

gmake

%install
gmake install

%clean
rm -rf %{buildroot}

%files
%defattr(-, root, root)
/usr/local/bin/*
/usr/local/etc/*
/usr/local/lib/*
/usr/local/share/*
