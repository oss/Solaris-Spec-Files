%define name mod_auth_radius
%define version 1.5.4
%define release 1
%define prefix /usr/local
%define apver 1.3.26
%define apache_prefix /usr/local/apache

Summary: Radius server authorization extension to Apache 
Name: %{name} 
Version: %{version}
Release: %{release} 
Group: Applications/Internet
License: BSD-type
Source: %{name}-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-root
BuildRequires: apache = 1.3.26
Requires: apache = %{apver} 

%description
mod_auth_radius allows users to request authentication via a Radius server.
Users can request that access to a directory require authentication
via radius by putting these commands in .htaccess.

%prep
%setup
%build

make clean
make APXS="/usr/local/apache-%{apver}/bin/apxs" GLIBDIR=
cd ..

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/local/apache-%{apver}/libexec
install -c -m 0755 mod_auth_radius.so $RPM_BUILD_ROOT/usr/local/apache-%{apver}/libexec

%clean
rm -rf $RPM_BUILD_ROOT

%post
cat <<EOF
If you are hoping this was the Rutgers hacked mod_auth_radius you are mistaken.
To get that rpm:
1)apt-get remove mod_auth_radius
2)apt-get install mod_auth_radius_RU
EOF

%files
%defattr(-,root,other)
%defattr(-,root,other)
%doc README
/usr/local/apache-%{apver}/libexec/mod_auth_radius.so



