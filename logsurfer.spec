Summary: monitors logfiles
Name: logsurfer
Version: 1.5b
Release: 3
License: Unknown
Group: Utilities/System
URL: http://www.cert.dfn.de/eng/logsurf/
Source: %{name}-%{version}.tar
Buildroot: %{_tmppath}/logsurfer-root

%description
The program "logsurfer" was designed to monitor any text-based logfiles 
on your system in realtime. The large amount of loginformation collected
(like all messages handled by the syslog-daemon or logfiles from your
information services FTP, WWW etc.) makes it nearly impossible to check
your logs manually to find any unusual activity. You need a program to do
this for you. If you do not want to use a script that checks your logs 
in certain time intervals (like once a day) then you might be interested
in the programs like swatch or logsurfer.


%prep
%setup

%build
./configure --prefix=/usr/local
make

%install
# why doesn't make install do these?  I don't know.
mkdir -p $RPM_BUILD_ROOT/usr/local/bin
mkdir -p $RPM_BUILD_ROOT/usr/local/man/man1
mkdir -p $RPM_BUILD_ROOT/usr/local/man/man4
make install prefix=$RPM_BUILD_ROOT/usr/local

%post
echo This needs a config file in /usr/local/etc/logsurfer.conf
echo see /usr/local/doc/logsurfer-%{version}/README
echo man logsurfer.conf 
echo and ftp://ftp.cert.dfn.de/pub/tools/audit/logsurfer/config-examples/


%files
%doc README
%defattr(-,root,root)
/usr/local/bin/logsurfer
/usr/local/man/man*/*

