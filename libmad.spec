Summary:	MAD: MPEG Audio Decoder 
Name:		libmad
Version:	0.15.1b
Release:        1
Copyright:	GPL
Group:		Applications/Multimedia
Source:		%{name}-%{version}.tar.gz
Distribution: 	RU-Solaris
Vendor: 	NBCS-OSS
Packager: 	Leo Zhadanovsky <leozh@nbcs.rutgers.edu>
BuildRoot:	/var/tmp/%{name}-%{version}-root

%description
MAD is a high-quality MPEG audio decoder. It currently supports MPEG-1 
and the MPEG-2 extension to lower sampling frequencies, as well as the 
de facto MPEG 2.5 format.

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

make

%install
rm -rf $RPM_BUID_ROOT

make install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,bin,bin)
/usr/local/lib/*.so
/usr/local/lib/*so*

%files devel
%defattr(-,root,root)
/usr/local/include/*

%changelog
* Wed May 17 2006 Leo Zhadanovsky <leozh@nbcs.rutgers.edu> - 0.15.1b-1
- Initial Rutgers release
