Name: readline
Version: 4.3
Copyright: GPL
Group: System Environment/Libraries
Summary: GNU readline
Release: 4
Source: readline-%{version}.tar.gz
Patch0: readline43-001
Patch1: readline43-002
Patch2: readline43-003
Patch3: readline43-004
Patch4: readline43-005
URL: http://cnswww.cns.cwru.edu/~chet/readline/rltop.html
Distribution: RU-Solaris 
Vendor: NBCS-OSS 
Packager: Eric Rivas <kc2hmv@nbcs.rutgers.edu>
BuildRoot: /var/tmp/%{name}-root
BuildRequires: autoconf

%description
GNU readline is a library that enables history, completion, and
emacs/vi-like motion functionality in a program linked with it.

%package devel
Summary: Readline header files, static libraries
Group: Development/Libraries
Requires: readline = %{version}

%description devel
This package contains the header files and static libraries for
readline.  Install this package if you want to write or compile a
program that needs readline.

%prep
%setup -q
%patch0 -p0
%patch1 -p0
%patch2 -p0
%patch3 -p0
%patch4 -p0

%build
CC='cc' 
CXX='CC' 
CFLAGS='-g -xs'
CPPFLAGS='-I/usr/local/include' 
LDFLAGS='-L/usr/local/lib -R/usr/local/lib' 
export CC CXX CFLAGS CPPFLAGS LDFLAGS
autoconf 
./configure --prefix=/usr/local
make
#make shared

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/local
make install prefix=$RPM_BUILD_ROOT/usr/local
#make install-shared prefix=$RPM_BUILD_ROOT/usr/local
#cd $RPM_BUILD_ROOT/usr/local/lib
#rm -f libhistory.so libreadline.so
#ln -s libreadline.so.4 libreadline.so
#ln -s libhistory.so.4 libhistory.so

%clean
rm -rf $RPM_BUILD_ROOT

%post 
if [ -x /usr/local/bin/install-info ] ; then
	/usr/local/bin/install-info --info-dir=/usr/local/info \
		 /usr/local/info/rluserman.info
	/usr/local/bin/install-info --info-dir=/usr/local/info \
		 /usr/local/info/history.info
fi

%preun
if [ -x /usr/local/bin/install-info ] ; then
	/usr/local/bin/install-info --delete --info-dir=/usr/local/info \
		 /usr/local/info/rluserman.info
	/usr/local/bin/install-info --delete --info-dir=/usr/local/info \
		 /usr/local/info/history.info
fi

%files
%defattr(-,bin,bin)
%doc COPYING
/usr/local/lib/lib*.so*
/usr/local/info/*.info*
/usr/local/man/man3/readline.3
/usr/local/man/man3/history.3

%files devel
%defattr(-,bin,bin)
/usr/local/include/readline
/usr/local/lib/lib*a
