Name: db3.3
Version: 3.3.11
Copyright: BSD 
Group: Development/Libraries
Summary: Berkeley DB libraries
Release: 2
Source: db-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-root
Requires: tcl
BuildRequires: tcl

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
%setup -q -n db-%{version}

%build
PATH="/opt/SUNWspro/bin:${PATH}" \
CC="cc" CXX="CC" CPPFLAGS="-I/usr/local/include" \
LD="/usr/ccs/bin/ld" \
LDFLAGS="-L/usr/local/lib -R/usr/local/lib" \
export PATH CC CXX CPPFLAGS LD LDFLAGS

cd build_unix
../dist/configure --enable-tcl --with-tcl=/usr/local/lib
make

%install
cd build_unix
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/local/BerkeleyDB.3.3
make install prefix=%{buildroot}/usr/local/BerkeleyDB.3.3

%clean
rm -rf %{buildroot}

%post
cat <<EOF
You may wish to link /usr/local/BerkeleyDB.3.3 to /usr/local/BerkeleyDB.
EOF

%files
%defattr(-,root,bin)
/usr/local/BerkeleyDB.3.3

%files doc
%defattr(-,root,bin)
%doc docs
