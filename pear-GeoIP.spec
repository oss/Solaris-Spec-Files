Summary:	PEAR: GeoIP - Resolve IP to country
Name: 		pear-geoip
Version: 	1.8
Release: 	3	
License: 	PHP/BSD
Group: 		Development/Libraries
Source: 	geoip-%{version}.tar.gz
BuildRoot: 	%{_tmppath}/%{name}-root
URL: 		http://pear.php.net/
Prefix: 	%{_prefix}
BuildRequires:  geoip-devel, geoip
Requires: 	geoip

%description
This library is a port and redesign of the Maxmind PHP API to PHP5 and PEAR standards. The API is actually modeled on the Java API (as the Maxmind PHP API is largely procedural) but uses the binary parsing code from the original PHP version.

%prep
%setup -q -n geoip-%{version}

%build
mkdir -p %{buildroot}/usr/local/lib/php/GeoIP

%clean
[ -n "%{buildroot}" -a "%{buildroot}" != / ] && rm -rf %{buildroot}

%install
cp GeoIP.php %{buildroot}/usr/local/lib/php/GeoIP
cp countries.php %{buildroot}/usr/local/lib/php/GeoIP
cp coordinates.php %{buildroot}/usr/local/lib/php/GeoIP
cp tld.php %{buildroot}/usr/local/lib/php/GeoIP

%files
%defattr(-,root,bin)
/usr/local/lib/php/GeoIP/GeoIP.php
/usr/local/lib/php/GeoIP/coordinates.php
/usr/local/lib/php/GeoIP/countries.php
/usr/local/lib/php/GeoIP/tld.php
%doc

%changelog
* Mon Jul 27 2009 Naveen Gavini <ngavini@nbcs.rutgers.edu> - 1.8-1
- Fixed php requires.
