Summary: xrender
Name: xrender
Version: 0.8.3
Release: 5
Copyright: GPL
Group: X11/Libraries
Source: http://fontconfig.org/release/xrender-0.8.3.tar.gz
Distribution: RU-Solaris
Vendor: NBCS-OSS
Packager: Christopher J. Suleski <chrisjs@nbcs.rutgers.edu>
BuildRoot: %{_tmppath}/%{name}-root
BuildRequires: render

%description
xrender for Xft2 

%package devel
Summary: %{name} include files, etc.
Requires: %{name} %{buildrequires}
Group: Development
%description devel
%{name} include files, etc.

%prep
%setup -q 


%build
LD_LIBRARY_PATH="/usr/local/lib"
LD_RUN_PATH="/usr/local/lib"
./configure --prefix=/usr/local

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT
/usr/ccs/bin/strip $RPM_BUILD_ROOT/usr/local/lib/libXrender.so*

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,other) 
/usr/local/lib/libXrender.so*

%files devel
%defattr(-,root,other) 
/usr/local/include/X11/extensions/*
/usr/local/lib/libXrender.a
/usr/local/lib/pkgconfig/xrender.pc
