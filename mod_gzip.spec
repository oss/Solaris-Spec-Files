%define apver 1.3.28
Summary: Apache module to gzip outgoing HTTP 1.1 HTML data
Name: apache-module-mod_gzip
Version: 1.3.19.1a
Release: 4
Group: Applications/Internet
License: Apache
#Source: http://www.remotecommunications.com/apache/mod_gzip/src/1.3.19.1a/mod_gzip.c
Source: mod_gzip-1.3.19.1a.tar.bz2
BuildRoot: /var/tmp/%{name}-root
Obsoletes: mod_gzip
Provides: mod_gzip

%define apache_prefix /usr/local/apache-%{apver}

BuildRequires: apache > 1.3 apache < 1.4 apache-devel = %{apver}
Requires: apache > 1.3 apache < 1.4 

%description
Enables Apache to gzip html pages sent to compliant HTTP/1.1 browsers
for blazingly fast downloads.

%prep
%setup -q -n mod_gzip-%{version}

%build
%{apache_prefix}/bin/apxs -c mod_gzip.c

%install
mkdir -p /var/tmp/%{name}-root/usr/local/lib/apache-modules/
cp mod_gzip.so /var/tmp/%{name}-root/usr/local/lib/apache-modules/
#%{apache_prefix}/bin/apxs -i -a mod_gzip.so

%post
cat <<EOF 
Run '%{apache_prefix}/bin/apxs -ain "gzip" /usr/local/lib/apache-modules/mod_gzip.so' to set up mod_gzip.
EOF

%files
%defattr(-,root,other)
%doc commands.txt samples.txt
/usr/local/lib/apache-modules/mod_gzip.so
