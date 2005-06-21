Summary: Fluxbox is a windowmanager that is based on Blackbox.
Name: fluxbox
Version: 0.9.13
Release: 1
Copyright: MIT
Group: X11/Window Managers
Source: http://download.sourceforge.net/fluxbox/fluxbox-0.9.13.tar.bz2
URL: http://fluxbox.org
Distribution: RU-Solaris
Vendor: NBCS-OSS
Packager: Randall Blecher <rblecher@nbcs.rutgers.edu>
BuildRoot: %{_tmppath}/%{name}-root
BuildRequires: zlib-devel

%description
Fluxbox is yet another windowmanager for X.
It's based on the Blackbox 0.61.1 code. Fluxbox looks like blackbox and handles styles, colors, window placement and similar thing exactly like blackbox (100% theme/style compability).

So what's the difference between fluxbox and blackbox then?
The answer is: LOTS!

%prep
%setup -q

%build
CC="gcc"
CXX="g++"
CPPFLAGS="-I/usr/local/include"
LDFLAGS="-L/usr/local/lib -R/usr/local/lib"
export CC CXX CPPFLAGS LDFLAGS

./configure --prefix=/usr/local --disable-dependency-tracking
gmake

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/local
gmake install prefix=$RPM_BUILD_ROOT/usr/local

%clean
rm -rf $RPM_BUILD_ROOT

%post
cat <<EOF

Just remember kids to enable fluxbox in your Sessions or local .xinitrc file

EOF

%files
%defattr(-,root,root,755)
%doc NEWS COPYING AUTHORS INSTALL TODO README ChangeLog

/usr/local/bin/*
/usr/local/man/man1/*
/usr/local/share/fluxbox/*

%changelog
* Mon Jun 13 2005 Randall Blecher <rblecher@nbcs.rutgers.edu> - 0.9.13-1
- updated to 0.9.13
- removed unneeded entry from specfile's 'files' section
