Name:       cpio
Version:    2.11
License:    GPL
Group:      System Environment/Base
Summary:    GNU cpio
Release:    1
URL:        http://ftp.gnu.org/gnu/cpio/
Source:     http://ftp.gnu.org/gnu/cpio/cpio-%{version}.tar.gz
BuildRoot:  %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

%description
GNU cpio is a program for making archives.  It is more powerful than tar
and has more features than Sun cpio.  You should install this package
if you are making archives or backups.

%prep
%setup -q

%build
%configure --prefix=/usr/local/gnu --disable-silent-rules
gmake

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/local/gnu
make install DESTDIR=%{buildroot}
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
%defattr(-,root,root,-)
/usr/local/gnu/bin/cpio
/usr/local/gnu/libexec/rmt-cpio
/usr/local/gnu/share/info/cpio.info
/usr/local/gnu/share/info/dir
/usr/local/gnu/share/man/man1/cpio.1
/usr/local/gnu/share/man/man1/mt.1

%changelog
* Fri Aug 06 2010 Orcan Ogetbil <orcan@nbcs.rutgers.edu> - 2.11.1
- Updated to the latest version.

* Mon Aug 20 2007 Naveen Gavini <ngavini@nbcs.rutgers.edu> - 2.9-5
- Updated to the latest version.
