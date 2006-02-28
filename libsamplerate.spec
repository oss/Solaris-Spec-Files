Summary:	%{name} - Sample Rate Converter for audio 
Name:		libsamplerate
Version:	0.1.2
Release:        1
Copyright:	GPL
Group:		System Environment/Libraries
Source:		%{name}-%{version}.tar.gz
Distribution: 	RU-Solaris
Vendor: 	NBCS-OSS
Packager: 	Leo Zhadanovsky <leozh@nbcs.rutgers.edu>
BuildRoot:	/var/tmp/%{name}-%{version}-root

%description
Secret Rabbit Code (aka libsamplerate) is a Sample Rate Converter for 
audio. One example of where such a thing would be useful is converting 
audio from the CD sample rate of 44.1kHz to the 48kHz sample rate used 
by DAT players.

SRC is capable of arbitrary and time varying conversions ; from 
downsampling by a factor of 256 to upsampling by the same factor. 
Arbitrary in this case means that the ratio of input and output sample 
rates can be an irrational number. The conversion ratio can also vary 
with time for speeding up and slowing down effects.

SRC provides a small set of converters to allow quality to be traded off 
against computation cost. The current best converter provides a 
signal-to-noise ratio of 97dB with -3dB passband extending from DC to 
96% of the theoretical best bandwidth for a given pair of input and 
output sample rates.

Since the library has few dependencies beyond that provided by the 
standard C library, it should compile and work on just about any 
operating system. It is know to work on Linux, MacOSX, Win32 and 
Solaris. With some relatively minor hacking it should also be relatively 
easy to port it to embedded systems and digital signal processors.

In addition, the library comes with a comprehensive test suite which can 
validate the performance of the library on new platforms. 

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
/usr/local/bin/*
/usr/local/lib/*so
/usr/local/lib/*so*

%files devel
%defattr(-,root,root)
/usr/local/include/*
/usr/local/lib/pkgconfig/*

%changelog
* Mon Feb 27 2006 Leo Zhadanovsky <leozh@nbcs.rutgers.edu> - 0.1.2-1
- Initial Rutgers release
