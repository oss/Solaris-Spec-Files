Summary: OpenOffice.org office suite
Name: openoffice.org
Version: 1.0.1
Release: 3ru
Group: System Environment/Base
Copyright: GPL
Source: oo-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-root
Provides: openoffice

%description
OpenOffice.org office suite.

%prep
%setup -q -n OpenOffice.org1.0

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/local/bin
cd ..
mv OpenOffice.org1.0 %{buildroot}/usr/local/


cat > %{buildroot}/usr/local/bin/ooffice << EOF
#!/bin/sh
exec /usr/local/OpenOffice.org1.0/program/soffice $*
EOF
chmod +x %{buildroot}/usr/local/bin/ooffice


ln -sf ooffice %{buildroot}/usr/local/bin/openoffice
ln -sf ooffice %{buildroot}/usr/local/bin/soffice

# Install component wrapper scripts
for app in agenda calc draw fax impress label letter master math memo vcard writer padmin; do
cat > %{buildroot}/usr/local/bin/oo${app} << EOF
#!/bin/sh
exec /usr/local/OpenOffice.org1.0/program/s${app} $*
EOF
chmod +x %{buildroot}/usr/local/bin/oo${app}
done

ln -sf oowriter %{buildroot}/usr/local/bin/writer
ln -sf oowriter %{buildroot}/usr/local/bin/swriter

%files
#%attr(0755, root, bin) /usr/local/bin/zap
#%attr(0644, root, bin) /usr/local/man/man1/zap.1
/usr/local/OpenOffice.org1.0
/usr/local/bin/*