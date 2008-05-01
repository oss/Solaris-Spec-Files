%define apver 1.3.41
Summary: 	Resolves IPs to countries
Name: 		apache-module-mod_geoip
Version: 	1.3.2
Release: 	1
Group: 		Applications/Internet
License: 	BSD
Source: 	mod_geoip_%{version}.tar.gz
BuildRoot: 	%{_tmppath}/%{name}-root

%define apache_prefix /usr/local/apache-%{apver}

BuildRequires: apache, geoip-devel, geoip, apache-devel
Requires: apache, geoip

%description
This apache module takes the php5 pear package NetGeoIP and provides it as an apache module.

%prep
%setup -q -n mod_geoip_%{version}

%build
%{apache_prefix}/bin/apxs -ca -o mod_geoip.so -I/usr/local/include -L/usr/local/lib -lGeoIP mod_geoip.c

%install
mkdir -p /var/local/tmp/%{name}-root/usr/local/lib/apache-modules/
cp mod_geoip.so /var/local/tmp/%{name}-root/usr/local/lib/apache-modules/

%post
echo "Run 'apxs -cia -I/usr/local/include -L/usr/local/lib -lGeoIP /usr/local/apache-modules/mod_geoip.so' to set up mod_geoip."
echo "To enable the module, place GeoIPEnable On inside your httpd.conf file."

%files
%defattr(-,root,other)
/usr/local/lib/apache-modules/mod_geoip.so
