Name: libtool
Version: 1.3.5
Copyright: GPL
Group: Development/Tools
Summary: A portability utility
Release: 3
Source: libtool-1.3.5.tar.gz
BuildRoot: /var/tmp/%{name}-root
Requires: m4

%description
GNU libtool is part of the magic behind configure; it helps programmers
generate shared and static libraries in a portable manner.  Install this
package if you are developing software that uses its own libraries and you
don't want to port it manually.

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
		 /usr/local/info/libtool.info
fi

%preun
if [ -x /usr/local/bin/install-info ] ; then
	/usr/local/bin/install-info --delete --info-dir=/usr/local/info \
		 /usr/local/info/libtool.info
fi

%files
%defattr(-,root,root)
/usr/local/bin/*
/usr/local/share/libtool
/usr/local/share/aclocal/libtool.m4
/usr/local/lib/lib*.so*
/usr/local/lib/lib*a
/usr/local/include/*
/usr/local/info/libtool.info*
