%define apver 1.3.28

Summary: Apache module for PAM authentication
Name: apache-module-mod_auth_ldap_clh
Version: 1
Release: 2
Group: Applications/Internet
License: Unknown
Source: mod_auth_ldap_clh.tar.gz
BuildRoot: /var/tmp/%{name}-root
Conflicts: mod_auth_ldap 

%define apache_prefix /usr/local/apache-%{apver}

BuildRequires: apache = %{apver} apache-devel = %{apver}
Requires: openldap-lib apache = %{apver}

%description
Hedrick special mod_auth_ldap code. 

%prep
%setup -n mod_auth_ldap 

%build
PATH=%{apache_prefix}/bin:$PATH
export PATH
make clean
rm mod_auth_ldap.so
gcc -DSOLARIS2=290 -DMOD_SSL=208115 -DEAPI -DEAPI_MM -I/usr/local/BerkeleyDB.3.3/include/ -fPIC -DSHARED_MODULE -I/usr/local/apache-1.3.28/include  -c mod_auth_ldap.c
ld -G -o mod_auth_ldap.so mod_auth_ldap.o -R/usr/local/lib -L/usr/local/lib -lldap

%install
mkdir -p $RPM_BUILD_ROOT/usr/local/apache-%{apver}/libexec
mkdir -p $RPM_BUILD_ROOT/usr/local/share/mod_auth_ldap_clh
cp mod_auth_ldap.so $RPM_BUILD_ROOT/usr/local/apache-%{apver}/libexec
chmod 755 $RPM_BUILD_ROOT/usr/local/apache-%{apver}/libexec/mod_auth_ldap.so
cp README.RUTGERS $RPM_BUILD_ROOT/usr/local/share/mod_auth_ldap_clh


%post
cat << EOF 
For more information about this package, please see the documentation
directory at /usr/local/share/mod_auth_ldap_clh.

EOF
%files
%defattr(-,root,other)
/usr/local/share/mod_auth_ldap_clh/README.RUTGERS
/usr/local/apache-%{apver}/libexec/mod_auth_ldap.so
