Name: make
Version: 3.81
Release: 1
Copyright: GPL
Group: Development/Tools
Source: make-%{version}.tar.gz
BuildRoot: /var/tmp/%{name}-root
Summary: GNU make
Conflicts: vpkg-SFWgmake
%description
From the documentation:

%prep
%setup -q

%build
PATH="/opt/SUNWspro/bin:/usr/ccs/bin:${PATH}"
CC="cc"
export PATH CC
./configure --prefix=/usr/local/gnu
make

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/local/gnu
make install prefix=%{buildroot}/usr/local/gnu
cd %{buildroot}/usr/local/gnu
ln -s make gmake

%post
if [ -x /usr/local/bin/install-info ] ; then
	/usr/local/bin/install-info --info-dir=/usr/local/gnu/info /usr/local/gnu/info/make.info
fi

%preun
if [ -x /usr/local/bin/install-info ] ; then
	/usr/local/bin/install-info --delete --info-dir=/usr/local/gnu/info \
		/usr/local/gnu/info/make.info
fi

%clean
rm -rf %{buildroot}

%files
%defattr(-, root, bin)
%doc COPYING AUTHORS
#/usr/local/gnu/share/locale/*/LC_MESSAGES/make.mo
/usr/local/gnu/bin/*
/usr/local/gnu/info/*info*
/usr/local/gnu/man/man1/make.1
