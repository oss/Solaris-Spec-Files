%include machine-header.spec

Name: Singular-libfac
Version: 2.0.2
Copyright: GPL
Group: Development/Libraries
Summary: Singular libfac libraries
Release: 1
Source: Singular-libfac-2-0-2.tar.gz
BuildRoot: /var/tmp/%{name}-root
%ifarch sparc64
BuildRequires: Singular-factory gcc3
%else
BuildRequires: Singular-factory
%endif

%description
Singular-libfac is an extension to Singular-factory which implements
factorization of polynomials over finite fields and algorithms for
manipulation of polynomial ideals via the characteristic set methods
(e.g., calculating the characteristic set and the irreducible
characteristic series).

This package contains the static library and header for libfac. The 
authors currently do not support shared objects.

%prep
%setup -q -n libfac

%build
%ifarch sparc64
CC=/usr/local/gcc-3.0.2/bin/sparcv9-sun-%{sol_os}-gcc CXX=/usr/local/gcc-3.0.2/bin/sparcv9-sun-%{sol_os}-g++ ./configure --includedir=/usr/local/include --with-NOSTREAMIO
%else
./configure --includedir=/usr/local/include --with-NOSTREAMIO --includedir=/usr/local/include 
%endif

sed s/'-Dconst= -Dinline='/' '/g Makefile > Makefile.ru
mv Makefile.ru Makefile
make

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/local/lib
mkdir -p %{buildroot}/usr/local/include
cp factor.h %{buildroot}/usr/local/include
cp libfac.a %{buildroot}/usr/local/lib

%clean
rm -rf %{buildroot}

%files
%defattr(-,bin,bin)
/usr/local/include/factor.h
/usr/local/lib/libfac.a
