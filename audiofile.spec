Summary: Audiofile library
Name: audiofile
Version: 0.2.3
Release: 1
Group: System Environment/Libraries
Copyright: GPL
Source: audiofile-0.2.3.tar.gz
Patch: audiofile.patch
BuildRoot: /var/tmp/%{name}-root

%description
Audiofile is one of the libraries used by Gnome.

%package devel
Summary: Headers and static libraries for audiofile
Group: System Environment/Libraries
Requires: audiofile = %{version}

%description devel
This package consists of the header files and static libraries used by
libaudiofile.

%prep
%setup -q
%patch -p1

%build
LDFLAGS="-L/usr/local/lib -R/usr/local/lib" ./configure --prefix=/usr/local \
    --enable-shared --enable-static
make
make check

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/local
make install prefix=$RPM_BUILD_ROOT/usr/local

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,bin,bin)
%doc COPYING
/usr/local/lib/lib*.so*
/usr/local/bin/sf*

%files devel
%defattr(-,bin,bin)
/usr/local/share/aclocal/audiofile.m4
/usr/local/lib/lib*a
/usr/local/include/*
/usr/local/bin/audiofile-config
