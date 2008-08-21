Summary: MSWord .doc viewer
Name: catdoc
Version: 0.94.2
Release: 1
Group: Applications/Text
License: GPL
Source: catdoc-%{version}.tar.gz
BuildRoot: /var/tmp/%{name}-root
Vendor: NBCS-OSS
Packager: Brian Schubert <schubert@nbcs.rutgers.edu>

%description
Catdoc is a viewer for MS-Word .doc files.

%prep
%setup -q

%build
PATH="/opt/SUNWspro/bin:${PATH}"
CC="cc" CXX="CC" CPPFLAGS="-I/usr/local/include"
LD="/usr/ccs/bin/ld"
LDFLAGS="-L/usr/local/lib -R/usr/local/lib"
export PATH CC CXX CPPFLAGS LD LDFLAGS

./configure --prefix=/usr/local
gmake

%install
rm -rf %{buildroot}
gmake install prefix=%{buildroot}%{_prefix}

%clean
rm -rf %{buildroot}

%files
%defattr(-,bin,bin)
%doc COPYING README TODO NEWS
%{_bindir}/*
%{_mandir}/man1/*.1
%{_datadir}/catdoc

%changelog
* Thu Aug 21 2008 Brian Schubert <schubert@nbcs.rutgers.edu> - 0.94.2-1
- Fixed/cleaned up some things and bumped to version 0.94.2
