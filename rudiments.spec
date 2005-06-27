%define _includedir /usr/local/include
%define _datadir /usr/local/share
%define _libdir /usr/local/lib
%define _mandir /usr/local/man
%define _bindir /usr/local/bin
%define _docdir /usr/local/doc
%define _tmppath /var/tmp

Summary: C++ class library for daemons, clients and servers.
Name: rudiments
Version: 0.28.2
Release: 1
License: LGPL
Group: Development/Libraries
Source0: %{name}-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}



%description
Rudiments is an Open Source C++ class library providing base classes
for things such as daemons, clients and servers, and wrapper classes
for the standard C functions for things like such as regular
expressions, semaphores and signal handling.


%package devel
Summary: Libraries and header files for developing with rudiments.
Group: Development/Libraries

%description devel
Libraries and header files for developing with rudiments.


%package doc
Summary: Documentation for rudiments.
Group: Development/Libraries

%description doc
Documentation for rudiments.


%prep
%setup -q

%build
LD="/usr/ccs/bin/ld -L/usr/local/lib -R/usr/local/lib -L$PREFIX/lib -R$PREFIX/li
b -L$PREFIX/lib -R$PREFIX/lib"
LDFLAGS="-L/usr/local/lib -R/usr/local/lib -L$PREFIX/lib -R$PREFIX/lib"
export LD
export LDFLAGS
./configure --prefix='/usr/local'
gmake 

%install
rm -rf %{buildroot}
gmake DESTDIR=%{buildroot} docdir=%{buildroot}%{_docdir} install


%clean
rm -rf %{buildroot}

%files
%defattr(-, root, root)
%{_libdir}/librudiments-*.so.*

%files devel
%{_includedir}/rudiments
%{_libdir}/*.so
%{_libdir}/*.a
%{_libdir}/*.la
%{_bindir}/rudiments-config
%{_libdir}/pkgconfig/rudiments.pc

%files doc
%{_docdir}/

%changelog
* Fri Jan  31 2003 David Muse <dmuse@firstworks.com>
- Made it so it could be distributed with rudiments.
- Added devel.

* Fri May  3 2002 Matthias Saou <matthias.saou@est.une.marmotte.net>
- Rebuilt against Red Hat Linux 7.3.
- Added the %{?_smp_mflags} expansion.

* Mon Apr 15 2002 Matthias Saou <matthias.saou@est.une.marmotte.net> 0.24-fr1
- Update to 0.24 at last.

* Wed May 16 2001 Matthias Saou <matthias.saou@est.une.marmotte.net>
- Initial RPM release.

