Name: db4
Version: 4.0.14
Copyright: BSD
Group: Development/Libraries
Summary: Berkeley DB libraries
Release: 2ru
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
cd build_unix
../dist/configure --enable-compat185 --disable-nls --prefix=
make

%install
cd build_unix
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/local/
make install prefix=%{buildroot}/usr/local/
mkdir -p %{buildroot}/usr/local/include/db4
mv %{buildroot}/usr/local/bin %{buildroot}/usr/local/db4/
mv %{buildroot}/usr/local/include/*.h %{buildroot}/usr/local/include/db4/

%clean
rm -rf %{buildroot}

%post
cat <<EOF
EOF

%files
%defattr(-,root,bin)
/usr/local/lib/libdb-4*

%files devel
%defattr(-,root,bin)
/usr/local/include/db4/*

%files tools
%defattr(-,root,bin)
/usr/local/db4/bin/*

%files doc
%defattr(-,root,bin)
%doc docs
