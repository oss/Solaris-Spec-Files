Summary: Apache module to gzip outgoing HTTP 1.1 HTML data
Name: mod_gzip
Version: 1.3.19.1a
Release: 1
Group: Applications/Internet
License: Apache
#Source: http://www.remotecommunications.com/apache/mod_gzip/src/1.3.19.1a/mod_gzip.c
Source: mod_gzip-1.3.19.1a.tar.bz2
BuildRoot: /var/tmp/%{name}-root

%define apver 1.3.23
%define apache_prefix /usr/local/apache-%{apver}

BuildRequires: apache = %{apver} apache-devel = %{apver}
Requires: apache = %{apver}

%description
Enables Apache to gzip html pages sent to compliant HTTP/1.1 browsers
for blazingly fast downloads.

%prep
%setup -q

%build
%{apache_prefix}/bin/apxs -c mod_gzip.c

%install
mkdir -p /var/tmp/%{name}-root/usr/local/apache-%{apver}/libexec/
cp mod_gzip.so /var/tmp/%{name}-root/usr/local/apache-%{apver}/libexec/
#%{apache_prefix}/bin/apxs -i -a mod_gzip.so

%post
cat <<EOF 
Run '%{apache_prefix}/bin/apxs -aen "gzip" %{apache_prefix}/libexec/mod_gzip.so' to set up mod_gzip.
EOF

%files
%defattr(-,root,other)
%doc commands.txt samples.txt
/usr/local/apache-%{apver}/libexec/mod_gzip.so
