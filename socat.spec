Summary: socat - multipurpose relay
Name: socat
Version: 1.5.0.0
Release: 3
License: GPL
Group: Applications/Communications
Source0: http://www.dest-unreach.org/socat/download/socat-%{version}.tar.gz
#Requires: readline
# readline support is broken.
Requires: openssl
BuildRequires: openssl
BuildRoot: /var/tmp/%{name}-root

%description
socat is a relay for bidirectional data transfer between two independent data
channels. Each of these data channels may be a file, pipe, device (terminal or
modem etc.), socket (UNIX, IP4, IP6 - raw, UDP, TCP), a file descriptor (stdin
etc.), a program, or an arbitrary combination of two of these.

%prep
%setup -q

%build
PATH="/opt/SUNWspro/bin:$PATH"
CC="gcc" # configure is stupid and accepts nothing else
CPPFLAGS='-I/usr/local/include -I/usr/local/ssl/include'
LIBS='-L/usr/local/lib -R/usr/local/lib -L/usr/local/ssl/lib -R/usr/local/ssl/lib'
export CPPFLAGS LIBS PATH CC
./configure --prefix=/usr/local --disable-readline --disable-libwrap
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
%doc README CHANGES EXAMPLES SECURITY xio.help socat.html FAQ BUGREPORTS
%doc COPYING COPYING.OpenSSL FILES PORTING DEVELOPMENT
/usr/local/bin/socat
/usr/local/bin/procan
/usr/local/bin/filan
/usr/local/man/man1/socat.1*
