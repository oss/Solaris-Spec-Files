Name: arts
Version: 1.0.0
Release: 1
Summary: aRts sound system
Group: System/X11
Copyright: GPL
Source: arts-%{version}.tar.bz2
BuildRoot: /var/tmp/%{name}-root
Requires: audiofile qt
BuildRequires: audiofile-devel qt-devel

%description
aRts multimedia daemon used by KDE 3.

%package devel
Summary: aRts development
Group: X11/Libraries

%description devel
Header files for the aRts daemon.

%prep
%setup -q

%build
QTDIR="/usr/local/qt"
LD_RUN_PATH="/usr/local/qt/lib"
LDFLAGS="-L/usr/local/lib -R/usr/local/lib"
LD_LIBRARY_PATH="/usr/local/lib"
export QTDIR LD_RUN_PATH LDFLAGS LD_LIBRARY_PATH
./configure --prefix=/usr/local
make

%install
make install prefix=$RPM_BUILD_ROOT/usr/local

#make install

#mkdir -p $RPM_BUILD_ROOT/usr/local/man/man1
#mkdir -p $RPM_BUILD_ROOT/usr/local/bin


%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc COPYING
/usr/local/lib/libmcop.so.1.0.0
/usr/local/lib/libmcop.so.1
/usr/local/lib/libmcop.so
/usr/local/lib/libmcop.la
/usr/local/lib/mcop/Arts
/usr/local/lib/mcop/artsflow.mcoptype
/usr/local/lib/mcop/artsflow.mcopclass
/usr/local/lib/mcop/soundserver.mcoptype
/usr/local/lib/mcop/soundserver.mcopclass
/usr/local/lib/mcop/kmedia2.mcoptype
/usr/local/lib/mcop/kmedia2.mcopclass
/usr/local/lib/mcop/x11globalcomm.mcoptype
/usr/local/lib/mcop/x11globalcomm.mcopclass
/usr/local/lib/libmcop_mt.so.1.0.0
/usr/local/lib/libmcop_mt.so.1
/usr/local/lib/libmcop_mt.so
/usr/local/lib/libmcop_mt.la
/usr/local/lib/libkmedia2_idl.so.1.0.0
/usr/local/lib/libkmedia2_idl.so.1
/usr/local/lib/libkmedia2_idl.so
/usr/local/lib/libkmedia2_idl.la
/usr/local/lib/libsoundserver_idl.so.1.0.0
/usr/local/lib/libsoundserver_idl.so.1
/usr/local/lib/libsoundserver_idl.so
/usr/local/lib/libsoundserver_idl.la
/usr/local/lib/libkmedia2.so.1.0.0
/usr/local/lib/libkmedia2.so.1
/usr/local/lib/libkmedia2.so
/usr/local/lib/libkmedia2.la
/usr/local/lib/libarts*
/usr/local/lib/libqtmcop.so.1.0.0
/usr/local/lib/libqtmcop.so.1
/usr/local/lib/libqtmcop.so
/usr/local/lib/libqtmcop.la
/usr/local/lib/libx11globalcomm.so.1.0.0
/usr/local/lib/libx11globalcomm.so.1
/usr/local/lib/libx11globalcomm.so
/usr/local/lib/libx11globalcomm.la
/usr/local/bin/mcopidl
/usr/local/bin/artsd
/usr/local/bin/artsplay
/usr/local/bin/artscat
/usr/local/bin/artswrapper
/usr/local/bin/artsshell
/usr/local/bin/artsrec
/usr/local/bin/artsc-config
/usr/local/bin/artsdsp

%files devel
%defattr(-, root, other)
/usr/local/include/arts
/usr/local/include/artsc