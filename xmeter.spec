Summary: rstat display for X
Name: xmeter
Version: 1.15
Release: 2
Group: User Interface/X
Copyright: Freely distributable
Source: xmeter-%{version}.tar.gz
BuildRoot: /var/tmp/%{name}-root

%description
xmeter displays a histogram of data returned by rstat(3).  It can be
told to monitor multiple hosts, or to monitor multiple statistics on the
same host.

%prep
%setup -c -T -n xmeter
%setup -T -D -a 0 -n xmeter

%build
xmkmf -a
make CC=gcc PICFLAGS="-fpic" \
   CCOPTIONS="-O -I/usr/local/include/X11 -L/usr/local/lib -R/usr/local/lib" \
   EXTRALDOPTIONS="-L/usr/local/lib -R/usr/local/lib"

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/local/man/man1
mkdir $RPM_BUILD_ROOT/usr/local/bin
mkdir -p $RPM_BUILD_ROOT/usr/openwin/lib/X11/app-defaults
install -m 0755 xmeter $RPM_BUILD_ROOT/usr/local/bin/xmeter
install -m 0644 XMeter.ad \
    $RPM_BUILD_ROOT/usr/openwin/lib/X11/app-defaults/XMeter
install -m 0644 xmeter.man $RPM_BUILD_ROOT/usr/local/man/man1/xmeter.1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,bin,bin)
%doc README
/usr/local/bin/xmeter
/usr/local/man/man1/xmeter.1
/usr/openwin/lib/X11/app-defaults/XMeter
