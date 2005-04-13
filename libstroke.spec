Name: libstroke
Version: 0.5.1
License: GPL
Summary: Mouse gesture recognition library
Release: 1
Group: Application/Libraries
Source: %{name}-%{version}.tar.gz
URL: http://www.etla.net/libstroke/
BuildRoot: /var/tmp/%{name}-root
BuildRequires: make

%package devel
Summary: %{name} include files, etc.
Requires: %{name} %{buildrequires}
Group: Development

%description
LibStroke is a stroke translation library. Strokes are motions of the mouse that can be interpreted by a program as a command. Strokes are used extensively in CAD programs.

%description devel
%{name} include files, etc.

%prep
%setup -q

%build
PATH=/opt/SUNWspro/bin:/usr/local/gnu/bin:/usr/ccs/bin:$PATH
CC="cc"
CPPFLAGS="-I/usr/local/include"
LDFLAGS="-L/usr/local/include -R/usr/local/include"
export PATH CC CPPFLAGS LDFLAGS
./configure --enable-tcl --disable-gtktest --with-x
gmake

%install
rm -rf %{buildroot}
gmake install DESTDIR=%{buildroot}
rm %{buildroot}/usr/local/lib/*.la

%clean
rm -rf %{buildroot}

%files
%defattr(-, root, other)
/usr/local/lib/*.so*

%files devel
%defattr(-, root, other)
/usr/local/include/*.h
/usr/local/lib/*.a
/usr/local/share/aclocal/*
