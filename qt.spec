%define maj_ver 2
%define min_ver 3
%define rev_ver 0

Name: qt
Version: %{maj_ver}.%{min_ver}.%{rev_ver}
Release: 2
Summary: Troll Tech X11 libraries
Copyright: QPL
Group: X11/Libraries
Source: qt-x11-%{version}.tar.gz
BuildRoot: /var/tmp/%{name}-root
Requires: libpng libjpeg libungif
Provides: libqt.so libqt.so.%{maj_ver} libqt.so.%{maj_ver}.%{min_ver}
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
%setup -q

%build
QTDIR=$RPM_BUILD_DIR/%{name}-%{version}
export QTDIR
echo "yes" | ./configure -shared -system-libpng -system-jpeg -system-zlib \
    -I/usr/local/include -L/usr/local/lib -platform solaris-g++
make SYSCONF_LFLAGS="-R/usr/local/qt/lib -R/usr/local/lib -L/usr/local/lib -lpng -lz -ljpeg" SYSCONF_CXXFLAGS="-O2 -fpermissive"

# We need -fpermissive, as the Sun X include files don't have return types
# for all the functions (which is illegal C++).

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/local/qt
tar cf - . | (cd $RPM_BUILD_ROOT/usr/local/qt && tar xvf -)

%clean
rm -rf $RPM_BUILD_ROOT

%post
for i in .so .so.%{maj_ver} .so.%{maj_ver}.%{min_ver} ; do
    ln -s /usr/local/qt/lib/libqt.so.%{version} /usr/local/qt/lib/libqt$i
done
echo "To use qt, set the environment variable QTDIR to /usr/local/qt."

%preun
for i in .so .so.%{maj_ver} .so.%{maj_ver}.%{min_ver} ; do
    rm -f /usr/local/lib/libqt$i
done

%post devel
cat <<EOF
To use moc, etc. add /usr/local/qt/bin to your PATH.  Also, set 
QTDIR=/usr/local/qt.
EOF


%post doc
echo "To read the manpages, add \$QTDIR/doc/man to your MANPATH."

%files
%defattr(-,bin,bin)
%doc LICENSE.QPL README README.QT INSTALL
/usr/local/qt/lib/libqt.so.%{version}

%files doc
%defattr(-,bin,bin)
/usr/local/qt/doc
/usr/local/qt/examples
/usr/local/qt/tutorial

%files devel
%defattr(-,bin,bin)
/usr/local/qt/include
/usr/local/qt/bin
/usr/local/qt/extensions
