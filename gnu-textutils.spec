Name: textutils
Version: 2.0
Release: 5
Copyright: GPL
Group: System Environment/Base
Source: textutils-2.0.tar.gz
BuildRoot: /var/tmp/%{name}-root
Summary: The GNU textutils
%description
The GNU textutils are: cat, cksum, comm, csplit, cut, expand, fmt, fold,
head, join, md5sum, nl, od, paste, pr, ptx, sort, split, sum, tac, tail,
tr, tsort, unexpand, uniq, and wc.

%prep
%setup -q

%build
./configure --prefix=/usr/local/gnu --disable-nls
make
#make check

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/local/gnu
make install prefix=%{buildroot}/usr/local/gnu

%post
if [ -x /usr/local/bin/install-info ] ; then
	/usr/local/bin/install-info --info-dir=/usr/local/gnu/info /usr/local/gnu/info/textutils.info
fi

%preun
if [ -x /usr/local/bin/install-info ] ; then
	/usr/local/bin/install-info --delete --info-dir=/usr/local/gnu/info \
		/usr/local/gnu/info/textutils.info
fi

%clean
rm -rf %{buildroot}

%files
%defattr(-, root, bin)
%doc doc/textutils.info doc/version.texi doc/textutils.texi doc/stamp-vti
%doc doc/mdate-sh NEWS AUTHORS COPYING
/usr/local/gnu/bin/*
/usr/local/gnu/info/textutils.*
/usr/local/gnu/man/man1/*
#/usr/local/gnu/lib/locale/*/LC_MESSAGES/*
