Summary: 	subversion version control system
Name: 		subversion
Version: 	1.3.2
Release: 	1
License: 	Apache/BSD-style
Source: 	%{name}-%{version}.tar.bz2
Group: 		Applications/Internet
Distribution:   RU-Solaris
Vendor:         NBCS-OSS
Packager:       Leo Zhadanovsky <leozh@nbcs.rutgers.edu>
Requires: 	db4, gdbm, openssl
BuildRequires: 	make, db4, gdbm, openssl, neon-static
BuildRoot:	%{_tmppath}/%{name}-root
Provides: 	neon

%description
Subversion is a version control system that is a compelling replacement for CVS

%package devel  
Summary: Libraries, includes to develop applications with %{name}.
Group: Applications/Libraries
Requires: %{name} = %{version}
Provides: neon-devel

%description devel
The %{name}-devel package contains the header files and static 
libraries
for building applications which use %{name}.

%prep
%setup -q -n %{name}-%{version}

%build
PATH="/opt/SUNWspro/bin:${PATH}" \
CC="cc" CXX="CC" CPPFLAGS="-I/usr/local/include" \
LD="/usr/ccs/bin/ld" \
LDFLAGS="-L/usr/local/lib -R/usr/local/lib" \
export PATH CC CXX CPPFLAGS LD LDFLAGS

./autogen.sh
./configure --prefix=/usr/local --with-zlib -disable-nls --with-ssl --with-libs=/usr/local/ssl
# --with-apr=/usr/local/apache2-%{apache_version}/bin\
# --with-apr-util=/usr/local/apache2-%{apache_version}/bin

# gmake external-all
# gmake local-all
# gmake check
gmake

%install
gmake install DESTDIR=$RPM_BUILD_ROOT
rm -f %{buildroot}/usr/local/lib/*.a
rm -f %{buildroot}/usr/local/lib/*.la
rm -f %{buildroot}/usr/local/apr/lib/*.a
rm -f %{buildroot}/usr/local/apr/lib/*.la
rm -f %{buildroot}/usr/local/lib/libneon.la

%clean
rm -rf %{buildroot}

%files
%defattr(-, root, root)
/usr/local/lib/lib*.so*
/usr/local/lib/*.exp
/usr/local/build
/usr/local/bin
/usr/local/man
/usr/local/share/doc

%files devel
%defattr(-,root,root)
/usr/local/include/*
/usr/local/lib/pkgconfig/*

%changelog
* Fri May 05 2006 Leo Zhadanovsky <leozh@nbcs.rutgers.edu> - 1.3.1-1
- Updated to 1.3.1, switched to Sun CC, cleaned up spec file, switched to internal neon
