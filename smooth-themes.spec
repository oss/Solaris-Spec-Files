Summary: smooth-themes
Name: smooth-themes
Version: 0.5.2
Release: 3
Copyright: GPL
Group: Applications/Editors
Source: http://aleron.dl.sourceforge.net/sourceforge/smooth-engine/smooth-themes-0.5.2.tar.gz
Distribution: RU-Solaris
Vendor: NBCS-OSS
Packager: Christopher J. Suleski <chrisjs@nbcs.rutgers.edu>
BuildRoot: %{_tmppath}/%{name}-root
Requires: gtk2 >= 2.2.2-1 gtk-smooth-engine
BuildRequires: gtk2-devel gtk-smooth-engine

%description
Smooth themes for gtk smooth engine

%prep
%setup -q

%build
./configure
make


%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT

%post
mv /usr/local/share/themes/Default /usr/local/share/themes/Default.smoothmove
ln -sf /usr/local/share/themes/Smooth-Winter /usr/local/share/themes/Default

%postun
if [ ! -e "/usr/local/share/themes/Default" ]; then
    mv /usr/local/share/themes/Default.smoothmove /usr/local/share/themes/Default
fi

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,other)
/usr/local/share/themes/Smooth-*

