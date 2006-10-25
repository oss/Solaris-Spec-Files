Summary: libIDL
Name: libIDL
Version: 0.6.8
Release: 2
Copyright: LGPL
Group: Applications/Editors
Source: libIDL-0.6.8.tar.gz
URL: http://www.libidl.org
Distribution: RU-Solaris
Vendor: NBCS-OSS
Packager: Jonathan Kaczynski <jmkacz@nbcs.rutgers.edu>
BuildRoot: %{_tmppath}/%{name}-root


%description
Phoenix needs this.

%prep
%setup -q

%build
CPPFLAGS="-I/usr/local/include"
LDFLAGS="-L/usr/local/lib -R/usr/local/lib"
LD_LIBRARY_PATH="/usr/local/lib"
LD_RUN_PATH="/usr/local/lib"
CC="gcc" 
export CPPFLAGS LDFLAGS LD_LIBRARY_PATH LD_RUN_PATH CC

#glibtest is a POS and has been disabled
./configure --prefix=/usr/local --disable-glibtest


%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/local
make install prefix=$RPM_BUILD_ROOT/usr/local

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,other)
 /usr/local/bin/libIDL-config
 /usr/local/include/libIDL/IDL.h
 /usr/local/info/libIDL.info
 /usr/local/lib/libIDL-0.6.so.0
 /usr/local/lib/libIDL-0.6.so.0.4.4
 /usr/local/lib/libIDL.a
 /usr/local/lib/libIDL.so
 /usr/local/lib/libIDLConf.sh
 /usr/local/share/aclocal/libIDL.m4
