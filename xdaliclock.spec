Name: xdaliclock
Version: 2.18
Copyright: BSD-type
Group: User Interface/X
Summary: jwz's digital clock
Release: 2
Source: xdaliclock-2.18.tar.gz
BuildRoot: /var/tmp/%{name}-root

%description
Xdaliclock is a digital clock for X where the digits morph into one
another.

%prep
%setup -q

%build
cd X11
./configure --prefix=/usr/local
make

%install
cd X11
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/local/bin
mkdir -p $RPM_BUILD_ROOT/usr/local/man/man1
make install prefix=$RPM_BUILD_ROOT/usr/local

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,bin,bin)
/usr/local/bin/xdaliclock
/usr/local/man/man1/xdaliclock.1
