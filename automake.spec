Name: automake
Version: 1.8.4
Copyright: GPL
Group: Development/Tools
Summary: GNU automake 
Release: 1
Source: automake-%{version}.tar.bz2
Requires: m4 perl
BuildRoot: /var/tmp/%{name}-root

%description
GNU automake is used to automatically generate makefiles compliant with
the GNU makefile standards.  If you are writing GNU software or if you
want GNU-style makefiles, install this package.

%prep
%setup -q

%build
./configure --prefix=/usr/local
make

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/local
make install prefix=$RPM_BUILD_ROOT/usr/local
/usr/local/bin/unhardlinkify.py %{buildroot}/usr/local

%clean
rm -rf $RPM_BUILD_ROOT

%post
if [ -x /usr/local/bin/install-info ] ; then
	/usr/local/bin/install-info --info-dir=/usr/local/info \
		 /usr/local/info/automake.info
fi

%preun
if [ -x /usr/local/bin/install-info ] ; then
	/usr/local/bin/install-info --delete --info-dir=/usr/local/info \
		 /usr/local/info/automake.info
fi

%files
%defattr(-,root,root)
%doc COPYING
/usr/local/bin/*
/usr/local/info/automake.info*
/usr/local/share/automake-*
/usr/local/share/aclocal-*
