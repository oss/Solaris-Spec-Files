Summary: the GNOME spreadsheet
Name: 		gnumeric
Version: 	0.56
Release: 3
Copyright: 	GPL
Group: 		Applications/Spreadsheets
Source: gnumeric-%{version}.tar.gz
Url:		http://www.gnome.org/gnumeric
BuildRoot:	/var/tmp/%{name}-root

Requires: gtk+ >= 1.2.7
Requires: gnome-libs >= 1.0.57
Requires: gnome-print >= 0.20
Requires: libglade >= 0.13
Requires: libxml >= 1.8.5
Requires: guile
BuildRequires:	gnome-applets

%description
GNOME (GNU Network Object Model Environment) is a user-friendly set of
applications and desktop tools to be used in conjunction with a window
manager for the X Window System.  GNOME is similar in purpose and scope
to CDE and KDE, but GNOME is based completely on free software.

This is the Gnumeric, the GNOME spreadsheet program. If you are familiar with 
Excel, you should be ready to use Gnumeric.  We have tried to clone all of 
the good features and stay as compatible as possible with Excel in terms of 
usability. Hopefully we left the bugs behind :).

%prep
%setup -q

%build
LD="/usr/ccs/bin/ld -L/usr/local/lib -R/usr/local/lib" \
  LDFLAGS="-L/usr/local/lib -R/usr/local/lib" \
  CPPFLAGS="-I/usr/local/include" ./configure --with-guile --sysconfdir=/etc \
  --prefix=/usr/local
make

%install
rm -rf $RPM_BUILD_ROOT

make prefix=$RPM_BUILD_ROOT/usr/local sysconfdir=$RPM_BUILD_ROOT/etc install

for i in `find $RPM_BUILD_ROOT/etc -type f` ; do
    mv $i $i.rpm
done

mv $RPM_BUILD_ROOT/usr/local/share/gnome/apps/Applications/gnumeric.desktop \
 $RPM_BUILD_ROOT/usr/local/share/gnome/apps/Applications/gnumeric.desktop.rpm

%post
cat <<EOF
You need to copy and move the files in /etc/CORBA/servers as well as
/usr/local/share/gnome/apps/Applications/gnumeric.desktop.rpm.
EOF

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr (0555, bin, bin)

/usr/local/bin/gnumeric
/usr/local/lib/gnumeric/%{version}/plugins/*.so
/usr/local/share/gnumeric/%{version}/glade/*.glade
/usr/local/share/gnumeric/%{version}/guile/*
/usr/local/lib/locale/*/LC_MESSAGES/*mo

%defattr (0444, bin, bin, 0555)
/usr/local/share/gnome/help/gnumeric/C/images/*
/usr/local/share/gnome/help/gnumeric/C/*.html
/usr/local/share/gnome/help/gnumeric/C/*.dat
/usr/local/share/gnome/help/gnumeric/C/docbook.css
/usr/local/share/gnome/apps/Applications/gnumeric.desktop.rpm
/usr/local/share/pixmaps/gnumeric/*
/usr/local/share/pixmaps/gnome-gnumeric.png
/usr/local/share/mime-info/gnumeric.keys
/usr/local/share/mime-info/gnumeric.mime
/usr/local/share/mc/templates/gnumeric.desktop


%defattr (0444, bin, bin, 555)
# This should go in a devel package...
/usr/local/share/idl/*.idl
/etc/CORBA/servers/gnumeric.gnorba.rpm
%doc HACKING AUTHORS ChangeLog NEWS README COPYING TODO
