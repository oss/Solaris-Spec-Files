Name:		libtool
Version:	1.5.24
Copyright:	GPL
Group:		Development/Tools
Summary:	A portability utility
Release:	3
Source:		libtool-%{version}.tar.gz
BuildRoot:	%{_tmppath}/%{name}-root
Requires:	m4

%description
GNU libtool is part of the magic behind configure; it helps programmers
generate shared and static libraries in a portable manner.  Install this
package if you are developing software that uses its own libraries and you
do not want to port it manually.


%package static
Summary:	libtool static libraries
Group:		Development/Tools
Requires:	libtool = %{version}-%{release}

%description static
libtool static libraries


%package devel
Summary:	libtool development files
Group:		Development/Tools
Requires:	libtool = %{version}-%{release}

%description devel
libtool development files


%prep
%setup -q

%build
%ifarch sparc64
CC="/opt/SUNWspro/bin/cc" CXX="/opt/SUNWspro/bin/CC" \
CPPFLAGS="-I/usr/local/include" \
LD="/usr/ccs/bin/ld" CFLAGS='-xarch=v9 -g -xs' \
LDFLAGS="-L/usr/local/lib -R/usr/local/lib" \
./configure --prefix=/usr/local
grep CFLAGS Makefile
sleep 2
gmake -j3

mkdir sparcv9
cp libltdl/.libs/libltdl.so.3.1.5 sparcv9
make clean
%endif

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

%ifarch sparc64
cd sparcv9
ln -s libltdl.so.3.1.5 libltdl.so.3
ln -s libltdl.so.3 libltdl.so
cd ..
cp -rp sparcv9 %{buildroot}/usr/local/lib
%endif

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
/usr/local/lib/*.so*
/usr/local/lib/sparcv9/*.so*

%files static
%defattr(-,root,root)
/usr/local/lib/libltdl.a

%files devel
%defattr(-,root,root)
%dir /usr/local/share/libtool
%dir /usr/local/share/aclocal
/usr/local/bin/*
/usr/local/share/libtool/*
/usr/local/share/aclocal/*.m4
/usr/local/include/ltdl.h
/usr/local/share/info/libtool.info

%changelog
* Mon Aug 27 2007 Eric Rivas <kc2hmv@nbcs.rutgers.edu> - 1.5.24-3
- Created break out packages
* Mon Aug 27 2007 Naveen Gavini <ngavini@nbcs.rutgers.edu> - 1.5.24-2
- Fixed 64-bit binaries
* Wed Aug 22 2007 David Lee Halik <dhalik@nbcs.rutgers.edu> - 1.5.24-1
- Bump to 1.5.24
* Thu Dec 14 2006 Leo Zhadanovsky <leozh@nbcs.rutgers.edu> - 1.5.22-2
- Got rid of static libraries from file
- Put proper build flags in place
* Tue Jun 27 2006 Jonathan Kaczynski <jmkacz@nbcs.rutgers.edu> 1.5.22-1
 - Updated to the latest version
