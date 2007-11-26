%include machine-header.spec

Name: db4
Version: 4.6.21
Copyright: BSD
Group: Development/Libraries
Summary: Berkeley DB libraries
Release: 1
Source: db-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-root

%description
Berkeley DB is an embedded database system that supports keyed access
to data. The software is distributed in source code form, and
developers can compile and link the source code into a single library
for inclusion directly in their applications.

   [from the documentation]

%package tools
Group: Development/Tools
Summary: Berkeley DB extra tools
Requires: %{name} = %{version}

%description tools
This package contains the tools for db.

%package devel
Group: Development/Headers
Summary: includes for db4
Requires: %{name} = %{version}

%description devel
includes for db4

%package doc
Group: Documentation
Summary: Berkeley DB documentation
Requires: %{name} = %{version}

%description doc
This package contains the documentation tree for db.

%prep
%setup -q -n db-%{version}

%build
%ifarch sparc64
cd build_unix

PATH="/opt/SUNWspro/bin:${PATH}" \
CC="cc -xarch=v9" CXX="CC -xarch=v9" CPPFLAGS="-I/usr/local/include" \
CFLAGS="-g -xs" \
LD="/usr/ccs/bin/ld" \
LDFLAGS="-L/usr/local/lib/sparcv9 -R/usr/local/lib/sparcv9"
export PATH CC CXX CPPFLAGS LD LDFLAGS

../dist/configure \
	--enable-compat185 \
	--disable-nls \
	--prefix=/usr/local

gmake -j3

umask 022
mkdir -p sparcv9/lib
mkdir -p sparcv9/bin
cd .libs/
ln -s libdb-4.6.so libdb-4.so
cd ../
mv .libs/*.so sparcv9/lib/
mv .libs/*.a sparcv9/lib/
mv .libs/db_* sparcv9/bin/
rm sparcv9/bin/*.o

gmake distclean

cd ..
%endif
cd build_unix

PATH="/opt/SUNWspro/bin:${PATH}" \
CC="cc" CXX="CC" CPPFLAGS="-I/usr/local/include" \
CFLAGS="-g -xs" \
LD="/usr/ccs/bin/ld" \
LDFLAGS="-L/usr/local/lib -R/usr/local/lib"
export PATH CC CXX CPPFLAGS LD LDFLAGS

../dist/configure \
	--enable-compat185 \
	--disable-nls \
	--prefix=/usr/local
gmake -j3

%install
cd build_unix
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/local/
gmake install prefix=%{buildroot}/usr/local/
mkdir -p %{buildroot}/usr/local/include/db4 %{buildroot}/usr/local/db4/
mv %{buildroot}/usr/local/bin %{buildroot}/usr/local/db4/
mv %{buildroot}/usr/local/include/*.h %{buildroot}/usr/local/include/db4/
rm -f %{buildroot}/usr/local/lib/libdb.a

%ifarch sparc64
umask 022
mkdir -p %{buildroot}/usr/local/lib/sparcv9
mkdir -p %{buildroot}/usr/local/db4/bin/sparcv9
install -m 0644 sparcv9/lib/* %{buildroot}/usr/local/lib/sparcv9
install -m 0755 sparcv9/bin/* %{buildroot}/usr/local/db4/bin/sparcv9
%endif

rm %{buildroot}/usr/local/lib/*.la

%clean
rm -rf %{buildroot}

%post
cat <<EOF
EOF

%files
%defattr(-,root,bin)
/usr/local/lib/libdb-4*.so
%ifarch sparc64
/usr/local/lib/sparcv9/libdb-4*.so
%endif

%files devel
%defattr(-,root,bin)
/usr/local/include/db4/*
/usr/local/lib/libdb-4*.a
%ifarch sparc64
/usr/local/lib/sparcv9/libdb-4*.a
%endif

%files tools
%defattr(-,root,bin)
# prevent globbing the sparcv9, breaks sol9-64 with rpm 4.2.1
/usr/local/db4/bin/db* 
%ifarch sparc64
/usr/local/db4/bin/sparcv9/*
%endif

%files doc
%defattr(-,root,bin)
%doc docs
# missing from -4 build
%doc /usr/local/docs

%changelog
* Sun Nov 25 2007 David Lee Halik <dhalik@nbcs.rutgers.edu> - 4.6.21
- Bump to 4.6.21
