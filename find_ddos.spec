Summary: Find distributed denial-of-service
Name: find_ddos
Version: 4.2
Release: 3
Source: find_ddos-%{version}.tar.gz
Copyright: FBI
Group: Applications/Internet
BuildRoot: /var/tmp/%{name}-root

%description
In response to a number of recent distributed denial-of-service (DDOS)
attacks that have been reported, the National Infrastructure
Proctection Center (NIPC) Special Technology Applications Unit (STAU)
has developed a tool to assist in combating this threat.  The tool
(called "find_ddos") is intended to scan a local system that is either
known or suspected to contain a DDOS program.  It is capable of
scanning executing processes on Solaris 2.6 or later, and of scanning
local files on a Solaris 2.x (or later) system.

[from the README]

%prep
%setup -q -n files

%build
# do nothing

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT
find usr -print | cpio -pdmv $RPM_BUILD_ROOT

# fix symlink
cd $RPM_BUILD_ROOT
rm usr/local/sbin/find_ddos
ln -s ../find_ddos/find_ddos usr/local/sbin/find_ddos

%post
chmod 0700 /usr/local/find_ddos

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-, root, other)
%attr(0500, root, other) /usr/local/find_ddos/find_ddos
%attr(0400, root, other) /usr/local/find_ddos/README
/usr/local/sbin/*
