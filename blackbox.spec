Summary: Blackbox window manager
Name: blackbox
Version: 0.61.1
Release: 2
Group: User Interface/X
Copyright: GPL
Source: blackbox-%{version}.tar.bz2
BuildRoot: /var/tmp/%{name}-root

%description
Blackbox is a minimalist window manager that has low resource usage
and is quite fast.

%prep
%setup -q

%build
LD="/usr/ccs/bin/ld -L/usr/local/lib -R/usr/local/lib" \
 LDFLAGS="-L/usr/local/lib -R/usr/local/lib" \
 CXX="g++ -fpermissive -I/usr/local/include" \
 ./configure --prefix=/usr/local --sysconfdir=/etc
make

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/local
make install prefix=$RPM_BUILD_ROOT/usr/local sysconfdir=$RPM_BUILD_ROOT/etc

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,bin,bin)
%doc LICENSE AUTHORS README TODO ChangeLog* 
%doc data/README.menu data/README.style
/usr/local/share/Blackbox
/usr/local/bin/*
