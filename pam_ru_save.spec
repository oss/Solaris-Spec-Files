Name: pam_ru_save
Version: 1.0
Copyright: Rutgers
Group: System Environment/Base
Summary: Rutgers PAM module caching Enigma passwords
Release: 1
Source: %{name}-%{version}.tar.gz
BuildRoot: /var/tmp/%{name}-root
BuildRequires: vpkg-SPROcc

%description
This package provide PAM authentication for caching Enigma passwords.

%prep
%setup -q

%build
CC=cc make

%install
mkdir -p %{buildroot}/usr/local/etc
mkdir -p %{buildroot}/usr/local/lib
cp pam.conf.example %{buildroot}/usr/local/etc
cp pam_ru_save.so.%{version} %{buildroot}/usr/local/lib
cp pam_ru_store.so.%{version} %{buildroot}/usr/local/lib
cd %{buildroot}/usr/local/lib
ln -sf pam_ru_save.so.%{version} pam_ru_save.so.1
ln -sf pam_ru_store.so.%{version} pam_ru_store.so.1

%clean
rm -rf $RPM_BUILD_ROOT

%post
cat <<EOF

EOF

%files
%defattr(-,root,root)
/usr/local/lib/pam_ru_save.so.%{version}
/usr/local/lib/pam_ru_store.so.%{version}
/usr/local/lib/pam_ru_save.so.1
/usr/local/lib/pam_ru_store.so.1
/usr/local/etc/pam.conf.example
