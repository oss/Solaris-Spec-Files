%include machine-header.spec

Name: db4
Version: 4.2.52
Copyright: BSD
Group: Development/Libraries
Summary: Berkeley DB libraries
Release: 5
Source: db-%{version}.tar.gz
Patch0: http://www.sleepycat.com/update/4.2.52/patch.4.2.52.1
Patch1: http://www.sleepycat.com/update/4.2.52/patch.4.2.52.2
Patch2: http://www.sleepycat.com/update/4.2.52/patch.4.2.52.3
Patch3: http://www.sleepycat.com/update/4.2.52/patch.4.2.52.4
Patch4: db4-4.2.52-longtxn.patch
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

%description tools
This package contains the tools for db.

%package devel
Group: Development/Headers
Summary: includes for db4

%description devel
includes for db4

%package doc
Group: Documentation
Summary: Berkeley DB documentation

%description doc
This package contains the documentation tree for db.

%prep
%setup -q -n db-%{version}

%patch0
%patch1 
%patch2
%patch3
%patch4 -p1

%build
%ifarch sparc64
cd build_unix
# I have no idea why -xarch is an LDFLAGS. But it's necessary.
CC=/opt/SUNWspro/bin/cc CFLAGS='-xarch=v9 -g -xs' \
LDFLAGS="-R/usr/local/lib/sparcv9 -xarch=v9" \
../dist/configure --enable-compat185 --disable-nls --prefix=
make
umask 022
mkdir -p sparcv9/lib
mkdir -p sparcv9/bin
cd .libs/
ln -s libdb-4.2.so libdb-4.so
cd ../
mv .libs/*.so sparcv9/lib/
mv .libs/*.a sparcv9/lib/
mv .libs/db_* sparcv9/bin/
# strange, this didn't used to happen...
rm sparcv9/bin/*.o
make distclean
cd ..
%endif
cd build_unix
CC=/opt/SUNWspro/bin/cc CFLAGS='-g -xs' \
LDFLAGS="-R/usr/local/lib" \
../dist/configure --enable-compat185 --disable-nls --prefix=
make

%install
cd build_unix
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/local/
make install prefix=%{buildroot}/usr/local/
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