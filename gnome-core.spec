Summary: The core programs for the GNOME GUI desktop environment
Name: gnome-core
Version: 1.2.4
Release: 2
Group: User Interface/X
Copyright: LGPL
Source: gnome-core-%{version}.tar.gz
Patch: gnome-core.patch
BuildRoot: /var/tmp/%{name}-root
Requires: gnome-libs >= 1.2.8
Requires: ORBit >= 0.5.5
Requires: gdk-pixbuf >= 0.7.0
BuildRequires: gnome-libs-devel >= 1.2.8
BuildRequires: ORBit-devel >= 0.5.5
BuildRequires: gdk-pixbuf-devel >= 0.7.0
BuildRequires: autoconf

%description
GNOME (GNU Network Object Model Environment) is a user-friendly
set of applications and desktop tools to be used in conjunction with a
window manager for the X Window System.  GNOME is similar in purpose and
scope to CDE and KDE, but GNOME is based completely on free
software.  The gnome-core package includes the basic programs and
libraries that are needed to install GNOME.

%package devel
Summary: GNOME core libraries, includes and more.
Group: 		Development/Libraries
Requires: 	gnome-core

%description devel
Panel libraries and header files for creating GNOME panels.

%prep
%setup -q
%patch

%build
autoconf
LD="/usr/ccs/bin/ld -L/usr/local/lib -R/usr/local/lib" \
    LDFLAGS="-L/usr/local/lib -R/usr/local/lib" \
    CPPFLAGS="-I/usr/local/include" ./configure --with-gnome=/usr/local \
    --enable-shared --enable-static --with-gtk-prefix=/usr/local \
    --with-window-manager=sawfish --sysconfdir=/etc
make

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/local
mkdir -p $RPM_BUILD_ROOT/etc
make install prefix=$RPM_BUILD_ROOT/usr/local sysconfdir=$RPM_BUILD_ROOT/etc
for i in `find $RPM_BUILD_ROOT/etc/ -type f`; do
    mv $i $i.rpm
done
find $RPM_BUILD_ROOT \! -type d -print | sed "s#^$RPM_BUILD_ROOT##" > all-files
echo "%defattr(-,bin,bin)" > REG 
echo "%defattr(-,bin,bin)" > DEV
egrep -v '/usr/local/(lib/(.*a|.*sh)|include.*|share/idl.*)$' all-files >>REG
egrep '/usr/local/(lib/(.*a|.*sh)|include.*|share/idl.*)$' all-files >>DEV

%clean
rm -rf $RPM_BUILD_ROOT

%post
cat <<EOF
I highly recommend that you install sawfish.  Without sawfish, you
will have to modify:

  /usr/local/bin/gnome-wm
  /usr/local/share/gnome/default.session
  /usr/local/share/gnome/default.wm

The sawfish rpm is compiled with GNOME support. 

You also have to move the files in /etc/CORBA/servers .
EOF


%files -f REG

%files devel -f DEV
