Summary:	Disk based hashtables
Name:		libdbh
Version:	4.5.0
Release:        2
Copyright:	GPL
Group:		Libraries/System
Source:		dbh-%{version}.tar.gz
Distribution: 	RU-Solaris
Vendor: 	NBCS-OSS
Packager: 	Leo Zhadanovsky <leozh@nbcs.rutgers.edu>
BuildRoot:	/var/tmp/%{name}-%{version}-root

%description
Disk based hashes is a method to create multidimensional binary trees 
on disk. This library permits the extension of database concept to a 
plethora of electronic data, such as graphic information.

%package devel 
Summary: Libraries, includes to develop applications with %{name}.
Group: Applications/Libraries
Requires: %{name} = %{version}

%description devel
The %{name}-devel package contains the header files and static libraries
for building applications which use %{name}.

%prep
%setup -q -n dbh-%{version}

%build
PATH="/opt/SUNWspro/bin:${PATH}" \
CC="cc" CXX="CC" CPPFLAGS="-I/usr/local/include" \
LD="/usr/ccs/bin/ld" \
LDFLAGS="-L/usr/local/lib -R/usr/local/lib" \
export PATH CC CXX CPPFLAGS LD LDFLAGS

./configure --prefix=/usr/local

make

%install
rm -rf $RPM_BUID_ROOT

make install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,bin,bin)
/usr/local/lib/*so*

%files devel
%defattr(-,root,root)
/usr/local/include/*
/usr/local/lib/pkgconfig/*

%changelog
* Wed May 24 2006 Leo Zhadanovsky <leozh@nbcs.rutgers.edu> - 4.5.0-1
- Initial Rutgers release
