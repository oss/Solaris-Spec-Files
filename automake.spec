Name: automake14
Version: 1.4p5
Copyright: GPL
Group: Development/Tools
Summary: GNU automake 
Release: 2
Source: automake-%{version}.tar.gz
Requires: m4
Requires: perl
BuildRoot: /var/tmp/%{name}-root
Obsoletes: automake
Provides: automake

%description
GNU automake is used to automatically generate makefiles compliant with
the GNU makefile standards.  If you are writing GNU software or if you
want GNU-style makefiles, install this package.

%prep
%setup -q -n automake-1.4-p5

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
/usr/local/share/automake/*
/usr/local/share/aclocal/*
