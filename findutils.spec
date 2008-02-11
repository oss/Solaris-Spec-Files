%define name		findutils
%define ver     	4.2.32
%define rel     	1

Summary: 	The GNU findutils
Name: 		%{name}
Version: 	%{ver}
Release: 	%{rel}
Copyright: 	GPL
Group: 		System Environment/Base
Source0: 	http://ftp.gnu.org/pub/gnu/findutils/%{name}-%{ver}.tar.gz
#Patch:		findutils.patch
Distribution:	RU-Solaris
Vendor:		NBCS-OSS
Packager:	David Diffenbaugh <davediff@nbcs.rutgers.edu>
BuildRoot: 	%{_tmppath}/%{name}-root
#BuildRequires:	teTeX

%description
The GNU findutils are find, xargs, updatedb and locate.

%prep
%setup -q -n %{name}-%{ver}
#%patch -p1

%build

#/usr/local/teTeX/bin:

PATH="/opt/SUNWspro/bin:${PATH}" \
CC="cc" CXX="CC" CPPFLAGS="-I/usr/local/include" \
LD="/usr/ccs/bin/ld" \
LDFLAGS="-L/usr/local/lib -R/usr/local/lib" \
export PATH CC CXX CPPFLAGS LD LDFLAGS

./configure --prefix=/usr/local/gnu --disable-nls
gmake

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/local/gnu
gmake DESTDIR=%{buildroot} install
rm %{buildroot}/usr/local/gnu/share/info/dir
rm %{buildroot}/usr/local/gnu/lib/charset.alias

%post
cat <<EOF
If you run 'updatedb' in cron, make sure to run it as user 'nobody'
instead of 'root'.
EOF
mkdir -p /usr/local/gnu/var

%clean
rm -rf %{buildroot}

%files
%defattr(-, root, bin)
%doc COPYING NEWS doc/*
/usr/local/gnu/bin/*
#/usr/local/gnu/share/locale/*
/usr/local/gnu/share/info/find.info
/usr/local/gnu/libexec/*
/usr/local/gnu/share/man/*
#/usr/local/gnu/lib/charset.alias

%changelog
* Mon Feb 11 2008 David Diffenbaugh <davediff@nbcs.rutgers.edu> - 4.2.32-1
- updated to latest version 4.2.32, removed install-info preun and post scripts
* Tue Nov 13 2007 David Lee Halik <dhalik@nbcs.rutgers.edu> - 4.2.31-3
- Disable NLS
* Tue Aug 14 2007 David Lee Halik <dhalik@nbcs.rutgers.edu> - 4.2.31
- Fixed charset.alias conflict
* Tue Aug 14 2007 David Lee Halik <dhalik@nbcs.rutgers.edu> - 4.2.31
- Updated to 4.2.31
* Mon Sep 18 2006 David Lee Halik <dhalik@nbcs.rutgers.edu> - 4.2.28
- Updated to latest version. Patched Regex bug.
* Thu Feb 02 2006 Jonathan Kaczynski <jmkacz@oss.rutgers.edu> - 4.2.27-2
- Made /usr/local/gnu/var in %post because updatedb stores the locate database there.
* Thu Feb 02 2006 Jonathan Kaczynski <jmkacz@oss.rutgers.edu> - 4.2.27-1
- Updated to latest version.
* Fri Sep 14 2001 Samuel Isaacson <sbi@nbcs.rutgers.edu>
- Fixed `locate' getshort() bug, added note on updatedb user.
