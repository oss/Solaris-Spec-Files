Name: pam_ru_become
Version: 1.0
Copyright: Rutgers
Group: System Environment/Base
Summary: Rutgers PAM module for become accounts
Release: 1
Source: %{name}-%{version}.tar.gz
BuildRoot: /var/tmp/%{name}-root
BuildRequires: vpkg-SPROcc

%description
This package provide PAM authentication for Rutgers' become accounts.

%prep
%setup -q

%build
CC=cc make

%install
mkdir -p %{buildroot}/usr/local/etc
mkdir -p %{buildroot}/usr/local/lib
cp pam.conf.example %{buildroot}/usr/local/etc
cp pam_ru_become.so.%{version} %{buildroot}/usr/local/lib
cd %{buildroot}/usr/local/lib
ln -sf pam_ru_become.so.%{version} pam_ru_become.so.1

%clean
rm -rf $RPM_BUILD_ROOT

%post
cat << EOF

EOF

%files
%defattr(-,root,root)
/usr/local/lib/pam_ru_become.so.%{version}
/usr/local/lib/pam_ru_become.so.1
/usr/local/etc/pam.conf.example
