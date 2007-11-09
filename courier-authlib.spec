Summary: Courier Authentication Library
Name: courier-authlib
Version: 0.60.2
Release: 1
Copyright: GPL
Group: Applications/Mail
Source0: courier-authlib-%{version}.tar.bz2
Distribution: RU-Solaris
Vendor: NBCS-OSS
Packager: David Lee Halik <dhalik@nbcs.rutgers.edu>
BuildRoot: %{_tmppath}/%{name}-root
BuildRequires: openssl >= 0.9.8 coreutils sed perl gdbm >= 1.8.3 openldap-devel >= 2.3 openldap-devel < 2.4
Requires: openssl >= 0.9.8 gdbm >= 1.8.3 openldap-lib >= 2.3 openldap-lib < 2.4
Patch0: courier-authlib-0.58-authpam.patch
Patch1: courier-authdaemon-initd.patch
Patch2:	courier-authlib-0.60-LD-Makefile.patch

%description
This is the Courier authentication library. Copies of this library code used
to exist in other tarballs: Courier, Courier-IMAP, and SqWebMail. Building and
installing any of these packages would've automatically installed this
authentication code.

Note: This contains a Rutgers' specific patch

%package static
Group: Applications/Mail
Summary:  Courier-Authlib
Requires: %{name} = %{version}-%{release}

%description static
These are the static libraries from the courier-authlib package.

Note: This contains a Rutgers' specific patch

%prep
%setup -q

%patch0 -p1
%patch1 -p1
%patch2 -p1

%build

CC='cc' CXX='CC' \
CFLAGS='' CXXFLAGS='' \
LDFLAGS='-L/usr/local/ssl/lib -R/usr/local/ssl/lib -L/usr/local/lib -R/usr/local/lib -L/usr/local/lib/courier-authlib -R/usr/local/lib/courier-authlib' \
CPPFLAGS='-I/usr/local/ssl/include -I/usr/local/include' \
PATH=/opt/SUNWspro/bin:/usr/ccs/bin:/usr/local/gnu/bin:$PATH
export CC CXX CFLAGS CXXFLAGS LDFLAGS CPPFLAGS PATH

./configure \
	--localstatedir=/var/run \
	--without-authdaemon \
	--with-db=gdbm \
	--without-ipv6 \
	--prefix=/usr/local \
	--enable-workarounds-for-imap-client-bugs
# --with-authdaemonvar=/var/run/authdaemon.courier-imap 

gmake -j3

# Correct something we don't like
sed 's/\/usr\/local\/etc\/authlib\/authdaemonrc/${prefix}\/etc\/authlib\/authdaemonrc/' authdaemond > authdaemond.patched
mv authdaemond.patched authdaemond

%install
%{__rm} -rf $RPM_BUILD_ROOT
%{__mkdir_p} $RPM_BUILD_ROOT/etc/pam.d
gmake install DESTDIR=$RPM_BUILD_ROOT
gmake install-configure DESTDIR=$RPM_BUILD_ROOT

# We would like an init file
mkdir -p $RPM_BUILD_ROOT/etc/init.d
install -m 0755 courier-authdaemon.initd \
   $RPM_BUILD_ROOT/etc/init.d/courier-authdaemon

# Note: keep the *.la files.
%files
%defattr(-,root,root)
%doc AUTHORS COPYING COPYING.GPL ChangeLog INSTALL NEWS README
%doc 00README.NOW.OR.SUFFER imap/ChangeLog 
%config(noreplace) /usr/local/etc/authlib/*
/etc/init.d/courier-authdaemon
/usr/local/lib/courier-authlib/*.so*
/usr/local/libexec/courier-authlib/*
/usr/local/include/*
/usr/local/share/man/*
/usr/local/bin/*
/usr/local/sbin/*
/var/*
/usr/local/lib/courier-authlib/*.la

%files static
%defattr(-,root,root)
/usr/local/lib/courier-authlib/*.a

%clean
rm -rf $RPM_BUILD_ROOT

%changelog
* Wed Nov 07 2007 David Lee Halik <dhalik@nbcs.rutgers.edu> - 0.60.2-1
- Added defattr to static libs
- Bumped to 0.60.2
* Fri Aug 24 2007 Eric Rivas <kc2hmv@nbcs.rutgers.edu> - 0.59.3-4
 - Correct file list and keep libtool la files.
* Thu Aug 23 2007 Eric Rivas <kc2hmv@nbcs.rutgers.edu>
 - Added init script.
* Wed Aug 22 2007 Eric Rivas <kc2hmv@nbcs.rutgers.edu>
 - Cleaned up paths.
* Mon Jan 16 2006 Eric Rivas <kc2hmv@nbcs.rutgers.edu>
 - Update to version 0.58
* Thu Jul 28 2005 Eric Rivas <kc2hmv@nbcs.rutgers.edu>
 - Update to version 0.57
* Tue May 03 2005 Leonid Zhadanovsky <leozh@nbcs.rutgers.edu>
 - New package, version 0.55
