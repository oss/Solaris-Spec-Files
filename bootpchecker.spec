Summary: Check integrity of bootptab file
Name: bootpchecker
Version: 1.0.1
Release: 2
Group: Applications/Intenet
Copyright: Rutgers
Source: bootpchecker.tar.gz
BuildRoot: /var/tmp/%{name}-root
Requires: perl

%description
Checks integrity of bootptab file.

%prep
%setup -q -n files

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/local/bin/
install usr/local/bin/bootpchecker \
   $RPM_BUILD_ROOT/usr/local/bin/bootpchecker

%clean
rm -rf $RPM_BUILD_ROOT

%files
%attr(0755,root,other) /usr/local/bin/bootpchecker
