Summary: Edit bootptab file
Name: bootpedit
Version: 1.0
Release: 2
Group: Applications/Intenet
Copyright: Rutgers
Source: bootpedit.tar.gz
Requires: perl
BuildRoot: /var/tmp/%{name}-root

%description
Edit bootptab with your favorite editor.

%prep
%setup -q -n files

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/local/bin/
install usr/local/bin/bootpedit $RPM_BUILD_ROOT/usr/local/bin/bootpedit

%post
echo To use this script, you need group cisco, gid 2009.

%clean
rm -rf $RPM_BUILD_ROOT

%files
%attr(0755,root,other) /usr/local/bin/bootpedit
