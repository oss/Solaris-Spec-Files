Name:      diffutils
Version:   3.0
Release:   1
License:   GPL
Group:     System Environment/Base
URL:       ftp://ftp.gnu.org/pub/gnu/diffutils/
Source:    ftp://ftp.gnu.org/pub/gnu/diffutils/diffutils-%{version}.tar.xz
BuildRoot: /var/tmp/%{name}-root
Summary:   The GNU diffutils
Requires:  info
%description
The GNU diffutils are cmp, diff, diff3, and sdiff.

%prep
%setup -q

%build
PATH="/opt/SUNWspro/bin:${PATH}" \
CC="cc" CXX="CC" CPPFLAGS="-I/usr/local/include" \
LD="/usr/ccs/bin/ld" \
LDFLAGS="-L/usr/local/lib -R/usr/local/lib" 
export PATH CC CXX CPPFLAGS LD LDFLAGS

./configure --prefix=/usr/local/gnu --disable-nls --disable-silent-rules
gmake

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/local/gnu
gmake install DESTDIR=%{buildroot}

rm -f %{buildroot}/usr/local/gnu/lib/charset.alias
rm -f %{buildroot}/usr/local/gnu/share/info/dir

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
/usr/local/gnu/share/info/diff.info*
/usr/local/gnu/share/man/man1/*
#/usr/local/gnu/share/locale/*


%changelog
* Thu Aug 05 2010  Orcan Ogetbil <orcan@nbcs.rutgers.edu> - 3.0-1
- Update to latest version

* Tue Nov 13 2007 David Lee Halik <dhalik@nbcs.rutgers.edu> - 2.8.7-4
- Disable NLS
* Fri Aug 31 2007 Naveen Gavini <ngavini@nbcs.rutgers.edu> - 2.8.7-1
- Updated to the latest version.
