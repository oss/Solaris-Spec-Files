Summary: The GNOME control center.
Name: control-center
Version: 1.2.2
Release: 2
Group: System Environment/Libraries
Copyright: LGPL
Source: control-center-%{version}.tar.gz
BuildRoot: /var/tmp/%{name}-root
Requires: xscreensaver >= 3.00
Requires: gnome-libs >= 1.2.3
Requires: ORBit >= 0.5.3
BuildRequires: gnome-libs-devel
BuildRequires: ORBit-devel

%description
Control-center is a configuration tool for easily
setting up your GNOME environment.

GNOME is the GNU Network Object Model Environment. That's
a fancy name, but really GNOME is a nice GUI desktop 
environment. 

It's a powerful, easy to configure environment which
helps to make your computer easy to use.

%package devel
Summary: GNOME control-center development files.
Group: System Environment/Libraries
Requires: control-center

%description devel
If you're interested in developing panels for the GNOME
control center, you'll want to install this package.

Control-center-devel helps you create the 'capplets'
which are used in the control center.

%prep
%setup -q

# Solaris tar doesn't work well with long filenames, so you need to
# use gnu tar with rpm for this package.

%build
LD="/usr/ccs/bin/ld -L/usr/local/lib -R/usr/local/lib" \
   LDFLAGS="-L/usr/local/lib -R/usr/local/lib" \
   CPPFLAGS="-I/usr/local/include" ./configure --with-gnome=/usr/local \
   --enable-shared --enable-static --with-gtk-prefix=/usr/local \
   --with-esd-prefix=/usr/local --with-imlib-prefix=/usr/local \
   --sysconfdir=/etc
make

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/local
make install prefix=$RPM_BUILD_ROOT/usr/local sysconfdir=$RPM_BUILD_ROOT/etc
mv $RPM_BUILD_ROOT/etc/CORBA/servers/gnomecc.gnorba \
   $RPM_BUILD_ROOT/etc/CORBA/servers/gnomecc.gnorba.rpm

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,bin,bin)
%doc AUTHORS COPYING ChangeLog NEWS README
/usr/local/lib/locale/*/LC_MESSAGES/control-center.mo
/usr/local/lib/lib*.so*
/usr/local/bin/*
/usr/local/share/control-center
/usr/local/share/gnome/help/control-center
/usr/local/share/gnome/apps/Settings/*
/usr/local/share/gnome/wm-properties/*
/usr/local/share/pixmaps/*
/etc/CORBA/servers/gnomecc.gnorba.rpm

%files devel
%defattr(-,bin,bin)
/usr/local/lib/lib*a
/usr/local/lib/*.sh
/usr/local/share/idl/control-center.idl
/usr/local/include/*

