Name: qt
Version: 3.0.4
Release: 4
Summary: Trolltech QT toolkit library.
Group: System/X11
Copyright: GPL or QPL
Source: qt-x11-free-3.0.4.tar.gz
BuildRoot: /var/tmp/%{name}-root
Requires: libpng libjpeg libungif
BuildRequires: libpng libjpeg zlib-devel libungif

%description
Qt is a user interface library for X11 written in C++.  This package
only includes the shared libraries; you need to install qt-devel to
compile programs for qt.  You may only be able to use programs
compiled with g++ with this library.

%package doc
Summary: Qt documentation
Group: Documentation
Requires: qt = %{version}

%description doc
This package contains the documentation included in the Qt source tree
and the Qt tutorials.  You may wish to install this if you are writing
Qt applications.

%package devel
Summary: Qt development files
Group: X11/Libraries
Requires: qt = %{version}

%description devel
This package contains the header files and auxiliary binaries needed
to compile Qt programs.  Install this if you are building Qt
applications.


%prep
%setup -q -n qt-x11-free-3.0.4

%build
QTDIR=`pwd`
LDFLAGS="-L/usr/local/lib -R/usr/local/lib"
LD_LIBRARY_PATH="/usr/local/lib"
LD_RUN_PATH="/usr/local/qt/lib:/usr/local/lib"
export QTDIR LDFLAGS LD_LIBRARY_PATH LD_RUN_PATH

echo "yes" | ./configure -system-zlib -qt-gif -system-libpng -system-libjpeg \
 -plugin-imgfmt-mng -thread -no-stl -no-xinerama -no-g++-exceptions -platform solaris-g++ \
 --prefix=$RPM_BUILD_ROOT/usr/local/qt
make


%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/local/qt/lib
cp lib/*.so* $RPM_BUILD_ROOT/usr/local/qt/lib
cp -r bin extensions $RPM_BUILD_ROOT/usr/local/qt/
mkdir -p $RPM_BUILD_ROOT/usr/local/qt/include/private
rm -f include/qt_windows.h
#cp -f include/private/* $RPM_BUILD_ROOT/usr/local/qt/include/private/
#rm -rf include/private
#cp -f include/* $RPM_BUILD_ROOT/usr/local/qt/include/
cp -r doc examples tutorial include src extensions $RPM_BUILD_ROOT/usr/local/qt/

#make install

#mkdir -p $RPM_BUILD_ROOT/usr/local/man/man1
#mkdir -p $RPM_BUILD_ROOT/usr/local/bin


%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc FAQ LICENSE.GPL LICENSE.QPL
/usr/local/qt/lib/*.so*

%files doc
%defattr(-,bin,bin)
/usr/local/qt/doc
/usr/local/qt/examples
/usr/local/qt/tutorial

%files devel
%defattr(-, root, other)
/usr/local/qt/include
/usr/local/qt/bin
/usr/local/qt/extensions
/usr/local/qt/src
