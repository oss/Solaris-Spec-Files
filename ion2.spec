Summary: The ion window manager
Name: ion2
Version: 20040729
Release: 1
License: LGPL
Group: User Interface/X11
Source: ion-2_%{version}.tar.gz
Patch: ion-2_%{version}.diff
Packager: Etan Reisner <deryni@jla.rutgers.edu>
BuildRoot: /var/tmp/%{name}-root
BuildRequires: lua, gcc, make, libtool
Requires: lua

%description
%{summary}

%prep
%setup -q -n ion-2-20040729
%patch -p1

%build
PATH=/usr/local/gnu/bin:/opt/SUNWspro/bin:/usr/ccs/bin:$PATH
CC=gcc
LD=ld
EXTRA_INCLUDES="-I/usr/local/include"
EXTRA_LIBS="-L/usr/local/lib -R/usr/local/lib"
export PATH CC LD EXTRA_INCLUDES EXTRA_LIBS

mv system.mk system.mk.ORIG
sed -e "s/@@@BUILDROOT@@@/\/var\/tmp\/ion2-root/" system.mk.ORIG > system.mk
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
