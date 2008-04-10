Summary: File type information tool

Name: file
Version: 4.21
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

%build
CC="/opt/SUNWspro/bin/cc" \
CXX="/opt/SUNWspro/bin/cc" \
CPPFLAGS="-I/usr/local/include -I/usr/include" \
LD="/usr/ccs/bin/ld" \
LDFLAGS="-L/usr/local/lib -R/usr/local/lib -L/usr/lib -R/usr/lib" 
export PATH CC CXX CPPFLAGS LD LDFLAGS

./configure --prefix=/usr/local

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

%changelog
* Wed Apr 09 2008 David Diffenbaugh <davediff@nbcs.rutgers.edu> - 4.21-1
- bumped to latest version, added LD env variable, to correct linking issues
