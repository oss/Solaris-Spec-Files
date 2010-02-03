%{!?python_sitelib: %global python_sitelib %(%{__python} -c "from distutils.sysconfig import get_python_lib; print get_python_lib()")}

Summary:	beecrypt encryption
Name:		beecrypt
Version:	4.2.1
Release:	3
License:	GPL
Group:		Applications/Editors
Source:		beecrypt-%{version}.tar.gz
Distribution:	RU-Solaris
Vendor:		NBCS-OSS
Packager:	Jarek Sedlacek <jarek@nbcs.rutgers.edu>
BuildRoot:	%{_tmppath}/%{name}-root
BuildRequires:	automake
BuildRequires:	python >= 2.6


%description
BeeCrypt is an ongoing project to provide a strong and fast cryptography 
toolkit. Includes entropy sources, random generators, block ciphers, hash 
functions, message authentication codes, multiprecision integer routines, 
and public key primitives.

%package devel
Summary: %{name} include files, etc.
Requires: %{name} = %{version}-%{release}
Group: Development
%description devel
%{name} include files, etc.

%package python
Summary: Files needed for python applications using beecrypt
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}
Requires: python >= 2.6

%description python
Beecrypt is a general-purpose cryptography library. This package contains
files needed for using python with beecrypt. 
 
%prep
%setup -q -n beecrypt-%{version}

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

rm -f $RPM_BUILD_ROOT/{%{_libdir},%{python_sitelib}}/*.la
rm -f $RPM_BUILD_ROOT/%{python_sitelib}/*.a 

%clean
rm -rf $RPM_BUILD_ROOT

%files
%doc AUTHORS BENCHMARKS BUGS CONTRIBUTORS COPYING COPYING.LIB ChangeLog INSTALL NEWS README README.WIN32
%defattr(-,root,root,-)
/usr/local/lib/*.so.*

%files devel
%defattr(-,root,root,-)
/usr/local/lib/*.so
/usr/local/include/beecrypt

%files python
%defattr(-,root,root,-)
%{python_sitelib}/_bc.so 

%changelog
* Wed Feb 03 2010 Orcan Ogetbil <orcan@nbcs.rutgers.edu> 4.2.1-3
- Move libbeecrypt.so to the devel package
* Mon Feb 01 2010 Orcan Ogetbil <orcan@nbcs.rutgers.edu> 4.2.1-2
- Rebuild
* Thu Oct 01 2009 Jarek Sedlacek <jarek@nbcs.rutgers.edu> 4.2.1-1
- bumped to 4.2.1
- eliminated need for patch by tweaking compiler/linker flags
* Thu Sep 13 2007 David Lee Halik <dhalik@nbcs.rutgers.edu> - 4.1.3-1
- Respun with SunCC
- Bumpt to latest CVS checkout (09-13-07)
