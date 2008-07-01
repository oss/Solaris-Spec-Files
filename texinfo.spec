Name: info
Version: 4.12
Release: 1
Copyright: GPL
Group: Applications/Text
Source: texinfo-%{version}.tar.gz
BuildRoot: /var/tmp/%{name}-root
Summary: GNU texinfo
Requires: ncurses
BuildRequires: ncurses
Conflicts: vpkg-SFWtexi

%description
Info is a hypertext documentation browser.  Info is the preferred
documentation format for most of the GNU tools.

%package -n texinfo
Summary: GNU texinfo
Group: Applications/Text
Version: 4.12
Release: 1
Requires: info

%description -n texinfo
Texinfo allows you to create info files.

%prep
%setup -q -n texinfo-%{version}

%build
PATH="/opt/SUNWspro/bin:${PATH}" \
CC="cc" CXX="CC" CPPFLAGS="-I/usr/local/include" \
LD="/usr/ccs/bin/ld" \
LDFLAGS="-L/usr/local/lib -R/usr/local/lib"
export PATH CC CXX CPPFLAGS LD LDFLAGS

./configure --prefix=/usr/local --disable-nls
gmake

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/local
gmake install prefix=%{buildroot}/usr/local
mkdir -p %{buildroot}/usr/local/gnu/bin
mv %{buildroot}/usr/local/bin/info %{buildroot}/usr/local/gnu/bin/
# texi2pdf is provided by teTeX
rm %{buildroot}/usr/local/bin/texi2pdf
# should this be included?
rm %{buildroot}/usr/local/lib/charset.alias

%post -n info
for i in /usr/local/share/info/*.info ; do
	echo /usr/local/bin/install-info --info-dir=/usr/local/share/info $i
	/usr/local/bin/install-info --info-dir=/usr/local/share/info $i
done
/usr/local/bin/install-info --info-dir=/usr/local/share/info /usr/local/share/info/info.info
/usr/local/bin/install-info --info-dir=/usr/local/share/info /usr/local/share/info/info-stnd.info

%preun -n info
/usr/local/bin/install-info --info-dir=/usr/local/share/info --delete /usr/local/share/info/info.info
/usr/local/bin/install-info --info-dir=/usr/local/share/info --delete /usr/local/share/info/info-stnd.info

%post -n texinfo
# sanity check
if [ -x /usr/local/bin/install-info ] ; then
    /usr/local/bin/install-info --info-dir=/usr/local/share/info /usr/local/share/info/texinfo
fi

%preun -n texinfo
if [ -x /usr/local/bin/install-info ] ; then
    /usr/local/bin/install-info --info-dir=/usr/local/share/info --delete /usr/local/share/info/texinfo
fi

%clean
rm -rf %{buildroot}

%files
%defattr(-, root, root)
%doc README README.dev NEWS COPYING AUTHORS INTRODUCTION
/usr/local/gnu/bin/info
/usr/local/bin/infokey
/usr/local/bin/install-info
/usr/local/share/info/info*
/usr/local/share/info/dir
/usr/local/share/man/man1/info.1
/usr/local/share/man/man1/infokey.1
/usr/local/share/man/man1/install-info.1
/usr/local/share/man/man5/info.5

%files -n texinfo
%defattr(-, root, root)
/usr/local/bin/makeinfo
/usr/local/bin/texindex
/usr/local/bin/texi2dvi
/usr/local/bin/pdftexi2dvi
/usr/local/share/man/man1/makeinfo.1
/usr/local/share/man/man1/texindex.1
/usr/local/share/man/man1/texi2dvi.1
/usr/local/share/man/man1/pdftexi2dvi.1
/usr/local/share/man/man1/texi2pdf.1
/usr/local/share/man/man5/texinfo.5
/usr/local/share/info/texinfo*
/usr/local/share/texinfo/texinfo.*

%changelog
* Tue Jul 1 2008 Brian Schubert <schubert@nbcs.rutgers.edu> - 4.12-1
- Modified to use sun studio cc, disabled nls, added changelog, and updated to version 4.12

