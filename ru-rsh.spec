# This package shouldn't be a binary-only package, but the source for
# in.rshd seems to be gone, as far as I can tell.

Summary: Rsh daemon and client replacements
Name: ru-rsh
Version: 1.0
Release: 4
Group: System Environment/Base
Copyright: Rutgers
Source: ru-rsh.tar.gz
BuildRoot: /var/tmp/%{name}-root

%description
This package has Rutgers-specific replacements for the rsh daemon and
client.

%prep
%setup -q -n files

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT
find . -print | cpio -pdm $RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%attr(0755,root,other) /usr/local/sbin/in.rshd
%attr(0755,root,other) /usr/local/sbin/in.rlogind
%attr(0555,root,other) /usr/local/sbin/in.rexecd
%attr(0644,root,other) /usr/local/man/man1m/*
%attr(0644,root,other) /usr/local/man/man4/*
%attr(4755,root,other) /usr/local/bin/rrsh
%attr(4755,root,other) /usr/local/bin/rrcp
%attr(-,root,other)    /usr/local/bin/rsh
