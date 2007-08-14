Name: sharutils
Version: 4.6.3
Release: 2
Copyright: GPL
Group: System Environment/Base
Summary: GNU sharutils
Source: %{name}-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-root

%description

%prep
%setup -q

%build
PATH="/opt/SUNWspro:/usr/ccs/bin:/usr/local/gnu/bin:$PATH"
CC=cc
CPPFLAGS="-I/usr/local/include"
LDFLAGS="-L/usr/local/lib -R/usr/local/lib"
export PATH CC CPPFLAGS LDFLAGS
./configure --prefix=/usr/local/gnu --disable-nls
gmake

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/local/gnu
gmake install DESTDIR=%{buildroot}

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
/usr/local/gnu/info/*info*
/usr/local/gnu/man/*/*

%changelog
* Tue Aug 14 2007 Eric Rivas <kc2hmv@nbcs.rutgers.edu> - 4.6.3-2
- Updated to 4.6.3
* Thu Feb 02 2006 Jonathan Kaczynski <jmkacz@oss.rutgers.edu> - 4.6.1-1
- Updated to the latest version.
