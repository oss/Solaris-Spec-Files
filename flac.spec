Summary:	flac - Library for the FLAC audio format
Name:		flac
Version:	1.1.2
Release:        1
Copyright:	GPL
Group:		Applications/Multimedia
Source:		%{name}-%{version}.tar.gz
Distribution: 	RU-Solaris
Vendor: 	NBCS-OSS
Packager: 	Leo Zhadanovsky <leozh@nbcs.rutgers.edu>
Requires:	xmms >= 1.2.10
BuildRoot:	/var/tmp/%{name}-%{version}-root

%description
FLAC stands for Free Lossless Audio Codec. Grossly oversimplified, FLAC 
is similar to MP3, but lossless, meaning that audio is compressed in 
FLAC without any loss in quality. This is similar to how Zip works, 
except with FLAC you will get much better compression because it is 
designed specifically for audio, and you can play back compressed FLAC 
files in your favorite player (or your car or home stereo) just like you 
would an MP3 file. 

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
/usr/local/bin/*
/usr/local/include/*
/usr/local/lib/*so
/usr/local/lib/*so*
/usr/local/lib/xmms/Input/*so
/usr/local/share/doc/*
/usr/local/man/man1/*
/usr/local/share/aclocal/*

%changelog
* Sun Feb 26 2006 Leo Zhadanovsky <leozh@nbcs.rutgers.edu> - 1.1.2-1
- Initial Rutgers release
