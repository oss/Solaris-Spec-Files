Name: transfig
Version: 3.2.3d
Release: 4
Summary: Xfig output translator
Copyright: Freely distributable
Group: Applications/Productivity
Source: transfig.%{version}.tar.gz
Patch: transfig.%{version}.patch
BuildRoot: /var/tmp/%{name}-root
BuildRequires: vpkg-SPROcc libpng libjpeg xpm Xaw3d
Requires: libpng libjpeg xpm Xaw3d teTeX

%description
Transfig translates the output produced by xfig.  If you plan to
export any xfig figures, install this package.

%prep
%setup -q -n transfig.%{version}
%patch -p1

%build
xmkmf -a
make

%install
rm -rf %{buildroot}
for i in /usr/local/lib/X11/xfig /usr/local/bin; do
    mkdir -p %{buildroot}$i
done
PATH=/usr/openwin/bin:$PATH make install DESTDIR=%{buildroot}/ BINDIR=usr/local/bin

%clean
rm -rf %{buildroot}

%files
%defattr(-, bin, bin)
%doc doc/manual
%doc README NOTES CHANGES LATEX.AND.XFIG
/usr/local/bin/transfig
/usr/local/bin/fig2dev
/usr/local/bin/fig2ps2tex
/usr/local/bin/fig2ps2tex.sh
/usr/local/bin/pic2tpic
/usr/local/lib/X11/xfig/bitmaps
/usr/local/lib/fig2dev
