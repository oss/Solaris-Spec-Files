%include gnome-header.spec
%include perl-header.spec

Summary: GTK+ AOL instant messenger client
Name: gaim
Version: 0.55
Release: 1
Copyright: GPL
Group: Applications/Productivity
Source: http://prdownloads.sourceforge.net/gaim/gaim-0.55.tar.bz2
BuildRoot: /var/tmp/%{name}-root
Requires: %{gtk_pkg}
Requires: %{glib_pkg}
Requires: perl
BuildRequires: %{gtk_pkg} %{glib_pkg} make
%if %{which_perl} == "REPOSITORY"
BuildRequires: perl-devel
%endif

%description
gaim is an Instant Messaging (IM) client designed primarily for use
with AOL Instant Messager (AIM).  However, it sup- ports most other
popular IM protocols including ICQ, MSN Messager, Jabber, Yahoo!, IRC,
Napster, and Zephyr. 
  (from the man page)

%prep
%setup -q

%build
%ifos solaris2.6
CFLAGS="-DNEED_SOCKLEN_T" LD="/usr/ccs/bin/ld" \
  LDFLAGS="-L/usr/local/lib -R/usr/local/lib %{gnome_ldflags}" \
  ./configure --disable-gnome --disable-esd
%else
LD="/usr/ccs/bin/ld" \
  LDFLAGS="-L/usr/local/lib -R/usr/local/lib %{gnome_ldflags}" \
  ./configure --disable-gnome --disable-esd
%endif
gmake

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT
gmake install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc AUTHORS HACKING NEWS README* STATUS TODO COPYING
%doc doc/*
/usr/local/lib/gaim
/usr/local/share/pixmaps/gaim.xpm
/usr/local/share/locale/*/LC_MESSAGES/gaim.mo
/usr/local/share/gnome/apps/Internet/gaim.desktop
/usr/local/man/man1/gaim.1
/usr/local/bin/gaim
