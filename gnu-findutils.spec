Name: findutils
Version: 4.1
Release: 3
Copyright: GPL
Group: System Environment/Base
Source: findutils-4.1.tar.gz
BuildRoot: /var/tmp/%{name}-root
Summary: The GNU findutils
%description
The GNU findutils are find, xargs, and locate.

%prep
%setup -q

%build
./configure --prefix=/usr/local/gnu
make

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/local/gnu
make install prefix=%{buildroot}/usr/local/gnu

%post
if [ -x /usr/local/bin/install-info ] ; then
	/usr/local/bin/install-info --info-dir=/usr/local/gnu/info /usr/local/gnu/info/find.info
fi

%preun
if [ -x /usr/local/bin/install-info ] ; then
	/usr/local/bin/install-info --delete --info-dir=/usr/local/gnu/info /usr/local/gnu/info/find.info
fi

%clean
rm -rf %{buildroot}

%files
%defattr(-, root, bin)
%doc COPYING NEWS doc/*
/usr/local/gnu/bin/*
/usr/local/gnu/man/*/*
/usr/local/gnu/libexec/*
/usr/local/gnu/info/find.info*
