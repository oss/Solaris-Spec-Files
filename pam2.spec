Name: pam2
Version: 1.2
Copyright: Rutgers
Group: System Environment/Base
Summary: pam libraries
Release: 1
Source: %{name}-%{version}.tar.gz
BuildRoot: /var/tmp/%{name}-root
#Provides: pam_ru.so.2
#BuildRequires: vpkg-SPROcc

%description
pam2 provides pam_ru.so.2, which provides Rutgers authentication using 
Kerberos and Enigma. pam_ru.so.2 allows for pam-enabled applications to 
have all of the strange things that Rutgers does with authentication, such as:

become accounts
"save" hack
loginnable group checks
etc.

%prep
%setup -q

%build
CC=cc make

%install
mkdir -p %{buildroot}/usr/lib/security
mkdir -p %{buildroot}/usr/local/lib/security
mkdir -p %{buildroot}/usr/local/man/man5
mkdir -p %{buildroot}/etc
mkdir -p %{buildroot}/var/spool/save-cache
cp pam_ru.so.2.%{version} %{buildroot}/usr/lib/security
cp pam_ru.5 %{buildroot}/usr/local/man/man5
cp krb_crypt.so rval_crypt.so %{buildroot}/usr/local/lib/security
cp pam.conf.example %{buildroot}/etc
cd %{buildroot}/usr/lib/security
ln -sf pam_ru.so.2.%{version} pam_ru.so.2

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
/var/spool/save-cache
/etc/pam.conf.example
/usr/local/man/man5/pam_ru.5
/usr/local/lib/security/krb_crypt.so
/usr/local/lib/security/rval_crypt.so
/usr/lib/security/pam_ru.so.2.1.2
/usr/lib/security/pam_ru.so.2
