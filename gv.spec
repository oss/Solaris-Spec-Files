Name: gv
Version: 3.5.8
Release: 2
Summary: The gv PostScript viewer
Group: Applications/Productivity
Copyright: GPL
Source: gv-3.5.8.tar.gz
Requires: Xaw3d >= 1.5
BuildRoot: /var/tmp/%{name}-gv
BuildRequires: make

%description
Gv is a PostScript viewer based on Ghostview.

%prep
%setup -q

%build
xmkmf -a
make Makefiles
gmake CC=gcc CCOPTIONS="-I/usr/local/include -L/usr/local/lib -R/usr/local/lib -O" MAKE=gmake

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/local/lib/gv
mkdir -p $RPM_BUILD_ROOT/usr/local/bin
mkdir -p $RPM_BUILD_ROOT/usr/openwin/lib/X11/app-defaults
cd source
install -c -m 0755 gv $RPM_BUILD_ROOT/usr/local/bin/gv
for i in system user class ; do
    install -c -m 0644 gv_$i.ad $RPM_BUILD_ROOT/usr/local/lib/gv/gv_$i.ad
done
install -c -m 0644 GV.ad $RPM_BUILD_ROOT/usr/openwin/lib/X11/app-defaults/GV

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-, bin, bin)
%doc COPYING
/usr/local/lib/gv
/usr/local/bin/gv
/usr/openwin/lib/X11/app-defaults/GV
