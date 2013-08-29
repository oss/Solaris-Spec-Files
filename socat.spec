Summary: 	socat - multipurpose relay
Name: 		socat
Version: 	1.6.0.1
Release: 	1
License: 	GPL
Group: 		Applications/Communications
Source0: 	http://www.dest-unreach.org/socat/download/socat-%{version}.tar.gz
#Patch: 		socat.suncc.patch
Distribution:   RU-Solaris
Vendor:         NBCS-OSS
Packager:       Brian Schubert <schubert@nbcs.rutgers.edu>
Requires: 	readline5
Requires: 	openssl >= 0.9.8
BuildRequires: 	openssl >= 0.9.8
BuildRoot: 	/var/tmp/%{name}-root

%description
socat is a relay for bidirectional data transfer between two independent data
channels. Each of these data channels may be a file, pipe, device (terminal or
modem etc.), socket (UNIX, IP4, IP6 - raw, UDP, TCP), a file descriptor (stdin
etc.), a program, or an arbitrary combination of two of these.

%prep
%setup -q
#%patch -p1

%build
#PATH="/opt/SUNWspro/bin:$PATH"
#CC="gcc" # configure is stupid and accepts nothing else
#CPPFLAGS='-I/usr/local/include -I/usr/local/ssl/include'
#LIBS='-L/usr/local/lib -R/usr/local/lib -L/usr/local/ssl/lib -R/usr/local/ssl/lib'
#export CPPFLAGS LIBS PATH CC

PATH="/opt/SUNWspro/bin:${PATH}" \
CC="cc" CXX="CC" CPPFLAGS="-I/usr/local/include" \
LD="/usr/ccs/bin/ld" \
LDFLAGS="-L/usr/local/lib -R/usr/local/lib -L/usr/local/ssl/lib -R/usr/local/ssl/lib" \
export PATH CC CXX CPPFLAGS LD LDFLAGS

./configure --prefix=/usr/local --disable-libwrap

for i in `find . -name 'Makefile*'`; do mv $i $i.wrong; sed -e 's/-Wall -Wno-parentheses//g' $i.wrong > $i; rm $i.wrong; done

make

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/local/bin
mkdir -p $RPM_BUILD_ROOT/usr/local/man/man1
make install DESTDIR=$RPM_BUILD_ROOT
#install -m 755 socat $RPM_BUILD_ROOT/usr/local/bin/
#install -m 755 procan $RPM_BUILD_ROOT/usr/local/bin/
#install -m 755 filan $RPM_BUILD_ROOT/usr/local/bin/
#install -m 644 socat.1 $RPM_BUILD_ROOT/usr/local/man/man1/
#cd $RPM_BUILD_ROOT/usr/local/man/man1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc README CHANGES EXAMPLES SECURITY FAQ BUGREPORTS
%doc COPYING COPYING.OpenSSL FILES PORTING DEVELOPMENT
/usr/local/bin/socat
/usr/local/bin/procan
/usr/local/bin/filan
/usr/local/man/man1/socat.1*

%changelog
* Fri Jun 13 2008 Brian Schubert <schubert@nbcs.rutgers.edu> - 1.6.0.1-1
- Updated to version 1.6.0.1
* Thu Dec 14 2006 Leo Zhadanovsky <leozh@nbcs.rutgers.edu> - 1.5.0.0-4
- Changed for OpenSSL 0.9.8
- Switched to readline5
- Switched to Sun CC
- Made patch to make code C99 compliant and thus buildable on Sun CC

