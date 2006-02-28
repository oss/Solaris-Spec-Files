Summary: a cross platform audio library
Name: mpd
Version: 0.8.6
Release: 1
License: GPL
Group: Development/Libraries
Source: %{name}-%{version}.tar.gz
URL: http://www.xiph.org/ao
Distribution: RU-Solaris
Vendor: NBCS-OSS
Packager: Leo Zhadanovsky <leozh@nbcs.rutgers.edu>
Requires: libogg, libvorbis, libmikmod
BuildRoot: %{_tmppath}/%{name}-root

%description
Libao is a cross-platform audio library that allows programs to output 
audio using a simple API on a wide variety of platforms. It currently 
supports:

    * Null output (handy for testing without a sound device)
    * WAV files
    * AU files
    * OSS (Open Sound System, used on Linux and FreeBSD
    * ALSA (Advanced Linux Sound Architecture)
    * polypaudio (next generation GNOME sound server)
    * esd (EsounD or Enlightened Sound Daemon)
    * AIX
    * Sun/NetBSD/OpenBSD
    * IRIX
    * NAS (Network Audio Server

%prep
%setup -q

%build
CC="gcc"
CPPFLAGS="-I/usr/local/include"
LDFLAGS="-L/usr/local/lib -R/usr/local/lib"
export CC CPPFLAGS LDFLAGS

./configure --prefix=/usr/local
make

%install
make install DESTDIR=%{buildroot}

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)

/usr/local/*

%changelog
* Mon Feb 20 2006 Leo Zhadanovsky <leozh@nbcs.rutgers.edu> - 0.8.6-1
- Initial Rutgers release
