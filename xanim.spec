Summary: Xanim video codec displayer
Name: xanim
Version: 27062
Release: 2
License: Free for noncommercial use
Source: xanim27062.tar.gz
Group: Amusements/Graphics
BuildRoot: /var/tmp/%{name}-root

%description
Xanim is a video player for X.

%prep
%setup -q -n xanim27062

%build
xmkmf -a
make CC=gcc PICFLAGS="-fpic" \
  CCOPTIONS="-O -I/usr/local/include/X11 -I/usr/openwin/include/X11 -L/usr/local/lib -R/usr/local/lib" \
  EXTRALDOPTIONS="-L/usr/local/lib -R/usr/local/lib"


%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/local/man/man1
mkdir $RPM_BUILD_ROOT/usr/local/bin
install -m 0755 xanim $RPM_BUILD_ROOT/usr/local/bin/xanim
install -m 0644 xanim.man $RPM_BUILD_ROOT/usr/local/man/man1/xanim.1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,bin,bin)
/usr/local/bin/xanim
/usr/local/man/man1/xanim.1
