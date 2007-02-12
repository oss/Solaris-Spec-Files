Summary: File type information tool

Name: file
Version: 4.19
Release: 1
Group: System Environment/Base
Copyright: GPL
Source: %{name}-%{version}.tar.gz
BuildRoot: /var/tmp/%{name}-root

%description
File tests each argument in an attempt to classify it.  There are
three sets of tests, performed in this order: filesystem tests, magic 
numbertests, and language tests. The first test that succeeds causes the
file type to be printed.

%prep

%setup -q 
CC="/opt/SUNWspro/bin/cc" CXX="/opt/SUNWspro/bin/cc" CPPFLAGS="-I/usr/local/include" LDFLAGS="-L/usr/local/lib -R/usr/local/lib" ./configure --prefix=/usr/local

%build
gmake

%install
mkdir -p $RPM_BUILD_ROOT/usr/local 
gmake install prefix=$RPM_BUILD_ROOT/usr/local
rm $RPM_BUILD_ROOT/usr/local/lib/libmagic.la

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,bin,bin)
/usr/local/bin/file
/usr/local/include/magic.h
/usr/local/lib/libmagic*
/usr/local/man/man1/file.1
/usr/local/man/man3/libmagic.3
/usr/local/man/man4/magic.4
/usr/local/share/file/magi*
