Summary: Rutgers PAM module caching Enigma passwords
Name: pam_ru_save
Version: 1.1
Release: 8
Copyright: Rutgers
Group: System Environment/Base
Source: %{name}-%{version}.tar.gz
BuildRoot: /var/tmp/%{name}-root
#BuildRequires: vpkg-SPROcc

%description
This package provide PAM authentication for caching Enigma passwords.

%prep
%setup -q

%build
PATH="/opt/SUNWspro/bin:${PATH}" \
CC="cc" CXX="CC" CPPFLAGS="-I/usr/local/include" \
LD="/usr/ccs/bin/ld" \
LDFLAGS="-L/usr/local/lib -R/usr/local/lib"
export PATH CC CXX CPPFLAGS LD LDFLAGS

%ifarch sparc64
gmake sparcv9 CFLAGS="-g -xs -xarch=generic64 -xcode=pic32 -K pic -G" LDFLAGS="-G -64" VERSION=".1.1"
gmake clean
%endif

# LFLAGS IS NOT A TYPO
gmake CFLAGS="-g -xs -K pic -G" LFLAGS="-G" VERSION=".1.1"

%install
mkdir -p %{buildroot}/usr/local/etc
mkdir -p %{buildroot}/usr/local/lib
cp pam_ru_save.so.%{version} %{buildroot}/usr/local/lib
cp pam_ru_store.so.%{version} %{buildroot}/usr/local/lib

%ifarch sparc64
mkdir -p %{buildroot}/usr/local/lib/sparcv9
cp sparcv9/pam_ru_save.so.%{version} $RPM_BUILD_ROOT/usr/local/lib/sparcv9
cp sparcv9/pam_ru_store.so.%{version} $RPM_BUILD_ROOT/usr/local/lib/sparcv9
cd %{buildroot}/usr/local/lib/sparcv9
ln -sf pam_ru_save.so.%{version} pam_ru_save.so.1
ln -sf pam_ru_store.so.%{version} pam_ru_store.so.1
%endif

cd %{buildroot}/usr/local/lib
ln -sf pam_ru_save.so.%{version} pam_ru_save.so.1
ln -sf pam_ru_store.so.%{version} pam_ru_store.so.1

%clean
rm -rf $RPM_BUILD_ROOT

%post
cat << EOF
This version was built with both 32bit and 64bit modules, as such you want to
make sure you have an appropriate pam.conf (should contain \$ISA items in the
module paths).
EOF

%files
%defattr(-,root,root)
/usr/local/lib/pam_ru_save.so.%{version}
/usr/local/lib/pam_ru_store.so.%{version}
/usr/local/lib/pam_ru_save.so.1
/usr/local/lib/pam_ru_store.so.1
%ifarch sparc64
/usr/local/lib/sparcv9/pam_ru_save.so.%{version}
/usr/local/lib/sparcv9/pam_ru_save.so.1
/usr/local/lib/sparcv9/pam_ru_store.so.%{version}
/usr/local/lib/sparcv9/pam_ru_store.so.1
%endif
