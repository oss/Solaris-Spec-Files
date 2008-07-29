Summary: cdrkit - portable command-line CD/DVD recorder software
Name: cdrkit
Version: 1.1.8
Release: 1
Group: Applications/System
Distribution: RU-Solaris
Vendor: NBCS-OSS
Packager: Brian Schubert <schubert@nbcs.rutgers.edu>
License: GPLv2
Source: %{name}-%{version}.tar.gz
Patch: cdrkit-1.1.8-suncc.patch
BuildRoot: %{_tmppath}/%{name}-root 
BuildRequires: cmake, make
Conflicts: cdrtools

%description
Derived from the various programs distributed in the cdrtools suite, cdrkit aims to maintain interface 
compatibility with those tools. The cdrecord program has been renamed to wodim ("write optical disk media") 
so that users will not confuse it with the original cdrecord, which is still maintained by its author, 
Jörg Schilling. wodim, and the other programs distributed with cdrkit, will retain a user interfae 
compatible with the corresponding programs from the cdrtools 2.01.01a08 release, at least for the near 
future. Thus, front-end programs, such as GUI-based CD writer applications, should be able to use cdrkit 
merely by substituting the name "wodim" for the name "cdrecord".

%prep
%setup -q
%patch -p1

%build
PATH="/opt/SUNWspro/bin:${PATH}"
CC="cc" CXX="CC" CPPFLAGS="-I/usr/local/include"
LD="/usr/ccs/bin/ld"
LDFLAGS="-L/usr/local/lib -R/usr/local/lib"
export PATH CC CXX CPPFLAGS LD LDFLAGS

gmake

%install
rm -rf %{buildroot}

gmake install DESTDIR=%{buildroot}

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc ABOUT COPYING FAQ FORK TODO Changelog
%doc doc/*
%{_bindir}/*
%{_sbindir}/netscsid
%{_datadir}/man/man1/*.1
%{_datadir}/man/man5/*.5

%changelog
* Tue Jul 29 2008 Brian Schubert <schubert@nbcs.rutgers.edu> 1.1.8-1
- Initial build.
