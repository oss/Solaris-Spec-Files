%define prefix /usr/local/proctool

Summary: Process monitoring tool
Name: proctool
Version: 1999_04
Release: 1
Group: System Environment/Base
License: Free beer
Source: proctool_%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-root

%description
Proctool is an unsupported tool used for monitoring and controlling
processes on a Solaris system.

%prep
%setup -q -n proctool

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{prefix} %{buildroot}/usr/local/bin
find . | cpio -pdmuv %{buildroot}%{prefix}

cd %{buildroot}%{prefix}
chmod 4755 bin/*/pmon

chmod 0755 bin/proctool
ESCAPED=`echo '%{prefix}' | sed 's/\//\\\\\//g'`
ed bin/proctool <<EOF
    /^INSTALLDIR=/s/\$/$ESCAPED/
    w
    q
EOF
install -m 0755 bin/proctool %{buildroot}/usr/local/bin/proctool

%clean
rm -rf %{buildroot}

%post
cat <<EOF
To use proctool you may have to remove the '*Font*' entries from your
X resource database.
EOF

%files
%defattr(-, root, bin)
%{prefix}
/usr/local/bin/proctool