Summary:	Xfce - lightweight desktop environment
Name:		libexo
Version:	0.3.2
Release:        1
Copyright:	GPL
Group:		Applications/Xfce
Source:		exo-%{version}.tar.bz2
#Patch:		libexo.patch
Distribution: 	RU-Solaris
Vendor: 	NBCS-OSS
Packager: 	Leo Zhadanovsky <leozh@nbcs.rutgers.edu>
BuildRoot:	/var/tmp/%{name}-%{version}-root
Requires:	libxml2, libdbh, librsvg, startup-notification, gtk2, pkgconfig, xfce4-dev-tools, libxfce4util, libxfcegui4, libxfce4mcs, xfce-mcs-manager, perl-module-URI
BuildRequires:	libxml2-devel, libdbh-devel, librsvg-devel, startup-notification, gtk2-devel, libxfce4util-devel, libxfcegui4-devel, libxfce4mcs-devel, xfce-mcs-manager-devel, perl-module-URI

%description
Xfce is a lightweight desktop environment for unix-like operating 
systems. It aims to be fast and lightweight, while still being visually 
appealing and easy to use.

Xfce 4.2 embodies the traditional UNIX philosophy of modularity and 
re-usability. It consists of a number of components that together 
provide the full functionality of the desktop environment. They are 
packaged separately and you can pick and choose from the available 
packages to create the best personal working environment.

Another priority of Xfce 4 is adhereance to standards, specifically 
those defined at freedesktop.org.

Xfce 4 can be installed on several UNIX platforms. It is known to 
compile on Linux, NetBSD, FreeBSD, Solaris, Cygwin and MacOS X, on x86, 
PPC, Sparc, Alpha...

%package devel
Summary: Libraries, includes to develop applications with %{name}.
Group: Applications/Libraries
Requires: %{name} = %{version}

%description devel
The %{name}-devel package contains the header files and static libraries
for building applications which use %{name}.

%prep
%setup -q -n exo-%{version}
#%patch -p1

%build
#CPPFLAGS="-I/usr/local/include"
#LDFLAGS="-L/usr/local/lib -R/usr/local/lib -lintl"
#LD_LIBRARY_PATH="/usr/local/lib"
#LD_RUN_PATH="/usr/local/lib"
#CC="gcc"
#export CPPFLAGS LDFLAGS LD_LIBRARY_PATH LD_RUN_PATH CC

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
/usr/local/lib/*.so*
/usr/local/lib/xfce4/mcs-plugins/*.so*
/usr/local/share/*
/usr/local/etc/xdg/xfce4/*
/usr/local/libexec/*
/usr/local/man/man1/*

%files devel
%defattr(-,root,root)
/usr/local/include/*
/usr/local/lib/pkgconfig/*

%changelog
* Thu May 25 2006 Leo Zhadanovsky <leozh@nbcs.rutgers.edu> - 0.3.1.6beta1-1
- Initial Rutgers release
