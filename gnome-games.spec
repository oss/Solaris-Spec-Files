Summary: GNOME games.
Name: gnome-games
Version: 1.2.0
Release: 2
Group: Amusements/Games
Copyright: GPL
Source: %{name}-%{version}.tar.gz
BuildRoot: /var/tmp/%{name}-root
Requires: gnome-libs
BuildRequires: gnome-libs-devel gnome-applets

%description
GNOME (GNU Network Object Model Environment) is a user-friendly set of
applications and desktop tools to be used in conjunction with a window
manager for the X Window System.  GNOME is similar in purpose and
scope to CDE and KDE, but GNOME is based completely on free software.
The gnome-games package containes a collection of simple games for
your amusement.

You should install the gnome-games package if you would like to play
the included games. You will also need to install the gnome-libs
package.  If you would like to develop addtional games that utilize
the GNOME games libraries then you should install the
gnome-games-devel package.

If you want high scores to work properly, you should create a new user
- games - and run the following commands in sh:

 GAMES="glines gnibbles gnobots2 gnome-stones gnome-xbill gnometris
        gnomine gnotravex gnotski gtali gturing iagno mahjongg same-gnome"
 chgrp games $GAMES
 chmod 2111 $GAMES
 rpm -q gnome-games -l | grep "var/games" | xargs chown games.games

%package devel
Summary:	GNOME games development libraries.
Group: 		Development/Libraries
Requires:	gnome-games

%description devel
GNOME (GNU Network Object Model Environment) is a user-friendly set of
applications and desktop tools to be used in conjunction with a window
manager for the X Window System.  GNOME is similar in purpose and
scope to CDE and KDE, but GNOME is based completely on free software.
The gnome-games-devel package contains the libraries and include files
needed for development of GNOME games.

You should install the gnome-games package if you would like to play
the included games. You will also need to install the gnome-libs
package.  If you would like to develop addtional games that utilize
the GNOME games libraries then you should install the
gnome-games-devel package.

%prep
%setup -q

%build
./configure --prefix=/usr/local
make

%install
build_dir=`pwd`
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/local
make install prefix=$RPM_BUILD_ROOT/usr/local

%clean
rm -rf $RPM_BUILD_ROOT

%post
cat <<EOF

If you want high scores to work properly, you should create a new user
- games - and run the following commands in sh:

 GAMES="glines gnibbles gnobots2 gnome-stones gnome-xbill gnometris
        gnomine gnotravex gnotski gtali gturing iagno mahjongg same-gnome"
 chgrp games $GAMES
 chmod 2111 $GAMES
 rpm -q gnome-games -l | grep "var/games" | xargs chown games.games

EOF

%files devel
%defattr(-,bin,bin)
/usr/local/lib/*a
/usr/local/lib/gnome-stones/objects/*a
/usr/local/include/*

%files
%defattr(-,bin,bin)
%config /usr/local/etc/sound/events/*
/usr/local/var/games/*
/usr/local/bin/*
/usr/local/share/gnome-stonesrc
/usr/local/share/gnome-stonesrc.ko
/usr/local/share/gnibbles/*
/usr/local/share/xbill/*
/usr/local/share/sol-games/*
/usr/local/share/mime-info/*
/usr/local/share/gnome-stones/*
/usr/local/share/sounds/*
/usr/local/share/gnobots2/*
/usr/local/share/gturing/*
/usr/local/share/gnome/help/*
/usr/local/share/gnome/apps/Games/*
/usr/local/share/pixmaps/*
/usr/local/lib/lib*.so*
/usr/local/lib/gnome-stones/objects/lib*.so*
/usr/local/lib/locale/*/LC_MESSAGES/*.mo
