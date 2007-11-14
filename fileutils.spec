Name: fileutils
Version: 4.1
Release: 2
Copyright: GPL
Group: System Environment/Base
Source: fileutils-4.1.tar.gz
BuildRoot: /var/tmp/%{name}-root
Summary: The GNU fileutils
%description
The GNU fileutils are: chgrp, chmod, chown, cp, dd, df, dir, dircolors,
du, install, ln, ls, mkdir, mkfifo, mknod, mv, rm, rmdir, sync, touch,
and vdir.

%prep
%setup -q

%build
PATH="/opt/SUNWspro/bin:${PATH}" \
CC="cc" CXX="CC" CPPFLAGS="-I/usr/local/include" \
LD="/usr/ccs/bin/ld" \
LDFLAGS="-L/usr/local/lib -R/usr/local/lib" 
export PATH CC CXX CPPFLAGS LD LDFLAGS

./configure --prefix=/usr/local/gnu --disable-nls
gmake
gmake check

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/local/gnu
gmake install prefix=$RPM_BUILD_ROOT/usr/local/gnu

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-, root, root)
%doc doc/* COPYING AUTHORS NEWS INSTALL
/usr/local/gnu/bin/*
/usr/local/gnu/man/man1/*
/usr/local/gnu/lib/locale/*/LC_MESSAGES/*
/usr/local/gnu/info/*info*

%changelog
* Tue Nov 13 2007 David Lee Halik <dhalik@nbcs.rutgers.edu> - 4.1-2
- Disable NLS
