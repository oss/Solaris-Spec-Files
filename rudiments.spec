%define _includedir /usr/local/include
%define _datadir /usr/local/share
%define _libdir /usr/local/lib
%define _mandir /usr/local/man
%define _bindir /usr/local/bin
%define _docdir /usr/local/doc
%define _tmppath /var/tmp

Summary: C++ class library for daemons, clients and servers.
Name: rudiments
Version: 0.31
Release: 1
License: LGPL
Group: Development/Libraries
Packager: Naveen Gavini <ngavini@nbcs.rutgers.edu>
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
make 

%install
rm -rf %{buildroot}
gmake DESTDIR=%{buildroot} docdir=%{buildroot}%{_docdir} install
cd %{buildroot}/%{_libdir}
rm *\.la #.la files are evil


%clean
rm -rf %{buildroot}

%files
%defattr(-, root, root)
%{_libdir}/librudiments-*.so.*

%files devel
%defattr(-, root, root)
%{_includedir}/rudiments
%{_libdir}/*.so
%{_bindir}/rudiments-config
%{_libdir}/pkgconfig/rudiments.pc
%{_libdir}/*.a

%files doc
%defattr(-, root, root)
%{_docdir}/

%changelog
* Thu Nov 8 2007 Naveen Gavini <ngavini@nbcs.rutgers.edu>
- Updated to the latest version.

* Mon Aug 03 2005 John M. Santel <jmsl@nbcs.rutgers.edu>
- It turns out we need .a files, so we include them again
 
* Mon Jul 11 2005 John M. Santel <jmsl@nbcs.rutgers.edu>
- Removed .la and .a files to comply with policy

* Mon Jun 27 2005 John M. Santel <jmsl@nbcs.rutgers.edu>
- Changed compiler from gcc to Sun Workshop/Forte


