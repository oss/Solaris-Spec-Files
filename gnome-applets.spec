Summary: Small applications which embed themselves in the GNOME panel
Name: gnome-applets
Version: 1.2.4
Release: 2
Group: User Interface/Desktops
Copyright: GPL
Source: gnome-applets-%{version}.tar.gz
BuildRoot: /var/tmp/%{name}-root
Requires: libxml, libgtop, libghttp, gnome-core >= 1.1.2, gdk-pixbuf >= 0.7.0
BuildRequires: libxml-devel
BuildRequires: libgtop-devel
BuildRequires: libghttp-devel
BuildRequires: gnome-core-devel
BuildRequires: gdk-pixbuf-devel

%description
GNOME (GNU Network Object Model Environment) is a user-friendly
set of applications and desktop tools to be used in conjunction with a
window manager for the X Window System.  GNOME is similar in purpose and
scope to CDE and KDE, but GNOME is based completely on Open Source
software.  The gnome-applets package provides Panel applets which
enhance your GNOME experience.

You should install the gnome-applets package if you would like embed small
utilities in the GNOME panel.

%prep
%setup -q

%build
LDFLAGS="-L/usr/local/lib -R/usr/local/lib" \
   LD="/usr/ccs/bin/ld -L/usr/local/lib -R/usr/local/lib" \
   CPPFLAGS="-I/usr/local/include" ./configure --with-gnome=/usr/local \
   --with-gtk-prefix=/usr/local --with-esd-prefix=/usr/local \
   --with-libgtop=/usr/local --sysconfdir=/etc
make

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/local
make install prefix=$RPM_BUILD_ROOT/usr/local sysconfdir=$RPM_BUILD_ROOT/etc
for i in $RPM_BUILD_ROOT/etc/CORBA/servers/* ; do
    mv $i $i.rpm
done
echo "%defattr(-,bin,bin)" >FILES
find $RPM_BUILD_ROOT \! -type d | sed "s#$RPM_BUILD_ROOT##" >>FILES

%clean
rm -rf $RPM_BUILD_ROOT

%post
cat <<EOF
The following files need to be moved:

/etc/CORBA/servers/another_clock_applet.gnorba.rpm
/etc/CORBA/servers/asclock_applet.gnorba.rpm
/etc/CORBA/servers/battery_applet.gnorba.rpm
/etc/CORBA/servers/charpick_applet.gnorba.rpm
/etc/CORBA/servers/clockmail_applet.gnorba.rpm
/etc/CORBA/servers/drivemount_applet.gnorba.rpm
/etc/CORBA/servers/fifteen_applet.gnorba.rpm
/etc/CORBA/servers/geyes_applet.gnorba.rpm
/etc/CORBA/servers/gkb_applet.gnorba.rpm
/etc/CORBA/servers/jbc_applet.gnorba.rpm
/etc/CORBA/servers/life_applet.gnorba.rpm
/etc/CORBA/servers/mini-commander_applet.gnorba.rpm
/etc/CORBA/servers/quicklaunch_applet.gnorba.rpm
/etc/CORBA/servers/tickastat_applet.gnorba.rpm
/etc/CORBA/servers/webcontrol_applet.gnorba.rpm
/etc/CORBA/servers/whereami_applet.gnorba.rpm
/etc/CORBA/servers/odometer_applet.gnorba.rpm
/etc/CORBA/servers/cpumemusage_applet.gnorba.rpm
/etc/CORBA/servers/diskusage_applet.gnorba.rpm
/etc/CORBA/servers/multiload_applet.gnorba.rpm
/etc/CORBA/servers/gweather.gnorba.rpm
/etc/CORBA/servers/slash_applet.gnorba.rpm
/etc/CORBA/servers/cdplayer_applet.gnorba.rpm
/etc/CORBA/servers/mixer_applet.gnorba.rpm
/etc/CORBA/servers/sound-monitor_applet.gnorba.rpm
/etc/CORBA/servers/screenshooter_applet.gnorba.rpm
/etc/CORBA/servers/gnotes_applet.gnorba.rpm
EOF

%files -f FILES
