Summary: OpenOffice.org office suite
Name: openoffice.org
Version: 1.0.0
Release: 1
Group: System Environment/Base
Copyright: GPL
Source: oo-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-root


%description
OpenOffice.org office suite.

%prep
%setup -q -n OpenOffice.org1.0

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/local/
cd ..
mv OpenOffice.org1.0 %{buildroot}/usr/local/
mkdir OpenOffice.org1.0

%clean
rm -rf %{buildroot}

%post
cat <<EOF
Each user will need to do a (small) local install to run OpenOffice.org.
They will need to run:    /usr/local/OpenOffice.org1.0/setup
EOF

%files
#%attr(0755, root, bin) /usr/local/bin/zap
#%attr(0644, root, bin) /usr/local/man/man1/zap.1
/usr/local/OpenOffice.org1.0