Name: fvwm
Version: 2.2.5
Copyright: GPL
Group: User Interface/X11
Summary: The F Virtual Window Manager
Release: 2
Source: fvwm-%{version}.tar.gz
BuildRoot: /var/tmp/%{name}-root
Requires: xpm readline
BuildRequires: readline-devel flex xpm
Conflicts: vpkg-SFWfvwm

%description
Fvwm is a simple, fast window manager for X.

%prep
%setup -q

%build
LDFLAGS="-R /usr/local/lib"
export LDFLAGS
./configure --prefix=/usr/local --with-xpm-library=/usr/local/lib \
    --with-xpm-includes=/usr/local/include \
    --with-readline-library=/usr/local/lib \
    --with-readline-includes=/usr/local/include \
    --enable-extras
make CXXFLAGS="-g -O2 -fpermissive"

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
