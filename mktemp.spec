Summary: 	Program for safe creation of temporary files
Name: 		mktemp
Version: 	1.6
Release: 	1
License: 	GPL
Group: 		Applications/Utilities
Source: 	ftp://ftp.mktemp.org/pub/mktemp/mktemp-%{version}.tar.gz
URL: 		http://www.mktemp.org/mktemp/
Distribution: 	RU-Solaris
Vendor: 	NBCS-OSS
Packager: 	Brian Schubert <schubert@nbcs.rutgers.edu>
BuildRoot: 	%{_tmppath}/%{name}-root

%description
Mktemp is a small program to allow safe temporary file creation from shell scripts.

%prep
%setup -q

%build
PATH="/opt/SUNWspro/bin:/usr/ccs/bin:${PATH}" \
CC="cc" CXX="CC" CPPFLAGS="-I/usr/local/include" \
LDFLAGS="-L/usr/local/lib -R/usr/local/lib" \
export PATH CC CXX CPPFLAGS LDFLAGS

./configure
gmake

%install
rm -rf %{buildroot}

gmake install \
prefix=%{buildroot}%{_prefix} \
exec_prefix=%{buildroot}%{_prefix} \
mandir=%{buildroot}%{_mandir}

%clean
rm -rf %{buildroot}

%files
%defattr(-, root, root)
%doc README RELEASE_NOTES LICENSE
%{_bindir}/mktemp
%{_mandir}/man1/mktemp.1

%changelog
* Thu Aug 21 2008 Brian Schubert <schubert@nbcs.rutgers.edu> - 1.6-1
- Fixed some things, added docs, updated to version 1.6
* Wed Nov 7 2007 Naveen Gavini <ngavini@nbcs.rutgers.edu> - 1.5-1
- Updated to latest version (1.5).
