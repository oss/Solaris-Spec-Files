Summary: 	File type information tool

Name: 		file
Version:	4.25
Release:	1
Group:		System Environment/Base
License:	GPL
Source:		%{name}-%{version}.tar.gz
Patch:		file-4.25-sunccfix.patch
Packager:	Brian Schubert <schubert@nbcs.rutgers.edu>
BuildRoot:	%{_tmppath}/%{name}-root
BuildRequires:	make, autoconf

%description
File tests each argument in an attempt to classify it.  There are
three sets of tests, performed in this order: filesystem tests, magic 
numbertests, and language tests. The first test that succeeds causes the
file type to be printed.

%prep
%setup -q
%patch -p1

%build
PATH="/opt/SUNWspro/bin:/usr/ccs/bin:${PATH}"
CC="cc" CXX="CC"
CPPFLAGS="-I/usr/local/include"
LD="/usr/ccs/bin/ld"
LDFLAGS="-L/usr/local/lib -R/usr/local/lib" 
export PATH CC CXX CPPFLAGS LD LDFLAGS

# Needed because Makefile.am was modified by the patch
autoreconf

./configure --prefix=%{_prefix} --mandir=%{_mandir}

gmake

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{_prefix}
gmake install DESTDIR=%{buildroot}
rm %{buildroot}%{_libdir}/libmagic.la

%clean
rm -rf %{buildroot}

%files
%defattr(-,bin,bin)
%doc README COPYING ChangeLog
%{_bindir}/file
%{_includedir}/magic.h
%{_libdir}/libmagic*
%{_datadir}/file
%{_mandir}/man1/file.1
%{_mandir}/man3/libmagic.3
%{_mandir}/man4/magic.4

%changelog
* Thu Aug 28 2008 Brian Schubert <schubert@nbcs.rutgers.edu> - 4.25-1
- Added a patch needed to compile with Sun cc, bumped to version 4.25
* Thu Apr 10 2008 David Diffenbaugh <davediff@nbcs.rutger.edu> - 4.23-1
- bumped to latest version
* Wed Apr 09 2008 David Diffenbaugh <davediff@nbcs.rutgers.edu> - 4.21-1
- bumped to latest version, added LD env variable, to correct linking issues
