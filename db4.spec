%include machine-header.spec

Name: db4
Version: 4.1.24
Copyright: BSD
Group: Development/Libraries
Summary: Berkeley DB libraries
Release: 3ru
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
Summary: Berkeley DB extra toold

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

%build
%ifarch == sparc64
cd build_unix
CC=/usr/local/gcc3/bin/sparcv9-sun-%{sol_os}-gcc \
../dist/configure --enable-compat185 --disable-nls --prefix=
make
umask 022
mkdir -p sparcv9/lib
mkdir -p sparcv9/bin
cd .libs/
ln -s libdb-4.1.so libdb-4.so
cd ../
mv .libs/*.so sparcv9/lib/
mv .libs/*.a sparcv9/lib/
mv .libs/db* sparcv9/bin/
make distclean
cd ..
%endif
cd build_unix
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

%ifarch ==  sparc64
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
/usr/local/lib/libdb-4*
%ifarch == sparc64
/usr/local/lib/sparcv9/libdb-4*
%endif

%files devel
%defattr(-,root,bin)
/usr/local/include/db4/*

%files tools
%defattr(-,root,bin)
/usr/local/db4/bin/*
%ifarch == sparc64
/usr/local/db4/bin/sparcv9/*
%endif

%files doc
%defattr(-,root,bin)
%doc docs
