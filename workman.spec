Name: workman
Version: 1.3.4
Release: 2
Summary: X11 CD player
Group: Applications/Productivity
Copyright: GPL
Source: workman-1.3.4.tar.gz
Patch: workman.patch
BuildRoot: /var/tmp/%{name}-root

%description
Workman is a CD player for X11 with playlists, shuffle mode, and
several other features.

%prep
%setup -q
%patch -p1

%build
make CPPFLAGS="-I/usr/openwin/include -DOWTOOLKIT_WARNING_DISABLED" \
     XLIBDIR="/usr/openwin/lib"

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/local/man/man1
mkdir -p $RPM_BUILD_ROOT/usr/local/bin
install -c -m 0755 workman $RPM_BUILD_ROOT/usr/local/bin/workman
install -c -m 0644 workman.man $RPM_BUILD_ROOT/usr/local/man/man1/workman.1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,bin,bin)
/usr/local/bin/workman
/usr/local/man/man1/workman.1


