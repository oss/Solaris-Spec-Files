Summary:	GNOME Structured File Library
Name:		libgsf
Version:	1.14.7
Release:        1
Copyright:	GPL
Group:		Libraries/System
Source:		%{name}-%{version}.tar.bz2
Distribution: 	RU-Solaris
Vendor: 	NBCS-OSS
Packager: 	David Lee Halik <dhalik@nbcs.rutgers.edu>
BuildRoot:	/var/tmp/%{name}-%{version}-root
Requires:	bzip2 >= 1.0.3-2
BuildRequires:	glib2-devel

%description
The GNOME Structured File Library is a utility library for reading and 
writing structured file formats. Support for MS OLE2 streams is 
complete, as is zip import. There is also support for document metadata 
and some initial work on decompressing VBA streams in OLE files for 
future conversion to other languages. This library replaces libole2 and 
is used in gnumeric, mrproject, abiword, libwv2, koffice. It is also 
part of the AAF format.

%package devel 
Summary: Libraries, includes to develop applications with %{name}.
Group: Applications/Libraries
Requires: %{name} = %{version}

%description devel
The %{name}-devel package contains the header files and static libraries
for building applications which use %{name}.

%package static
Summary: Libraries, includes to develop applications with %{name}.
Group: Applications/Libraries
Requires: %{name} = %{version}

%description static
static libraries for %{name}

%prep
%setup -q -n %{name}-%{version}

%build
PATH="/opt/SUNWspro/bin:${PATH}" \
CC="cc" CXX="CC" CPPFLAGS="-I/usr/local/include" \
LD="/usr/ccs/bin/ld" \
LDFLAGS="-L/usr/local/lib -R/usr/local/lib" \
export PATH CC CXX CPPFLAGS LD LDFLAGS

./configure --prefix=/usr/local --with-zlib=/usr/local --disable-nls

gmake -j3

%install
rm -rf $RPM_BUID_ROOT

gmake install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,bin,bin)
/usr/local/bin/*
/usr/local/lib/*so*
#/usr/local/etc/gconf/schemas/*
/usr/local/share/*
/usr/local/share/man/man1/*

%files devel
%defattr(-,root,root)
/usr/local/include/*
/usr/local/lib/pkgconfig/*

%files static
%defattr(-,root,root)
/usr/local/lib/libgsf-1.a
/usr/local/lib/libgsf-1.la

%changelog
* Wed May 24 2006 Leo Zhadanovsky <leozh@nbcs.rutgers.edu> - 1.14.1-1
- Initial Rutgers release
