Summary:	libiconv
Name:		libiconv
Version:	1.13
Release:        1
License:	GPL
Group:		Libraries/System
Source:		%{name}-%{version}.tar.gz
Distribution: 	RU-Solaris
Vendor: 	NBCS-OSS
Packager: 	David Lee Halik <dhalik@nbcs.rutgers.edu>
BuildRoot:	/var/tmp/%{name}-%{version}-root

%description
For historical reasons, international text is often encoded using a 
language or country dependent character encoding. With the advent of the 
internet and the frequent exchange of text across countries - even the 
viewing of a web page from a foreign country is a "text exchange" in 
this context -, conversions between these encodings have become 
important. They have also become a problem, because many characters 
which are present in one encoding are absent in many other encodings. To 
solve this mess, the Unicode encoding has been created. It is a 
super-encoding of all others and is therefore the default encoding for 
new text formats like XML.

Still, many computers still operate in locale with a traditional 
(limited) character encoding. Some programs, like mailers and web 
browsers, must be able to convert between a given text encoding and the 
user's encoding. Other programs internally store strings in Unicode, to 
facilitate internal processing, and need to convert between internal 
string representation (Unicode) and external string representation (a 
traditional encoding) when they are doing I/O. GNU libiconv is a 
conversion library for both kinds of applications. 

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
CC="cc" CXX="CC" CPPFLAGS="-g -xs -I/usr/local/include" \
LD="/usr/ccs/bin/ld" \
LDFLAGS="-L/usr/ucblib -R/usr/ucblib -L/usr/local/lib -R/usr/local/lib" \
export PATH CC CXX CPPFLAGS LD LDFLAGS

./configure --prefix=/usr/local --disable-nls

gmake -j3

%install
rm -rf $RPM_BUID_ROOT

PATH="/opt/SUNWspro/bin:${PATH}" \
CC="cc" CXX="CC" CPPFLAGS="-g -xs -I/usr/local/include" \
LD="/usr/ccs/bin/ld" \
LDFLAGS="-L/usr/ucblib -R/usr/ucblib -L/usr/local/lib -R/usr/local/lib" \
export PATH CC CXX CPPFLAGS LD LDFLAGS

gmake install DESTDIR=$RPM_BUILD_ROOT

rm -f %{buildroot}/usr/local/lib/charset.alias
rm -f %{buildroot}/usr/local/lib/libcharset.a
rm -f %{buildroot}/usr/local/lib/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%files
%doc README NEWS COPYING* AUTHORS ChangeLog
%defattr(-,bin,bin)
/usr/local/bin/*
/usr/local/lib/*.so*
/usr/local/share/*

%files devel
%defattr(-,root,root)
/usr/local/include/*

%changelog
* Tue Mar 31 2009 David Diffenbaugh <davediff@nbcs.rutgers.edu> - 1.13-1
- updated to 1.13
- removed patch
* Mon Mar 23 2009 David Diffenbaugh <davediff@nbcs.rutgers.edu> - 1.12-3
- respun so package could be signed
* Sat Mar 21 2009 David Lee Halik <dhalik@nbcs.rutgers.edu> - 1.12-2
- Fix incorrect patch
* Mon Nov 12 2007 David Lee Halik <dhalik@nbcs.rutgers.edu> - 1.12-1
- Bump to 1.12
* Wed May 25 2006 Leo Zhadanovsky <leozh@nbcs.rutgers.edu> - 1.9.2-1
- Initial Rutgers release
