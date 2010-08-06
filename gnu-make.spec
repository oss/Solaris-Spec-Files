Name:      make
Version:   3.82
Release:   1
License:   GPL
Group:     Development/Tools
URL:       http://ftp.gnu.org/gnu/make/
Source:    http://ftp.gnu.org/gnu/make/make-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
Summary:   GNU make
Conflicts: vpkg-SFWgmake
%description
GNU make

%prep
%setup -q

%build
PATH="/opt/SUNWspro/bin:/usr/ccs/bin:${PATH}"
CC="cc"
CLAGS="-g -xO2"
LDFLAGS="-Bdirect -zdefs"
export PATH CC CFLAGS LDFLAGS
./configure --prefix=/usr/local/gnu --program-prefix=g
make

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/local/gnu
mkdir -p %{buildroot}/usr/local/bin

rm -f %{buildroot}/usr/local/gnu/share/info/dir
make install DESTDIR=%{buildroot}

# Symlink to /usr/local
cd %{buildroot}/usr/local/bin
ln -s ../gnu/bin/gmake .

%clean
rm -rf %{buildroot}

%post
if [ -x /usr/local/bin/install-info ] ; then
	/usr/local/bin/install-info --info-dir=/usr/local/gnu/share/info /usr/local/gnu/share/info/make.info
fi

%preun
if [ -x /usr/local/bin/install-info ] ; then
	/usr/local/bin/install-info --delete --info-dir=/usr/local/gnu/share/info \
		/usr/local/gnu/share/info/make.info
fi

%files
%defattr(-, root, bin)
%doc COPYING AUTHORS
#/usr/local/gnu/share/locale/*/LC_MESSAGES/make.mo
/usr/local/bin/*
/usr/local/gnu/bin/*
/usr/local/gnu/share/info/*info*
/usr/local/gnu/share/man/man1/gmake.1

%changelog
* Thu Aug 05 2010 Orcan Ogetbil <orcan@nbcs.rutgers.edu> - 3.82-1
- Update to latest version