Summary: ZMODEM file transfer protocol
Name: zmodem
Version: 1.36
Release: 2
Group: Applications/Productivity
License: Commercial
Source: %{name}-%{version}.tar.gz
BuildRoot: /var/tmp/%{name}-root

%description
ZMODEM compression programs.

%prep
%setup -q -n zmodem

%build
make sysvr3

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/local/bin %{buildroot}/usr/local/man/man1

install -m 0755 rz %{buildroot}/usr/local/bin/rz
install -m 0755 sz %{buildroot}/usr/local/bin/sz
install -m 0755 gz %{buildroot}/usr/local/bin/gz
install -m 0644 sz.1   %{buildroot}/usr/local/man/man1/sz.1
install -m 0644 rz.doc %{buildroot}/usr/local/man/man1/rz.1
cd %{buildroot}/usr/local/bin
ln -s rz rb
ln -s rz rx
ln -s sz sb
ln -s sz sx

%clean
rm -rf %{buildroot}

%files
%defattr(-, root, bin)
/usr/local/bin/*
/usr/local/man/man1/*
