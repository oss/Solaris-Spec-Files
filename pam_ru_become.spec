Name:		pam_ru_become
Version:	1.2.1
Release:	1
Group:		System Environment/Base
License:	Rutgers
Source: 	pam_ru_become-%{version}.tar.gz
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root

Summary:	Rutgers PAM module for become accounts

%description
This package provide PAM authentication for Rutgers become accounts.

%prep
%setup -q

%build
LD=/usr/ccs/bin/ld
export LD

CC=/opt/SUNWspro/bin/cc
export CC

%ifarch sparc64
gmake sparcv9 CFLAGS="-g -xs -v -m64 -xcode=pic32 -K pic -G" LDFLAGS="-G -64" VERSION=".%{version}"
gmake clean
%endif

# LFLAGS IS NOT A TYPO
gmake CFLAGS="-g -xs -v -K pic -G" LFLAGS="-G" VERSION=".%{version}"

%install
rm -rf %{buildroot}

%{__install} -d %{buildroot}%{_sysconfdir}
%{__install} -d %{buildroot}%{_libdir}
%{__install} -d %{buildroot}%{_mandir}/man5

%{__install} -m 0644 pam_ru_become.5 %{buildroot}%{_mandir}/man5/
%{__install} -m 0755 pam_ru_become.so.%{version} %{buildroot}%{_libdir}

%ifarch sparc64
%{__install} -d %{buildroot}%{_libdir}/sparcv9
%{__install} -m 0755 sparcv9/pam_ru_become.so.%{version} %{buildroot}%{_libdir}/sparcv9
cd %{buildroot}%{_libdir}/sparcv9
ln -sf pam_ru_become.so.%{version} pam_ru_become.so.1
%endif

cd %{buildroot}%{_libdir}
ln -sf pam_ru_become.so.%{version} pam_ru_become.so.1

%clean
rm -rf %{buildroot}

%post
cat << EOF

This version was built with both 32bit and 64bit modules, as such you want to
make sure you have an appropriate pam.conf (should contain \$ISA items in the
module paths). 

See /usr/local/doc/pam_ru_become-%{version}/ for sample configuration files.

EOF

%files
%defattr(-, root, root)
%doc TODO pam.conf.*
%{_libdir}/pam_ru_become.so.%{version}
%{_libdir}/pam_ru_become.so.1
%{_mandir}/man5/pam_ru_become.5

%ifarch sparc64
%{_libdir}/sparcv9/pam_ru_become.so.%{version}
%{_libdir}/sparcv9/pam_ru_become.so.1
%endif

%changelog
* Wed Jan 20 2010 Brian Schubert <schubert@nbcs.rutgers.edu> - 1.2.1-1
- Updated to version 1.2.1 for consistency with Linux package

* Fri Oct 16 2009 Brian Schubert <schubert@nbcs.rutgers.edu> - 1.2-4
- Added pam.conf.ru_hybrid
- Modified pam.conf.example and renamed it to pam.conf.ru_ldap

* Thu Aug 13 2009 Brian Schubert <schubert@nbcs.rutgers.edu> - 1.2-3
- More sample conf file changes

* Fri Aug 07 2009 Brian Schubert <schubert@nbcs.rutgers.edu> - 1.2-2
- Made some changes to the man page and the sample configuration file

* Wed Jul 29 2009 Brian Schubert <schubert@nbcs.rutgers.edu> - 1.2-1
- Version 1.2 adds "unbecome" mode and includes some fixes and a man page

* Tue Oct 14 2008 Brian Schubert <schubert@nbcs.rutgers.edu> - 1.1-1
- A user is now able to login normally if his/her password contains a ':'
