Name: glib
Version: 1.2.10
Copyright: LGPL
Group: Development/Libraries
Summary: GNU GLib
Release: 2
Source: glib-%{version}.tar.gz
Patch: glib-%{version}.patch
BuildRoot: /var/tmp/%{name}-root
Conflicts: vpkg-SFWglib

%description
GNU glib is a library that provides support for common data structures
such as trees and hash tables in C.  It is used in GTK.  Install this
package if you have software that requires it, or if you want to build
software with it.

%prep
%setup -q
%patch -p1

# adds -R to glib-config

%build
LDFLAGS="-L/usr/local/lib -R/usr/local/lib" ./configure --prefix=/usr/local
make

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/local
make install prefix=$RPM_BUILD_ROOT/usr/local

%clean
rm -rf $RPM_BUILD_ROOT

%post
if [ -x /usr/local/bin/install-info ] ; then
	/usr/local/bin/install-info --info-dir=/usr/local/info \
		 /usr/local/info/glib.info
fi

%preun
if [ -x /usr/local/bin/install-info ] ; then
	/usr/local/bin/install-info --delete --info-dir=/usr/local/info \
		 /usr/local/info/glib.info
fi

%files
%defattr(-,root,root)
%doc COPYING
/usr/local/lib/lib*.so*
/usr/local/lib/lib*a
/usr/local/lib/glib
/usr/local/lib/pkgconfig/*
/usr/local/bin/glib-config
/usr/local/share/aclocal/glib.m4
/usr/local/include/*
/usr/local/info/glib.info
/usr/local/man/man1/glib-config.1
