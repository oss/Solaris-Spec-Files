Summary: minimal window manager
Name: lwm
Version: 1.00
Release: 3
Group: User Interface/X
License: GPL
Source: lwm.tar.gz
BuildRoot: /var/tmp/%{name}-root

%description
lwm is a window manager for X that tries to keep out of your face.
There are no icons, no button bars, no icon docks, no root menus, no
nothing: if you want all that, then other programs can provide
it. There's no configurability either: if you want that, you want a
different window manager; one that helps your operating system in its
evil conquest of your disc space and its annexation of your physical
memory.

%prep
%setup -q

%build
xmkmf -a
# lwm is not ANSI C, as far as Sun's cc is concerned.
make CCOPTIONS="" LINTOPTS=""

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/local/bin
install -m 0755 lwm $RPM_BUILD_ROOT/usr/local/bin/lwm

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,bin,bin)
%doc COPYRIGHT
/usr/local/bin/lwm

