%include gnome-header.spec

Summary: Free Civilization II clone
Name: freeciv
Version: 1.11.4
Release: 2
Group: Amusements/Games
Copyright: GPL
Source: freeciv-%{version}.tar.gz
Requires: %{gtk_pkg}
Requires: %{imlib_pkg}
Requires: xpm
BuildRoot: /var/tmp/%{name}-root
BuildRequires: %{imlib_dev}
BuildRequires: %{gtk_dev}
BuildRequires: xpm

%description
Freeciv is a free Civilization clone for X.  It has support for
multiplayer games locally or over a network, and has a good AI.

%prep
%setup -q

%build
LD="/usr/ccs/bin/ld %{gnome_ldflags}" \
 LDFLAGS="%{gnome_ldflags}" CPPFLAGS="-I/usr/local/include" \
 ./configure --prefix=/usr/local --sysconfdir=/etc \
 --with-gtk-prefix=%{gtk_prefix} --with-imlib-prefix=%{imlib_prefix} \
 --with-xpm-prefix=/usr/local
make

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/local
make install prefix=$RPM_BUILD_ROOT/usr/local sysconfdir=$RPM_BUILD_ROOT/etc

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,bin,bin)
%doc README* NEWS PEOPLE AUTHORS BUGS COPYING HOWTOPLAY TODO
%doc freeciv_hackers_guide.txt
/usr/local/share/freeciv
/usr/local/bin/*
/usr/local/lib/locale/*/LC_MESSAGES/freeciv.mo
