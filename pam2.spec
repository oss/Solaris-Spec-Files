Name: pam2
Version: 4.3
Copyright: Rutgers
Group: System Environment/Base
Summary: pam libraries
Release: 1
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

In addition, pam2 provides pam_wheel.so which will allow users in groups slide
to su to root without a password provided the proper options are set (see 
pam.conf.example).

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
cp pam_wheel.so %{buildroot}/usr/lib/security
cd %{buildroot}/usr/lib/security
ln -sf pam_ru.so.2.%{version} pam_ru.so.2

%clean
rm -rf $RPM_BUILD_ROOT

%post
cat <<EOF
If upgrading from a version earlier than 4.2, you must

rm -R /var/spool/save-cache

This is best practice for all upgrades, but not strictly required.

EOF

%files
%defattr(-,root,root)
%dir /var/spool/save-cache
/etc/pam.conf.example
/usr/local/man/man5/pam_ru.5
/usr/local/lib/krb_crypt.so
/usr/local/lib/rval_crypt.so
/usr/lib/security/pam_ru.so.2.%{version}
/usr/lib/security/pam_ru.so.2
/usr/lib/security/pam_wheel.so
/usr/local/sbin/testpam
