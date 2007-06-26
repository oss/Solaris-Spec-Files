Name: less
Version: 406
Copyright: GPL
Group: Applications/Text
Summary: less, a better text viewer
Release: 3
Source: less-%{version}.tar.gz
Distribution: RU-Solaris
Vendor: NBCS-OSS
Packager: Naveen Gavini <ngavini@nbcs.rutgers.edu>
BuildRoot: /var/tmp/%{name}-root

%description
Less is a lot like more, except you can scroll up as well as down.

%prep
%setup -q

%build
rm -rf %{buildroot}

LD_RUN_PATH="/usr/local/lib" \
PATH="/opt/SUNWspro/bin:${PATH}" \
CC="cc" CXX="CC" CPPFLAGS="-I/usr/local/include" \
LDFLAGS="-L/usr/local/lib -R/usr/local/lib" \
export LD_RUN_PATH PATH CC CXX CPPFLAGS LDFLAGS

./configure --prefix=/usr/local
make
make install prefix=%{buildroot}/usr/local

%ifarch sparc64
LD_RUN_PATH="/usr/local/lib/sparcv9" \
CC="cc -xtarget=ultra -xarch=v9" CXX="CC -xtarget=ultra -xarch=v9" \
CPPFLAGS="-I/usr/local/include/sparcv9" \
LDFLAGS="-L/usr/local/lib/sparcv9 -R/usr/local/lib/sparcv9" \
export LD_RUN_PATH CC CXX CPPFLAGS LDFLAGS
make clean
./configure --prefix=/usr/local
make
%endif

%install
%ifarch sparc64
mkdir -p %{buildroot}/usr/local/bin/sparcv9
/usr/local/gnu/bin/install -c less %{buildroot}/usr/local/bin/sparcv9/less
/usr/local/gnu/bin/install -c lesskey %{buildroot}/usr/local/bin/sparcv9/lesskey
/usr/local/gnu/bin/install -c lessecho %{buildroot}/usr/local/bin/sparcv9/lessecho
%endif
mkdir -p %{buildroot}/usr/local/man/man1
/usr/local/gnu/bin/install -c -m 644 ./less.nro %{buildroot}/usr/local/man/man1/less.1
/usr/local/gnu/bin/install -c -m 644 ./lesskey.nro %{buildroot}/usr/local/man/man1/lesskey.1
/usr/local/gnu/bin/install -c -m 644 ./lessecho.nro %{buildroot}/usr/local/man/man1/lessecho.1

%clean
rm -rf %{buildroot}

%files
%defattr(-,bin,bin)
%doc COPYING LICENSE NEWS README
/usr/local/bin/*
/usr/local/bin/sparcv9/*
/usr/local/man/man1/*

%changelog
* Tue Jun 26 2007 Naveen Gavini <ngavini@nbcs.rutgers.edu> - 406-3
- Updated to 406
* Fri Feb 24 2006 Leo Zhadanovsky <leozh@nbcs.rutgers.edu> - 394-2
- Made seperate binaries for sparc64 and 32
* Wed Feb 22 2006 Leo Zhadanovksy <leozh@nbcs.rutgers.edu> - 394-1
- Updated to 394, switched to Sun CC
