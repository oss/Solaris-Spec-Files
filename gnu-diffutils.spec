Name: diffutils
Version: 2.7
Release: 3
Copyright: GPL
Group: System Environment/Base
Source: diffutils-2.7.tar.gz
BuildRoot: /var/tmp/%{name}-root
Summary: The GNU diffutils
Requires: info
%description
The GNU diffutils are cmp, diff, diff3, and sdiff.

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
		--entry="* Diffutils: (diff).   diff, diff3, etc." \
		 /usr/local/gnu/info/diff.info
fi

%preun
if [ -x /usr/local/bin/install-info ] ; then
	/usr/local/bin/install-info --delete --info-dir=/usr/local/gnu/info \
		/usr/local/gnu/info/diff.info
fi

%files
%defattr(-, root, bin)
%doc COPYING NEWS
/usr/local/gnu/bin/*
/usr/local/gnu/info/diff.info*
