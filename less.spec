Name: less
Version: 358
Copyright: GPL
Group: Applications/Text
Summary: less, a better text viewer
Release: 4
Source: less-%{version}.tar.gz
BuildRoot: /var/tmp/%{name}-root

%description
Less is a lot like more, except you can scroll up as well as down.

%prep
%setup -q

%build
./configure --prefix=/usr/local/gnu
make

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/local/gnu
make install prefix=%{buildroot}/usr/local/gnu

%clean
rm -rf %{buildroot}

%files
%defattr(-,bin,bin)
%doc COPYING LICENSE NEWS README
/usr/local/gnu/bin/*
/usr/local/gnu/man/man1/*
