Summary: gtk-theme-switch
Name: gtk-theme-switch
Version: 2.0.0rc2
Release: 0
Copyright: GPL
Group: Applications/Editors
Source: gtk-theme-switch-%{version}.tar.gz
Distribution: RU-Solaris
Vendor: NBCS-OSS
Packager: Christopher J. Suleski <chrisjs@nbcs.rutgers.edu>
BuildRoot: %{_tmppath}/%{name}-root
Requires: gtk2
BuildRequires: gtk2-devel

%description
change gtk2 theme


%prep
%setup -q

%build
sed "s/cc/gcc/" Makefile > Makefile.new
mv Makefile.new Makefile
LD_LIBRARY_PATH="/usr/local/lib" \
LD_RUN_PATH="/usr/local/lib" \
make


%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/local/bin $RPM_BUILD_ROOT/usr/local/man/man1
install -m0755 switch2 $RPM_BUILD_ROOT/usr/local/bin/
install -m0644 switch.1 $RPM_BUILD_ROOT/usr/local/man/man1/

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,other)
/usr/local/bin/switch2
/usr/local/man/man1/switch.1
