Summary: MSWord .doc viewer
Name: catdoc
Version: 0.90.3
Release: 2
Group: Applications/Text
Copyright: GPL
Source: catdoc-%{version}.tar.gz
BuildRoot: /var/tmp/%{name}-root

%description
Catdoc is a viewer for MS-Word .doc files.

%prep
%setup -q

%build
LD="/usr/ccs/bin/ld -L/usr/local/lib -R/usr/local/lib" \
 LDFLAGS="-L/usr/local/lib -R/usr/local/lib" CPPFLAGS="-I/usr/local/include" \
 ./configure --prefix=/usr/local --sysconfdir=/etc
make

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/local
make install prefix=$RPM_BUILD_ROOT/usr/local sysconfdir=$RPM_BUILD_ROOT/etc

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,bin,bin)
%doc COPYING README TODO NEWS
/usr/local/bin/catdoc
/usr/local/bin/wordview
/usr/local/man/man1/catdoc.1
/usr/local/lib/catdoc
