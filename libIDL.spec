Summary: libIDL
Name: libIDL
Version: 0.8.6
Release: 1
Copyright: GPL
Group: Applications/Editors
Source: libIDL-%{version}.tar.bz2
Distribution: RU-Solaris
Vendor: NBCS-OSS
BuildRoot: %{_tmppath}/%{name}-root

%description
libIDL is a front-end for CORBA IDL (2.2) and Mozilla's XPIDL, currently
used in the GNOME  project (bundled with ORBit), and the Mozilla  project
(if you are not using Firefox, you should), and other projects here and there.

%prep
%setup -q

%build
CPPFLAGS="-I/usr/local/include"
LDFLAGS="-L/usr/local/lib -R/usr/local/lib"
CC="cc" 
PATH="/opt/SUNWspro/bin:/usr/local/bin:/usr/local/gnu/bin:${PATH}"
export CPPFLAGS LDFLAGS CC PATH

./configure --prefix=/usr/local

gmake

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

