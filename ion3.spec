Summary: The ion window manager
Name: ion3
%define preversion ds-
Version: 20060326
Release: 3
License: LGPL
Group: User Interface/X11
Source: ion-3%{preversion}%{version}.tar.gz
Source1: tkmessage
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
EXTRA_INCLUDES="-I/usr/local/include"
EXTRA_LIBS="-L/usr/local/lib -R/usr/local/lib"
export PATH EXTRA_INCLUDES EXTRA_LIBS

cp system.mk system.mk.orig
sed -e 's#^PREFIX=/usr/local#PREFIX=\$(DESTDIR)/usr/local#' system.mk > system.mk.ru.6
sed -e 's/^\(X11_PREFIX=.*\)/\#\1/' system.mk.ru.6 > system.mk.ru.5
sed -e 's/^#X11_PREFIX=\(.*\)/X11_PREFIX=\1/' system.mk.ru.5 > system.mk.ru.3
sed -e 's/^\(XINERAMA_LIBS=.*\)/\#\1/' system.mk.ru.3 > system.mk.ru.2
sed -e 's/^#\(DEFINES += -DCF_NO_XINERAMA\)$/\1/' system.mk.ru.2 > system.mk.ru.1
sed -e 's/^#\(DEFINES += -DCF_SUN_F1X_REMAP\)$/\1/' system.mk.ru.1 > system.mk.ru
cp system.mk.ru system.mk

cp config.h config.h.orig
sed -e 's/^\(#define CF_XMESSAGE\).*/\1 "tkmessage "/' config.h > config.h.ru
cp config.h.ru config.h

cd utils/ion-completefile
sed -e 's#NGROUPS#NGROUPS_MAX#' ion-completefile.c > ion-com.ru
awk '/^#include <stdlib.h>$/ {print "#include <limits.h>"}; {print}' ion-com.ru > ion-com.ru-2
mv ion-com.ru-2 ion-completefile.c
cd ../..

# The Sun F11 and F12 keys are defined as SunXK_F36 and SunXK_F37 as opposed to XK_SunF36 and XK_SunF37 like ion expects.
cd ioncore
cp conf-bindings.c conf-bindings.c.orig
sed '/XK_SunF/s/XK_SunF/SunXK_F/' < conf-bindings.c > conf-bindings.c.ru.1
awk '{print}; /keysymdef/ {print "#include <X11/Sunkeysym.h>"}' < conf-bindings.c.ru.1 > conf-bindings.c.ru
cp conf-bindings.c.ru conf-bindings.c
cd ..

gmake

%install
gmake install DESTDIR=%{buildroot}
chmod 755 %{SOURCE1}
cp %{SOURCE1} %{buildroot}/usr/local/bin

%clean
rm -rf %{buildroot}

%files
%defattr(-, root, root)
/usr/local/bin/*
/usr/local/etc/*
/usr/local/lib/*
/usr/local/share/*
