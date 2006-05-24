Summary: The ion window manager
Name: ion3
%define preversion ds-
Version: 20060519
Release: 1
License: LGPL
Group: User Interface/X11
Source: ion-3%{preversion}%{version}.tar.gz
Source1: tkmessage
Source2: Xsession.ion3
Source3: Xinitrc.ion3
Source4: Xresources.ion3
Patch: Sun_Xinerama.diff
Patch1: ion3_post_release_changes.diff
Packager: Etan Reisner <deryni@jla.rutgers.edu>
BuildRoot: /var/tmp/%{name}-root
BuildRequires: lua >= 5.1, gcc, make
Requires: lua >= 5.1

%description
%{summary}

%prep
%setup -q -n ion-3%{preversion}%{version}
%patch -p1
%patch1 -p1

%build
CC=/opt/SUNWspro/bin/cc
PATH=/usr/local/gnu/bin:/opt/SUNWspro/bin:/usr/ccs/bin:$PATH
EXTRA_INCLUDES="-I/usr/local/include"
EXTRA_LIBS="-L/usr/local/lib -R/usr/local/lib"
export PATH EXTRA_INCLUDES EXTRA_LIBS

cp system.mk system.mk.orig
sed -e 's/^CC=gcc/CC=cc/' system.mk > system.mk.ru.10
sed -e 's/^\(CFLAGS=-g \)-Os \$(WARN)\(.*\)/\1-xO2 \2/' system.mk.ru.10 > system.mk.ru.9
sed -e 's/^\(LDFLAGS=-g \)-Os\(.*\)/\1-xO2 \2/' system.mk.ru.9 > system.mk.ru.8
sed -e 's/^EXPORT_DYNAMIC=.*/EXPORT_DYNAMIC=/' system.mk.ru.8 > system.mk.ru.7
sed -e 's#^PREFIX=/usr/local#PREFIX=\$(DESTDIR)/usr/local#' system.mk.ru.7 > system.mk.ru.6
sed -e 's/^\(X11_PREFIX=\/usr\/X11R6\)/#\1/' system.mk.ru.6 > system.mk.ru.5
sed -e 's/^#X11_PREFIX=\/usr\/op\(.*\)/X11_PREFIX=\1/' system.mk.ru.5 > system.mk.ru.3
sed -e 's/^\(XINERAMA_LIBS=.*\)/\#\1/' system.mk.ru.3 > system.mk.ru.2
sed -e 's/^\(DEFINES += -DCF_XINERAMA\)$/#\1/' system.mk.ru.2 > system.mk.ru.2.foo
sed -e 's/^#\(XINERAMA_LIBS=\)$/\1/' system.mk.ru.2.foo > system.mk.ru.2.bar
sed -e 's/^#\(DEFINES += -DCF_SUN_XINERAMA\)/\1/' system.mk.ru.2.bar > system.mk.ru.1
sed -e 's/^#\(DEFINES += -DCF_SUN_F1X_REMAP\)$/\1/' system.mk.ru.1 > system.mk.ru
cp system.mk.ru system.mk

cp rules.mk rules.mk.orig
sed -e 's/^CC_PICFLAGS=.*/CC_PICFLAGS=-xcode=pic32/' rules.mk > rules.mk.ru.1
sed -e 's/^LD_SHAREDFLAGS=-shared/LD_SHAREDFLAGS=-G/' rules.mk.ru.1 > rules.mk.ru
cp rules.mk.ru rules.mk

cp ion/Makefile ion/Makefile.orig
sed -e 's/^WHOLEA =.*/WHOLEA =/' ion/Makefile > ion/Makefile.ru.1
sed -e 's/^NO_WHOLEA = .*/NO_WHOLEA =/' ion/Makefile.ru.1 > ion/Makefile.ru
cp ion/Makefile.ru ion/Makefile

cp pwm/Makefile pwm/Makefile.orig
sed -e 's/^WHOLEA =.*/WHOLEA =/' pwm/Makefile > pwm/Makefile.ru.1
sed -e 's/^NO_WHOLEA = .*/NO_WHOLEA =/' pwm/Makefile.ru.1 > pwm/Makefile.ru
cp pwm/Makefile.ru pwm/Makefile

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
mkdir -p %{buildroot}/usr/local/etc/dt/config
cp %{SOURCE2} %{buildroot}/usr/local/etc/dt/config
cp %{SOURCE3} %{buildroot}/usr/local/etc/dt/config
mkdir -p %{buildroot}/usr/local/etc/dt/config/C/Xresources.d
cp %{SOURCE4} %{buildroot}/usr/local/etc/dt/config/C/Xresources.d

%clean
rm -rf %{buildroot}

%files
%defattr(-, root, root)
/usr/local/bin/*
/usr/local/etc/*
/usr/local/lib/*
/usr/local/share/*
