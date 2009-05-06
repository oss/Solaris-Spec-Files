Summary: PAM CAS module
Name: Pam_cas
Version: 2.0.11
Release: 2.0.5
License: GPL
Group: System Environment/Base
Source: %{name}-%{version}-esup-%{release}.tar.gz
URL: http://sourcesup.cru.fr/frs/?group_id=213
Patch0: pam_cas.Makefile-suncc.patch
BuildRoot: /var/tmp/%{name}-root

%description
This package provide PAM authentication using CAS.

%prep
%setup -q -n %{name}-%{version}-esup-%{release}
cd sources
%patch0 -p0

%build
PATH="/opt/SUNWspro/bin:${PATH}" \
CC="cc" CXX="CC" CPPFLAGS="-I/usr/local/include" \
LD="/usr/ccs/bin/ld" \
LDFLAGS="-G -L/usr/local/lib -R/usr/local/lib"
export PATH CC CXX CPPFLAGS LD LDFLAGS

cd sources
mv Makefile.solaris Makefile
for i in `ls`;  do
sed -e 's///g' $i > $i.new
mv $i.new $i
done

gmake
gmake test

%install
mkdir -p %{buildroot}/usr/local/lib
mkdir -p %{buildroot}/usr/local/bin
cp sources/pam_cas.so %{buildroot}/usr/local/lib
cp sources/castest %{buildroot}/usr/local/bin

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc
/usr/local/lib/pam_cas.so
/usr/local/bin/castest

%changelog
*Fri May 1 2009 David Diffenbaugh <davediff@nbcs.rutgers.edu> - 2.0.11-2.0.5
- bumped to 2.0.5
*Fri May 1 2009 David Diffenbaugh <davediff@nbcs.rutgers.edu> - 2.0.11-2.0.4
- initial rutgers release
- patched Makefile to work with Sun cc
