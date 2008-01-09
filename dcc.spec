Summary:	Distributed Checksum Clearinghouse 
Name:		dcc
Version:	1.3.80
Release:        1
Copyright:	GPL
Group:		System/Utilities
Source:		%{name}.tar.Z
Distribution: 	RU-Solaris
Vendor: 	NBCS-OSS
Packager: 	David Diffenbaugh <davediff@nbcs.rutgers.edu>
BuildRoot:	/var/tmp/%{name}-%{version}-root

%description
The DCC or Distributed Checksum Clearinghouse is an anti-spam content 
filter that runs on a variety of operating systems. As of mid-2006, it 
involves millions of users, tens of thousands of clients and more than 
250 servers collecting and counting checksums related to more than 300 
million mail messages on week days. The counts can be used by SMTP 
servers and mail user agents to detect and reject or filter spam or 
unsolicited bulk mail. DCC servers exchange or "flood" common checksums. 
The checksums include values that are constant across common variations 
in bulk messages, including "personalizations."

The idea of the DCC is that if mail recipients could compare the mail 
they receive, they could recognize unsolicited bulk mail. A DCC server 
totals reports of checksums of messages from clients and answers queries 
about the total counts for checksums of mail messages. A DCC client 
reports the checksums for a mail message to a server and is told the 
total number of recipients of mail with each checksum. If one of the 
totals is higher than a threshold set by the client and according to 
local whitelists the message is unsolicited, the DCC client can log, 
discard, or reject the message.

Because simplistic checksums of spam would not be effective, the main 
DCC checksums are fuzzy and ignore aspects of messages. The fuzzy 
checksums are changed as spam evolves. Since the DCC started being used 
in late 2000, the fuzzy checksums have been modified several times.

Unless used with isolated DCC servers and so losing much of its power, 
the DCC causes some additional network traffic. However, the 
client-server interaction for a mail message consists of exchanging a 
single pair of UDP/IP datagrams of about 100 bytes. That is often less 
than the several pairs of UDP/IP datagrams required for a single DNS 
query. SMTP servers make DNS queries to check the envelope Mail_From 
value and often several more. As with the Domain Name System, DCC 
servers should be placed near active clients to reduce the DCC network 
costs. DCC servers exchange or flood reports of checksums, but only the 
checksums of bulk mail. Since most mail is not bulk and only 
representative checksums of bulk mail need to be exchanged, flooding 
checksums among DCC servers involves a manageable amount of data. 

%prep
%setup -q

%build
PATH="/opt/SUNWspro/bin:${PATH}" \
CC="cc" CXX="CC" CPPFLAGS="-I/usr/local/include" \
LD="/usr/ccs/bin/ld" \
LDFLAGS="-L/usr/local/lib -R/usr/local/lib" \
export PATH CC CXX CPPFLAGS LD LDFLAGS

./configure --with-installroot=$RPM_BUILD_ROOT --homedir=/usr/local/var/dcc

gmake

%install
slide rm -rf $RPM_BUILD_ROOT

slide gmake install

slide chown -R davediff:studsys $RPM_BUILD_ROOT

%clean
slide rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,bin,bin)
/usr/local/bin/*
/usr/local/man/cat8/*
/usr/local/var/dcc/*

%changelog
* Wed Aug 22 2007 Naveen Gavini <ngavini@nbcs.rutgers.edu> - 1.3.58-1
- Updated to the latest version.
* Wed Mar 02 2007 Leo Zhadanovsky <leozh@nbcs.rutgers.edu> - 1.3.52-1
- Initial Rutgers release
