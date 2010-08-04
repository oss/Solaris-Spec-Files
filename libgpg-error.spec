Summary:	libgpg-error
Name:		libgpg-error
Version:	1.7
Release:	1
URL:		ftp://ftp.gnupg.org/gcrypt/libgpg-error/
Source0:	ftp://ftp.gnupg.org/gcrypt/libgpg-error/%{name}-%{version}.tar.bz2
Source3:	gpg-error.pc.in
Patch0: 	libgpg-error-1.3-pkgconfig.patch
Group:		System Environment/Libraries
License:	LGPL
BuildRoot:	%{_tmppath}/%{name}-%{version}-root

%description
This is a library that defines common error values for all GnuPG
components.  Among these are GPG, GPGSM, GPGME, GPG-Agent, libgcrypt,
pinentry, SmartCard Daemon and possibly more in the future.

%package devel
Summary: Development files for the %{name} package
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}

%description devel
This is a library that defines common error values for all GnuPG
components.  Among these are GPG, GPGSM, GPGME, GPG-Agent, libgcrypt,
pinentry, SmartCard Daemon and possibly more in the future. This package
contains files necessary to develop applications using libgpg-error.

%prep
%setup -q
#%patch0 -p1 -b .pkgconfig
sed -i -e 's|^libdir=@libdir@$|libdir=@exec_prefix@/lib|g' src/gpg-error-config.in

%build
PATH="/opt/SUNWspro/bin:${PATH}" \
CC="cc" CXX="CC" CPPFLAGS="-I/usr/local/include" \
LD="/usr/ccs/bin/ld" \
LDFLAGS="-L/usr/local/lib -R/usr/local/lib"
export PATH CC CXX CPPFLAGS LD LDFLAGS

./configure \
	--prefix="/usr/local" \
	--disable-nls

gmake -j3

%install
rm -fr $RPM_BUILD_ROOT

gmake DESTDIR=%{buildroot} install

#mkdir -p $RPM_BUILD_ROOT/%{_libdir}/pkgconfig
#cp -f gpg-error.pc $RPM_BUILD_ROOT/%{_libdir}/pkgconfig/gpg-error.pc
rm -f $RPM_BUILD_ROOT/%{_libdir}/*.la
rm -rf $RPM_BUILD_ROOT/%{_datadir}/common-lisp

%clean
rm -fr $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc COPYING COPYING.LIB AUTHORS README INSTALL NEWS ChangeLog
%{_bindir}/gpg-error
%{_libdir}/libgpg-error.so.*

%files devel
%defattr(-,root,root)
%{_bindir}/gpg-error-config
%{_libdir}/libgpg-error.so
%{_libdir}/libgpg-error.a
#%{_libdir}/pkgconfig/gpg-error.pc
%{_includedir}/gpg-error.h
%{_datadir}/aclocal/gpg-error.m4

%changelog
* Wed Aug 04 2010 Steven Lu <sjlu@nbcs.rutgers.edu> - 1.7-1
- bump to 1.7
* Tue Jun 17 2008 David Diffenbaugh <davediff@nbcs.rutgers.edu> - 1.6-1
- bump
* Sat Oct 06 2007 David Lee Halik <dhalik@nbcs.rutgers.edu> - 1.4-1
- Initial Rutgers Build
