Summary: Lars Tiling Window Manager
Name: larswm
Version: 5.8
Release: 3
License: GPL
Group: User Interface/Desktops
Source: %{name}-%{version}.tar.gz
BuildRoot: /var/tmp/%{name}-%{version}-root

%description
This is a small tiling window manager based on David Hogan's 9wm.
Please see http://www.fnurt.net/larswm for more information.

%prep
%setup -q

%build
xmkmf -a
make

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/local/bin
mkdir -p $RPM_BUILD_ROOT/usr/local/man/man1
install -m 0755 larswm $RPM_BUILD_ROOT/usr/local/bin/larswm
install -m 0644 larswm.man $RPM_BUILD_ROOT/usr/local/man/man1/larswm.1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc                    ChangeLog README sample.larswmrc README.9wm
%attr(0755,root,root)   /usr/local/bin/larswm
%attr(0755,root,root)   /usr/local/man/man1/larswm.1
