Summary: Apache modules to allow macros in apache config files
Name: mod_macro
Version: 1.1.2
Release: 3
Group: Applications/Internet
License: FSF
Source: http://www.cri.ensmp.fr/~coelho/mod_macro/mod_macro-1.1.2.tar.bz2
BuildRoot: /var/tmp/%{name}-root

%define apver 1.3.24
%define apache_prefix /usr/local/apache-%{apver}

BuildRequires: apache > 1.3 apache < 1.4 apache-devel = %{apver}
Requires: apache > 1.3 apache < 1.4

%description
Lets you define macros for use in apache's configuration files.

%prep
%setup -q

%build
%{apache_prefix}/bin/apxs -c mod_macro.c

%install
mkdir -p /var/tmp/%{name}-root/usr/local/lib/apache-extramodules/
cp mod_macro.so /var/tmp/%{name}-root/usr/local/lib/apache-extramodules/
#%{apache_prefix}/bin/apxs -i -a mod_macro.so

%post
echo "Run 'apxs -ain \"macro\" /usr/local/apache-extramodules/mod_macro.so' to set up mod_macro."

%files
%defattr(-,root,other)
%doc mod_macro.html
/usr/local/lib/apache-extramodules/mod_macro.so






