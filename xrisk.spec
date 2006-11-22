Summary:	xrisk
Name:		xrisk
Version:	2.15
Release:        1
Copyright:	GPL
Group:		Applications/Games
Source:		%{name}-%{version}.tar.gz
Source1:	Makefile.unix
URL:		http://my.pages.de/pub/comp/unix/games/xrisk
Distribution: 	RU-Solaris
Vendor: 	NBCS-OSS
Packager: 	Leo Zhadanovsky <leozh@nbcs.rutgers.edu>
BuildRoot:	/var/tmp/%{name}-%{version}-root

%description
xrisk - the legend continues

%package devel 
Summary: Libraries, includes to develop applications with %{name}.
Group: Applications/Libraries
Requires: %{name} = %{version}

%description devel
The %{name}-devel package contains the header files and static libraries
for building applications which use %{name}.

%prep
%setup -q

%build
cp %{SOURCE1} ./
PATH="/opt/SUNWspro/bin:${PATH}" \
CC="cc" CXX="CC" CPPFLAGS="-I/usr/local/include" \
LD="/usr/ccs/bin/ld" \
LDFLAGS="-L/usr/local/lib -R/usr/local/lib" \
export PATH CC CXX CPPFLAGS LD LDFLAGS

make -f Makefile.unix

%install
rm -rf $RPM_BUID_ROOT

mkdir -p $RPM_BUILD_ROOT/usr/local/bin
mkdir -p $RPM_BUILD_ROOT/usr/local/lib/xrisk
mkdir -p $RPM_BUILD_ROOT/usr/local/man/man1

install -m 0755 src/xrisk $RPM_BUILD_ROOT/usr/local/bin/xrisk
install -m 0644 lib/*.mapping $RPM_BUILD_ROOT/usr/local/lib/xrisk/
install -m 0644 lib/#* $RPM_BUILD_ROOT/usr/local/lib/xrisk/
install -m 0644 lib/*.data $RPM_BUILD_ROOT/usr/local/lib/xrisk/
install -m 0644 doc/xrisk.man $RPM_BUILD_ROOT/usr/local/man/man1/xrisk.1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
/usr/local/bin/*
/usr/local/lib/*
/usr/local/man/man1/*

%changelog
* Tue Nov 21 2006 Leo Zhadanovsky <leozh@nbcs.rutgers.edu> - 2.1.5-1
- Initial Rutgers release
