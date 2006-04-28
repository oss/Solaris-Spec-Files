Name: rsync
Version: 2.6.8
Release: 1
Copyright: GPL 
Group: Applications/Internet
Summary: rsync is an open source utility that provides fast incremental file transfer. 
URL: http://samba.anu.edu.au/rsync
Distribution: RU-Solaris
Vendor: NBCS-OSS
Packager: Leo Zhadanovsky <leozh@nbcs.rutgers.edu>
Source: rsync-%{version}.tar.gz
BuildRoot: /var/tmp/%{name}-root

%description
rsync uses the "rsync algorithm" which provides a very fast method for
bringing remote files into sync. It does this by sending just the
differences in the files across the link, without requiring that both
sets of files are present at one of the ends of the link beforehand.
At first glance this may seem impossible because the calculation of
diffs between two files normally requires local access to both
files. 

%prep
%setup -q

%build
PATH="/opt/SUNWspro/bin:${PATH}" \
CC="cc -xO4" CXX="CC -xO4" CPPFLAGS="-I/usr/local/include" \
LD="/usr/ccs/bin/ld" \
LDFLAGS="-L/usr/local/lib -R/usr/local/lib" \
export PATH CC CXX CPPFLAGS LD LDFLAGS

./configure --prefix=/usr/local
make

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/local
make install prefix=$RPM_BUILD_ROOT/usr/local

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,bin,bin)
/usr/local/bin/rsync
/usr/local/man/man1/rsync.1
/usr/local/man/man5/rsyncd.conf.5
