%define apver 1.3.37

Summary: Apache module for PAM authentication
Name: apache-module-mod_auth_ldap_clh
Version: 1
Release: 9
Group: Applications/Internet
License: Unknown
Source: mod_auth_ldap_clh.tar.gz
BuildRoot: /var/tmp/%{name}-%{release}-root
BuildRequires: apache, apache-devel, openldap-lib >= 2.3
Requires: openldap-lib >= 2.3, apache
Conflicts: mod_auth_ldap 

%define apache_prefix /usr/local/apache-%{apver}

%description
Hedrick special mod_auth_ldap code. 

%prep
%setup -n mod_auth_ldap 

%build


PATH="%{apache_prefix}/bin:/opt/SUNWspro/bin:${PATH}" \
CC="cc" CXX="CC" CPPFLAGS="-I/usr/local/include" \
LD="/usr/ccs/bin/ld" \
LDFLAGS="-L/usr/local/lib -R/usr/local/lib -L/usr/ucblib -R/usr/ucblib"
export PATH CC CXX CPPFLAGS LD LDFLAGS

make clean
rm mod_auth_ldap.so
cc -DSOLARIS2=290 -DMOD_SSL=208115 -DEAPI -DEAPI_MM -I/usr/local/BerkeleyDB.3.3/include/ -Kpic -DSHARED_MODULE -I/usr/local/apache-%{apver}/include  -c mod_auth_ldap.c
ld -G $LDFLAGS -o mod_auth_ldap.so mod_auth_ldap.o -lldap

%install
mkdir -p $RPM_BUILD_ROOT/usr/local/apache-modules
mkdir -p $RPM_BUILD_ROOT/usr/local/share/mod_auth_ldap_clh
cp mod_auth_ldap.so $RPM_BUILD_ROOT/usr/local/apache-modules
chmod 755 $RPM_BUILD_ROOT/usr/local/apache-modules/mod_auth_ldap.so
cp README.RUTGERS $RPM_BUILD_ROOT/usr/local/share/mod_auth_ldap_clh


%post
cat << EOF 
For more information about this package, please see the documentation
directory at /usr/local/share/mod_auth_ldap_clh.

EOF
%files
%defattr(-,root,other)
/usr/local/share/mod_auth_ldap_clh/README.RUTGERS
/usr/local/apache-modules/mod_auth_ldap.so

%changelog
* Mon Aug 13 2007 David Lee Halik <dhalik@nbcs.rutgers.edu> - 1-9
- Fixed ldap R path
* Mon Aug 13 2007 David Lee Halik <dhalik@nbcs.rutgers.edu> - 1-8
- Fixing ucb again
* Mon Aug 13 2007 David Lee Halik <dhalik@nbcs.rutgers.edu> - 1-7
- Respun against the proper compiler
* Thu Aug 09 2007 David Lee Halik <dhalik@nbcs.rutgers.edu> - 1-6
- Respun against openldap-lib 2.3
