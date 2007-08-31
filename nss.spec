Summary:	nss and nspr libraries
Name:		nss
Version:	3.11.6
License:	Mozilla Public License
Group:		Application/Libraries
Release:	1
Source:		ftp://ftp.mozilla.org/pub/mozilla.org/security/nss/releases/NSS_3_11_7_RTM/src/%{name}-%{version}.tar.gz
URL:		http://mozilla.org/
Packager:	David Lee Halik <dhalik@nbcs.rutgers.edu>
BuildRoot:	/var/tmp/%{name}-root
Provides:	nspr
BuildRequires:	make, infozip, findutils, coreutils

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
PATH="/opt/SUNWspro/bin:${PATH}" \
CC="cc" CXX="CC" CPPFLAGS="-I/usr/local/include" \
LD="/usr/ccs/bin/ld" \
LDFLAGS="-L/usr/local/lib -R/usr/local/lib"
export PATH CC CXX CPPFLAGS LD LDFLAGS

cd mozilla/security/nss
gmake nss_build_all

%install
cd mozilla/security/nss
gmake install DESTDIR=%{buildroot}
mkdir -p %{buildroot}/usr/local/lib
mkdir -p %{buildroot}/usr/local/include/nspr
/usr/local/gnu/bin/find ../../dist/*/lib -type l \( -name "*.so" -o -name "*.chk" \) \
-exec cp -L {} %{buildroot}/usr/local/lib \;
cp -Lr ../../dist/public/* %{buildroot}/usr/local/include
cp -Lr ../../dist/*/include/* %{buildroot}/usr/local/include/nspr

%clean
rm -rf %{buildroot}

%files
%defattr(-, root, root)
/usr/local/lib/*

%files devel
%defattr(-, root, root)
/usr/local/include/*

%changelog
* Tue Aug 21 2007 David Lee Halik <dhalik@nbcs.rutgers.edu> - 3.11.6
- Bump to 3.11.6
* Fri Apr 14 2006 Leo Zhadanovsky <leozh@nbcs.rutgers.edu> - 3.11
- Updated to 3.11
