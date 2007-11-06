Summary:	ClamSMTP
Name:		clamsmtp
Version:	1.9
Release:        1
Copyright:	GPL
Group:		Applications/System
Source:		%{name}-%{version}.tar.gz
Distribution: 	RU-Solaris
Vendor: 	NBCS-OSS
Packager: 	Naveen Gavini <ngavini@nbcs.rutgers.edu>
BuildRoot:	/var/tmp/%{name}-%{version}-root
Requires:	clamav

%description
ClamSMTP is an SMTP filter that allows you to check for viruses using 
the ClamAV anti-virus software. It accepts SMTP connections and forwards 
the SMTP commands and responses to another SMTP server. The 'DATA' email 
body is intercepted and scanned before forwarding.

ClamSMTP aims to be lightweight, reliable, and simple rather than have a 
myriad of options. It's written in C without major dependencies. If you 
need more options then you could use something big like AMaViS which is 
written in PERL and can do almost anything.

I wrote this with the Postfix mail server in mind. Here's how to 
configure it as a Postfix Content Filter.

ClamSMTP can also be used as a transparent proxy to filter an entire 
network's SMTP traffic at the router.

%prep
%setup -q

%build
PATH="/opt/SUNWspro/bin:${PATH}" \
CC="cc" CXX="CC" CPPFLAGS="-I/usr/local/include" \
LD="/usr/ccs/bin/ld" \
LDFLAGS="-L/usr/local/lib -R/usr/local/lib" \
export PATH CC CXX CPPFLAGS LD LDFLAGS

./configure --prefix=/usr/local

make

%install
rm -rf $RPM_BUID_ROOT

make install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,bin,bin)
/usr/local/sbin/*
/usr/local/share/man/*

%changelog
* Tue Nov 6 2007 Naveen Gavini <ngavini@nbcs.rutgers.edu> - 1.9-1
- Updated to 1.9
* Tue Jan 30 2007 Leo Zhadanovsky <leozh@nbcs.rutgers.edu> - 1.8-1
- Initial Rutgers release
