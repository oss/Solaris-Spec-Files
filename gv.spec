Name: gv
Version: 3.6.5
Release: 1
Summary: The gv PostScript viewer
Group: Applications/Productivity
Copyright: GPL
Source: %{name}-%{version}.tar.gz
#Patch: gv-zero-length.patch
Requires: Xaw3d >= 1.5
BuildRoot: /var/local/tmp/%{name}-root/

%description
Gv is a PostScript viewer based on Ghostview.

%prep
%setup -q
cd src
#%patch -p0
cd ..

%build

PATH="/opt/SUNWspro/bin:${PATH}" \
CC="cc" CXX="CC" CPPFLAGS="-I/usr/local/include" \
LD="/usr/ccs/bin/ld" \
LDFLAGS="-L/usr/local/lib -R/usr/local/lib" \
export PATH CC CXX CPPFLAGS LD LDFLAGS CFLAGS

./configure  --enable-setenv-code
gmake

%install
gmake install DESTDIR=%{buildroot}
rm -rf %{buildroot}/usr/local/share/info/dir
%clean
rm -rf %{buildroot}

%files
%doc AUTHORS COPYING ChangeLog INSTALL NEWS README
%defattr(644,bin,bin)
%attr(755,bin,bin) /usr/local/bin/gv
/usr/local/lib/gv/GV
/usr/local/lib/gv/gv_class.ad
/usr/local/lib/gv/gv_copyright.dat
/usr/local/lib/gv/gv_spartan.dat
/usr/local/lib/gv/gv_system.ad
/usr/local/lib/gv/gv_user.ad
/usr/local/lib/gv/gv_user_res.dat
/usr/local/lib/gv/gv_widgetless.dat
/usr/local/share/info/gv.info
/usr/local/share/man/man1/gv.1

%changelog
* Tue Jul 29 2008 David Diffenbaugh <davediff@nbcs.rutgers.edu> - 3.6.5-1
- wrote new spec file
- updated to 3.6.5
- changed compiler to sun studio
- added patch to fix C99 compatability 
