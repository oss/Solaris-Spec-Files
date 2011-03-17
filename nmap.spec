Name:		nmap
Version:	5.51
Release:        1
License:	GPL
Group:		Applications/Network
URL:            http://www.insecure.org/nmap
Source:		%{name}-%{version}.tar.bz2
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root

Requires:	openssl >= 0.9.8

BuildRequires:	lua-devel, pcre-devel, openssl >= 0.9.8, gcc

Summary:        Network exploration tool and security scanner

%description
Nmap ("Network Mapper") is a free open source utility for network 
exploration or security auditing. It was designed to rapidly scan large 
networks, although it works fine against single hosts. Nmap uses raw IP 
packets in novel ways to determine what hosts are available on the 
network, what services (application name and version) those hosts are 
offering, what operating systems (and OS versions) they are running, 
what type of packet filters/firewalls are in use, and dozens of other 
characteristics. Nmap runs on most types of computers and both console 
and graphical versions are available. Nmap is free and open source 
(license).

%prep
%setup -q

%build
PATH="/usr/ccs/bin:${PATH}"
CC="gcc" CXX="g++"
CPPFLAGS="-I/usr/local/ssl/include -I/usr/local/include \
          -D__func__=__FILE__"
LDFLAGS="-L/usr/local/lib -R/usr/local/lib"
export PATH CC CXX CPPFLAGS LDFLAGS

./configure \
	--prefix=%{_prefix}			\
	--mandir=%{_mandir}			\
	--with-openssl=%{_prefix}/ssl 		\
	--with-liblua=%{_prefix}		\
	--with-libpcre=%{_prefix}		\
	--with-ndiff				\
	--without-zenmap

gmake

%install
rm -rf %{buildroot}
gmake install DESTDIR=%{buildroot}

%clean
rm -rf %{buildroot}

%files
%defattr(-, root, root)
%doc
%{_bindir}/*
%{_datadir}/nmap/
%{_mandir}/man1/*

%changelog
* Thu Mar 17 2011 Phillip Quiza <pquiza@nbcs.rutgers.edu> - 5.51-1
- Update to 5.51
* Fri Jun 05 2009 Brian Schubert <schubert@nbcs.rutgers.edu> - 4.76-1
- Update to 4.76
- Optional gui (zenmap) is not built
- Use gcc due to many compilation issues with sun studio
* Wed Nov 14 2007 David Lee Halik <dhalik@nbcs.rutgers.edu> - 4.20-2
- Disable NLS
- Fix some Leo-isms
* Wed Mar 01 2006 Leo Zhadanovsky <leozh@nbcs.rutgers.edu> - 4.0.1-1
- Redid RPM, built for GTK2, made breakout packages, updated to 4.0.1
