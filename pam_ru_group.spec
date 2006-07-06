Name: pam_ru_group
Version: 1.0
Copyright: Rutgers
Group: System Environment/Base
Summary: Rutgers PAM module for group checking
Release: 2
Source: %{name}-%{version}.tar.gz
BuildRoot: /var/tmp/%{name}-root
BuildRequires: vpkg-SPROcc

%description
This package provides a PAM module for group checking.

%prep
%setup -q

%build
CC=cc make

%install
mkdir -p %{buildroot}/etc
mkdir -p %{buildroot}/usr/local/lib
cp pam.conf.group %{buildroot}/etc
cp pam_ru_group.so.%{version} %{buildroot}/usr/local/lib
cd %{buildroot}/usr/local/lib
ln -sf pam_ru_group.so.%{version} pam_ru_group.so.1

%clean
rm -rf $RPM_BUILD_ROOT

%post
cat << EOF

Please refer to /etc/pam.conf.group for instructions and examples of how to use
this module.

EOF

%files
%defattr(-,root,root)
/usr/local/lib/pam_ru_group.so.%{version}
/usr/local/lib/pam_ru_group.so.1
/etc/pam.conf.group
