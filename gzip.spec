Name: gzip
Version: 1.2.4a
Copyright: GPL
Group: System Environment/Base
Summary: GNU zip
Release: 4
Source: gzip-1.2.4a.tar.gz
BuildRoot: /var/tmp/%{name}-root

%description
Gzip is used to uncompress and compress data.  You want this package.

%prep
%setup -q

%build
./configure --prefix=/usr/local/gnu
make

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/local/gnu
make install prefix=$RPM_BUILD_ROOT/usr/local/gnu

%clean
rm -rf $RPM_BUILD_ROOT

%post
if [ -x /usr/local/bin/install-info ] ; then
	/usr/local/bin/install-info --info-dir=/usr/local/gnu/info \
	--entry "* Gzip: (gzip).		GNU compression utility" \
		 /usr/local/gnu/info/gzip.info
fi

%preun
if [ -x /usr/local/bin/install-info ] ; then
	/usr/local/bin/install-info --delete --info-dir=/usr/local/gnu/info \
		 /usr/local/gnu/info/gzip.info
fi

%files
%defattr(-,root,root)
%doc COPYING
/usr/local/gnu/man/man1/*
/usr/local/gnu/bin/*
/usr/local/gnu/info/gzip.info
