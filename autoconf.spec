Name: autoconf
Version: 2.52i
Copyright: GPL
Group: Development/Tools
Summary: GNU autoconf
Release: 1
Source: autoconf-%{version}.tar.bz2
BuildRoot: /var/tmp/%{name}-root
Requires: m4
Conflicts: vpkg-SFWaconf

%description
GNU autoconf generates shell scripts used to configure programs.  Install
this package if you are writing Unix software for several platforms and
you want GNU-style configure scripts.

%prep
%setup -q

%build
./configure --prefix=/usr/local
make

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/local
make install prefix=$RPM_BUILD_ROOT/usr/local

%clean
rm -rf $RPM_BUILD_ROOT

%post
if [ -x /usr/local/bin/install-info ] ; then
	/usr/local/bin/install-info --info-dir=/usr/local/info \
		 /usr/local/info/autoconf.info
fi

%preun
if [ -x /usr/local/bin/install-info ] ; then
	/usr/local/bin/install-info --delete --info-dir=/usr/local/info \
		 /usr/local/info/autoconf.info
fi

%files
%defattr(-,root,root)
%doc COPYING
/usr/local/bin/*
/usr/local/info/autoconf.info
/usr/local/share/autoconf
