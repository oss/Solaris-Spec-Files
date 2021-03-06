Summary: Rutgers PAM module for group checking
Name: pam_ru_group
Version: 1.1
Release: 2
Copyright: Rutgers
Group: System Environment/Base
Source: %{name}-%{version}.tar.bz2
BuildRoot: /var/tmp/%{name}-root
#BuildRequires: vpkg-SPROcc

%description
This package provides a PAM module for group checking.

%prep
%setup -q

%build
CC=/opt/SUNWspro/bin/cc
export CC

%ifarch sparc64
make CFLAGS="-xarch=generic64 -xcode=pic32 -Kpic -g -xs" LDFLAGS="-64"
mkdir sparcv9
cp pam_ru_group.so.* sparcv9
make clean
%endif

make

%install
mkdir -p %{buildroot}/etc
mkdir -p %{buildroot}/usr/local/lib
cp pam.conf.group %{buildroot}/etc
cp pam_ru_group.so.%{version} %{buildroot}/usr/local/lib

%ifarch sparc64
mkdir -p %{buildroot}/usr/local/lib/sparcv9
cp sparcv9/pam_ru_group.so.%{version} %{buildroot}/usr/local/lib/sparcv9
cd %{buildroot}/usr/local/lib/sparcv9
ln -sf pam_ru_group.so.%{version} pam_ru_group.so.1
%endif

cd %{buildroot}/usr/local/lib
ln -sf pam_ru_group.so.%{version} pam_ru_group.so.1

%clean
rm -rf $RPM_BUILD_ROOT

%post
cat << EOF

Please refer to /etc/pam.conf.group for instructions and examples of how to use
this module.
This version has been built with both 32-bit and 64-bit modules, as such you
want to make sure that you have an appropriate pam.conf (should contain \$ISA
items in the modules paths).

EOF

%files
%defattr(-,root,root)
/usr/local/lib/pam_ru_group.so.%{version}
/usr/local/lib/pam_ru_group.so.1
/etc/pam.conf.group
%ifarch sparc64
/usr/local/lib/sparcv9/pam_ru_group.so.%{version}
/usr/local/lib/sparcv9/pam_ru_group.so.1
%endif
