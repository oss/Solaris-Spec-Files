Summary: ttf-bitstream-vera
Name: ttf-bitstream-vera
Version: 1.10
Release: 1
Copyright: GPL
Group: Applications/Editors
Source: http://ftp.gnome.org/pub/GNOME/sources/ttf-bitstream-vera/1.10/ttf-bitstream-vera-1.10.tar.bz2  
Distribution: RU-Solaris
Vendor: NBCS-OSS
Packager: Christopher J. Suleski <chrisjs@nbcs.rutgers.edu>
BuildRoot: %{_tmppath}/%{name}-root
Requires: fontconfig

%description
Smooth themes for gtk smooth engine

%prep
%setup -q

%build


%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/local/share/fonts/BitstreamVera \
    $RPM_BUILD_ROOT/usr/local/etc/fonts/
install -m0644 *.ttf $RPM_BUILD_ROOT/usr/local/share/fonts/BitstreamVera/
install -m0644 local.conf $RPM_BUILD_ROOT/usr/local/etc/fonts/

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,other)
/usr/local/etc/fonts/local.conf
/usr/local/share/fonts/BitstreamVera
