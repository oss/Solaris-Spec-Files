Summary:	a freely available, patent free (see below), high-quality data compressor
Name:		bzip2
Version:	1.0.4
Release:        5
Copyright:	GPL
Group:		System Environemtn/Base
Source:		%{name}-%{version}.tar.gz
Patch0: 	bzip2-1.0.4-suncc.patch
Distribution: 	RU-Solaris
Vendor: 	NBCS-OSS
Packager: 	David Lee Halik <dhalik@nbcs.rutgers.edu>
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
# Makefile patched in order to produce a SunCC shared object
%patch -p1

%build
PATH="/opt/SUNWspro/bin:${PATH}" \
CC="cc" CXX="CC" CPPFLAGS="-I/usr/local/include" \
LD="/usr/ccs/bin/ld" \
LDFLAGS="-L/usr/local/lib -R/usr/local/lib" \
export PATH CC CXX CPPFLAGS LD LDFLAGS

# We need a shared object to be built manually

gmake
gmake -f Makefile-libbz2_so

%install
rm -rf $RPM_BUILD_ROOT

PATH="/opt/SUNWspro/bin:${PATH}" \
CC="cc" CXX="CC" CPPFLAGS="-I/usr/local/include" \
LD="/usr/ccs/bin/ld" \
LDFLAGS="-L/usr/local/lib -R/usr/local/lib" \
export PATH CC CXX CPPFLAGS LD LDFLAGS

gmake install PREFIX=$RPM_BUILD_ROOT/usr/local

cp libbz2.so.1.0.4 %{buildroot}/usr/local/lib
cd %{buildroot}/usr/local/lib
ln -s libbz2.so.1.0.4 libbz2.so.1.0

cd $RPM_BUILD_ROOT
unhardlinkify.py ./

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,bin,bin)
/usr/local/bin/bunzip2
/usr/local/bin/bzcat
/usr/local/bin/bzdiff
/usr/local/bin/bzgrep
/usr/local/bin/bzip2
/usr/local/bin/bzip2recover
/usr/local/bin/bzmore
/usr/local/man/man1/bzcmp.1
/usr/local/man/man1/bzdiff.1
/usr/local/man/man1/bzegrep.1
/usr/local/man/man1/bzfgrep.1
/usr/local/man/man1/bzgrep.1
/usr/local/man/man1/bzip2.1
/usr/local/man/man1/bzless.1
/usr/local/man/man1/bzmore.1
/usr/local/lib/libbz2.so.1.0.4

%files devel 
%defattr(-,root,root)
/usr/local/include/*
/usr/local/lib/libbz2.a

%changelog
* Wed Sep 12 2007 David Lee Halik <dhalik@nbcs.rutgers.edu> - 1.0.4-5
- Added makefile hacks to create a shared object which is needed
* Fri Jul 27 2007 Naveen Gavini <ngavini@nbcs.rutgers.edu> - 1.0.4-4
- Fixed files
* Tue Jun 26 2007 Naveen Gavini <ngavini@nbcs.rutgers.edu> - 1.0.4-3
- Updated to 1.0.4
* Wed May 24 2006 Leo Zhadanovsky <leozh@nbcs.rutgers.edu> - 1.0.3-2
- Created new spec file
