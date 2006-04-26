Summary: A requirement for gaim
Name: intltool
Version: 0.34.2
Release: 1
License: GPL
Group: System Environment/Base
Source: %{name}-%{version}.tar.bz2
URL: http://ftp.gnome.org/pub/gnome/sources/intltool
Distribution: RU-Solaris
Vendor: NBCS-OSS
Packager: Leo Zhadanovsky <leozh@nbcs.rutgers.edu>
Requires: perl-module-XML-Parser
BuildRoot: %{_tmppath}/%{name}-root

%description
This is needed to build gaim 2.0.0

%prep
%setup -q

%build
CC="gcc"
CPPFLAGS="-I/usr/local/include"
LDFLAGS="-L/usr/local/lib -R/usr/local/lib"
export CC CPPFLAGS LDFLAGS


./configure --prefix=/usr/local
gmake

%install
gmake install DESTDIR=%{buildroot}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
/usr/local/*

%changelog
* Fri Feb 10 2006 Leo Zhadanovsky <leozh@nbcs.rutgers.edu> - 0.34.2-1
- First Rutgers release
