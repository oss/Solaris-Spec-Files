%define name    ipmitool
%define ver     1.8.8
%define rel     2

Summary: 	Intel Platform Management Interface tools
Name: 		%{name}
Version: 	%{ver} 
Release: 	%{rel}
Copyright: 	GPL
Group: 		System/Utilities
Source: 	http://downloads.sourceforge.net/ipmitool/ipmitool-1.8.8.tar.gz
URL: 		http://ipmitool.sourceforge.net/
Distribution: 	RU-Solaris
Vendor: 	NBCS-OSS
Packager:       Aaron Richton <richton@nbcs.rutgers.edu>
BuildRoot: 	%{_tmppath}/%{name}-root


%description
IPMItool provides a simple command-line interface to IPMI-enabled devices through an IPMIv1.5 or IPMIv2.0 LAN interface or Linux/Solaris kernel driver.

%prep
%setup -q

%build
# bug near include/ipmitool/helper.h:# define __maxlen(a, b) ({ int x=strlen(a); int y=strlen(b); (x > y) ? x : y;})
# gcc only!
#CC="/opt/SUNWspro/bin/cc" CXX="/opt/SUNWspro/bin/CC" \
#LD="/usr/ccs/bin/ld" CFLAGS='-g -xs' \
LDFLAGS="-L/usr/local/lib -R/usr/local/lib -L/usr/local/ssl/lib -R/usr/local/ssl/lib" \
CPPFLAGS="-I/usr/local/include -I/usr/local/ssl/include" \
./configure --prefix=/usr/local

gmake

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT
gmake install DESTDIR=$RPM_BUILD_ROOT
rm -Rf $RPM_BUILD_ROOT/usr/local/share/doc/ipmitool

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc AUTHORS COPYING ChangeLog README
/usr/local/bin/*
/usr/local/man/man1/*
/usr/local/man/man8/*
/usr/local/sbin/*
%dir /usr/local/share/ipmitool
/usr/local/share/ipmitool/*
