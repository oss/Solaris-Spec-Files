Summary: Motif calendar for X11
Name: xmcalendar
Version: 1.1beta
Release: 2
Group: Applications/Productivity
Copyright: BSD-type
Source: xmcalendar-1.1beta.tar.Z
BuildRoot: /var/tmp/%{name}-root

%description
XmCalendar is a X11/Motif based calendar program.  It can display the
calendar by month or year. It also has support for alarms. It saves
its data in a text file.

%prep
%setup -q -n xmcalendar

%build
rm -f Makefile
xmkmf -a
make CC=gcc PICFLAGS="-fpic" \
   CCOPTIONS="-O -I/usr/local/include/X11 -L/usr/local/lib -R/usr/local/lib" \
   EXTRALDOPTIONS="-L/usr/local/lib -R/usr/local/lib"

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/local/bin
mkdir -p $RPM_BUILD_ROOT/usr/local/man/man1
mkdir -p $RPM_BUILD_ROOT/usr/openwin/lib/X11/xmcalendar
mkdir -p $RPM_BUILD_ROOT/usr/openwin/lib/X11/app-defaults
install -m 0755 xmcalendar $RPM_BUILD_ROOT/usr/local/bin/xmcalendar
install -m 0644 xmcalendar.1 $RPM_BUILD_ROOT/usr/local/man/man1/xmcalendar.1
install -m 0444 XmCalendar.ad \
   $RPM_BUILD_ROOT/usr/openwin/lib/X11/app-defaults/XmCalendar
install -m 0444 xmcalendar.hlp $RPM_BUILD_ROOT/usr/openwin/lib/X11/xmcalendar

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,bin,bin)
%doc README VERSION TODO
/usr/local/bin/xmcalendar
/usr/local/man/man1/xmcalendar.1
/usr/openwin/lib/X11/xmcalendar
/usr/openwin/lib/X11/app-defaults/XmCalendar
