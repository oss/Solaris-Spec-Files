%include machine-header.spec

Summary: An extensible window manager for the X Window System.
Name: sawfish
Version: 0.34
Release: 2
Group: User Interface/Desktops
Copyright: GPL
Source: sawfish-%{version}.tar.gz
Patch: sawfish.patch
BuildRoot: /var/tmp/%{name}-root
Requires: librep >= 0.12, rep-gtk >= 0.13
BuildRequires: librep-devel >= 0.12, rep-gtk >= 0.13
BuildRequires: autoconf gnome-applets

%description
Sawfish is an extensible window manager which uses a Lisp-based
scripting language.  All window decorations are configurable and the
basic idea is to have as much user-interface policy as possible
controlled through the Lisp language.  Configuration can be
accomplished by writing Lisp code in a personal .sawfishrc file, or
using a GTK+ interface.  Sawfish is mostly GNOME compliant

%package themer
Summary: A GUI for creating sawfish window manager themes.
Group: User Interface/Desktops
Requires: %{name}, rep-gtk

%description themer
The sawfish-themer package contains an optional theme builder for the
sawfish window manager. sawfish-themer allows static window themes to
be created and edited in a graphical environment.

%prep
%setup -q
%patch

%build
autoconf
LDFLAGS="-L/usr/local/lib -R/usr/local/lib" \
 LD="/usr/ccs/bin/ld -L/usr/local/lib -R/usr/local/lib" \
 CPPFLAGS="-I/usr/local/include" ./configure --with-rep-prefix=/usr/local \
 --with-imlib-prefix=/usr/local --with-gtk-prefix=/usr/local \
 --with-audiofile --with-esd --enable-capplet --enable-themer --with-readline
make

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/local/share/gnome/wm-properties
mkdir -p $RPM_BUILD_ROOT/usr/local/share/control-center
mkdir -p $RPM_BUILD_ROOT/usr/local/share/gnome/apps/Settings
mkdir -p $RPM_BUILD_ROOT/usr/local/bin
make install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post
if [ -x /usr/local/bin/install-info ] ; then
	/usr/local/bin/install-info --info-dir=/usr/local/info \
		 /usr/local/info/sawfish.info
fi

%preun
if [ -x /usr/local/bin/install-info ] ; then
	/usr/local/bin/install-info --delete --info-dir=/usr/local/info \
		 /usr/local/info/sawfish.info
fi

%files
%defattr(-,bin,bin)
%doc README NEWS FAQ THANKS BUGS TODO
/usr/local/bin/sawfish
/usr/local/bin/sawfish-client
/usr/local/bin/sawfish-ui
/usr/local/bin/sawfish-capplet
/usr/local/share/sawfish
/usr/local/share/gnome/apps/Settings/Sawfish
/usr/local/share/gnome/wm-properties/Sawfish.desktop
/usr/local/share/pixmaps/*
/usr/local/share/control-center/Sawfish
/usr/local/share/locale/*/LC_MESSAGES
/usr/local/libexec/sawfish/%{version}/%{sparc_arch}
/usr/local/libexec/rep/%{sparc_arch}/sawfish
/usr/local/info/sawfish*

%files themer
%defattr(-,bin,bin)
/usr/local/bin/sawfish-themer
/usr/local/share/sawfish/%{version}/themer.glade
