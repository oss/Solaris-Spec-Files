Summary: GNOME Personal Information Manager
Name: gnome-pim
Version: 1.2.0
Release: 2
Group: Applications/Productivity
Copyright: GPL
Source: %{name}-%{version}.tar.gz
BuildRoot: /var/tmp/%{name}-root
Requires: gnome-libs >= 1.0.0, ORBit >= 0.4.0
BuildRequires: gnome-libs-devel gnome-applets

%description
GNOME (GNU Network Object Model Environment) is a user-friendly set of
applications and desktop tools to be used in conjunction with a window
manager for the X Window System.  GNOME is similar in purpose and scope
to CDE and KDE, but GNOME is based completely on free software.
The GNOME Personal Information Manager consists of applications to make
keeping up with your busy life easier.

Currently these apps are present:

 - gnomecal :  personal calendar and todo list
 - gnomecard:  contact list of friends and business associates




You should install the gnome-pim package if you would like to bring some
order to your life. You will also need to install the gnome-libs and ORBit
packages. If you would like to develop addtional applications for the 
Personal Information Manager suite you will need to install the 
gnome-pim-devel package.

%package devel
Summary: Libraries and include files for developing gnome-pim applications.
Group:  	Development/Libraries
Requires: 	gnome-pim = %{PACKAGE_VERSION}

%description devel 
GNOME (GNU Network Object Model Environment) is a user-friendly set of
applications and desktop tools to be used in conjunction with a window
manager for the X Window System.  GNOME is similar in purpose and scope
to CDE and KDE, but GNOME is based completely on free software.
The gnome-pim-devel package includes the libraries and include files that
you will need to develop addtional gnome-pim applications.

Currently these apps are present:

 - gnomecal :  personal calendar and todo list
 - gnomecard:  contact list of friends and business associates

You should install the gnome-pim package if you would like to bring some
order to your life. You will also need to install the gnome-libs and ORBit
packages. If you would like to develop addtional applications for the 
Personal Information Manager suite you will need to install the 
gnome-pim-devel package.

%prep
%setup -q

%build
./configure --prefix=/usr/local --sysconfdir=/etc
make

%install
build_dir=`pwd`
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/local
make install prefix=$RPM_BUILD_ROOT/usr/local sysconfdir=$RPM_BUILD_ROOT/etc
for i in `find $RPM_BUILD_ROOT/etc -type f`; do
    mv $i $i.rpm
done

%clean
rm -rf $RPM_BUILD_ROOT

%post
cat <<EOF
You need to edit and move
	/etc/CORBA/servers/gnomecal.gnorba.rpm
	/etc/CORBA/servers/gnomecard.gnorba.rpm
EOF

%files devel
%defattr(-,bin,bin)
/usr/local/share/idl/*.idl

%files
%defattr(-,bin,bin)
%doc AUTHORS COPYING ChangeLog NEWS README

/etc/CORBA/servers/*
/usr/local/bin/*
/usr/local/share/mime-info/*
/usr/local/share/pixmaps/*
/usr/local/share/gnome/apps/Applications/*
/usr/local/share/gnome/help/gnomecal
/usr/local/lib/locale/*/LC_MESSAGES/*
