Name: findutils
Version: 4.1
Release: 4
Copyright: GPL
Group: System Environment/Base
Source: %{name}-%{version}.tar.gz
Patch: %{name}-%{version}.patch
BuildRoot: %{_tmppath}/%{name}-root
Summary: The GNU findutils
%description
The GNU findutils are find, xargs, and locate.

%prep
%setup -q
%patch -p1

%build
./configure --prefix=/usr/local/gnu
make

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/local/gnu
make install prefix=%{buildroot}/usr/local/gnu

%post
if [ -x /usr/local/bin/install-info ] ; then
	/usr/local/bin/install-info --info-dir=/usr/local/gnu/info /usr/local/gnu/info/find.info
fi
cat <<EOF
If you run 'updatedb' in cron, make sure to run it as user 'nobody'
instead of 'root'.
EOF

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
/usr/local/gnu/man/*/*
/usr/local/gnu/libexec/*
/usr/local/gnu/info/find.info*

%changelog
* Fri Sep 14 2001 Samuel Isaacson <sbi@nbcs.rutgers.edu>
- Fixed `locate' getshort() bug, added note on updatedb user.
