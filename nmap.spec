Summary:	Network exploration tool and security scanner
Name:		nmap
Version:	4.11
Release:        1
Copyright:	GPL
Group:		Applications/System
Source:		%{name}-%{version}.tar.bz2
URL:		http://www.insecure.org/nmap
Distribution: 	RU-Solaris
Vendor: 	NBCS-OSS
Packager: 	Leo Zhadanovsky <leozh@nbcs.rutgers.edu>
BuildRoot:	/var/tmp/%{name}-%{version}-root

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

%package frontend
Summary: GTK2 frontend for %{name}
Group: Applications/System
Requires: %{name} = %{version}

%description frontend
The %{name}-frontend package contains the GTK2 and X11 frontends for 
%{name}.

%prep
%setup -q

%build
CPPFLAGS="-I/usr/local/include -I/usr/sfw/include"
LDFLAGS="-L/usr/local/lib -R/usr/local/lib -L/usr/sfw/lib -R/usr/sfw/lib"
LD_LIBRARY_PATH="/usr/local/lib:/usr/sfw/lib"
LD_RUN_PATH="/usr/local/lib:/usr/sfw/lib"
CC="gcc" 
export CPPFLAGS LDFLAGS LD_LIBRARY_PATH LD_RUN_PATH CC

#PATH="/opt/SUNWspro/bin:${PATH}" \
#CC="cc" CXX="CC" CPPFLAGS="-I/usr/local/include" \
#LD="/usr/ccs/bin/ld" \
#LDFLAGS="-L/usr/local/lib -R/usr/local/lib" \
#export PATH CC CXX CPPFLAGS LD LDFLAGS

./configure --prefix=/usr/local --with-openssl=/usr/local/ssl

#for i in `find . -name '*.cc'`; do mv $i $i.wrong; sed -e 's/__FUNCTION__/__FILE__/g' $i.wrong > $i; done

gmake

%install
rm -rf $RPM_BUID_ROOT

make install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,bin,bin)
/usr/local/bin/nmap
/usr/local/share/nmap/*
/usr/local/man/man1/nmap.1

%files frontend
%defattr(-,bin,bin)
/usr/local/bin/nmapfe
/usr/local/bin/xnmap
/usr/local/share/applications/*
/usr/local/man/man1/nmapfe.1
/usr/local/man/man1/xnmap.1

%changelog
* Wed Mar 01 2006 Leo Zhadanovsky <leozh@nbcs.rutgers.edu> - 4.0.1-1
- Redid RPM, built for GTK2, made breakout packages, updated to 4.0.1
