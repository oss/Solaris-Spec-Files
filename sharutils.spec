Name: sharutils
Version: 4.6.1
Copyright: GPL
Group: System Environment/Base
Summary: GNU sharutils
Release: 1
Source: %{name}-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-root

%description

%prep
%setup -q

%build
PATH="/usr/local/gnu/bin:/usr/local/bin:/usr/sfw/bin:$PATH"
export PATH
./configure --prefix=/usr/local/gnu --disable-nls
make

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/local/gnu
/usr/local/gnu/bin/make install prefix=%{buildroot}/usr/local/gnu

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
/usr/local/gnu/bin/*
/usr/local/gnu/info/*
/usr/local/gnu/man/*/*

%changelog
* Thu Feb 02 2006 Jonathan Kaczynski <jmkacz@oss.rutgers.edu> - 4.6.1-1
- Updated to the latest version.
