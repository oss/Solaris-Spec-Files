Summary: CORBA Interface Definition Language
Name: libIDL2
Version: 0.8.9
Release: 1
Copyright: GPL
Group: Applications/Editors
Source: libIDL-%{version}.tar.bz2
Distribution: RU-Solaris
Vendor: NBCS-OSS
BuildRoot: %{_tmppath}/%{name}-root
BuildRequires: flex glib2-devel
Requires: glib2

%description
libIDL is a front-end for CORBA IDL (2.2) and Mozilla's XPIDL, currently
used in the GNOME  project (bundled with ORBit), and the Mozilla  project
(if you are not using Firefox, you should), and other projects here and there.

%prep
%setup -q -n libIDL-%{version}

%build
PATH="/opt/SUNWspro/bin:${PATH}" \
CC="cc" CXX="CC" CPPFLAGS="-I/usr/local/include" \
LD="/usr/ccs/bin/ld" \
LDFLAGS="-L/usr/local/lib -R/usr/local/lib"
export PATH CC CXX CPPFLAGS LD LDFLAGS

./configure --prefix=/usr/local --disable-nls

gmake
gmake check

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/local

PATH="/opt/SUNWspro/bin:/usr/local/bin:/usr/local/gnu/bin:${PATH}"
export PATH

gmake install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,bin)
/usr/local/bin/libIDL-config-2
/usr/local/include/libIDL-2.0/libIDL/IDL.h
/usr/local/lib/libIDL-2.*
/usr/local/lib/pkgconfig/libIDL-2.0.pc
/usr/local/share/info/libIDL2.info

%changelog
* Sun Nov 18 2007 David Lee Halik <dalik@nbcs.rutgers.edu> - 0.8.9-1
- Bump to 0.8.9
- Disable NLS
