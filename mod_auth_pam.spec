%define apver 1.3.29

Summary: Apache module for PAM authentication
Name: apache-module-mod_auth_pam
Version: 1.1.1
Release: 6
Group: Applications/Internet
License: Unknown
Source: http://pam.sourceforge.net/mod_auth_pam/dist/mod_auth_pam-1.1.1.tar.gz
Patch0: mod_auth_pam-rutgers.patch
Patch1: mod_auth_pam-rutgers2.patch
Patch2: mod_auth_pam-rutgers3.patch
Patch3: mod_auth_pam-linebreakfix.patch
BuildRoot: /var/tmp/%{name}-root
Conflicts: pam2 < 4.2
Provides: mod_auth_pam
Obsoletes: mod_auth_pam

%define apache_prefix /usr/local/apache-%{apver}

BuildRequires: apache = %{apver} apache-devel = %{apver}
Requires: apache 

%description
Lets you define macros for use in apache's configuration files.

%prep
%setup -q -n mod_auth_pam-%{version}
%patch0 -p0
%patch1 -p0
%patch2 -p1
%patch3 -p1

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
mkdir -p /var/tmp/%{name}-root/usr/local/apache-modules/
cp mod_auth_pam.so /var/tmp/%{name}-root/usr/local/apache-modules/

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
/usr/local/apache-modules/mod_auth_pam.so
