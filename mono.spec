Summary:	Mono 
Name:		mono
Version:	1.2.5.2
Release:        1
Copyright:	GPL
Group:		Applications/Multimedia
Source:		%{name}-%{version}.tar.bz2
Distribution: 	RU-Solaris
Vendor: 	NBCS-OSS
Packager: 	David Lee Halik <dhalik@nbcs.rutgers.edu>
BuildRoot:	/var/tmp/%{name}-%{version}-root
Requires:	glib2 >= 2.10
BuildRequires:	glib2-devel >= 2.10, bison

%description
Mono provides the necessary software to develop and run .NET client and 
server applications on Linux, Solaris, Mac OS X, Windows, and Unix. 
Sponsored by Novell (http://www.novell.com), the Mono open source 
project has an active and enthusiastic contributing community and is 
positioned to become the leading choice for development of Linux 
applications.

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
CPPFLAGS="-I/usr/local/include"
CFLAGS="-I/usr/local/include" 
LDFLAGS="-L/usr/local/lib -R/usr/local/lib"
LD_LIBRARY_PATH="/usr/local/lib"
LD_RUN_PATH="/usr/local/lib"
CC="gcc"
export CPPFLAGS CFLAGS LDFLAGS LD_LIBRARY_PATH LD_RUN_PATH CC

./configure --prefix=/usr/local --with-x --disable-nls

gmake

%install
rm -rf $RPM_BUID_ROOT

gmake install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,bin,bin)
/usr/local/bin/*
/usr/local/lib/*.so*
/usr/local/lib/*so*
/usr/local/lib/mono/*
/usr/local/etc/*
/usr/local/share/*
/usr/local/share/man/*

%files devel
%defattr(-,root,root)
/usr/local/include/*
/usr/local/lib/pkgconfig/*

%changelog
* Sat Nov 16 2007 David Lee Halik <dhalik@nbcs.rutgers.edu> - 1.2.5.2-1
- Quick bump to disable NLS
* Fri Apr 20 2007 Leo Zhadanovsky <leozh@nbcs.rutgers.edu> - 1.2.3.1-1
- Initial Rutgers release
