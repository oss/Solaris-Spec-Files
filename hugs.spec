Name: hugs98
Version: Sep2006
Release: 1
Copyright: BSDish
Group: Development/Languages/Haskell
Summary: A Haskell Interpreter
Source: hugs98-%{version}.tar.gz
BuildRoot: /var/tmp/%{name}-root

%description
Hugs 98 is an interpreter for Haskell, a lazy functional programming
language.  It is mostly compliant with the Haskell 98 standard, differing
mostly in some minor details of the module system.

%prep
%setup -q

%build
PATH="/opt/SUNWspro/bin:${PATH}" \
CC="cc" CXX="CC" CPPFLAGS="-I/usr/local/include" \
LD="/usr/ccs/bin/ld" \
LDFLAGS="-L/usr/local/lib -R/usr/local/lib" \
export PATH CC CXX CPPFLAGS LD LDFLAGS
./configure --prefix=/usr/local --with-readline
make

%install
cd src
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/local/man/man1
make install DESTDIR=$RPM_BUILD_ROOT
install -c -m 0644 ../docs/hugs.1 $RPM_BUILD_ROOT/usr/local/man/man1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,bin,bin)
/usr/local/man/man1/hugs.1
/usr/local/bin/*
