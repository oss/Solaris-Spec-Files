Name: sgmltools-lite
Version: 3.0.0
Release: 3
Summary: Tools for SGML files
License: GPL
Group: Documentation
Source: sgmltools-lite-3.0.0.tar.gz
Requires: python
BuildRoot: /var/tmp/%{name}-root

%description
SGMLtools are a set of tools for working with SGML files.

%prep
%setup -q

%build
./configure

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/local/bin
for i in sgmltools buildcat gensgmlenv sgmlwhich ; do
    install -m 0755 -c bin/$i $RPM_BUILD_ROOT/usr/local/bin/$i
done
umask 022
mkdir -p $RPM_BUILD_ROOT/usr/local/share/sgml/stylesheets/sgmltools
for i in dsssl/*.dsl dsssl/*.cat ; do
    install -c -m 0644 $i \
    $RPM_BUILD_ROOT/usr/local/share/sgml/stylesheets/sgmltools
done
mkdir -p $RPM_BUILD_ROOT/usr/local/man/man1
install -c -m 0644 man/sgmltools.1 $RPM_BUILD_ROOT/usr/local/man/man1
mkdir -p $RPM_BUILD_ROOT/usr/local/share/sgml/misc/sgmltools/site-backends
mkdir -p $RPM_BUILD_ROOT/usr/local/share/sgml/misc/sgmltools/python/backends
for i in python/*.py ; do
    install -c -m 0644 $i \
    $RPM_BUILD_ROOT/usr/local/share/sgml/misc/sgmltools/python
done
for i in python/backends/* ; do
    install -c -m 0644 $i \
    $RPM_BUILD_ROOT/usr/local/share/sgml/misc/sgmltools/python/backends
done
mkdir -p $RPM_BUILD_ROOT/etc/sgml
install -c -m 0644 aliases $RPM_BUILD_ROOT/etc/sgml/aliases.rpm

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
/usr/local/bin/buildcat
/usr/local/bin/gensgmlenv
/usr/local/bin/sgmltools
/usr/local/bin/sgmlwhich
/usr/local/share/sgml/stylesheets/sgmltools
/usr/local/share/sgml/misc/sgmltools
/usr/local/man/man1/sgmltools.1
/etc/sgml/aliases.rpm
