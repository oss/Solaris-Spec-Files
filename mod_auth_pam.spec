%define apver 1.3.26

Summary: Apache module for PAM authentication
Name: mod_auth_pam
Version: 1.1.1
Release: %{apver}_3ru
Group: Applications/Internet
License: Unknown
Source: http://pam.sourceforge.net/mod_auth_pam/dist/mod_auth_pam-1.1.1.tar.gz
Patch: mod_auth_pam-rutgers.patch
BuildRoot: /var/tmp/%{name}-root
Conflicts: pam2 < 4.2

%define apache_prefix /usr/local/apache-%{apver}

BuildRequires: apache = %{apver} apache-devel = %{apver}
Requires: apache = %{apver}

%description
Lets you define macros for use in apache's configuration files.

%prep
%setup -q
%patch -p0

%build
PATH=%{apache_prefix}/bin:$PATH
export PATH
make
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
mkdir -p /var/tmp/%{name}-root/usr/local/apache-%{apver}/libexec/
cp mod_auth_pam.so /var/tmp/%{name}-root/usr/local/apache-%{apver}/libexec/

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
%defattr(-,root,other)
%doc mod_auth_pam-install.txt
/usr/local/apache-%{apver}/libexec/mod_auth_pam.so
