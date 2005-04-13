Name: fvwm
Version: 2.5.12
License: GPL
Group: User Interface/X11
Summary: F(?) Virtual Window Manager
Release: 1
Source: fvwm-%{version}.tar.gz
BuildRoot: /var/tmp/%{name}-root
Requires: xpm readline libpng3 xrender fribidi libstroke
BuildRequires: readline-devel flex xpm make libpng3-devel render xrender-devel fribidi-devel libstroke-devel
Conflicts: vpkg-SFWfvwm

%description
Fvwm is a simple, fast window manager for X.

%prep
%setup -q

%build
PATH=/opt/SUNWspro/bin:/usr/local/gnu/bin:/usr/ccs/bin:$PATH
CC="cc"
CFLAGS="-g -xs -xO2"
CPPFLAGS="-I/usr/local/include"
LDFLAGS="-L/usr/local/lib -R/usr/local/lib"
export PATH CC CFLAGS CPPFLAGS LDFLAGS
#./configure --prefix=/usr/local --with-xpm-library=/usr/local/lib \
#    --with-xpm-includes=/usr/local/include \
#    --with-readline-library=/usr/local/lib \
#    --with-readline-includes=/usr/local/include \
#    --enable-extras
#make CXXFLAGS="-g -O2 -fpermissive"
./configure --without-gnome --without-rplay-library
gmake

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/local
make install prefix=$RPM_BUILD_ROOT/usr/local

%clean
rm -rf $RPM_BUILD_ROOT

%post
cat <<EOF
To set system-wide preferences for fvwm, you can copy one of the sample
files in /usr/local/doc/fvwm-%{version} to /usr/local/etc/system.fvwm2rc.
EOF

%files
%defattr(-,bin,bin)
%doc sample.fvwmrc/*
/usr/local/bin/*
/usr/local/man/man1/*
/usr/local/libexec/fvwm/%{version}
/usr/local/share/fvwm/*
/usr/local/share/fvwm/perllib/FVWM/*
/usr/local/share/fvwm/perllib/General/*
/usr/local/share/locale/*/LC_MESSAGES/*
