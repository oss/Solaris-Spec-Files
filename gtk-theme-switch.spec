Summary: gtk-theme-switch
Name: gtk-theme-switch
Version: 2.0.0rc2
Release: 1
Copyright: GPL
Group: Applications/Editors
Source: gtk-theme-switch-%{version}.tar.gz
Distribution: RU-Solaris
Vendor: NBCS-OSS
Packager: Leo Zhadanovsky <leozh@nbcs.rutgers.edu>
BuildRoot: %{_tmppath}/%{name}-root
Requires: gtk2
BuildRequires: gtk2-devel

%description
change gtk2 theme

%prep
%setup -q

%build
PATH="/opt/SUNWspro/bin:${PATH}" \
CC="cc" CXX="CC" CPPFLAGS="-I/usr/local/include" \
LD="/usr/ccs/bin/ld" \
LDFLAGS="-L/usr/local/lib -R/usr/local/lib" \
export PATH CC CXX CPPFLAGS LD LDFLAGS

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
