Summary: Midnight Commander visual shell
Name: mc
Version: 4.5.51
Release: 3
Group: System Environment/Shells
Copyright: GPL
Source: mc-4.5.51.tar.gz
BuildRoot: /var/tmp/%{name}-root
BuildRequires: gnome-applets

%description
Midnight Commander is a visual shell much like a file manager, only with way
more features.  It is text mode, but also includes mouse support if you are
running GPM.  Its coolest feature is the ability to ftp, view tar, zip
files, and poke into RPMs for specific files.  :-)

%package -n gmc
Summary:  Midnight Commander visual shell (GNOME version)
Requires: mc >= 4.5.51
Requires: gnome-libs >= 1.2.3
Group:    User Interface/Desktops

%description -n gmc
Midnight Commander is a visual shell much like a file manager, only with
way more features.  This is the GNOME version. Its coolest feature is the
ability to ftp, view tar, zip files and poke into RPMs for specific files.

%prep
%setup -q

%build
LDFLAGS="-L/usr/local/lib -R/usr/local/lib" \
  LD="/usr/ccs/bin/ld -L/usr/local/lib -R/usr/local/lib" \
  CPPFLAGS="-I/usr/local/include" ./configure --with-x \
  --with-gnome=/usr/local --sysconfdir=/etc
make

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/local
make install prefix=$RPM_BUILD_ROOT/usr/local sysconfdir=$RPM_BUILD_ROOT/etc
for i in etc/mc.global etc/CORBA/servers/gmc.gnorba ; do 
    mv $RPM_BUILD_ROOT/$i $RPM_BUILD_ROOT/$i.rpm
done

%clean
rm -rf $RPM_BUILD_ROOT

%post
echo You need to move /etc/mc.global.rpm .

%post -n gmc
echo You need to move /etc/CORBA/servers/gmc.gnorba.rpm .

%files
%defattr(-,bin,bin)
%doc FAQ COPYING NEWS README
/usr/local/lib/locale/*/LC_MESSAGES/mc.mo
/usr/local/bin/mc
/usr/local/bin/mcmfmt
/usr/local/bin/mcedit
/usr/local/man/man1/*
/etc/mc.global.rpm
/usr/local/lib/mc

%files -n gmc
%defattr(-,bin,bin)
/usr/local/bin/plain-gmc
/usr/local/bin/gmc
/usr/local/bin/gmc-client
/usr/local/share/pixmaps/mc/*
/usr/local/share/idl/FileManager.idl
/usr/local/share/mime-info/mc.keys
/usr/local/share/gnome/help/gmc/*
/etc/CORBA/servers/gmc.gnorba.rpm
