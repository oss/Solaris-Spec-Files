Summary: Extended twm
Name: ctwm
Version: 3.5.2
Release: 2
Group: User Interface/X
License: BSD-type
Source: ctwm-%{version}.tar.gz
BuildRoot: /var/tmp/%{name}-root
BuildRequires: xpm
Requires: xpm

%description
    CTWM is an extension to twm, that support multiple virtual
screens, and a lot of other goodies.

    You can use and manage up to 32 virtual screens called workspaces.
You swap from one workspace to another by clicking on a button in an
optionnal panel of buttons (the workspace manager) or by invoking a
function.

    You can custom each workspace by choosing different colors, names
and pixmaps for the buttons and background root windows.

    Main features are :

        - Optional 3D window titles and border (ala Motif).
        - Shaped, colored icons.
        - Multiple icons for clients based on the icon name.
        - Windows can belong to several workspaces.
        - A map of your workspaces to move quickly windows between
          different workspaces.
        - Animations : icons, root backgrounds and buttons can be 
          animated.
        - Pinnable and sticky menus.
        - etc...

%prep
%setup -q

%build
xmkmf -a
make CCOPTIONS="-I/usr/local/include" LINTOPTS="" \
     EXTRA_LDOPTIONS="-L/usr/local/lib -R/usr/local/lib"

%install
rm -rf $RPM_BUILD_ROOT

for i in local/bin openwin/lib/X11/twm/images local/man/man1 ; do
    mkdir -p $RPM_BUILD_ROOT/usr/$i
done

install -m 0755 ctwm $RPM_BUILD_ROOT/usr/local/bin
install -m 0444 system.ctwmrc \
        $RPM_BUILD_ROOT/usr/openwin/lib/X11/twm/system.twmrc.rpm
for i in xpm/?* ; do
    install -m 0644 $i $RPM_BUILD_ROOT/usr/openwin/lib/X11/twm/images
done
install -m 0644 ctwm.man $RPM_BUILD_ROOT/usr/local/man/man1/ctwm.1

%clean
rm -rf $RPM_BUILD_ROOT

%post
cat <<EOF

You need to move /usr/openwin/lib/X11/twm/system.twmrc.rpm to
/usr/openwin/lib/X11/twm/system.twmrc.

EOF

%files
%defattr(-,bin,bin)
/usr/local/bin/ctwm
/usr/local/man/man1/ctwm.1
/usr/openwin/lib/X11/twm
