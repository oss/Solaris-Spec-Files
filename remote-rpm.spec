Summary: Remote RPM management tool
Name: remote-rpm
Version: 9.13.2001
Release: 1
Copyright: Rutgers
Group: Applications/Productivity
Source: %{name}-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-root
Requires: perl openssh

%description
Remote-rpm lets you build RPMs on several machines at once using ssh.

%prep
%setup -q

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/local/bin %{buildroot}/usr/local/etc
sh install %{buildroot}
install -m 0644 buildmachinetab %{buildroot}/usr/local/etc/buildmachinetab.rpm

%clean
rm -rf %{buildroot}

%post
cat <<EOF

Edit and copy /usr/local/etc/buildmachinetab.rpm.  You may have to
change the defaults in /usr/local/bin/remote_rpm.  Currently
documentation is included with the build-repository package.

EOF
if [ ! -x /usr/local/bin/perl ]; then
    echo "You need to link perl to /usr/local/bin/perl."
fi

%files
%defattr(-, root, bin)
/usr/local/bin/remote_rpm
/usr/local/etc/buildmachinetab.rpm
