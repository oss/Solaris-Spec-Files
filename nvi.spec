Name:		nvi 
Summary:	The 4BSD ex/vi text editor 
Version:	1.79
Release:        1
Copyright:      BSD	
Group:		Applications/Editors	
Vendor:	        skimo@kotnet.org, bostic@bostic.com	
Url:		http://www.bostic.com/vi/	
Source:		ftp://ftp.sleepycat.com/pub/nvi-1.79.tar.gz
BuildRoot:	/var/tmp/%{name}-%{version}-root

%description
Nvi is an implementation of the ex/vi text editor originally distributed as 
part of the Fourth Berkeley Software Distribution (4BSD), by the University of 
California, Berkeley. The source code to nvi is freely available, and nvi may 
be freely redistributed.

%prep
%setup -q

%build
PATH="/opt/SUNWspro/bin:${PATH}" \
CC="cc" CXX="CC" CPPFLAGS="-I/usr/local/include" \
LD="/usr/ccs/bin/ld" \
LDFLAGS="-L/usr/local/lib -R/usr/local/lib" \
export PATH CC CXX CPPFLAGS LD LDFLAGS

build/configure --prefix=/usr/local 

make

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/local
install -d $RPM_BUILD_ROOT/usr/local/bin
install -d $RPM_BUILD_ROOT/usr/local/man/man1
install -d $RPM_BUILD_ROOT/usr/local/sbin

install nvi $RPM_BUILD_ROOT/usr/local/bin/vi
install docs/USD.doc/vi.man/vi.1 $RPM_BUILD_ROOT/usr/local/man/man1/vi.1
install recover $RPM_BUILD_ROOT/usr/local/sbin/recover

cd $RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,bin,bin)
/usr/local/bin/vi
/usr/local/man/man1/vi.1
/usr/local/sbin/recover

