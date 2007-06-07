Summary: cronolog
Name: cronolog
Version: 1.6.2
Release: 3
License: GPL2
Group: Utilities
Source0: http://www.cronolog.org/download/cronolog-%{version}.tar.gz

BuildRoot: /var/local/tmp/%{name}-root

%description
cronolog is a simple filter program that reads log file entries from standard
input and writes each entry to the output file specified by a filename
template and the current date and time. When the expanded filename changes,
the current file is closed and a new one opened. cronolog is intended to be
used in conjunction with a Web server, such as Apache, to split the access
log into daily or monthly logs.

Note: This program is compiled with Large File support.


%prep
%setup 


%build
PATH="/opt/SUNWspro/bin:/usr/ccs/bin:${PATH}"
CC="cc"
LARGEFLAGS=`getconf LFS_CFLAGS`
CFLAGS="-g -xs ${LARGEFLAGS}"
export PATH CC CFLAGS

./configure --prefix=/usr/local
make

%install
make install DESTDIR=$RPM_BUILD_ROOT


%post 

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-, root, root)
/usr/local/sbin/cronolog
/usr/local/sbin/cronosplit
/usr/local/info/cronolog.info
/usr/local/man/man1/cronolog.1m
/usr/local/man/man1/cronosplit.1m

%changelog
* Thu Jun 07 2007 Eric Rivas <kc2hmv@nbcs.rutgers.edu> - 1.6.2-3
- Build with large file support.

