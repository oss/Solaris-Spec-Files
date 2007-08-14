Name: gawk
Version: 3.1.5
Copyright: GPL
Group: Development/Languages
Summary: Gnu awk
Release: 3
Source0: gawk-%{version}.tar.gz
Source1: gawk-%{version}-doc.tar.gz
Source2: gawk-%{version}-ps.tar.gz
BuildRoot: /var/tmp/%{name}-root

%description
The awk programming language is a text processing language designed by
Alfred V. Aho, Peter J. Weinberger, and Brian W. Kernighan.  Install
this package if you wish to develop or run awk programs that use GNU
extensions to awk.

%prep
%setup -q
%setup -D -T -b 1
%setup -D -T -b 2

%build
./configure --prefix=/usr/local
make

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/local
make install DESTDIR=$RPM_BUILD_ROOT
cd %{buildroot}/usr/local
/usr/local/bin/unhardlinkify.py ./

%clean
rm -rf $RPM_BUILD_ROOT

%post
if [ -x /usr/local/bin/install-info ] ; then
	/usr/local/bin/install-info --info-dir=/usr/local/info \
		 /usr/local/info/gawk.info
fi

%preun
if [ -x /usr/local/bin/install-info ] ; then
	/usr/local/bin/install-info --delete --info-dir=/usr/local/info \
		 /usr/local/info/gawk.info
fi

%files
%defattr(-,root,root)
%doc COPYING
%doc doc/*ps
%doc doc/gawk.dvi
%doc doc/awkforai.txt
/usr/local/bin/*
/usr/local/share/awk/*
/usr/local/info/*info*
/usr/local/man/man1/*
/usr/local/libexec/awk/*
/usr/local/info/dir
/usr/local/share/locale/ca/LC_MESSAGES/gawk.mo
/usr/local/share/locale/da/LC_MESSAGES/gawk.mo
/usr/local/share/locale/de/LC_MESSAGES/gawk.mo
/usr/local/share/locale/es/LC_MESSAGES/gawk.mo
/usr/local/share/locale/fr/LC_MESSAGES/gawk.mo
/usr/local/share/locale/ga/LC_MESSAGES/gawk.mo
/usr/local/share/locale/he/LC_MESSAGES/gawk.mo
/usr/local/share/locale/it/LC_MESSAGES/gawk.mo
/usr/local/share/locale/ja/LC_MESSAGES/gawk.mo
/usr/local/share/locale/nl/LC_MESSAGES/gawk.mo
/usr/local/share/locale/pl/LC_MESSAGES/gawk.mo
/usr/local/share/locale/pt_BR/LC_MESSAGES/gawk.mo
/usr/local/share/locale/ro/LC_MESSAGES/gawk.mo
/usr/local/share/locale/rw/LC_MESSAGES/gawk.mo
/usr/local/share/locale/sv/LC_MESSAGES/gawk.mo
/usr/local/share/locale/tr/LC_MESSAGES/gawk.mo
/usr/local/share/locale/vi/LC_MESSAGES/gawk.mo
#/usr/local/lib/locale/*/LC_MESSAGES
#/usr/local/lib/locale/*/LC_TIME


%changelog
* Tue Aug 14 2007 Naveen Gavini <ngavini@nbcs.rutgers.edu> - 3.1.5
- Updated to 3.1.5
