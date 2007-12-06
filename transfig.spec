Name: transfig
Version: 3.2.5
Release: 1
Summary: Xfig output translator
Copyright: Freely distributable
Group: Applications/Productivity
Source: transfig.%{version}.tar.gz
Patch: transfig-3.2.5-build.patch
BuildRoot: %{_tmppath}/%{name}-root
BuildRequires: libpng3-devel libjpeg-devel xpm Xaw3d
Requires: libpng3 libjpeg xpm Xaw3d teTeX

%description
Transfig translates the output produced by xfig.  If you plan to
export any xfig figures, install this package.

%prep
%setup -q -n transfig.%{version}
%patch -p1

%build
PATH="/opt/SUNWspro/bin:${PATH}" \
CC="cc" CXX="CC" CPPFLAGS="-I/usr/local/include" \
LD="/usr/ccs/bin/ld" \
LDFLAGS="-L/usr/local/lib -R/usr/local/lib"
export PATH CC CXX CPPFLAGS LD LDFLAGS

xmkmf
gmake Makefiles
gmake includes
gmake depend

gmake

%install
rm -rf %{buildroot}
for i in /usr/local/lib/X11/xfig /usr/local/bin; do
    mkdir -p %{buildroot}$i
done
PATH=/usr/openwin/bin:$PATH gmake install DESTDIR=%{buildroot}/ BINDIR=usr/local/bin
mkdir -p %{buildroot}/usr/local/man/man1/
cp doc/*.1 %{buildroot}/usr/local/man/man1/

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
/usr/local/man/man1

%changelog
* Thu Nov 29 2007 David Lee Halik <dhalik@nbcs.rutgers.edu> - 3.2.5-1
- Bump to 3.2.5
