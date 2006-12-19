Summary:	Wireshark - Network Protocol Analyzer (Formerly Ethereal)
Name:		wireshark
Version:	0.99.4
Release:        1
Copyright:	GPL
Group:		System/Utilities
Source:		%{name}-%{version}.tar.gz
Patch:		wireshark.suncc.patch
Distribution: 	RU-Solaris
Vendor: 	NBCS-OSS
Packager: 	Leo Zhadanovsky <leozh@nbcs.rutgers.edu>
BuildRoot:	/var/tmp/%{name}-%{version}-root
Requires:	gtk2 libpcap >= 0.9.5 pcre net-snmp heimdal
BuildRequires:	gtk2-devel libpcap-devel >= 0.9.5 pcre net-snmp heimdal-devel
Obsoletes:	ethereal

%description
Wireshark is one of the world's foremost network protocol analyzers, 
and is the standard in many parts of the industry.

It is the continuation of a project that started in 1998. Hundreds of 
developers around the world have contributed to it, and it it still 
under active development.

Wireshark has a rich feature set which includes the following:

    * Standard three-pane packet browser
    * Multi-platform: Runs on Windows, Linux, OS X, Solaris, FreeBSD, 
      NetBSD, and many others
    * Multi-interface: Along with a standard GUI, Wireshark includes 
      TShark, a text-mode analyzer which is useful for remote capture, 
      analysis, and scripting
    * The most powerful display filters in the industry
    * VoIP analysis
    * Live capture and offline analysis are supported
    * Read/write many different capture file formats: tcpdump 
      (libpcap), NAI's Sniffer™ (compressed and uncompressed), 
      Sniffer™ Pro, NetXray™, Sun snoop and atmsnoop, 
      Shomiti/Finisar Surveyor, AIX's iptrace, Microsoft's Network 
      Monitor, Novell's LANalyzer, RADCOM's WAN/LAN Analyzer, HP-UX 
      nettl, i4btrace from the ISDN4BSD project, Cisco Secure IDS 
      iplog, the pppd log (pppdump-format), the AG 
      Group's/WildPacket's EtherPeek/TokenPeek/AiroPeek, Visual 
      Networks' Visual UpTime and many others
    * Capture files compressed with gzip can be decompressed on the fly
    * Hundreds of protocols are supported, with more being added all 
      the time
    * Coloring rules can be applied to the packet list, which eases 
      analysis 

%package devel 
Summary: Libraries, includes to develop applications with %{name}.
Group: Applications/Libraries
Requires: %{name} = %{version}

%description devel
The %{name}-devel package contains the header files and static libraries
for building applications which use %{name}.

%prep
%setup -q
%patch -p1

%build
PATH="/opt/SUNWspro/bin:${PATH}:/usr/perl5/5.6.1/bin" \
CC="cc" CXX="CC" CPPFLAGS="-I/usr/local/include -I/usr/local/pcre/include" \
LD="/usr/ccs/bin/ld" \
LDFLAGS="-L/usr/local/lib -R/usr/local/lib -L/usr/local/pcre/lib -R/usr/local/pcre/lib" \
export PATH CC CXX CPPFLAGS LD LDFLAGS

./configure --prefix=/usr/local --enable-threads --with-plugins --with-ssl

make

%install
rm -rf $RPM_BUID_ROOT

make install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,bin,bin)
/usr/local/bin/*
/usr/local/lib/*.so*
/usr/local/share/*
/usr/local/man/man1/*

%files devel
%defattr(-,root,root)
/usr/local/include/*
/usr/local/lib/pkgconfig/*

%changelog
* Tue Dec 19 2006 Leo Zhadanovsky <leozh@nbcs.rutgers.edu> - 0.99.4-1
- Initial Rutgers release
