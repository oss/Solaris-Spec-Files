Summary: gtk-smooth-engine
Name: gtk-smooth-engine
Version: 0.5.2
Release: 0
Copyright: GPL
Group: Applications/Editors
Source: gtk-smooth-engine-%{version}.tar.gz
Distribution: RU-Solaris
Vendor: NBCS-OSS
Packager: Christopher J. Suleski <chrisjs@nbcs.rutgers.edu>
BuildRoot: %{_tmppath}/%{name}-root
Requires: gtk2
BuildRequires: gtk2-devel

%description
Smooth engine for gtk themes

%prep
%setup -q

%build
LD_LIBRARY_PATH="/usr/local/lib"
LD_RUN_PATH="/usr/local/lib"
LDFLAGS="-R/usr/local/lib -L/usr/local/lib"
PATH="/usr/local/bin:$PATH"
CPPFLAGS="-I/usr/local/include"
export LD_LIBRARY_PATH PATH CPPFLAGS LDFLAGS
CC="gcc" ./configure --prefix=/usr/local --disable-gtk-1 --enable-gtk-2
make


%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/local/bin 
make install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,other)
/usr/local/lib/gtk-2.0/engines/libsmooth.so
