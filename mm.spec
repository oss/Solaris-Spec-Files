Summary: mm library
Name: mm	
Version: 1.1.3
Release: 1
Group: System/Libraries
Copyright: BSD-Like/Apache
Source: mm-%{version}.tar.gz
BuildRoot: /var/tmp/%{name}-root

%description

The MM library is a 2-layer abstraction library which simplifies the usage
of shared memory between forked (and this way strongly related) processes
under Unix platforms. On the first layer it hides all platform dependent
implementation details (allocation and locking) when dealing with shared
memory segments and on the second layer it provides a high-level
malloc(3)-style API for a convenient and well known way to work with
data-structures inside those shared memory segments.

%package devel
Summary: Libraries, includes, etc to develop mm applications
Group: System/libraries

%description devel
Libraries, include files, etc you can use to develop mm applications.

%prep
%setup -q

%build
LD="/usr/ccs/bin/ld -L/usr/local/lib -R/usr/local/lib" \
    LDFLAGS="-L/usr/local/lib -R/usr/local/lib" ./configure
make

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/local
make install prefix=$RPM_BUILD_ROOT/usr/local

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,bin,bin)
/usr/local/lib/lib*.so*
/usr/local/bin
/usr/local/man/man1

%files devel
%defattr(-,bin,bin)
/usr/local/lib/lib*a
/usr/local/include
/usr/local/man/man3
