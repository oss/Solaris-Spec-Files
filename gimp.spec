%define major_version 1.2
%define minor_version 2

Name: gimp
Version: %{major_version}.%{minor_version}
Copyright: GPL
Group: Amusements/Graphics
Summary: The GNU Image Manipulation Program
Release: 1
Source: gimp-%{version}.tar.bz2
BuildRoot: /var/tmp/%{name}-root
BuildRequires: libpng libjpeg tiff gtk+-devel
Requires: libpng libjpeg tiff gtk+

%description
Gimp is the premiere free-software image manipulation program.
Install this package if you want to manpulate images.

%prep
%setup -q

%build
LDFLAGS="-R/usr/local/lib" ./configure --prefix=/usr/local
make

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/local
make install prefix=$RPM_BUILD_ROOT/usr/local

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,bin,bin)
/usr/local/lib/lib*a
/usr/local/lib/lib*.so*
/usr/local/lib/gimp/%{major_version}
/usr/local/include/libgimp
/usr/local/include/gck
/usr/local/man/man5/*
/usr/local/man/man1/*
/usr/local/share/gimp
/usr/local/share/aclocal/gimp.m4
/usr/local/bin/*
