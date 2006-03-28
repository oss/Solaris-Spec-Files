Summary:	Portable Musepack decoder library 
Name:		libmpcdec
Version:	1.2.2
Release:        2
Copyright:	GPL
Group:		System Environment/Libraries
Source:		%{name}-%{version}.tar.bz2
Distribution: 	RU-Solaris
Vendor: 	NBCS-OSS
Packager: 	Leo Zhadanovsky <leozh@nbcs.rutgers.edu>
BuildRoot:	/var/tmp/%{name}-%{version}-root

%description
Musepack is an audio compression format with a strong emphasis on high 
quality. It's not lossless, but it is designed for transparency, so that 
you won't be able to hear differences between the original wave file and 
the much smaller MPC file.

It is based on the MPEG-1 Layer-2 / MP2 algorithms, but since 1997 it 
has rapidly developed and vastly improved and is now at an advanced 
stage in which it contains heavily optimized and patentless code.

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

%changelog
* Mon Feb 27 2006 Leo Zhadanovsky <leozh@nbcs.rutgers.edu> - 0.1.2-1
- Initial Rutgers release
