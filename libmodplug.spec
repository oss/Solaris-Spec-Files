Summary:	library for mod-like music formats
Name:		libmodplug
Version:	0.7
Release:        2
Copyright:	GPL
Group:		System Environment/Libraries
Source:		%{name}-%{version}.tar.gz
Distribution: 	RU-Solaris
Vendor: 	NBCS-OSS
Packager: 	Leo Zhadanovsky <leozh@nbcs.rutgers.edu>
BuildRoot:	/var/tmp/%{name}-%{version}-root

%description
libmodplug is a library for mod-like music formats. It is based on the 
mod rendering code from ModPlug, a popular windows mod player written 
by Olivier Lapicque, found at http://www.modplug.com

%package devel 
Summary: Libraries, includes to develop applications with %{name}.
Group: Applications/Libraries
Requires: %{name} = %{version}

%description devel
The %{name}-devel package contains the header files and static libraries
for building applications which use {%name}.

%prep
%setup -q

%build
CPPFLAGS="-I/usr/local/include -I/usr/sfw/include"
LDFLAGS="-L/usr/local/lib -R/usr/local/lib -L/usr/sfw/lib -R/usr/sfw/lib"
LD_LIBRARY_PATH="/usr/local/lib:/usr/sfw/lib"
LD_RUN_PATH="/usr/local/lib:/usr/sfw/lib"
CC="gcc" CXX="g++"
export CPPFLAGS LDFLAGS LD_LIBRARY_PATH LD_RUN_PATH CC CXX

./configure --prefix=/usr/local

make

%install
rm -rf $RPM_BUID_ROOT

make install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,bin,bin)
/usr/local/lib/*so
/usr/local/lib/*so*

%files devel
%defattr(-,root,root)
/usr/local/include/*
/usr/local/lib/pkgconfig/*

%changelog
* Mon Feb 27 2006 Leo Zhadanovsky <leozh@nbcs.rutgers.edu> - 0.7-1
- Initial Rutgers release
