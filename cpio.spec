Name: cpio
Version: 2.4.2
Copyright: GPL
Group: System Environment/Base
Summary: GNU cpio
Release: 4
Source: cpio-2.4.2.tar.gz
BuildRoot: /var/tmp/%{name}-root

%description
GNU cpio is a program for making archives.  It is more powerful than tar
and has more features than Sun cpio.  You should install this package
if you are making archives or backups.

%prep
%setup -q

%build
./configure --prefix=/usr/local/gnu
make

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/local/gnu
make install prefix=%{buildroot}/usr/local/gnu
mv %{buildroot}/usr/local/gnu/libexec/rmt \
   %{buildroot}/usr/local/gnu/libexec/rmt-cpio

%clean
rm -rf %{buildroot}

%post
if [ -x /usr/local/bin/install-info ] ; then
	/usr/local/bin/install-info --info-dir=/usr/local/gnu/info \
		 /usr/local/gnu/info/cpio.info
fi

%preun
if [ -x /usr/local/bin/install-info ] ; then
	/usr/local/bin/install-info --delete --info-dir=/usr/local/gnu/info \
		 /usr/local/gnu/info/cpio.info
fi

%files
%defattr(-,root,bin)
/usr/local/gnu/bin/cpio
/usr/local/gnu/bin/mt
/usr/local/gnu/libexec/rmt-cpio
/usr/local/gnu/man/man1/cpio.1
/usr/local/gnu/man/man1/mt.1
/usr/local/gnu/info/cpio.info
