Summary:	The ID3v1/ID3v2 Tagging Library 
Name:		id3lib
Version:	3.8.3
Release:        1
Copyright:	GPL
Group:		System Environment/Libraries
Source0:	%{name}-%{version}.tar.gz
Source1:	Makefile.id3lib.examples
Patch:		id3lib.patch
Distribution: 	RU-Solaris
Vendor: 	NBCS-OSS
Packager: 	Leo Zhadanovsky <leozh@nbcs.rutgers.edu>
BuildRoot:	/var/tmp/%{name}-%{version}-root
Conflicts:	libid3

%description
id3lib is an open-source, cross-platform software development library 
for reading, writing, and manipulating ID3v1  and ID3v2 tags. It is an 
on-going project whose primary goals are full compliance with the ID3v2 
standard, portability across several platforms, and providing a powerful 
and feature-rich API with a highly stable and efficient implementation.

%package devel 
Summary: Libraries, includes to develop applications with %{name}.
Group: Applications/Libraries
Requires: %{name} = %{version}

%description devel
The %{name}-devel package contains the header files and static libraries
for building applications which use %{name}.

%prep
%setup -q
%patch -p1 

%build
PATH="/opt/SUNWspro/bin:${PATH}" \
CC="cc" CXX="CC" CPPFLAGS="-I/usr/local/include" \
LD="/usr/ccs/bin/ld" \
LDFLAGS="-L/usr/local/lib -R/usr/local/lib -L/usr/opt/SUNWspro/lib -R/usr/opt/SUNWspro/lib  -lCstd -lCrun" \
export PATH CC CXX CPPFLAGS LD LDFLAGS

./configure --prefix=/usr/local

cp %{SOURCE1} examples/Makefile

make

%install
rm -rf $RPM_BUID_ROOT

make install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,bin,bin)
/usr/local/bin/*
/usr/local/lib/*so
/usr/local/lib/*so*

%files devel
%defattr(-,root,root)
/usr/local/include/*

%changelog
* Mon Feb 27 2006 Leo Zhadanovsky <leozh@nbcs.rutgers.edu> - 3.8.3-1
- Initial Rutgers release
