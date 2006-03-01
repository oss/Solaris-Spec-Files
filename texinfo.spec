Name: info
Version: 4.8
Release: 1
Copyright: GPL
Group: Applications/Text
Source: texinfo-%{version}.tar.gz
BuildRoot: /var/tmp/%{name}-root
Summary: GNU texinfo
Conflicts: vpkg-SFWtexi

%description
Info is a hypertext documentation browser.  Info is the preferred
documentation format for most of the GNU tools.

%package -n texinfo
Summary: GNU texinfo
Group: Applications/Text
Version: 4.8
Release: 1
Requires: info

%description -n texinfo
Texinfo allows you to create info files.

%prep
%setup -q -n texinfo-%{version}

%build
./configure --prefix=/usr/local
make

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/local
make install prefix=%{buildroot}/usr/local
mkdir -p %{buildroot}/usr/local/gnu/bin
mv %{buildroot}/usr/local/bin/info %{buildroot}/usr/local/gnu/bin/
# texi2pdf is provided by teTeX
rm %{buildroot}/usr/local/bin/texi2pdf
# should these be included?
rm %{buildroot}/usr/local/lib/charset.alias
rm %{buildroot}/usr/local/share/locale/locale.alias

%post -n info
for i in /usr/local/info/*.info ; do
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
rm -rf %{buildroot}

%files
%defattr(-, root, root)
%doc COPYING AUTHORS INTRODUCTION
/usr/local/gnu/bin/info
/usr/local/bin/infokey
/usr/local/bin/install-info
/usr/local/info/info*
/usr/local/info/dir
/usr/local/man/man1/info.1
/usr/local/man/man1/infokey.1
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
/usr/local/share/texinfo/texinfo.*



