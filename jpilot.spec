Summary: jpilot
Name: jpilot
Version: 0.99.5
Release: 6
Copyright: GPL
Group: Applications/Productivity
Source: %{name}-%{version}.tar.gz
URL: http://http://www.jpilot.org/
Distribution: RU-Solaris
Vendor: NBCS-OSS
Packager: Robert Renaud <rrenaud@nbcs.rutgers.edu>
BuildRoot: %{_tmppath}/%{name}-root
BuildRequires: gtk2-devel
Requires: pilot-link gtk2
BuildRequires: pilot-link

%description
Graphical interface to palm pilots.

%prep
%setup -q

%build
LD_RUN_PATH=/usr/local/lib LD_LIBRARY_PATH=/usr/local/lib LDFLAGS="-L/usr/local/lib -R/usr/local/lib" CPPFLAGS="-I/usr/local/include/gtk-2.0/ `pkg-config --cflags glib-2.0` -I/usr/local/include/pango-1.0 -I/usr/local/include/atk-1.0" ./configure --enable-gtk2 --prefix=/usr/local --enable-gtk2

make

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/local
make install prefix=$RPM_BUILD_ROOT/usr/local
mv $RPM_BUILD_ROOT/usr/local/lib/charset.alias $RPM_BUILD_ROOT/usr/local/lib/charset.alias.jpilot
%clean
rm -rf $RPM_BUILD_ROOT

%post
if [ ! -f /usr/local/lib/charset.alias ] ; then
    echo pointing /usr/local/lib/charset.alias to /usr/local/lib/charset.alias.jpilot
   ln -s /usr/local/lib/charset.alias.jpilot /usr/local/lib/charset.alias
fi
    

%files
%defattr(-, root, bin)
/usr/local/bin/*
/usr/local/doc/jpilot-%{version}/*
/usr/local/man/man1/*
# gets la files
/usr/local/lib/* 
/usr/local/share/jpilot/*

