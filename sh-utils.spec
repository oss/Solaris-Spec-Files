Name: sh-utils
Version: 2.0
Copyright: GPL
Group: System Environment/Base
Summary: GNU sh-utils
Release: 3
Source: sh-utils-2.0.tar.gz
BuildRoot: /var/tmp/%{name}-root

%description
The sh-utils are basename, date, dirname, echo, env, expr, factor,
false, hostname, id, logname, pathchk, pinky, printenv, printf, pwd,
seq, sleep, tee, test, true, tty, users, who, whoami, yes, uname,
chroot, hostid, nice, uptime, stty, groups, and nohup.  GNU's are a
little more featureful, so install this package if you like features.

%prep
%setup -q

%build
./configure --prefix=/usr/local/gnu
make

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/local/gnu
make install prefix=%{buildroot}/usr/local/gnu

%clean
rm -rf %{buildroot}

%post
if [ -x /usr/local/bin/install-info ] ; then
	/usr/local/bin/install-info --info-dir=/usr/local/gnu/info \
		 /usr/local/gnu/info/sh-utils.info
fi

%preun
if [ -x /usr/local/bin/install-info ] ; then
	/usr/local/bin/install-info --delete --info-dir=/usr/local/gnu/info \
		 /usr/local/gnu/info/sh-utils.info
fi

%files
%defattr(-,root,bin)
%doc COPYING
/usr/local/gnu/bin/*
/usr/local/gnu/info/sh-utils.info
/usr/local/gnu/man/man1/*
/usr/local/gnu/lib/locale/*/LC_MESSAGES/sh-utils.mo
