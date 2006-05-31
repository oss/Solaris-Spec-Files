Summary: beecrypt encryption
Name: beecrypt
Version: 4.1.2
Release: 1
Copyright: GPL
Group: Applications/Editors
Source: beecrypt-%{version}.tar.gz
Distribution: RU-Solaris
Vendor: NBCS-OSS
Packager: Christopher J. Suleski <chrisjs@nbcs.rutgers.edu>
BuildRoot: %{_tmppath}/%{name}-root
BuildRequires: automake

%description
BeeCrypt is an ongoing project to provide a strong and fast cryptography 
toolkit. Includes entropy sources, random generators, block ciphers, hash 
functions, message authentication codes, multiprecision integer routines, 
and public key primitives.

%package devel
Summary: %{name} include files, etc.
Requires: %{name} %{buildrequires}
Group: Development
%description devel
%{name} include files, etc.
 
%prep
%setup -q -n beecrypt-%{version}

%build
LD_LIBRARY_PATH="/usr/local/lib"
LD_RUN_PATH="/usr/local/lib"
LDFLAGS="-R/usr/local/lib -L/usr/local/lib"
PATH="/usr/local/bin:$PATH"
CPPFLAGS="-I/usr/local/include"
export LD_LIBRARY_PATH PATH CPPFLAGS LDFLAGS

./autogen.sh
./configure --prefix=/usr/local/ --without-java

gmake

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT

/usr/ccs/bin/strip $RPM_BUILD_ROOT/usr/local/lib/*.so*

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,other)
/usr/local/lib/*.so*

%files devel
%defattr(-,root,other)
/usr/local/lib/*.a
/usr/local/include/beecrypt
