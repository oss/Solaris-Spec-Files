Summary: The AfterStep window manager
Name: AfterStep
Version: 1.8.10
Release: 3
Group: User Interface/X
Copyright: GPL
Source: AfterStep-1.8.10.tar.bz2
BuildRoot: /var/tmp/%{name}-root
Requires: libjpeg62 libpng3 xpm
BuildRequires: libjpeg62-devel libpng3-devel

%description
AfterStep is a window manager for the X Window System (hereafter
referred to as X). It was started to emulate the look and feel of
NeXTSTEP(tm), but has evolved into something that while still being
able to emulate NeXT, can do much much more. Without using much memory
or cpu time, AfterStep provides all the features one could want in a
window manager.

%prep
%setup -q

%build
LD="/usr/ccs/bin/ld -L/usr/local/lib -R/usr/local/lib" CFLAGS="-O3" \
 LDFLAGS="-L/usr/local/lib -R/usr/local/lib" FLAGS="-I/usr/local/include" \
 ./configure --prefix=/usr/local --sysconfdir=/etc --with-jpeg --with-png \
  --with-xpm
make

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/local
make install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,bin,bin)
%doc doc/*html
/usr/local/share/afterstep
/usr/local/bin/*
/usr/local/man/man1/*
