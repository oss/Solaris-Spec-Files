Name: info
Version: 4.0
Release: 5
Copyright: GPL
Group: Applications/Text
Source: texinfo-4.0.tar.gz
BuildRoot: /var/tmp/%{name}-root
Summary: GNU texinfo
Conflicts: vpkg-SFWtexi

%description
Info is a hypertext documentation browser.  Info is the preferred
documentation format for most of the GNU tools.

%package -n texinfo
Summary: GNU texinfo
Group: Applications/Text
Version: 4.0
Release: 3
Requires: info

%description -n texinfo
Texinfo allows you to create info files.

%prep
%setup -q -n texinfo-4.0

%build
./configure --prefix=/usr/local
make

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/local
make install prefix=$RPM_BUILD_ROOT/usr/local

%post -n info
for i in /usr/local/info/*info ; do
	echo /usr/local/bin/install-info --info-dir=/usr/local/info $i
	/usr/local/bin/install-info --info-dir=/usr/local/info $i
done
/usr/local/bin/install-info --info-dir=/usr/local/info /usr/local/info/info.info
/usr/local/bin/install-info --info-dir=/usr/local/info /usr/local/info/info-stnd.info

%preun -n info
/usr/local/bin/install-info --info-dir=/usr/local/info --delete /usr/local/info/info.info
/usr/local/bin/install-info --info-dir=/usr/local/info --delete /usr/local/info/info-stnd.info

%post -n texinfo
# sanity check
if [ -x /usr/local/bin/install-info ] ; then
    /usr/local/bin/install-info --info-dir=/usr/local/info /usr/local/info/texinfo
fi

%preun -n texinfo
if [ -x /usr/local/bin/install-info ] ; then
    /usr/local/bin/install-info --info-dir=/usr/local/info --delete /usr/local/info/texinfo
fi

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-, root, root)
%doc COPYING AUTHORS INTRODUCTION
/usr/local/bin/info
/usr/local/bin/install-info
/usr/local/info/info*
/usr/local/info/dir
/usr/local/man/man1/info.1
/usr/local/man/man1/install-info.1
/usr/local/man/man5/info.5

%files -n texinfo
%defattr(-, root, root)
/usr/local/bin/makeinfo
/usr/local/bin/texindex
/usr/local/bin/texi2dvi
/usr/local/share/locale/*/LC_MESSAGES/*
/usr/local/man/man1/makeinfo.1
/usr/local/man/man1/texindex.1
/usr/local/man/man1/texi2dvi.1
/usr/local/man/man5/texinfo.5
/usr/local/info/texinfo*
