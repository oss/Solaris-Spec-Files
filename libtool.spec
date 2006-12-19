Name: libtool
Version: 1.5.22
Copyright: GPL
Group: Development/Tools
Summary: A portability utility
Release: 2
Source: libtool-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-root
Requires: m4

%description
GNU libtool is part of the magic behind configure; it helps programmers
generate shared and static libraries in a portable manner.  Install this
package if you are developing software that uses its own libraries and you
do not want to port it manually.

%prep
%setup -q

%build
PATH="/opt/SUNWspro/bin:${PATH}" \
CC="cc" CXX="CC" CPPFLAGS="-I/usr/local/include" \
LD="/usr/ccs/bin/ld" \
LDFLAGS="-L/usr/local/lib -R/usr/local/lib" \
export PATH CC CXX CPPFLAGS LD LDFLAGS

./configure --prefix=/usr/local
make

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}
make install DESTDIR=%{buildroot}

%clean
rm -rf %{buildroot}

%post
if [ -x /usr/local/bin/install-info ] ; then
	/usr/local/bin/install-info --info-dir=/usr/local/info \
		 /usr/local/share/info/libtool.info
fi

%preun
if [ -x /usr/local/bin/install-info ] ; then
	/usr/local/bin/install-info --delete --info-dir=/usr/local/info \
		 /usr/local/share/info/libtool.info
fi

%files
%defattr(-,root,root)
/usr/local/bin/*
%dir /usr/local/share/libtool
/usr/local/share/libtool/*
%dir /usr/local/share/aclocal
/usr/local/share/aclocal/*.m4
/usr/local/lib/lib*.so*
/usr/local/include/ltdl.h
/usr/local/share/info/libtool.info

%changelog
* Thu Dec 14 2006 Leo Zhadanovsky <leozh@nbcs.rutgers.edu> - 1.5.22-2
- Got rid of static libraries from file
- Put proper build flags in place
* Tue Jun 27 2006 Jonathan Kaczynski <jmkacz@nbcs.rutgers.edu> 1.5.22-1
 - Updated to the latest version
