Name: fileutils
Version: 4.0
Release: 5
Copyright: GPL
Group: System Environment/Base
Source: fileutils-4.0.tar.gz
BuildRoot: /var/tmp/%{name}-root
Summary: The GNU fileutils
%description
The GNU fileutils are: chgrp, chmod, chown, cp, dd, df, dir, dircolors,
du, install, ln, ls, mkdir, mkfifo, mknod, mv, rm, rmdir, sync, touch,
and vdir.

%prep
%setup -q

%build
./configure --prefix=/usr/local/gnu
make
make check

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/local/gnu
make install prefix=$RPM_BUILD_ROOT/usr/local/gnu

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-, root, root)
%doc doc/* COPYING AUTHORS NEWS INSTALL
/usr/local/gnu/bin/*
/usr/local/gnu/man/man1/*
/usr/local/gnu/lib/locale/*/LC_MESSAGES/*
/usr/local/gnu/info/*info*
