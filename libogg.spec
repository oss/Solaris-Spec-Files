Summary:	libogg - Library for the Ogg Vorbis audio format
Name:		libogg
Version:	1.1.3
Release:        1
Copyright:	BSD
Group:		Applications/Multimedia
Source:		%{name}-%{version}.tar.gz
BuildRoot:	/var/tmp/%{name}-%{version}-root

%description
Ogg project codecs use the Ogg bitstream format to arrange the raw,
compressed bitstream into a more robust, useful form.  For example,
the Ogg bitstream makes seeking, time stamping and error recovery
possible, as well as mixing several sepearate, concurrent media
streams into a single physical bitstream.

%prep
%setup -q

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
/usr/local/share/aclocal/ogg.m4
%dir /usr/local/share/doc/libogg-%{version}/
/usr/local/share/doc/libogg-%{version}/*

