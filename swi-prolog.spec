Summary: SWI Prolog compiler
Name: swi-prolog
Version: 5.6.27
Release: 1
Group: Development/Languages
Copyright: GPL
Source: pl-%{version}.tar.gz
BuildRoot: /var/tmp/%{name}-root

%description
Pl is a Prolog compiler compliant with part 1 of the ISO standard.

%prep
%setup -q -n pl-%{version}

%build
PATH="/opt/SUNWspro/bin:${PATH}" \
CC="cc" CXX="CC" CPPFLAGS="-I/usr/local/include" \
LD="/usr/ccs/bin/ld" \
LDFLAGS="-L/usr/local/lib -R/usr/local/lib" \
export PATH CC CXX CPPFLAGS LD LDFLAGS
./configure --prefix=/usr/local

make

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/local
make install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,bin,bin)
/usr/local/lib/pl-%{version}
/usr/local/bin/*
/usr/local/man/man1/*
