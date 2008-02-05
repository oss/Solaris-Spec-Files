Name:		autogen
Version:	5.9.4
Copyright:	GPL
Group:		Development/Tools
Summary:	GNU autogen
Release:	1
Source:		%{name}-%{version}.tar.bz2
BuildRoot:	/var/tmp/%{name}-root
Requires:	m4
Conflicts:	vpkg-SFWagen

%description
AutoGen is a tool designed to simplify the creation and maintenance of 
programs that contain large amounts of repetitious text. It is 
especially valuable in programs that have several blocks of text that 
must be kept synchronized.

%prep
%setup -q

%build
PATH="/opt/SUNWspro/bin:${PATH}" \
CC="cc" CXX="CC" CPPFLAGS="-I/usr/local/include" \
LD="/usr/ccs/bin/ld" \
LDFLAGS="-L/usr/local/lib -R/usr/local/lib"
export PATH CC CXX CPPFLAGS LD LDFLAGS

./configure \
	--prefix=/usr/local \
	--without-libguile \
	--with-libguile-cflags \
	--with-libguile-libs
gmake

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/local
gmake install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post
if [ -x /usr/local/bin/install-info ] ; then
	/usr/local/bin/install-info --info-dir=/usr/local/share/info \
		 /usr/local/share/info/autoconf.info
fi
if [ -x /usr/local/bin/install-info ] ; then
        /usr/local/bin/install-info --info-dir=/usr/local/share/info \
                 /usr/local/share/info/standards.info
fi

%preun
if [ -x /usr/local/bin/install-info ] ; then
	/usr/local/bin/install-info --delete --info-dir=/usr/local/share/info \
		 /usr/local/share/info/autoconf.info
fi
if [ -x /usr/local/bin/install-info ] ; then
        /usr/local/bin/install-info --delete --info-dir=/usr/local/share/info \
                 /usr/local/share/info/standards.info
fi 

%files
%defattr(-,root,root)
%doc COPYING
/usr/local/bin/*
/usr/local/include/autoopts/*
/usr/local/lib/*
/usr/local/share/*

%changelog
* Tue Feb 05 2008 David Diffenbaugh <davediff@nbcs.rutgers.edu> - 5.9.4-1
* updated to 5.9.4
* Sat Oct 20 2007 David Lee Halik <dhalik@nbcs.rutgers.edu> - 5.9.3-1
- Bump to 5.9.3
* Wed Aug 22 2007 Naveen Gavini <ngavini@nbcs.rutgers.edu> - 5.9.2-1
- Updated to the latest version.
