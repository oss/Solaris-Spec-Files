Name: readline5
Version: 5.1
Copyright: GPL
Group: System Environment/Libraries
Summary: GNU readline
Release: 2
Source: readline-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-root
#BuildRequires: autoconf >= 2.50
Obsoletes: readline
Provides: readline5 readline

%description
GNU readline is a library that enables history, completion, and
emacs/vi-like motion functionality in a program linked with it.

%package devel
Summary: Readline header files, static libraries
Group: Development/Libraries
Requires: readline5
Obsoletes: readline-devel
Provides: readline5-devel readline-devel

%description devel
This package contains the header files and static libraries for
readline.  Install this package if you want to write or compile a
program that needs readline.

%prep
%setup -q -n readline-%{version}

%build
#autoconf
CC="cc" \
CPPFLAGS="-I/usr/local/include" \
LDFLAGS="-L/usr/local/lib -R/usr/local/lib" \
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
#ln -s libreadline.so.5 libreadline.so
#ln -s libhistory.so.5 libhistory.so
#ln -s libreadline.so.5 libreadline.so.4
#ln -s libhistory.so.5 libhistory.so.4
rm $RPM_BUILD_ROOT/usr/local/info/dir

%clean
rm -rf $RPM_BUILD_ROOT

%post 
if [ -x /usr/local/bin/install-info ] ; then
	/usr/local/bin/install-info --info-dir=/usr/local/info \
		 /usr/local/info/rluserman.info
	/usr/local/bin/install-info --info-dir=/usr/local/info \
		 /usr/local/info/history.info
	/usr/local/bin/install-info --info-dir=/usr/local/info \
		 /usr/local/info/readline.info
fi

%preun
if [ -x /usr/local/bin/install-info ] ; then
	/usr/local/bin/install-info --delete --info-dir=/usr/local/info \
		 /usr/local/info/rluserman.info
	/usr/local/bin/install-info --delete --info-dir=/usr/local/info \
		 /usr/local/info/history.info
	/usr/local/bin/install-info --delete --info-dir=/usr/local/info \
		 /usr/local/info/readline.info
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

%changelog
* Wed Oct 04 2006 Eric Rivas <kc2hmv@nbcs.rutgers.edu> 5.1-2
- Figure out where a so version of old is coming from and get rid of it.
* Wed Jun 28 2006 Jonathan Kaczynski <jmkacz@nbcs.rutgers.edu> 5.1-1
- Gave readline5-devel similar Obsoletes and Provides as readline5
