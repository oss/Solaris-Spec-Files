%define apver 2.2.11 
Summary: 	Resolves IPs to countries
Name: 		apache2-module-mod_geoip2
Version: 	1.2.5
Release:        2 
Group: 		Applications/Internet
License: 	BSD
Source: 	mod_geoip2_%{version}.tar.gz
Patch0:		mod_geoip2_union.patch
Packager:	Naveen Gavini <ngavini@nbcs.rutgers.edu>
BuildRoot: 	%{_tmppath}/%{name}-root

%define apache_prefix /usr/local/apache2-%{apver}

BuildRequires: apache2, geoip-devel, geoip, apache-devel
Requires: apache2, geoip
Provides: mod_geoip

%description
This apache module takes the php5 pear package NetGeoIP and provides it as an apache module.

%prep
%setup -q -n mod_geoip2_%{version}
%patch0 -p0

%build
PATH="/opt/SUNWspro/bin:/usr/ccs/bin:${PATH}" \
CC="/opt/SUNWspro/bin/cc" CXX="/opt/SUNWspro/bin/CC" CPPFLAGS="-I/usr/local/include" \
CFLAGS="-D__unix__" \
LD="/usr/ccs/bin/ld" \
LDFLAGS="-L/usr/local/lib -R/usr/local/lib" \
export PATH CC CXX CPPFLAGS LD LDFLAGS CFLAGS
%{apache_prefix}/bin/apxs -ca -o mod_geoip.so -I/usr/local/include -L/usr/local/lib -Wl,-R/usr/local/lib -lGeoIP mod_geoip.c

%install
mkdir -p /var/local/tmp/%{name}-root/usr/local/apache2-modules/
cp .libs/mod_geoip.so /var/local/tmp/%{name}-root/usr/local/apache2-modules/

%post
echo "To enable the module place the below inside your httpd.conf file:"
echo "LoadModule geoip_module /usr/local/apache2-modules/mod_geoip.so"
echo "AddModule mod_geoip.c"
echo "<IfModule mod_geoip.c>"
echo "GeoIPEnable on"
echo "GeoIPDb /usr/local/share/GeoIP/GeoIP.dat"
echo "</IfModule>"

%files
%defattr(-,root,other)
/usr/local/apache2-modules/mod_geoip.so
%doc

%changelog
* Tue Jul 14 2009 Naveen Gavini <ngavini@nbcs.rutgers.edu> - 1.2.5-1
- Initial Build.
