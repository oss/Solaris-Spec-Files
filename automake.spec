Name:		automake
Version:	1.10
Copyright:	GPL
Group:		Development/Tools
Summary:	GNU automake 
Release:	1
Source:		automake-%{version}.tar.gz
Requires:	m4 perl
BuildRoot:	/var/tmp/%{name}-root

%description
GNU automake is used to automatically generate makefiles compliant with
the GNU makefile standards.  If you are writing GNU software or if you
want GNU-style makefiles, install this package.

%prep
%setup -q

%build
PATH="/opt/SUNWspro/bin:${PATH}" \
CC="cc" CXX="CC" CPPFLAGS="-I/usr/local/include" \
LD="/usr/ccs/bin/ld" \
LDFLAGS="-L/usr/local/lib -R/usr/local/lib"
export PATH CC CXX CPPFLAGS LD LDFLAGS

./configure --prefix=/usr/local

gmake

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/local

gmake DESTDIR=%{buildroot} install

# Workaround for broken script
cd %{buildroot}/usr/local
/usr/local/bin/unhardlinkify.py ./

%clean
rm -rf $RPM_BUILD_ROOT

%post
if [ -x /usr/local/bin/install-info ] ; then
	/usr/local/bin/install-info --info-dir=/usr/local/share/info \
		 /usr/local/share/info/automake.info
fi

%preun
if [ -x /usr/local/bin/install-info ] ; then
	/usr/local/bin/install-info --delete --info-dir=/usr/local/share/info \
		 /usr/local/share/info/automake.info
fi

%files
%defattr(-,root,root)
%doc COPYING
/usr/local/bin/*
#/usr/local/share/info/*
/usr/local/share/doc/automake/amhello-1.0.tar.gz
/usr/local/share/info/automake.info
/usr/local/share/info/automake.info-1
/usr/local/share/info/automake.info-2
/usr/local/share/automake-*
/usr/local/share/aclocal-*

%changelog
* Wed Sep 12 2007 David Lee Halik <dhalik@nbcs.rutgers.edu> - 1.10
- Bumped to 1.10 and switched to SunCC
