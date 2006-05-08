Summary:	allows you to access the data held on the MusicBrainz server 
Name:		libmusicbrainz
Version:	2.1.2
Release:        1
Copyright:	GPL
Group:		Applications/Multimedia
Source:		%{name}-%{version}.tar.gz
Distribution: 	RU-Solaris
Vendor: 	NBCS-OSS
Packager: 	Leo Zhadanovsky <leozh@nbcs.rutgers.edu>
BuildRoot:	/var/tmp/%{name}-%{version}-root
Requires:	python

%description
The MusicBrainz client is a library which can be built into other 
programs.  The library allows you to access the data held on the 
MusicBrainz server.

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
LDFLAGS="-lc -lCstd -lCrun -L/usr/local/lib -R/usr/local/lib" \
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
/usr/local/lib/pkgconfig/*

%files devel
%defattr(-,root,root)
/usr/local/include/*

%changelog
* Tue May 02 2006 Leo Zhadanovsky <leozh@nbcs.rutgers.edu> - 2.1.2-1
- Initial Rutgers release
