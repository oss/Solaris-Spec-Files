Summary: 	Cisco Discovery Protocol Reporter
Name: 		cdpr
Version: 	2.2.1
Release: 	1
Copyright: 	GPL
Group: 		Applications/Internet
Source: 	http://www.monkeymental.com/mmfiles/%{name}-%{version}.tar.gz
URL: 		http://www.monkeymental.com/
Distribution: 	RU-Solaris
Vendor: 	NBCS-OSS
Packager:       David Lee Halik <dhalik@nbcs.rutgers.edu>
BuildRoot: 	%{_tmppath}/%{name}-root
Requires:       libpcap
BuildRequires:  libpcap

%description
Cisco Discovery Protocol Reporter

%prep
%setup -q

%build
PATH="/opt/SUNWspro/bin:${PATH}" \
CC="cc" CXX="CC" CPPFLAGS="-I/usr/local/include" \
LD="/usr/ccs/bin/ld" \
LDFLAGS="-L/usr/local/lib -R/usr/local/lib"
export PATH CC CXX CPPFLAGS LD LDFLAGS

sed "s/CFLAGS = -Wall -W -O2 -ggdb/#CFLAGS = -Wall -W -O2 -ggdb/" Makefile > z
mv z Makefile

sed "s@#CFLAGS = -DSOLARIS -Wall -I. -I../libpcap-0.7.1 -L../libpcap-0.7.1 -ggdb@CFLAGS = -DSOLARIS -I. -I/usr/local/include -L/usr/local/lib -R/usr/local/lib -g@" Makefile > z
mv z Makefile

sed "s/LDFLAGS = -lpcap/#LDFLAGS = -lpcap/" Makefile > z
mv z Makefile

sed "s/#LDFLAGS = -lsocket -lnsl -lpcap/LDFLAGS = -lsocket -lnsl -lpcap/" Makefile > z
mv z Makefile

sed "s/gcc/$(CC)/g" Makefile > z
mv z Makefile

for i in cdpr.h u_ints.h cdp.h cdprs.c conffile.c
do
	/usr/bin/dos2unix $i > z
	mv z $i
done

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
* Tue Nov 06 2007 David Lee Halik <dhalik@nbcs.rutgers.edu> - 2.2.1-1
- Bump to 2.2.1
- Switched to SunCC
- Removed BAD WINDOWS line endings
* Fri Jun 02 2006 Jonathan Kaczynski <jmkacz@nbcs.rutgers.edu> - 2.2.0-1
- Initial package
