Summary: nss and nspr libraries
Name: nss
Version: 3.9
License: Mozilla Public License
Group: Application/Libraries
Release: 1
Source: ftp://ftp.mozillla.org/pub/mozilla.org/security/nss/releases/NSS_3_9_TRM/src/nss-3.9.tar.gz
URL: http://mozilla.org/
Packager: Etan Reisner <deryni@jla.rutgers.edu>
BuildRoot: /var/tmp/%{name}-root
BuildRequires: make, infozip, findutils, coreutils

%description
The %{name} package provides the mozilla nss and nspr libraries.

%package devel
Summary: Header files needed to compile programs against nss and nspr.
Requires: %{name} = %{version}
Group: Application/Libraries

%description devel
The %{name}-devel package provides the header files and other files needed to compile programs against the mozilla nss and nspr libraries.

%prep
%setup -q

%build
CC="/opt/SUNWspro/bin/cc"
LDFLAGS="-L/usr/local/lib -R/usr/local/lib"
CPPFLAGS="-I/usr/local/include"
export CC LDFLAGS CPPFLAGS

cd mozilla/security/nss
gmake nss_build_all

%install
cd mozilla/security/nss
gmake install
mkdir -p %{buildroot}/usr/local/lib
mkdir -p %{buildroot}/usr/local/include/nspr
/usr/local/gnu/bin/find ../../dist/*/lib -type l \( -name "*.so" -o -name "*.chk" \) \
-exec cp -L {} %{buildroot}/usr/local/lib \;
cp -Lr ../../dist/public/* %{buildroot}/usr/local/include
cp -Lr ../../dist/*/include/* %{buildroot}/usr/local/include/nspr

%clean

%files
%defattr(-, root, root)
/usr/local/lib/*

%files devel
%defattr(-, root, root)
/usr/local/include/*
