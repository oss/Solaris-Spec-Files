Name: sharutils
Version: 4.2.1
Copyright: GPL
Group: System Environment/Base
Summary: GNU sharutils
Release: 5
Source: sharutils-4.2.1.tar.gz
Patch: sharutils.patch
BuildRoot: /var/tmp/%{name}-root

%description

%prep
%setup -q
%patch -p1

# The patch fixes the locale files, which have some errant trailing 
# newlines.

%build
./configure --prefix=/usr/local/gnu --disable-nls
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
		 /usr/local/gnu/info/sharutils.info
fi

%preun
if [ -x /usr/local/bin/install-info ] ; then
	/usr/local/bin/install-info --delete --info-dir=/usr/local/gnu/info \
		 /usr/local/gnu/info/sharutils.info
fi

%files
%defattr(-, root, bin)
%doc COPYING
/usr/local/gnu/info/sharutils.info
/usr/local/gnu/info/remsync.info
#/usr/local/gnu/lib/locale/*/LC_MESSAGES/sharutils.mo
#/usr/local/gnu/share/locale/*/LC_MESSAGES/sharutils.mo
/usr/local/gnu/bin/*
