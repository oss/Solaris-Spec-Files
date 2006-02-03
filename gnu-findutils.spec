Name: findutils
Version: 4.2.27
Release: 2
Copyright: GPL
Group: System Environment/Base
Source: %{name}-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-root
Summary: The GNU findutils
%description
The GNU findutils are find, xargs, updatedb and locate.

%prep
%setup -q

%build
PATH="/usr/local/gnu/bin:/usr/local/bin:/usr/sfw/bin:$PATH"
export PATH
./configure --prefix=/usr/local/gnu
make

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/local/gnu
/usr/local/gnu/bin/make install prefix=%{buildroot}/usr/local/gnu

%post
if [ -x /usr/local/bin/install-info ] ; then
	/usr/local/bin/install-info --info-dir=/usr/local/gnu/info /usr/local/gnu/info/find.info
fi
cat <<EOF
If you run 'updatedb' in cron, make sure to run it as user 'nobody'
instead of 'root'.
EOF
mkdir -p /usr/local/gnu/var

%preun
if [ -x /usr/local/bin/install-info ] ; then
	/usr/local/bin/install-info --delete --info-dir=/usr/local/gnu/info /usr/local/gnu/info/find.info
fi

%clean
rm -rf %{buildroot}

%files
%defattr(-, root, bin)
%doc COPYING NEWS doc/*
/usr/local/gnu/bin/*
/usr/local/gnu/info/find.info
/usr/local/gnu/libexec/*
/usr/local/gnu/man/*/*

%changelog
* Thu Feb 02 2006 Jonathan Kaczynski <jmkacz@oss.rutgers.edu> - 4.2.27-2
- Made /usr/local/gnu/var in %post because updatedb stores the locate database there.

* Thu Feb 02 2006 Jonathan Kaczynski <jmkacz@oss.rutgers.edu> - 4.2.27-1
- Updated to latest version.

* Fri Sep 14 2001 Samuel Isaacson <sbi@nbcs.rutgers.edu>
- Fixed `locate' getshort() bug, added note on updatedb user.
