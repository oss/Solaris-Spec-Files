Summary: Fast Light toolkit
Name: fltk
Version: 1.0.9
Release: 3
License: GPL
Group: Usr Interface/X
Source: fltk-%{version}-source.tar.bz2
BuildRoot: /var/tmp/%{name}-root

%description
The Fast Light Tool Kit ("FLTK", pronounced "fulltick") is a LGPL'd
C++ graphical user interface toolkit for X (UNIX(r)), OpenGL(r), and
Microsoft(r) Windows(r) NT 4.0, 95, or 98. It was originally developed
by Mr. Bill Spitzak and is currently maintained by a small group of
developers across the world with a central repository in the US.

%package devel
Summary: fltk headers and static libraries
Group: Development/Libraries
Requires: fltk = %{version}

%description devel
Fltk-devel contains the fltk documentation, headers and static
libraries; you only need this if you are building programs with fltk.

%prep
%setup -q

%build
LD="/usr/ccs/bin/ld -L/usr/local/lib -R/usr/local/lib" \
 LDFLAGS="-L/usr/local/lib -R/usr/local/lib" ./configure --enable-shared
make

%install
# make install doesn't seem to work.

rm -rf $RPM_BUILD_ROOT

mkdir -p $RPM_BUILD_ROOT/usr/local/lib
install -m 0644 lib/libfltk.a $RPM_BUILD_ROOT/usr/local/lib
install -m 0755 src/libfltk.so.1 $RPM_BUILD_ROOT/usr/local/lib

mkdir -p $RPM_BUILD_ROOT/usr/local/include/FL
for i in FL/*.[hH]; do 
    install -m 0644 $i $RPM_BUILD_ROOT/usr/local/include/FL
done

mkdir -p $RPM_BUILD_ROOT/usr/local/bin
strip fluid/fluid

install -m 0755 fluid/fluid $RPM_BUILD_ROOT/usr/local/bin/fluid

cd $RPM_BUILD_ROOT/usr/local/include
ln -s FL Fl

cd $RPM_BUILD_ROOT/usr/local/include/FL
for i in *.H ; do 
    ln -s $i "`basename $i H`h"
done

cd $RPM_BUILD_ROOT/usr/local/lib
ln -s libfltk.so.1 libfltk.so

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,bin,bin)
/usr/local/lib/lib*.so*

%files devel
%defattr(-,bin,bin)
/usr/local/bin/fluid
/usr/local/include/FL
/usr/local/include/Fl
/usr/local/lib/*a
