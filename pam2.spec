Name: pam2
Version: 2.2
Copyright: Rutgers
Group: System Environment/Base
Summary: pam libraries
Release: 2
Source: %{name}-%{version}.tar.gz
BuildRoot: /var/tmp/%{name}-root
BuildRequires: vpkg-SPROcc

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
mkdir -p %{buildroot}/usr/local/lib
mkdir -p %{buildroot}/usr/local/man/man5
mkdir -p %{buildroot}/etc
mkdir -p %{buildroot}/var/spool/save-cache
mkdir -p %{buildroot}/usr/local/sbin
cp pam_ru.so.2.%{version} %{buildroot}/usr/lib/security
cp pam_ru.5 %{buildroot}/usr/local/man/man5
cp krb_crypt.so rval_crypt.so %{buildroot}/usr/local/lib
cp pam.conf.example %{buildroot}/etc
cp testpam %{buildroot}/usr/local/sbin
cd %{buildroot}/usr/lib/security
ln -sf pam_ru.so.2.%{version} pam_ru.so.2

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%dir /var/spool/save-cache
/etc/pam.conf.example
/usr/local/man/man5/pam_ru.5
/usr/local/lib/krb_crypt.so
/usr/local/lib/rval_crypt.so
/usr/lib/security/pam_ru.so.2.%{version}
/usr/lib/security/pam_ru.so.2
/usr/local/sbin/testpam
