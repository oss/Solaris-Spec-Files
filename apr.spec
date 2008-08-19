Summary:	Apache Portable Runtime
Name:		apr
Version:	1.3.3
Release:        1
License:	Apache
Group:		System/Utilities
Source:		%{name}-%{version}.tar.bz2
Distribution: 	RU-Solaris
Vendor: 	NBCS-OSS
Packager: 	Brian Schubert <schubert@nbcs.rutgers.edu>
BuildRoot:	/var/tmp/%{name}-%{version}-root

%description
The mission of the Apache Portable Runtime (APR) project is to create and 
maintain software libraries that provide a predictable and consistent 
interface to underlying platform-specific implementations. The primary 
goal is to provide an API to which software developers may code and be 
assured of predictable if not identical behaviour regardless of the 
platform on which their software is built, relieving them of the need to 
code special-case conditions to work around or take advantage of 
platform-specific deficiencies or features.

%package devel 
Summary: Libraries, includes to develop applications with %{name}.
Group: Applications/Libraries
Requires: %{name} = %{version}

%description devel
The %{name}-devel package contains the header files and static libraries
for building applications which use %{name}.

%prep
%setup -q

%build
PATH="/opt/SUNWspro/bin:${PATH}" \
CC="cc" CXX="CC" CPPFLAGS="-I/usr/local/include" \
LD="/usr/ccs/bin/ld" \
LDFLAGS="-L/usr/local/lib -R/usr/local/lib" \
export PATH CC CXX CPPFLAGS LD LDFLAGS

./configure --prefix=/usr/local --disable-nls

gmake

%install
rm -rf %{buildroot}

gmake install DESTDIR=%{buildroot}
rm -f %{buildroot}/usr/local/lib/libapr-1.la

%clean
rm -rf %{buildroot}

%files
%defattr(-,bin,bin)
%doc NOTICE LICENSE CHANGES
/usr/local/bin/*
/usr/local/lib/*.so*
/usr/local/lib/apr.exp
/usr/local/build-1/*

%files devel
%defattr(-,root,root)
/usr/local/include/*
/usr/local/lib/pkgconfig/*
/usr/local/lib/libapr-1.a

%changelog
* Tue Aug 19 2008 Brian Schubert <schubert@nbcs.rutgers.edu> - 1.3.3-1
- Switched to gmake, added doc entry, removed libapr-1.la, updated to 1.3.3
* Thu Jun 05 2008 Brian Schubert <schubert@nbcs.rutgers.edu> 1.3.0-1
- Updated to 1.3.0
* Wed Jan 02 2008 Naveen Gavini <ngavini@nbcs.rutgers.edu> - 1.2.12-1
- Updated to 1.2.12
* Fri Nov 02 2007 Naveen Gavini <ngavini@nbcs.rutgers.edu> - 1.2.11-1
- Updated to 1.2.11
* Wed Jun 07 2007 Naveen Gavini <ngavini@nbcs.rutgers.edu> - 1.2.9-2
- Updated to 1.2.9
* Wed Jun 07 2007 Naveen Gavini <ngavini@nbcs.rutgers.edu> - 1.2.7-1
- Updated to 1.2.8
* Wed Oct 11 2006 Leo Zhadanovsky <leozh@nbcs.rutgers.edu> - 1.2.7-1
- Initial Rutgers release
