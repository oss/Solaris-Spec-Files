Name:		oaf
Summary:	Object activation framework for GNOME
Version: 	0.5.1
Release: 2
Copyright: 	GPL
Group:		System Environment/Libraries
Source: 	%{name}-%{version}.tar.gz
URL: 		http://www.gnome.org/
BuildRoot:	/var/tmp/%{name}-root

%description
OAF is an object activation framework for GNOME. It uses ORBit.

%package devel
Summary:	Libraries and include files for OAF
Group:		Development/Libraries
Requires:	oaf = %{PACKAGE_VERSION}

%description devel

%prep
%setup -q

%build
LD="/usr/ccs/bin/ld -L/usr/local/lib -R/usr/local/lib" \
 LDFLAGS="-L/usr/local/lib -R/usr/local/lib" \
 CPPFLAGS="-I/usr/local/include" ./configure --prefix=/usr/local \
 --sysconfdir=/etc
make


%install
rm -rf $RPM_BUILD_ROOT

make prefix=$RPM_BUILD_ROOT/usr/local sysconfdir=$RPM_BUILD_ROOT/etc install

for FILE in "$RPM_BUILD_ROOT/bin/*"; do
    file "$FILE" | grep -q not\ stripped && strip $FILE
done

for FILE in $RPM_BUILD_ROOT/etc/oaf/* ; do
    mv $FILE $FILE.rpm
done

%post
cat <<EOF
You need to edit and copy the files in /etc/oaf.
EOF

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(0555, bin, bin)
%doc AUTHORS COPYING ChangeLog NEWS README
/etc/oaf/*.rpm
/usr/local/bin/oaf-client
/usr/local/bin/oaf-config
/usr/local/bin/oaf-run-query
/usr/local/bin/oaf-slay
/usr/local/bin/oaf-sysconf
/usr/local/bin/oafd
/usr/local/lib/*.0
/usr/local/lib/*.sh
/usr/local/lib/*.so

%defattr (0444, bin, bin)
/usr/local/share/idl/*.idl
/usr/local/lib/locale/*/LC_MESSAGES/*.mo
/usr/local/share/oaf/*.oafinfo

%files devel

%defattr(0555, bin, bin)
%dir /usr/local/include/liboaf
/usr/local/lib/*.la

%defattr(0444, bin, bin)
/usr/local/include/liboaf/*.h
/usr/local/share/aclocal/*.m4
