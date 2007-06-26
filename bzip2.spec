Summary:	a freely available, patent free (see below), high-quality data compressor
Name:		bzip2
Version:	1.0.4
Release:        3
Copyright:	GPL
Group:		System Environemtn/Base
Source:		%{name}-%{version}.tar.gz
Distribution: 	RU-Solaris
Vendor: 	NBCS-OSS
Packager: 	Naveen Gavini <ngavini@nbcs.rutgers.edu>
BuildRoot:	/var/tmp/%{name}-%{version}-root

%description
bzip2 is a freely available, patent free (see below), high-quality data 
compressor. It typically compresses files to within 10% to 15% of the 
best available techniques (the PPM family of statistical compressors), 
whilst being around twice as fast at compression and six times faster at 
decompression.

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

make

%install
rm -rf $RPM_BUILD_ROOT

make install PREFIX=$RPM_BUILD_ROOT/usr/local

cd $RPM_BUILD_ROOT
unhardlinkify.py ./

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,bin,bin)
#/usr/local/bin/*
#/usr/local/lib/*.so*
#/usr/local/man/man1/*

%files devel 
%defattr(-,root,root)
/usr/local/include/*

%changelog
* Tue Jun 26 2007 Naveen Gavini <ngavini@nbcs.rutgers.edu> - 1.0.4-3
- Updated to 1.0.4
* Wed May 24 2006 Leo Zhadanovsky <leozh@nbcs.rutgers.edu> - 1.0.3-2
- Created new spec file
