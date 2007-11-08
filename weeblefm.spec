Summary: 	weeblefm
Name: 		weeblefm
Version: 	1.2.1
Release: 	1
Group: 		System Environment/Base
Copyright: 	GPL
Distribution:   RU-Solaris
Vendor:         NBCS-OSS
Packager:       Naveen Gavini <ngavini@nbcs.rutgers.edu>
Source: 	%{name}-%{version}.tar.gz
BuildRoot: 	%{_tmppath}/%{name}-root
Requires: 	php

%description
Weeble File Manager is a web based file manager / ftp client, built on php4. It allows users to Copy, Move, Rename, Upload, 
Download, & Edit files on an FTP server, through their web browsers.

%prep
%setup -q -n weeblefm

%build
PATH="/opt/SUNWspro/bin:${PATH}" \
CC="cc" CXX="CC" CPPFLAGS="-I/usr/local/include" \
LD="/usr/ccs/bin/ld" \
LDFLAGS="-L/usr/local/lib -R/usr/local/lib" \
export PATH CC CXX CPPFLAGS LD LDFLAGS

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/local/apache/htdocs/weeblefm
cp -r * %{buildroot}/usr/local/apache/htdocs/weeblefm/

%clean
rm -rf %{buildroot}

%files
%attr(0755, root, bin) /usr/local/apache/htdocs/weeblefm

%changelog
* Wed Nov 7 2007 Naveen Gavini <ngavini@nbcs.rutgers.edu> - 1.2.1-1
- Updated to the latest version (1.2.1).

