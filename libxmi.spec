Summary: GNU machine-independent vector graphics library
Name: libxmi
Version: 1.2
Release: 3
Group: System Environment/Libraries
Copyright: GPL
Source: libxmi-%{version}.tar.gz
BuildRoot: /var/tmp/%{name}-root

%description
Libxmi is a system-independent vector graphics rasterization library
based on the sample X server that is part of the X11 distribution.

%package devel
Summary: Libxmi headers and static libraries
Group: System Environment/Libraries
Requires: libxmi = %{version}

%description devel
Libxmi-devel contains the static libraries, headers and documentation
for libxmi.

%prep
%setup -q

%build
LD="/usr/ccs/bin/ld -L/usr/local/lib -R/usr/local/lib" \
 LDFLAGS="-L/usr/local/lib -R/usr/local/lib" CPPFLAGS="-I/usr/local/include" \
 ./configure --prefix=/usr/local --sysconfdir=/etc
make

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/local
make install prefix=$RPM_BUILD_ROOT/usr/local sysconfdir=$RPM_BUILD_ROOT/etc

%clean
rm -rf $RPM_BUILD_ROOT

%post devel
if [ -x /usr/local/bin/install-info ] ; then
	/usr/local/bin/install-info --info-dir=/usr/local/info \
		 /usr/local/info/libxmi.info
fi

%preun devel
if [ -x /usr/local/bin/install-info ] ; then
	/usr/local/bin/install-info --delete --info-dir=/usr/local/info \
		 /usr/local/info/libxmi.info
fi

%files
%defattr(-,bin,bin)
%doc COPYING AUTHORS CUSTOMIZE NEWS README README-X TODO drawing.c
/usr/local/lib/lib*.so*

%files devel
%defattr(-,bin,bin)
/usr/local/info/*info*
/usr/local/lib/lib*a
/usr/local/include/*
