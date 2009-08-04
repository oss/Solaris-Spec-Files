Name:		pam_ru_save
Version:	1.2
Release:	1
Group:		System Environment/Base
License:	Rutgers
Source: 	pam_ru_save-%{version}.tar.gz
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root

Summary:        Rutgers PAM module for caching Enigma passwords

%description
This package provide PAM authentication for caching Enigma passwords.

%prep
%setup -q

%build
PATH="/opt/SUNWspro/bin:/usr/ccs/bin:${PATH}"
CC="cc" LD="ld"
export PATH CC LD

%ifarch sparc64
gmake sparcv9 \
	CFLAGS="-v -g -xs -xarch=generic64 -xcode=pic32 -K pic -G"	\
	LDFLAGS="-G -64 -B direct -z defs"				\
	LIBS="-lpam -lsocket -lnsl -ldl -lc"				\
	VERSION=".%{version}"
gmake clean
%endif

# LFLAGS IS NOT A TYPO
gmake \
	CFLAGS="-v -g -xs -K pic -G" 		\
	LFLAGS="-G -B direct -z defs" 		\
	LIBS="-lpam -lsocket -lnsl -ldl -lc"	\
	VERSION=".%{version}"

%install
%{__install} -d %{buildroot}%{_libdir}
%{__install} -m 0755 pam_ru_save.so.%{version} %{buildroot}%{_libdir}
%{__install} -m 0755 pam_ru_store.so.%{version} %{buildroot}%{_libdir}

%ifarch sparc64
%{__install} -d %{buildroot}%{_libdir}/sparcv9
%{__install} -m 0755 sparcv9/pam_ru_save.so.%{version} %{buildroot}%{_libdir}/sparcv9/
%{__install} -m 0755 sparcv9/pam_ru_store.so.%{version} %{buildroot}%{_libdir}/sparcv9/
cd %{buildroot}%{_libdir}/sparcv9
ln -sf pam_ru_save.so.%{version} pam_ru_save.so.1
ln -sf pam_ru_store.so.%{version} pam_ru_store.so.1
%endif

cd %{buildroot}%{_libdir}
ln -sf pam_ru_save.so.%{version} pam_ru_save.so.1
ln -sf pam_ru_store.so.%{version} pam_ru_store.so.1

%clean
rm -rf %{buildroot}

%post
cat << EOF

This version was built with both 32bit and 64bit modules, as such you want to
make sure you have an appropriate pam.conf (should contain \$ISA items in the
module paths).

EOF

%files
%defattr(-,root,root)
%{_libdir}/pam_ru_save.so.%{version}
%{_libdir}/pam_ru_store.so.%{version}
%{_libdir}/pam_ru_save.so.1
%{_libdir}/pam_ru_store.so.1
%ifarch sparc64
%{_libdir}/sparcv9/pam_ru_save.so.%{version}
%{_libdir}/sparcv9/pam_ru_save.so.1
%{_libdir}/sparcv9/pam_ru_store.so.%{version}
%{_libdir}/sparcv9/pam_ru_store.so.1
%endif

%changelog
* Tue Aug 04 2009 Brian Schubert <schubert@nbcs.rutgers.edu> - 1.2-1
- Added "unbecome" PAM_USER reset
- Miscellaneous fixes
- Added changelog
