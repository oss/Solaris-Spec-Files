%include machine-header.spec

Name: Singular-factory
Version: 2.0.2
Copyright: GPL
Group: Development/Libraries
Summary: Singular factory libraries
Release: 1
Source: Singular-factory-2-0-2.tar.gz
Patch: factory.patch
BuildRoot: /var/tmp/%{name}-root
%ifarch sparc64
BuildRequires: gmp-devel gcc3
%else
BuildRequires: gmp-devel
%endif
Requires: gmp

%description 
Factory is a C++ class library that implements a recursive representation
of multivariate polynomial data.  It is being developed by Ruediger Stobbe
and Jens Schmidt at the University of Kaiserslautern as an independent and
self-contained part of the computer algebra system Singular (developed by
G.-M. Greuel, G. Pfister and H. Schoenemann).

This package contains static libraries and headers to develop using the 
Factory library. The authors do not support shared objects in this 
version.

%prep
%setup -q -n factory
%patch -p1

%build
%ifarch sparc64
CC=/usr/local/gcc-3.0.2/bin/sparcv9-sun-%{sol_os}-gcc CXX=/usr/local/gcc-3.0.2/bin/sparcv9-sun-%{sol_os}-g++ ./configure --with-gmp=/usr/local/include,/usr/local/lib
%else
./configure
%endif
make

%install
rm -rf $RPM_BUILD_ROOT
make install prefix=$RPM_BUILD_ROOT/usr/local

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,bin,bin)
/usr/local/lib/libcf*
/usr/local/include/*

