Name: hugs98
Version: Feb2001
Release: 2
Copyright: BSDish
Group: Development/Languages/Haskell
Summary: A Haskell Interpreter
Source: hugs98-Feb2001.tar.gz
BuildRoot: /var/tmp/%{name}-root

%description
Hugs 98 is an interpreter for Haskell, a lazy functional programming
language.  It is mostly compliant with the Haskell 98 standard, differing
mostly in some minor details of the module system.

%prep
%setup -q

%build
cd src/unix
LDFLAGS="-L/usr/local/lib -R/usr/local/lib" ./configure --with-readline
cd ..
make

%install
cd src
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/local/man/man1
make install prefix=$RPM_BUILD_ROOT/usr/local
install -c -m 0644 ../docs/hugs.1 $RPM_BUILD_ROOT/usr/local/man/man1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,bin,bin)
/usr/local/man/man1/hugs.1
/usr/local/bin/*
/usr/local/share/hugs/lib
/usr/local/share/hugs/demos
