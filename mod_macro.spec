%define apver 1.3.26
Summary: Apache modules to allow macros in apache config files
Name: mod_macro
Version: 1.1.2
Release: 5_%{apver}
Group: Applications/Internet
License: FSF
Source: http://www.cri.ensmp.fr/~coelho/mod_macro/mod_macro-1.1.2.tar.bz2
BuildRoot: /var/tmp/%{name}-root

%define apache_prefix /usr/local/apache-%{apver}

BuildRequires: apache = %{apver} apache-devel = %{apver}
Requires: apache = %{apver}

%description
Lets you define macros for use in apache's configuration files.

%prep
%setup -q

%build
%{apache_prefix}/bin/apxs -c mod_macro.c

%install
mkdir -p /var/tmp/%{name}-root/usr/local/apache-%{apver}/libexec/
cp mod_macro.so /var/tmp/%{name}-root/usr/local/apache-%{apver}/libexec/
#%{apache_prefix}/bin/apxs -i -a mod_macro.so

%post
echo "Run 'apxs -aen \"macro\" /usr/local/apache-%{apver}/libexec/mod_macro.so' to set up mod_macro."

%files
%defattr(-,root,other)
%doc mod_macro.html
/usr/local/apache-%{apver}/libexec/mod_macro.so
