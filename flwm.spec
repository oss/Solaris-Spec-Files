Summary: Fast Light Window Manager
Name: flwm
Version: 0.25
Release: 2
Group: User Interface/X
License: GPL
Source: flwm-%{version}.tgz
BuildRoot: /var/tmp/%{name}-root
Requires: fltk
BuildRequires: fltk-devel

%description
flwm is a very small and fast X window manager, featuring no icons and
"sideways" title bars.

%prep
%setup -q

%build
LD="/usr/ccs/bin/ld -L/usr/local/lib -R/usr/local/lib" \
  LDFLAGS="-L/usr/local/lib -R/usr/local/lib" CXXFLAGS="-I/usr/localinclude" \
  ./configure
make LDFLAGS="-L/usr/local/lib -R/usr/local/lib" \
     CXXFLAGS="-I/usr/local/include"

%install
rm -rf $RPM_BUILD_ROOT
for i in bin man/man1; do
    mkdir -p $RPM_BUILD_ROOT/usr/local/$i
done
install -m 0755 flwm $RPM_BUILD_ROOT/usr/local/bin/flwm
install -m 0644 flwm.1 $RPM_BUILD_ROOT/usr/local/man/man1/flwm.1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,bin,bin)
/usr/local/bin/flwm
/usr/local/man/man1/flwm.1
