Summary: 	mktemp
Name: 		mktemp
Version: 	1.5
Release: 	2
Copyright: 	GPL
Group: 		Applications/Utilities
Source: 	ftp://ftp.mktemp.org/pub/mktemp/mktemp-1.5.tar.gz
URL: 		http://www.mktemp.org/mktemp/
Distribution: 	RU-Solaris
Vendor: 	NBCS-OSS
Packager: 	Naveen Gavini <ngavini@nbcs.rutgers.edu>
BuildRoot: 	%{_tmppath}/%{name}-root


%description
Mktemp is a small program to allow safe temporary file creation from shell scripts.

%prep
%setup -q

%build
CC="gcc" ./configure --prefix=/usr/local


%install
rm -rf %{buildroot}
mkdir -p %{buildroot}
make install prefix=%{buildroot}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-, root, root)
/bin/mktemp
/man/man1/*

%changelog
* Wed Nov 7 2007 Naveen Gavini <ngavini@nbcs.rutgers.edu> - 1.5-1
- Updated to latest version (1.5).
