Name: rsync 
Version: 2.6.0
Release: 1
Copyright: GPL 
Group: Applications/Internet
Summary: rsync is an open source utility that provides fast incremental file transfer. 
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
CC='/opt/SUNWspro/bin/cc' CXX='/opt/SUNWSpro/bin/CC' ./configure --prefix=/usr/local
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