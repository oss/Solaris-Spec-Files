Summary: SWI Prolog compiler
Name: swi-prolog
Version: 3.3.8
Release: 3
Group: Development/Languages
Copyright: GPL
Source: pl-%{version}.tar.gz
BuildRoot: /var/tmp/%{name}-root

%description
Pl is a Prolog compiler compliant with part 1 of the ISO standard.

%prep
%setup -q -n pl-%{version}

%build
LD="/usr/ccs/bin/ld -L/usr/local/lib -R/usr/local/lib" \
    LDFLAGS="-L/usr/local/lib -R/usr/local/lib" \
    ./configure --prefix=/usr/local --sysconfdir=/etc
make

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/local
make install prefix=$RPM_BUILD_ROOT/usr/local sysconfdir=$RPM_BUILD_ROOT/etc

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,bin,bin)
/usr/local/lib/pl-%{version}
/usr/local/bin/*
/usr/local/man/man1/*
