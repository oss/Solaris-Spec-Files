%define apver 1.3.31

Summary: Apache module for PAM authentication
Name: apache-module-mod_auth_ldap
Version: 2.4.2
Release: 0
Group: Applications/Internet
License: Unknown
Source: mod_auth_ldap.tar.gz
BuildRoot: /var/tmp/%{name}-root
Conflicts: mod_auth_ldap_clh 

%define apache_prefix /usr/local/apache-%{apver}

BuildRequires: apache apache-devel
Requires: openldap-lib apache

%description
Apache module for PAM authentication 

%prep
%setup -n mod_auth_ldap 

%build
PATH=%{apache_prefix}/bin:$PATH
export PATH
make clean
gcc -DSOLARIS2=290 -DMOD_SSL=208115 -DEAPI -DEAPI_MM -I/usr/local/BerkeleyDB.3.3/include/ -fPIC -DSHARED_MODULE -I/usr/local/apache-%{apver}/include  -c mod_auth_ldap.c
ld -G -o mod_auth_ldap.so mod_auth_ldap.o -R/usr/local/lib -L/usr/local/lib -lldap

%install
mkdir -p $RPM_BUILD_ROOT/usr/local/apache-modules
mkdir -p $RPM_BUILD_ROOT/usr/local/share/mod_auth_ldap
cp mod_auth_ldap.so $RPM_BUILD_ROOT/usr/local/apache-modules
chmod 755 $RPM_BUILD_ROOT/usr/local/apache-modules/mod_auth_ldap.so
#cp README.RUTGERS $RPM_BUILD_ROOT/usr/local/share/mod_auth_ldap


%post
cat << EOF 
For more information about this package, please see the documentation
directory at /usr/local/share/mod_auth_ldap.

EOF
%files
%defattr(-,root,other)
#/usr/local/share/mod_auth_ldap_clh/README.RUTGERS
/usr/local/apache-modules/mod_auth_ldap.so

%changelog
* Tue Nov 30 2004 Leo Zhadanovsky <leozh@nbcs.rutgers.edu>
 - Initial package
