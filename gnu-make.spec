Name: make
Version: 3.81
Release: 2
Copyright: GPL
Group: Development/Tools
Source: make-%{version}.tar.gz
BuildRoot: /var/tmp/%{name}-root
Summary: GNU make
Conflicts: vpkg-SFWgmake
%description
GNU make

%prep
%setup -q

%build
PATH="/opt/SUNWspro/bin:/usr/ccs/bin:${PATH}"
CC="cc"
export PATH CC
./configure --prefix=/usr/local/gnu --program-prefix=g
make

%install
mkdir -p %{buildroot}/usr/local/gnu
mkdir -p %{buildroot}/usr/local/bin

make install DESTDIR=%{buildroot}

# Symlink to /usr/local
cd %{buildroot}/usr/local/bin
ln -s ../gnu/bin/gmake .

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
/usr/local/bin/*
/usr/local/gnu/bin/*
/usr/local/gnu/info/*info*
/usr/local/gnu/man/man1/gmake.1
