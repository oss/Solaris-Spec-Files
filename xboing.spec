Name: xboing
Version: 2.4000
Release: 2
Summary: The xboing game
Copyright: Freely distributable
Group: Amusements/Games
Source: xboing2.4.tar.gz
Patch: xboing2.4.patch
BuildRoot: /var/tmp/%{name}-root
BuildRequires: xpm >= 3.4k
BuildRequires: vpkg-SUNWaudmo
Requires: xpm >= 3.4k

%description
XBoing is an X11 game similar to Breakout.

%prep
%setup -q -n xboing
%patch -p1

%build
xmkmf -a
make CC=gcc PICFLAGS="-fpic" \
   CCOPTIONS="-O -I/usr/local/include/X11 -L/usr/local/lib -R/usr/local/lib" \
   EXTRALDOPTIONS="-L/usr/local/lib -R/usr/local/lib"

%install
umask 022
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/local/games/levels
mkdir $RPM_BUILD_ROOT/usr/local/games/sounds
touch $RPM_BUILD_ROOT/usr/local/games/.xboing.scr
chmod a+rw ./.xboing.scr
cp xboing $RPM_BUILD_ROOT/usr/local/games
for file in levels/* ; do
    [ ! -d $file ] && cp $file $RPM_BUILD_ROOT/usr/local/games/$file
done
for file in sounds/* ; do
    [ ! -d $file ] && cp $file $RPM_BUILD_ROOT/usr/local/games/$file
done

%post
cat <<EOF
Add /usr/local/games to your path.
Run
  chmod a+rw /usr/local/games/.xboing.scr
to make the high-score board function.
EOF

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,bin,bin)
%doc docs
/usr/local/games/xboing
/usr/local/games/levels
/usr/local/games/sounds




