Summary: render
Name: render
Version: 0.8
Release: 1
Copyright: GPL
Group: X11/Libraries
Source: http://fontconfig.org/release/render-0.8.tar.gz
Distribution: RU-Solaris
Vendor: NBCS-OSS
Packager: Christopher J. Suleski <chrisjs@nbcs.rutgers.edu>
BuildRoot: %{_tmppath}/%{name}-root

%description
render headers

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

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,other)
/usr/local/include/X11/extensions/*
/usr/local/lib/pkgconfig/render.pc
/usr/local/share/doc/render

