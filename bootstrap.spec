%define in_prefix /usr/local/lib/rpm/bootstrap

Summary: RPM bootstrap scripts
Name: bootstrap
Version: 2001.12.17
Release: 1
Group: System Environment/Base
Copyright: Rutgers
Source: %{name}-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-root

Requires: perl

%description
This package contains the scripts used to bootstrap RPM on Solaris.
You do not need to install this to bootstrap RPM, but you may wish to
install this if you have upgraded, installed, or removed Solaris
packages.

%prep
%setup -q
rm melty-perl.cpio.Z

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{in_prefix}
cp -pr . %{buildroot}%{in_prefix}

mkdir -p %{buildroot}/usr/local/sbin
cat <<EOF > %{buildroot}/usr/local/sbin/update-rpm-database
#!/bin/sh

cd %{in_prefix} && sh update-rpm-database.sh
EOF
chmod 700 %{buildroot}/usr/local/sbin/update-rpm-database

%files
%defattr(-, root, bin)
%{in_prefix}
/usr/local/sbin/update-rpm-database
