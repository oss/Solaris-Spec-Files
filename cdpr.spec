Summary: 	Cisco Discovery Protocol Reporter
Name: 		cdpr
Version: 	2.2.0
Release: 	1
Copyright: 	GPL
Group: 		Applications/Internet
Source: 	http://www.monkeymental.com/mmfiles/cdpr-2.2.0.tar.gz
URL: 		http://www.monkeymental.com/
Distribution: 	RU-Solaris
Vendor: 	NBCS-OSS
Packager:       Jonathan Kaczynski <jmkacz@nbcs.rutgers.edu>
BuildRoot: 	%{_tmppath}/%{name}-root
Requires:       libpcap
BuildRequires:  libpcap

%description
Cisco Discovery Protocol Reporter

%prep
%setup -q

%build
PATH="/opt/SUNWspro/bin:$PATH"
CC="/opt/SUNWspro/bin/cc"
CXX="/opt/SUNWspro/bin/CC"
export PATH CC CXX CFLAGS LDFLAGS

sed "s/CFLAGS = -Wall -W -O2 -ggdb/#CFLAGS = -Wall -W -O2 -ggdb/" Makefile > z
mv z Makefile

sed "s@#CFLAGS = -DSOLARIS -Wall -I. -I../libpcap-0.7.1 -L../libpcap-0.7.1 -ggdb@CFLAGS = -DSOLARIS -Wall -I. -I/usr/local/include -L/usr/local/lib -R/usr/local/lib -ggdb@" Makefile > z
mv z Makefile

sed "s/LDFLAGS = -lpcap/#LDFLAGS = -lpcap/" Makefile > z
mv z Makefile

sed "s/#LDFLAGS = -lsocket -lnsl -lpcap/LDFLAGS = -lsocket -lnsl -lpcap/" Makefile > z
mv z Makefile

gmake

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/local/bin/
cp cdpr %{buildroot}/usr/local/bin/
chmod 0755 %{buildroot}/usr/local/bin/

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc COPYING INSTALL README
/usr/local/bin/cdpr

%changelog
* Fri Jun 02 2006 Jonathan Kaczynski <jmkacz@nbcs.rutgers.edu> - 2.2.0-1
- Initial package
