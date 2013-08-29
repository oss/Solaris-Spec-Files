%define apver 2.2.13
%define apache_prefix %{_prefix}/apache2-%{apver}

Name:		apache2-module-mod_auth_pam
Version:	1.1.1
Release:	2	
Group:		Applications/Internet
License:	Unknown
Source:		http://pam.sourceforge.net/mod_auth_pam/dist/mod_auth_pam-2.0-%{version}.tar.gz
Patch:		mod_auth_pam-2.0-1.1.1-rutgers.patch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root

Requires:	apache2 = %{apver}
BuildRequires:	apache2-devel = %{apver}

Provides:       mod_auth_pam

Summary:        Apache module for PAM authentication

%description
mod_auth_pam is an Apache module that provides PAM authentication support.

%prep
%setup -q -n mod_auth_pam
%patch -p1

%build
PATH="%{apache_prefix}/bin:${PATH}"
export PATH
gmake -j3

echo "..... mod_auth_pam configuration instructions .....

Add each of these lines in their appropriate location in httpd.conf:
  LoadModule pam_auth_module    libexec/mod_auth_pam.so
  AddModule mod_auth_pam.c

Add appropriate lines to /etc/pam.conf, for example:
  # httpd
  httpd  auth     required  /usr/lib/security/pam_ru.so.2 debug save
  httpd  account  required  /usr/lib/security/pam_ru.so.2 debug
  httpd  session  required  /usr/lib/security/pam_unix.so.1
  httpd  password required  /usr/lib/security/pam_unix.so.1

Use .htaccess files similiar to:

  AuthPAM_Enabled on
  AuthType Basic
  AuthName pam
  AuthPAM_FallThrough off
  <Limit GET POST PUT>
   require valid-user
  </Limit>" >> mod_auth_pam-install.txt

%install
%{__install} -d %{buildroot}%{_prefix}/apache2-modules
%{__install} -m 0755 .libs/mod_auth_pam.so %{buildroot}%{_prefix}/apache2-modules/

%post
cat << EOF 
..... mod_auth_pam configuration instructions .....

Add each of these lines in their appropriate location in httpd.conf:
  LoadModule pam_auth_module    libexec/mod_auth_pam.so
  AddModule mod_auth_pam.c

Add appropriate lines to /etc/pam.conf, for example:
  # httpd
  httpd  auth     required  /usr/lib/security/pam_ru.so.2 debug save
  httpd  account  required  /usr/lib/security/pam_ru.so.2 debug
  httpd  session  required  /usr/lib/security/pam_unix.so.1
  httpd  password required  /usr/lib/security/pam_unix.so.1

Use .htaccess files similiar to:

  AuthPAM_Enabled on
  AuthType Basic
  AuthName pam
  AuthPAM_FallThrough off
  <Limit GET POST PUT>
   require valid-user
  </Limit>

EOF

%files
%defattr(-, root, root)
%doc mod_auth_pam-install.txt
%{_prefix}/apache2-modules/mod_auth_pam.so

%changelog
* Wed Aug 12 2009 Naveen Gavini <ngavini@nbcs.rutgers.edu> - 1.1.1-2
- Updated for new apache
* Mon Jul 20 2009 Brian Schubert <schubert@nbcs.rutgers.edu> - 1.1.1-1
- Initial build
