Summary: Rutgers PAM module for become accounts
Name: pam_ru_become
Version: 1.0
Release: 3
Copyright: Rutgers
Group: System Environment/Base
Source: %{name}-%{version}.tar.gz
BuildRoot: /var/tmp/%{name}-root
BuildRequires: vpkg-SPROcc

%description
This package provide PAM authentication for Rutgers' become accounts.

%prep
%setup -q

%build
LD=/usr/ccs/bin/ld
export LD

%ifarch sparc64
make sparcv9 CFLAGS="-g -xs -xarch=generic64 -xcode=pic32 -K pic -G" LDFLAGS="-G -64" VERSION=".1.0"
make clean
%endif

# LFLAGS IS NOT A TYPO
make CFLAGS="-g -xs -K pic -G" LFLAGS="-G" VERSION=".1.0"

%install
mkdir -p %{buildroot}/usr/local/etc
mkdir -p %{buildroot}/usr/local/lib
cp pam.conf.example %{buildroot}/usr/local/etc
cp pam_ru_become.so.%{version} %{buildroot}/usr/local/lib

%ifarch sparc64
mkdir -p %{buildroot}/usr/local/lib/sparcv9
cp sparcv9/pam_ru_become.so.%{version} $RPM_BUILD_ROOT/usr/local/lib/sparcv9
cd %{buildroot}/usr/local/lib/sparcv9
ln -sf pam_ru_become.so.%{version} pam_ru_become.so.1
%endif

cd %{buildroot}/usr/local/lib
ln -sf pam_ru_become.so.%{version} pam_ru_become.so.1

%clean
rm -rf $RPM_BUILD_ROOT

%post
cat << EOF
This version was built with both 32bit and 64bit modules, as such you want to
make sure you have an appropriate pam.conf (should contain $ISA items in the
module paths).
EOF

%files
%defattr(-,root,root)
/usr/local/lib/pam_ru_become.so.%{version}
/usr/local/lib/pam_ru_become.so.1
/usr/local/etc/pam.conf.example

%ifarch sparc64
/usr/local/lib/sparcv9/pam_ru_become.so.%{version}
/usr/local/lib/sparcv9/pam_ru_become.so.1
%endif
