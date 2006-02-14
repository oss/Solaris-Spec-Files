# remote_rpm doesn't like the "-" in the version number
%define	sourcefilename libmikmod-3.2.0-beta2

Summary:	libmikmod - Library for the various audio format
Name:		libmikmod
Version:	3.2.0.beta2
Release:        1
Copyright:	LGPL
Group:		Applications/Multimedia
#Source:		%{name}-%{version}.tar.bz2
Source:		%{sourcefilename}.tar.bz2
BuildRoot:	/var/tmp/%{name}-%{version}-root

%description
Mikmod is a module player and library supporting many formats, including mod,
s3m, it, and xm. Originally a player for MS-DOS, MikMod has been ported to
other platforms, such as Unix, Macintosh, BeOS, and Java(!!)

%prep
%setup -q -n %{sourcefilename}

%build
PATH="/opt/SUNWspro/bin:${PATH}" \
CC="cc" CXX="CC" CPPFLAGS="-I/usr/local/include" \
LDFLAGS="-L/usr/local/lib -R/usr/local/lib" \
./configure --prefix=/usr/local

make

%install
rm -rf $RPM_BUID_ROOT

make install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,bin,bin)
/usr/local/include/*
/usr/local/lib/*
/usr/local/bin/*
/usr/local/man/man1/*
/usr/local/share/aclocal/libmikmod.m4

