Summary: 	File type information tool
Name: 		file
Version:	5.00
Release:	1
Group:		System Environment/Base
License:	GPL
URL:		http://www.darwinsys.com/file
Source:		ftp://ftp.astron.com/pub/file/%{name}-%{version}.tar.gz
Patch:		file-5.00-warnings.patch
Packager:	Brian Schubert <schubert@nbcs.rutgers.edu>
BuildRequires:	autoconf >= 2.62
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root

%description
File tests each argument in an attempt to classify it.  There are
three sets of tests, performed in this order: filesystem tests, magic 
numbertests, and language tests. The first test that succeeds causes the
file type to be printed.

%package devel
Summary:	Libraries and header files for file development
Group:		Development/Headers
Requires:	%{name} = %{version}-%{release}

%description devel
The file-devel package contains the header files and libmagic library
necessary for developing programs using libmagic.

%prep
%setup -q
%patch -p1
autoreconf

%build
PATH="/opt/SUNWspro/bin:${PATH}"
CC="cc" CXX="CC" GCC="no"
CPPFLAGS="-I/usr/local/include"
LD="/usr/ccs/bin/ld"
LDFLAGS="-L/usr/local/lib -R/usr/local/lib" 
export PATH CC CXX GCC CPPFLAGS LD LDFLAGS

./configure --prefix=%{_prefix} --mandir=%{_mandir}

gmake -j3

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{_prefix}
gmake install DESTDIR=%{buildroot}
rm %{buildroot}%{_libdir}/libmagic.la

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,bin)
%doc README COPYING ChangeLog
%{_bindir}/file
%{_libdir}/libmagic.so.*
%{_datadir}/file
%{_mandir}/man1/file.1
%{_mandir}/man4/magic.4

%files devel
%defattr(-,root,bin)
%{_includedir}/magic.h
%{_libdir}/libmagic.so
%{_libdir}/libmagic.a
%{_mandir}/man3/libmagic.3

%changelog
* Mon Feb 09 2009 Brian Schubert <schubert@nbcs.rutgers.edu> - 5.00-1
- Updated to version 5.00
- Added separate devel package
* Thu Aug 28 2008 Brian Schubert <schubert@nbcs.rutgers.edu> - 4.25-1
- Added a patch needed to compile with Sun cc, bumped to version 4.25
* Thu Apr 10 2008 David Diffenbaugh <davediff@nbcs.rutger.edu> - 4.23-1
- bumped to latest version
* Wed Apr 09 2008 David Diffenbaugh <davediff@nbcs.rutgers.edu> - 4.21-1
- bumped to latest version, added LD env variable, to correct linking issues
