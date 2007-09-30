Summary:	beecrypt encryption
Name:		beecrypt
Version:	4.1.3
Release:	3
Copyright:	GPL
Group:		Applications/Editors
Source:		beecrypt-%{version}.tar.gz
Patch0:		beecrypt-4.1.3-noexec.patch
Distribution:	RU-Solaris
Vendor:		NBCS-OSS
Packager:	David Lee Halik <dhalik@nbcs.rutgers.edu>
BuildRoot:	%{_tmppath}/%{name}-root
BuildRequires:	automake
BuildArch:	sparc64

# NOTE: This is the most recent (9-13-07) cvs checkout NOT the real 4.1.3
# Due to a --noexecstack bug and linking issues, we found that the latest
# unreleased CVS had a fix and works

%description
BeeCrypt is an ongoing project to provide a strong and fast cryptography 
toolkit. Includes entropy sources, random generators, block ciphers, hash 
functions, message authentication codes, multiprecision integer routines, 
and public key primitives.

%package devel
Summary: %{name} include files, etc.
Requires: %{name} = %{version}
Group: Development
%description devel
%{name} include files, etc.
 
%prep
%setup -q -n beecrypt-%{version}

%patch -p1

%build
PATH="/opt/SUNWspro/bin:${PATH}" \
CC="cc" CXX="CC" CPPFLAGS="-I/usr/local/include" \
LD="/usr/ccs/bin/ld" \
LDFLAGS="-L/usr/local/lib -R/usr/local/lib"
export PATH CC CXX CPPFLAGS LD LDFLAGS

./autogen.sh --noconfigure
./configure \
	--prefix=/usr/local/ \
	--without-java

gmake -j3

%install
rm -rf $RPM_BUILD_ROOT
gmake install DESTDIR=$RPM_BUILD_ROOT

/usr/ccs/bin/strip $RPM_BUILD_ROOT/usr/local/lib/*.so*

rm -rf $RPM_BUILD_ROOT/usr/local/lib/libbeecrypt.la

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,other)
/usr/local/lib/*.so*

%files devel
%defattr(-,root,other)
/usr/local/lib/*.a
/usr/local/include/beecrypt

%changelog
* Thu Sep 13 2007 David Lee Halik <dhalik@nbcs.rutgers.edu> - 4.1.3-1
- Respun with SunCC
- Bumpt to latest CVS checkout (09-13-07)
