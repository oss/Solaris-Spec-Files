Summary: mktemp
Name: mktemp
Version: 1.4
Release: 1ru
Copyright: GPL
Group: Applications/Utilities
Source: ftp://ftp.mktemp.org/pub/mktemp/mktemp-1.4.tar.gz
URL: http://www.mktemp.org/mktemp/
Distribution: RU-Solaris
Vendor: NBCS-OSS
Packager: Christopher J. Suleski <chrisjs@nbcs.rutgers.edu>
BuildRoot: %{_tmppath}/%{name}-root


%description
Mktemp is a small program to allow safe temporary file creation from shell scripts.

%prep
%setup -q

%build
CC="gcc" ./configure --prefix=/usr/local


%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/local
make install prefix=$RPM_BUILD_ROOT/usr/local


%clean
rm -rf $RPM_BUILD_ROOT

%files
/usr/local/bin/mktemp
/usr/local/man/man1/mktemp.1




