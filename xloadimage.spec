Summary: X11 image viewer
Name: xloadimage
Version: 4.1
Release: 1
Group: User Interface/X11
License: modified MIT X Consortium
Source: %{name}.%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-root

%description

%prep
%setup -q -n %{name}.%{version}
CC='/usr/local/bin/gcc' CXX='/usr/local/bin/gcc' ./autoconfig 

%build
make </dev/null

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/local/bin %{buildroot}/usr/lib/X11/Xloadimage \
         %{buildroot}/usr/local/man/man1

install -m 0755 xloadimage %{buildroot}/usr/local/bin/xloadimage
ln -s xloadimage %{buildroot}/usr/local/bin/xsetbg
ln -s xloadimage %{buildroot}/usr/local/bin/xview
install -m 0755 uufilter %{buildroot}/usr/local/bin/uufilter
install -m 0644 xloadimage.man %{buildroot}/usr/local/man/man1/xloadimage.1

%clean
rm -rf %{buildroot}

%files
%defattr(-, root, bin)
%doc xloadimagerc README
/usr/local/bin/*
/usr/local/man/*/*
