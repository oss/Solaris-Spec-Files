Name: pam_ru_prompt
Version: 1.0
Copyright: Rutgers
Group: System Environment/Base
Summary: Rutgers PAM module for prompt accounts
Release: 2
Source: %{name}-%{version}.tar.gz
BuildRoot: /var/tmp/%{name}-root
BuildRequires: vpkg-SPROcc

%description
This package provides a common prompt for all services.

%prep
%setup -q

%build
CC=cc make

%install
mkdir -p %{buildroot}/usr/local/etc
mkdir -p %{buildroot}/usr/local/lib
cp pam.conf.prompt %{buildroot}/usr/local/etc
cp pam_ru_prompt.so.%{version} %{buildroot}/usr/local/lib
cd %{buildroot}/usr/local/lib
ln -sf pam_ru_prompt.so.%{version} pam_ru_prompt.so.1

%clean
rm -rf $RPM_BUILD_ROOT

%post
cat << EOF

This PAM module must be stacked on top.  Otherwise, it is useless.

EOF

%files
%defattr(-,root,root)
/usr/local/lib/pam_ru_prompt.so.%{version}
/usr/local/lib/pam_ru_prompt.so.1
/usr/local/etc/pam.conf.prompt
