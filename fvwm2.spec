Name: fvwm
Version: 2.4.20
License: GPL
Group: User Interface/X11
Summary: F(?) Virtual Window Manager
Release: 1
Source: fvwm-%{version}.tar.bz2
BuildRoot: /var/tmp/%{name}-root
Requires: readline
Requires: libpng3
Requires: fribidi
Requires: fontconfig
Requires: libstroke
BuildRequires: readline-devel
BuildRequires: libpng3-devel
BuildRequires: fribidi-devel
BuildRequires: libstroke-devel
Conflicts: vpkg-SFWfvwm

%description
Fvwm is a simple, fast window manager for X.

%prep
%setup -q

%build
PATH=/opt/SUNWspro/bin:/usr/local/gnu/bin:/usr/ccs/bin:$PATH
CC="cc"
CFLAGS="-xs -xO3"
CPPFLAGS="-I/usr/local/include"
LDFLAGS="-L/usr/local/lib -R/usr/local/lib"
export PATH CC CFLAGS CPPFLAGS LDFLAGS

./configure --without-gnome --without-rplay-library --enable-extras
gmake

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/local
gmake install prefix=$RPM_BUILD_ROOT/usr/local

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
/usr/local/libexec/fvwm/%{version}
/usr/local/share/man/man1/*
/usr/local/share/fvwm/*
