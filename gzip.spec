Name: gzip
Version: 1.3.3
Copyright: GPL
Group: System Environment/Base
Summary: GNU zip
Release: 1
Source: ftp://alpha.gnu.org/gnu/gzip/gzip-%{version}.tar.gz
Patch0: gzip-1.3-openbsd-owl-tmp.diff
Patch1: gzip-1.2.4-zforce.patch
Patch2: gzip-1.2.4a-dirinfo.patch
Patch3: gzip-1.3-stderr.patch
Patch4: gzip-1.3.1-zgreppipe.patch
Patch5: gzip-1.3-rsync.patch
BuildRoot: /var/tmp/%{name}-root

%description
Gzip is used to uncompress and compress data.  You want this package.

%prep
%setup -q
%patch0 -p1
%patch1 -p1 
#%patch2 -p1 
%patch3 -p1
%patch4 -p1 -b .nixi
%patch5 -p1 -b .rsync

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
