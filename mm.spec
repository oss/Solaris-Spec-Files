Summary:	mm library
Name:		mm	
Version:	1.4.2
Release:	1
Group:		System/Libraries
Copyright:	BSD-Like/Apache
URL:            http://www.ossp.org/pkg/lib/mm/
Distribution:   RU-Solaris
Vendor:         NBCS-OSS
Packager:       David Lee Halik <dhalik@nbcs.rutgers.edu>
Source:		mm-%{version}.tar.gz
BuildRoot:	/var/tmp/%{name}-%{version}-root

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
PATH="/opt/SUNWspro/bin:${PATH}" \
CC="cc" CXX="CC" CPPFLAGS="-I/usr/local/include" \
LD="/usr/ccs/bin/ld" \
LDFLAGS="-L/usr/local/lib -R/usr/local/lib"
export PATH CC CXX CPPFLAGS LD LDFLAGS

./configure --prefix="/usr/local"

gmake

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/local
make DESTDIR=%{buildroot} install

rm -f %{buildroot}/usr/local/lib/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,bin,bin)
/usr/local/lib/lib*.so*
/usr/local/bin/*
/usr/local/share/man/man1

%files devel
%defattr(-,bin,bin)
/usr/local/lib/lib*a
/usr/local/include
/usr/local/share/man/man3

%changelog
* Tue Aug 28 2007 David Lee Halik <dhalik@nbcs.rutgers.edu> - 1.4.2-1
- Bump to 1.4.2
- Cleaned up spec
