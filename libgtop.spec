Summary: LibGTop Library
Name: libgtop
Version: 1.0.10
Release: 2
Group: X11/Libraries
Copyright: LGPL
Source: libgtop-%{version}.tar.gz
BuildRoot: /var/tmp/%{name}-root
Requires: glib >= 1.2.8
Requires: guile >= 1.4
Requires: gnome-libs >= 1.2.3
Requires: ORBit >= 0.5.3
BuildRequires: glib >= 1.2.8
BuildRequires: guile >= 1.4
BuildRequires: gnome-libs-devel >= 1.2.3
BuildRequires: ORBit-devel >= 0.5.3

%description

A library that fetches information about the running system such as
cpu and memory usage, active processes etc.

On Linux systems, these information are taken directly from the /proc
filesystem while on other systems a server is used to read those
information from /dev/kmem or whatever. 

%package devel
Summary: Libraries, includes, etc to develop LibGTop applications
Group: X11/libraries
Requires: libgtop = %{version}

%description devel
Libraries, include files, etc you can use to develop GNOME applications.

%package examples
Summary: Examples for LibGTop
Group: X11/libraries
Requires: libgtop

%description examples
Examples for LibGTop.

%prep
%setup -q

%build
CPPFLAGS="-I/usr/local/include" \
    LD="/usr/ccs/bin/ld -L/usr/local/lib -R/usr/local/lib" \
    LDFLAGS="-L/usr/local/lib -R/usr/local/lib" ./configure \
    --enable-shared --enable-static --with-gnome-includes=/usr/local \
    --with-gnome-libs=/usr/local --with-glib-prefix=/usr/local \
    --with-libgtop-examples --with-libgtop-guile
make

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/local
make install prefix=$RPM_BUILD_ROOT/usr/local

%clean
rm -rf $RPM_BUILD_ROOT

%post devel
if [ -x /usr/local/bin/install-info ] ; then
	/usr/local/bin/install-info --info-dir=/usr/local/info \
		 /usr/local/info/libgtop.info \
  --entry="* LibGTop: (libgtop).                         GTop library"
fi

%preun devel
if [ -x /usr/local/bin/install-info ] ; then
	/usr/local/bin/install-info --delete --info-dir=/usr/local/info \
		 /usr/local/info/libgtop.info
fi

%files
%defattr(-,bin,bin)
%doc RELNOTES-0.25 RELNOTES-1.0 AUTHORS ChangeLog NEWS README
%doc copyright.txt
%doc src/inodedb/README.inodedb
/usr/local/lib/locale/*/LC_MESSAGES/libgtop.mo
/usr/local/lib/lib*.so*
/usr/local/bin/*

%files devel
%defattr(-,bin,bin)
/usr/local/include/*
/usr/local/lib/lib*a
/usr/local/lib/*.sh
/usr/local/lib/*.def
/usr/local/info/*info*

%files examples
%defattr(-,bin,bin)
/usr/local/libexec/libgtop
