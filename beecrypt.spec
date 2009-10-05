Summary:	beecrypt encryption
Name:		beecrypt
Version:	4.2.1
Release:	1
License:	GPL
Group:		Applications/Editors
Source:		beecrypt-%{version}.tar.gz
Distribution:	RU-Solaris
Vendor:		NBCS-OSS
Packager:	Jarek Sedlacek <jarek@nbcs.rutgers.edu>
BuildRoot:	%{_tmppath}/%{name}-root
BuildRequires:	automake

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

#%patch -p1

%build
PATH="/opt/SUNWspro/bin:/usr/ccs/bin/:${PATH}" \
CC="cc" CXX="CC" CPPFLAGS="-I/usr/local/include -L/lib -xlic_lib=sunperf -lmtsk" \
LD="/usr/ccs/bin/ld" \
LDFLAGS="-L/lib -R/lib -lmtsk" \
RANLIB="/usr/ccs/bin/ranlib"
export PATH CC CXX CPPFLAGS LD LDFLAGS RANLIB

./autogen.sh --noconfigure
./configure \
	--prefix=/usr/local/ \
	--without-java

gmake

%install
rm -rf $RPM_BUILD_ROOT
gmake install DESTDIR=$RPM_BUILD_ROOT

/usr/ccs/bin/strip $RPM_BUILD_ROOT/usr/local/lib/*.so*

%clean
rm -rf $RPM_BUILD_ROOT

%files
%doc AUTHORS BENCHMARKS BUGS CONTRIBUTORS COPYING COPYING.LIB ChangeLog INSTALL NEWS README README.WIN32
%defattr(-,root,other)
/usr/local/lib/*.so*

%files devel
%defattr(-,root,other)
/usr/local/lib/*.a
/usr/local/include/beecrypt

%changelog
* Thu Oct 01 2009 Jarek Sedlacek <jarek@nbcs.rutgers.edu> 4.2.1-1
- bumped to 4.2.1
- eliminated need for patch by tweaking compiler/linker flags
* Thu Sep 13 2007 David Lee Halik <dhalik@nbcs.rutgers.edu> - 4.1.3-1
- Respun with SunCC
- Bumpt to latest CVS checkout (09-13-07)
