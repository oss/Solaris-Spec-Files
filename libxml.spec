Summary: libXML library
Name: libxml
Version: 1.8.10
Release: 2
Group: LGPL
Copyright: Development/Libraries
Source: libxml-%{version}.tar.gz
BuildRoot: /var/tmp/%{name}-root
Provides: libxml.so
Provides: libxml.so.1
Requires: readline
Requires: zlib
BuildRequires: readline-devel
BuildRequires: zlib-devel
BuildRequires: autoconf

%description
This library allows you to manipulate XML files.

%package devel
Summary: Libraries, includes, etc to develop libxml applications
Group: Development/Libraries
Requires: libxml = %{version}

%description devel
Libraries, include files, etc you can use to develop libxml applications.

%package docs
Summary: LibXML documentation
Group: Documentation

%description docs
Documentation for libxml (located in /usr/local/share/gnome-xml)

%prep
%setup -q

%build
autoconf
LD="/usr/ccs/bin/ld -L/usr/local/lib -R/usr/local/lib" \
    LDFLAGS="-L/usr/local/lib -R/usr/local/lib" ./configure \
     --enable-shared --enable-static --with-zlib=/usr/local
make

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/local
make install prefix=$RPM_BUILD_ROOT/usr/local

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,bin,bin)
%doc AUTHORS ChangeLog NEWS README COPYING COPYING.LIB TODO
/usr/local/lib/lib*.so*

%files devel
%defattr(-,bin,bin)
/usr/local/lib/lib*a
/usr/local/lib/*.sh
/usr/local/bin/xml-config
/usr/local/include/gnome-xml

%files docs
%defattr(-,bin,bin)
/usr/local/share/gnome-xml
