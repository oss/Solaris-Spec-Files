%define apver 1.3.41
Summary: 	Resolves IPs to countries
Name: 		apache-module-mod_geoip
Version: 	1.3.4
Release:        3 
Group: 		Applications/Internet
License: 	BSD
Source: 	mod_geoip_%{version}.tar.gz
Packager:	David Diffenbaugh <davediff@nbcs.rutgers.edu>
BuildRoot: 	%{_tmppath}/%{name}-root
Patch0:		mod_geoip_1.3.4-union.patch

%define apache_prefix /usr/local/apache-%{apver}

BuildRequires: apache, geoip-devel, geoip, apache-devel
Requires: apache, geoip
Provides: mod_geoip

%description
This apache module takes the php5 pear package NetGeoIP and provides it as an apache module.

%prep
%setup -q -n mod_geoip_%{version}
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
mkdir -p /var/local/tmp/%{name}-root/usr/local/apache-modules/
cp mod_geoip.so /var/local/tmp/%{name}-root/usr/local/apache-modules/

%post
echo "To enable the module place the below inside your httpd.conf file:"
echo "LoadModule geoip_module /usr/local/apache-modules/mod_geoip.so"
echo "AddModule mod_geoip.c"
echo "<IfModule mod_geoip.c>"
echo "GeoIPEnable on"
echo "GeoIPDb /usr/local/share/GeoIP/GeoIP.dat"
echo "</IfModule>"

%files
%defattr(-,root,other)
/usr/local/apache-modules/mod_geoip.so
%doc

%changelog
* Wed Feb 25 2009 David Diffenbaugh <davediff@nbcs.rutgers.edu> - 1.3.4-2
- Updated to 1.3.4
- added /usr/ccs/bin to PATH so that correct ld is used
* Wed Aug 20 2008 Naveen Gavini <ngavini@nbcs.rutgers.edu> - 1.3.3-1
- Updated to 1.3.3.
* Fri Apr 02 2008 Naveen Gavini <ngavini@nbcs.rutgers.edu> - 1.3.2-1
- Initial Build.
