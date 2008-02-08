Name:		autogen
Version:	5.9.4
Copyright:	GPL
Group:		Development/Tools
Summary:	GNU autogen
Release:	2
Source:		%{name}-%{version}.tar.gz
BuildRoot:	/var/tmp/%{name}-root
Requires:	m4
Conflicts:	vpkg-SFWagen
BuildRequires:  guile gmp-devel

%description
AutoGen is a tool designed to simplify the creation and maintenance of 
programs that contain large amounts of repetitious text. It is 
especially valuable in programs that have several blocks of text that 
must be kept synchronized.

%prep
%setup -q

%build
PATH="/opt/SUNWspro/bin:${PATH}" \
CC="cc" CXX="CC" CPPFLAGS="-I/usr/local/include -I/usr/local/include/gmp32 \
-I/usr/local/include/guile" \
LD="/usr/ccs/bin/ld" \
LDFLAGS="-L/usr/local/lib -R/usr/local/lib"
export PATH CC CXX CPPFLAGS LD LDFLAGS

./configure \
	--prefix=/usr/local \
	--with-libguile \
	--with-libguile-cflags \
	--with-libguile-libs \
	--infodir=/usr/local/info
	
gmake

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/local
gmake install DESTDIR=$RPM_BUILD_ROOT
rm %{buildroot}/usr/local/info/dir
rm %{buildroot}/usr/local/lib/*.la


%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root)
%doc COPYING
/usr/local/bin/*
/usr/local/include/autoopts/*
/usr/local/lib/*
/usr/local/share/aclocal/*
/usr/local/share/autogen/*
/usr/local/share/man/*
/usr/local/info/*

%changelog
* Fri Feb 08 2008 David Diffenbaugh <davediff@nbcs.rutgers.edu> - 5.9.4-2
  removed info post and pre scripts, updated files section, removed info/dir
* Tue Feb 05 2008 David Diffenbaugh <davediff@nbcs.rutgers.edu> - 5.9.4-1
- updated to 5.9.4
* Sat Oct 20 2007 David Lee Halik <dhalik@nbcs.rutgers.edu> - 5.9.3-1
- Bump to 5.9.3
* Wed Aug 22 2007 Naveen Gavini <ngavini@nbcs.rutgers.edu> - 5.9.2-1
- Updated to the latest version.
