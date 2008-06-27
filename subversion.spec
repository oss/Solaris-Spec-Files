Summary: 	subversion version control system
Name: 		subversion
Version: 	1.5.0
Release: 	2
License: 	Apache/BSD-style
Source: 	%{name}-%{version}.tar.gz
Group: 		Applications/Internet
Distribution:   RU-Solaris
Vendor:         NBCS-OSS
Packager:       Brian Schubert <schubert@nbcs.rutgers.edu>
Requires: 	gdbm, openssl >= 0.9.8, neon, python, apr, apr-util, expat
BuildRequires: 	gdbm, make, openssl >= 0.9.8, neon-devel, neon-static, cyrus-sasl >= 2.1.18-3
BuildRequires:	python, apr-devel, apr-util-devel, expat-devel, expat-static, cyrus-sasl >= 2.1.18-3
BuildRoot:	%{_tmppath}/%{name}-root

%description
Subversion is a version control system that is a compelling replacement for CVS

%package devel  
Summary: Libraries, includes to develop applications with %{name}.
Group: Applications/Libraries
Requires: %{name} = %{version}

%description devel
The %{name}-devel package contains the header files and static 
libraries
for building applications which use %{name}.

%prep
%setup -q -n %{name}-%{version}

%build
PATH="/opt/SUNWspro/bin:${PATH}" \
CC="cc" CXX="CC" CPPFLAGS="-I/usr/local/include -I/usr/include" \
LD="/usr/ccs/bin/ld" \
LDFLAGS="-L/usr/local/lib -R/usr/local/lib -L/usr/lib -R/usr/lib" \
export PATH CC CXX CPPFLAGS LD LDFLAGS

./configure \
	--prefix=/usr/local \
	--disable-nls \
	--with-ssl \
	--with-libs=/usr/local/ssl \
	--with-neon=/usr/local \
	--without-berkeley-db

# gmake external-all
# gmake local-all
# gmake check
gmake -j3

%install
gmake install DESTDIR=%{buildroot}

rm -rf %{buildroot}/usr/local/lib/*.la

%clean
rm -rf %{buildroot}

%files
%defattr(-, root, root)
/usr/local/lib/lib*.so*
/usr/local/bin
/usr/local/apache2-2.2.9/modules/mod_authz_svn.so
/usr/local/apache2-2.2.9/modules/mod_dav_svn.so
/usr/local/share/man/*

%files devel
%defattr(-,root,root)
/usr/local/include/*
/usr/local/lib/*.a

%changelog
* Fri Jun 27 2008 Brian Schubert <schubert@nbcs.rutgers.edu> - 1.5.0-2
- Added cyrus-sasl >= 2.1.18-3 requirement
* Tue Jun 24 2008 Brian Schubert <schubert@nbcs.rutgers.edu> - 1.5.0-1
- Updated to version 1.5.0
* Mon Jan 14 2008 David Diffenbaugh <davediff@nbcs.rutgers.edu> - 1.4.6-1
- Updated to 1.4.6
* Fri Sep 14 2007 David Lee Halik <dhalik@nbcs.rutgers.edu> - 1.4.5-1
- Bump to 1.4.5
- Built against neon and got rid of the neon255 require
* Wed Aug 22 2007 David Lee Halik <dhalik@nbcs.rutgers.edu> - 1.4.4-1
- Bump to 1.4.4
- Cleaned up spec, set proper requires.
- Turned off db4 since it wasn't using it anyways
* Thu Feb 15 2007 Leo Zhadanovsky <leozh@nbcs.rutgers.edu> - 1.4.3-1
- Updated to 1.4.3
* Fri Dec 08 2006 Leo Zhadanovsky <leozh@nbcs.rutgers.edu> - 1.4.2-2
- Updated for OpenSSL 0.9.8
* Fri Nov 24 2006 Leo Zhadanovsky <leozh@nbcs.rutgers.edu> - 1.4.2-1
- Updated to 1.4.2
* Thu Oct 12 2006 Leo Zhadanovsky <leozh@nbcs.rutgers.edu> - 1.4.0-1
- Updated to 1.4.0
- Made subversion depend on seperate apr, apr-util and neon packages
* Fri May 05 2006 Leo Zhadanovsky <leozh@nbcs.rutgers.edu> - 1.3.1-1
- Updated to 1.3.1, switched to Sun CC, cleaned up spec file, switched to internal neon
