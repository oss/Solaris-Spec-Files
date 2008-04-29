%define real_name GeoIP

Summary:	C library for country/city/organization to IP address or hostname mapping
Name: 		geoip
Version: 	1.4.4
Release: 	1
License: 	GPL
Group: 		Development/Libraries
URL: 		http://www.maxmind.com/app/c            
Source: 	http://www.maxmind.com/download/geoip/api/c/GeoIP-%{version}.tar.gz 
Packager: 	Naveen Gavini <ngavini@nbcs.rutgers.edu>
Vendor: 	OSS http://rpm.rutgers.edu
BuildRoot: 	%{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: 	zlib-devel
Obsoletes: 	GeoIP < %{version}-%{release}
Provides: 	GeoIP = %{version}-%{release}

%description
GeoIP is a C library that enables the user to find the country that any IP
address or hostname originates from. It uses a file based database that is
accurate as of March 2003. This database simply contains IP blocks as keys, and
countries as values. This database should be more complete and accurate than
using reverse DNS lookups.

%package devel
Summary: Header files, libraries and development documentation for %{name}.
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}
Provides: GeoIP-devel = %{version}-%{release}
Obsoletes: GeoIP-devel < %{version}-%{release}

%description devel
This package contains the header files, static libraries and development
documentation for %{name}. If you like to develop programs using %{name},
you will need to install %{name}-devel.

%prep
%setup -q -n %{real_name}-%{version}

%build

./configure --disable-static --disable-dependency-tracking
gmake

%install
rm -rf %{buildroot}
gmake install DESTDIR="%{buildroot}"

%post 
%postun

%clean
rm -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING INSTALL README TODO
%doc %{_mandir}/man1/geoiplookup.1*
%doc %{_mandir}/man1/geoipupdate.1*
%config(noreplace) %{_sysconfdir}/GeoIP.conf.default
%config(noreplace) %{_sysconfdir}/GeoIP.conf
%{_bindir}/geoiplookup
%{_bindir}/geoipupdate
%{_datadir}/GeoIP/
%{_libdir}/libGeoIP.so.*
%{_libdir}/libGeoIPUpdate.so.*

%files devel
%defattr(-, root, root, 0755)
%{_includedir}/GeoIP.h
%{_includedir}/GeoIPCity.h
%{_includedir}/GeoIPUpdate.h
%exclude %{_libdir}/libGeoIP.la
%{_libdir}/libGeoIP.so
%exclude %{_libdir}/libGeoIPUpdate.la
%{_libdir}/libGeoIPUpdate.so

%changelog
* Tue Apr 29 2008 Naveen Gavini <ngavini@nbcs.rutgers.edu> - 1.4.4-1
- Initial build.
