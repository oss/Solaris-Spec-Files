Name: tar
Version: 1.13
Copyright: GPL
Group: System Environment/Base
Summary: GNU tar
Release: 3
Requires: gzip
Source: tar-1.13.tar.gz
BuildRoot: /var/tmp/%{name}-root

%description
GNU tar lets you create archives of several files.  It's a lot like Sun
tar, but it has a few more features.  Install this rpm if you want the
extra functionality of GNU tar.

%prep
%setup -q

%build
./configure --prefix=/usr/local/gnu
make

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/local/gnu
make install prefix=%{buildroot}/usr/local/gnu

%clean
rm -rf %{buildroot}

%post
if [ -x /usr/local/bin/install-info ] ; then
	/usr/local/bin/install-info --info-dir=/usr/local/gnu/info \
		 /usr/local/gnu/info/tar.info
fi

%preun
if [ -x /usr/local/bin/install-info ] ; then
	/usr/local/bin/install-info --delete --info-dir=/usr/local/gnu/info \
		 /usr/local/gnu/info/tar.info
fi

%files
%defattr(-,root,root)
%doc COPYING
/usr/local/gnu/info/tar.info*
/usr/local/gnu/bin/tar
/usr/local/gnu/libexec/rmt
/usr/local/gnu/lib/locale/*/LC_MESSAGES/tar.mo
