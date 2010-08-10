Name:         sharutils
Version:      4.9
Release:      1
License:      GPL
Group:        System Environment/Base
Summary:      GNU sharutils
URL:          http://ftp.gnu.org/gnu/sharutils/
Source:       http://ftp.gnu.org/gnu/sharutils/%{name}-%{version}.tar.bz2
BuildRoot:    %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

%description

%prep
%setup -q

%build
%configure --disable-nls
gmake

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/local/gnu
gmake install DESTDIR=%{buildroot}

rm -f %{buildroot}%{_infodir}/dir
rm -f %{buildroot}%{_libdir}/charset.alias

%clean
rm -rf %{buildroot}

%post
if [ -x /usr/local/bin/install-info ] ; then
	/usr/local/bin/install-info --info-dir=/usr/local/share/info \
		 /usr/local/share/info/sharutils.info
fi

%preun
if [ -x /usr/local/bin/install-info ] ; then
	/usr/local/bin/install-info --delete --info-dir=/usr/local/share/info \
		 /usr/local/share/info/sharutils.info
fi

%files
%defattr(-, root, bin)
%doc COPYING
/usr/local/bin/*
/usr/local/share/info/*info*
/usr/local/share/man/*/*

%changelog
* Mon Aug 09 2009 Orcan Ogetbil <orcan@nbcs.rutgers.edu> - 4.9-1
- Update to the latest version

* Tue Aug 14 2007 Eric Rivas <kc2hmv@nbcs.rutgers.edu> - 4.6.3-2
- Updated to 4.6.3

* Thu Feb 02 2006 Jonathan Kaczynski <jmkacz@oss.rutgers.edu> - 4.6.1-1
- Updated to the latest version.
