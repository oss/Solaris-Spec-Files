Summary: Esound library
Name: esound
Version: 0.2.36
Release: 1
Group: System Environment/Libraries
Copyright: GPL
Source: esound-%{version}.tar.bz2
BuildRoot: /var/tmp/%{name}-root
Distribution: RU-Solaris
Vendor: NBCS-OSS
Packager: Leo Zhadanovsky <leozh@nbcs.rutgers.edu>
Provides: libesd.so.0
Provides: libesd.so
Requires: audiofile >= 0.2.6
BuildRequires: audiofile >= 0.2.6

%description
The esound library is used by gnome.

%package devel
Summary: Esound development files
Group: System Environment/Libraries

%description devel
The esound-devel package contains the esound documentation, header
files and static libraries.

%prep
%setup -q

%build
#LD="/usr/ccs/bin/ld -L/usr/local/lib -R/usr/local/lib" \
#    LDFLAGS="-L/usr/local/lib -R/usr/local/lib"

PATH="/opt/SUNWspro/bin:${PATH}" \
CC="cc" CXX="CC" CPPFLAGS="-I/usr/local/include" \
LD="/usr/ccs/bin/ld" \
LDFLAGS="-L/usr/local/lib -R/usr/local/lib" \
export PATH CC CXX CPPFLAGS LD LDFLAGS

./configure --enable-shared --enable-static \
--with-audiofile-prefix=/usr/local --sysconfdir=/etc --prefix=/usr/local

make

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/local
mkdir -p $RPM_BUILD_ROOT/etc
make prefix=$RPM_BUILD_ROOT/usr/local sysconfdir=$RPM_BUILD_ROOT/etc install
mv $RPM_BUILD_ROOT/etc/esd.conf $RPM_BUILD_ROOT/etc/esd.conf.rpm

%clean
rm -rf $RPM_BUILD_ROOT

%post
echo move /etc/esd.conf.rpm to /etc/esd.conf

%files
%defattr(-,bin,bin)
/usr/local/lib/lib*.so*
/usr/local/bin/*
/usr/local/man/man1/*
/etc/esd.conf.rpm

%files devel
%defattr(-,bin,bin)
%doc docs/*
/usr/local/lib/lib*a
/usr/local/share/aclocal/esd.m4
/usr/local/include/*
/usr/local/lib/pkgconfig/*
