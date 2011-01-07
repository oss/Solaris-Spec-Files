%define real_name GeoIP

Summary:	C library for country/city/organization to IP address or hostname mapping
Name: 		geoip
Version: 	1.4.6
Release: 	7
License: 	GPL
Group: 		Development/Libraries
URL: 		http://www.maxmind.com/app/c            
Source0: 	http://www.maxmind.com/download/geoip/api/c/GeoIP-%{version}.tar.gz
Source1:	http://geolite.maxmind.com/download/geoip/database/GeoLiteCountry/GeoIP.dat.gz
Patch:		geoip-1.4.5-union.patch
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
cd libGeoIP
%patch -p0
cd ..
cp %{_sourcedir}/GeoIP.dat.gz data/
%{__gzip} -df data/GeoIP.dat.gz
%{__sed} -i "s:-Wall::g" Makefile* libGeoIP/Makefile* test/Makefile* apps/Makefile*

%build
CFLAGS="-D__unix__"
%configure --mandir=%{_mandir} --disable-static --disable-dependency-tracking
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
%doc %{_mandir}/man1/*
%config(noreplace) %{_sysconfdir}/GeoIP.conf.default
%config(noreplace) %{_sysconfdir}/GeoIP.conf
%{_bindir}/geoiplookup
%{_bindir}/geoiplookup6
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
* Wed Jan 05 2011 Orcan Ogetbil <orcan@nbcs.rutgers.edu> - 1.4.6-7
- Updated to Jan 2011 database
* Thu Nov 11 2010 Daiyan Alamgir <daiyan@nbcs.rutgers.edu> - 1.4.6-6
- Updated to Nov 2010 database
* Tue Oct 05 2010 Orcan Ogetbil <orcan@nbcs.rutgers.edu> - 1.4.6-5
- Updated to Oct 2010 database
* Thu Jul 29 2010 Orcan Ogetbil <orcan@nbcs.rutgers.edu> - 1.4.6-4
- Updated to Jul 2010 database
* Tue Jun 01 2010 Orcan Ogetbil <orcan@nbcs.rutgers.edu> - 1.4.6-3
- Updated to May 2010 database
* Tue Sep 15 2009 Naveen Gavini <ngavini@nbcs.rutgers.edu> - 1.4.6-2
- Updated to September 2009 database.
* Thu May 21 2009 Brian Schubert <schubert@nbcs.rutgers.edu> - 1.4.6-1
- Updated to version 1.4.6
- Removed patches 
- Latest database included
* Tue Feb 24 2009 David Diffenbaugh <davediff@nbcs.rutgers.edu> - 1.4.5-2
- added patch to remove unneccessary anonymous union
- updated nogcc.patch for Makefile in test directory 
* Wed Feb 18 2009 Naveen Gavini <ngavini@nbcs.rutgers.edu> - 1.4.5-1
- Updated to new version.
* Tue Sep 16 2008 Brian Schubert <schubert@nbcs.rutgers.edu> - 1.4.4-4
- Bumped release number to 4
* Mon Sep 15 2008 Naveen Gavini <ngavini@nbcs.rutgers.edu> - 1.4.4-3
- Updated to September 2008 Database.
* Tue Apr 29 2008 Naveen Gavini <ngavini@nbcs.rutgers.edu> - 1.4.4-1
- Initial build.
