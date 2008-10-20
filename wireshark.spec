Summary:	Wireshark - Network Protocol Analyzer (Formerly Ethereal)
Name:		wireshark
Version:	1.1.1
Release:        1
License:	GPL
Group:		System/Utilities
Source:		%{name}-%{version}.tar.gz
Distribution: 	RU-Solaris
Vendor: 	NBCS-OSS
Packager: 	Brian Schubert <schubert@nbcs.rutgers.edu>
BuildRoot:	/var/tmp/%{name}-%{version}-root
Requires:       glib2, gtk2, libpcap >= 0.9.8, pcre, expat, net-snmp, openssl
Requires:	zlib, pango, atk, cairo, pixman, libjpeg, fontconfig, libpng3
BuildRequires:  glib2-devel, gtk2-devel, libpcap-devel >= 0.9.8, perl
BuildRequires:	pcre-devel, expat-devel, openssl-devel, zlib-devel
BuildRequires:	libpcap-devel, pango-devel, atk-devel, fontconfig-devel 
BuildRequires:	libpng3-devel, xrender-devel, render, libjpeg-devel, 
BuildRequires:	cairo-devel, pixman-devel, libpng3-devel
Obsoletes: 	ethereal

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
Requires: %{name} = %{version}-%{release}

%description devel
The %{name}-devel package contains the header files and static libraries
for building applications which use %{name}.

%package static
Summary: Static libraries to develop applications with %{name}.
Group: Applications/Libraries
Requires: %{name} = %{version}

%description static
The %{name}-static package contains the static libraries
for building applications which use %{name}.

%prep
%setup -q

%build
PATH="/opt/SUNWspro/bin:${PATH}:/usr/perl5/5.6.1/bin" \
CC="cc" CXX="CC" CPPFLAGS="-I/usr/local/include " \
LD="/usr/ccs/bin/ld" \
LDFLAGS="-L/usr/local/lib -R/usr/local/lib " \
export PATH CC CXX CPPFLAGS LD LDFLAGS

./configure \
	--prefix=%{_prefix} \
	--mandir=%{_mandir} \
	--enable-threads \
	--with-plugins \
	--with-ssl \
	--enable-gtk2 \
	--enable-usr-local

gmake -j3

%install
rm -rf %{buildroot}

gmake install DESTDIR=%{buildroot}

%clean
rm -rf %{buildroot}

%files
%doc AUTHORS COPYING ChangeLog FAQ NEWS README 
%defattr(-,bin,bin)
%{_bindir}/*
%{_libdir}/*.so*
%{_datadir}/wireshark
%{_mandir}/man1/*
%{_mandir}/man4/*
%dir %{_libdir}/wireshark
%dir %{_libdir}/wireshark/plugins
%dir %{_libdir}/wireshark/plugins/%{version}
%{_libdir}/wireshark/plugins/%{version}/*.so

%files devel
%defattr(-,root,root)

%files static
%defattr(-,root,root)
%{_libdir}/*.la
%{_libdir}/wireshark/plugins/%{version}/*.la

%changelog
* Wed Oct 15 2008 Brian Schubert <schubert@nbcs.rutgers.edu> - 1.1.1-1
- Fixed a few things and bumped to 1.1.1 (development release)
* Tue Jul 22 2008 David Diffenbaugh <davediff@nbcs.rutgers.edu> - 1.0.2-1
- bumped to 1.0.2
* Mon Jun 16 2008 David Diffenbaugh <davediff@nbcs.rutgers.edu> - 1.0.0-1
- bumped to 1.0.0
* Mon Jan 07 2008 David Lee Halik <dhalik@nbcs.rutgers.edu> - 0.99.7-2
- Bump
* Fri Oct 12 2007 David Lee Halik <dhalik@nbcs.rutgers.edu> - 0.99.7-SVN
- Bump
* Tue Dec 19 2006 Leo Zhadanovsky <leozh@nbcs.rutgers.edu> - 0.99.4-1
- Initial Rutgers release
