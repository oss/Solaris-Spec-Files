Summary: Nearly minimal window manager
Name: wm2
Version: 4
Release: 2
License: Freely distributable
Group: User Interface/X
Source: wm2-%{version}.tar.gz
BuildRoot: /var/tmp/%{name}-root

%description
wm2 is a window manager for X.  It provides an unusual style of window
decoration and as little functionality as I feel comfortable with in a
window manager.  wm2 is not configurable, except by editing the source
and recompiling the code, and is really intended for people who don't
particularly want their window manager to be too friendly.

wm2 provides:

  -- Decorative frames for your windows.

  -- The ability to move, resize, hide and restore windows.

  -- No icons.

  -- No configurable root menus, buttons or mouse or keyboard bindings.

  -- No virtual desktop, toolbars or integrated applications.

%prep
%setup -q

%build
make

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/local/bin
install -m 0755 wm2 $RPM_BUILD_ROOT/usr/local/bin/wm2

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,bin,bin)
%doc README
/usr/local/bin/wm2
