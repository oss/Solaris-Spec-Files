Summary: Remote RPM management tool
Name: remote-rpm-bs
Version: 1
Release: 1ru
Copyright: Rutgers
Group: Applications/Productivity
Source: remote-rpm.tar.bz2
BuildRoot: %{_tmppath}/%{name}-root
Requires: openssh

%description
Remote-rpm lets you build RPMs on several machines at once using ssh.

%prep
%setup -q -n remote-rpm

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/local/bin %{buildroot}/usr/local/etc
cp quickbuild %{buildroot}/usr/local/bin/quickbuild
cp remote_rpm2 %{buildroot}/usr/local/bin/remote_rpm
cp buildmachinetab2 %{buildroot}/usr/local/etc/buildmachinetab
chmod 755 %{buildroot}/usr/local/bin/*
chmod 644 %{buildroot}/usr/local/etc/buildmachinetab

%clean
rm -rf %{buildroot}

%files
%defattr(-, root, bin)
/usr/local/bin/remote_rpm
/usr/local/etc/buildmachinetab
/usr/local/bin/quickbuild