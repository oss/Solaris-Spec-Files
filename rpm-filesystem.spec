Summary:	Basic filesystem needed by rpm 	
Name: 		rpm-filesystem
Version: 	1.0
Release: 	4
Group: 		System Environment/Base
Copyright: 	GPL
Distribution:   RU-Solaris
Vendor:         NBCS-OSS
Packager:       David Lee Halik <dhalik@nbcs.rutgers.edu>
BuildRoot: 	/var/tmp/%{name}-%{version}-root
Provides:	/usr /var /usr/local /var/local /usr/local/lib /usr/local/man /usr/local/share /usr/local/doc /usr/local/gnu /usr/local/gnu/bin /usr/local/gnu/info /usr/local/gnu/man /usr/local/include

%description
Base RPM package that throws down the need /var/local and /usr/local
paths. This is necessary for RPM 4 to be able to install due to strict
file restrictions. This package contains no files or directories.

%prep

%build

%install

%clean

%post
cat << EOF
====================================
Note: This package contains no files
and is for RPM compatability only!
====================================
EOF

%files

%changelog
* Mon Sep 17 2007 David Lee Halik <dhalik@nbcs.rutgers.edu> - 1.0-1
- Attempting the first rpm filesystem package
