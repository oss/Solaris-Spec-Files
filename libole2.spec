Summary: Structured Storage OLE2 library
Name: libole2
Version: 0.1.6
Release: 2
Group: System Environment/Libraries
Copyright: GPL
Source: libole2-%{version}.tar.gz
Buildroot: /var/tmp/%{name}-root
Requires: glib
BuildRequires: glib

%description
A library containing functionality to manipulate OLE2 Structured
Storage files. It is used by Gnumeric from Gnome, AbiWord from
AbiSuite and by other programs.

%package devel
Summary: Libraries, includes, etc to develop libole2 applications
Group: X11/Libraries
Requires: libole2 = %{version}

%description devel
Libraries, include files, etc you can use to develop libole2
applications.

%prep
%setup -q

%build
LD="/usr/ccs/bin/ld -L/usr/local/lib -R/usr/local/lib" \
  LDFLAGS="-L/usr/local/lib -R/usr/local/lib" \
  CPPFLAGS="-I/usr/local/include" ./configure
make

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/local
make prefix=$RPM_BUILD_ROOT/usr/local install

%files
%defattr(-,root,root)
%doc README
/usr/local/lib/lib*.so.*
/usr/local/share/*

%files devel
%defattr(-,root,root)
%attr(755,root,root) /usr/local/bin/libole2-config
/usr/local/lib/lib*.so
/usr/local/lib/*a
/usr/local/lib/*.sh
/usr/local/include/*

%clean
rm -rf $RPM_BUILD_ROOT

