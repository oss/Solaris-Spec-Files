Name: db
Version: 3.1.17
Copyright: BSD 
Group: Development/Libraries
Summary: Berkeley DB libraries
Release: 5
Source: db-%{version}.tar.gz
BuildRoot: /var/tmp/%{name}-root

%description
Berkeley DB is an embedded database system that supports keyed access
to data. The software is distributed in source code form, and
developers can compile and link the source code into a single library
for inclusion directly in their applications.

   [from the documentation]

%package doc
Group: Documentation
Summary: Berkeley DB documentation

%description doc
This package contains the documentation tree for db.

%prep
%setup -q

%build
cd build_unix
LD="/usr/ccs/bin/ld" CC="gcc" \
     LDFLAGS="-L/usr/local/lib -R/usr/local/lib -R/usr/ucblib" \
    ../dist/configure --enable-compat185 --enable-test --prefix=/usr/local \
    --enable-shared
make

# Unfortunately, we can't build shared and static libraries in the same build.

rm config.cache
LD="/usr/ccs/bin/ld" CC="gcc" \
     LDFLAGS="-L/usr/local/lib -R/usr/local/lib -R/usr/ucblib" \
    ../dist/configure --enable-compat185 --enable-test --prefix=/usr/local \
    --disable-shared
make

%install
cd build_unix
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/local/
../dist/configure --enable-compat185 --enable-test --prefix=/usr/local \
    --enable-shared
make install prefix=$RPM_BUILD_ROOT/usr/local

../dist/configure --enable-compat185 --enable-test --prefix=/usr/local
make install prefix=$RPM_BUILD_ROOT/usr/local

mkdir -p $RPM_BUILD_ROOT/usr/local/include/db3
ln -s ../db.h $RPM_BUILD_ROOT/usr/local/include/db3/db.h

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,bin,bin)
/usr/local/include/*
/usr/local/lib/lib*a
/usr/local/lib/lib*.so*
/usr/local/bin/*

%files doc
%defattr(-,bin,bin)
%doc docs
