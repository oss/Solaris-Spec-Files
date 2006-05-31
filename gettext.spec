Summary:        Internationalization Tools
Name:           gettext
Version:        0.14.5
Release:        2
Copyright:      GPL
Group:          Development/Tools
Source:         %{name}-%{version}.tar.gz
Distribution:   RU-Solaris
Vendor:         NBCS-OSS
Packager:       Leo Zhadanovsky <leozh@nbcs.rutgers.edu>
BuildRoot:      /var/tmp/%{name}-%{version}-root
Requires:	libiconv
BuildRequires:	libiconv-devel

%description
GNU gettext is a tool that helps programmers write programs that
are "portable" culturally: by marking strings in your program that
potentially should be in several languages and compiling with gettext,
you can add translations with minimum effort.  Install gettext if you
are developing software that potentially would be used by non-English
speakers or compiling software that requires it.

%package devel
Summary: Libraries, includes to develop applications with %{name}.
Group: Applications/Libraries
Requires: %{name} = %{version}

%description devel
The %{name}-devel package contains the header files and static libraries
for building applications which use %{name}.

%prep
%setup -q

%build
PATH="/opt/SUNWspro/bin:/usr/local/teTeX/bin:${PATH}" \
CC="cc" CXX="CC" CPPFLAGS="-I/usr/local/include" \
LD="/usr/ccs/bin/ld" \
LDFLAGS="-L/usr/local/lib -R/usr/local/lib" \
export PATH CC CXX CPPFLAGS LD LDFLAGS

./configure --prefix=/usr/local --with-libiconv-prefix=/usr/local
make

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/local
make install prefix=$RPM_BUILD_ROOT/usr/local

%clean
rm -rf $RPM_BUILD_ROOT

%post
if [ -x /usr/local/bin/install-info ] ; then
	/usr/local/bin/install-info --info-dir=/usr/local/info \
		 /usr/local/info/gettext.info
fi

%preun
if [ -x /usr/local/bin/install-info ] ; then
	/usr/local/bin/install-info --delete --info-dir=/usr/local/info \
		 /usr/local/info/gettext.info
fi

%files
%defattr(-,root,root)
%doc COPYING
/usr/local/info/*.info*
/usr/local/bin/*
/usr/local/lib/*.so*
/usr/local/share/*
/usr/local/lib/gettext/*

%files devel
%defattr(-,root,root)
/usr/local/include/*

%changelog
* Mon May 22 2006 Leo Zhadanovsky <leozh@nbcs.rutgers.edu> - 0.14.5-1
- Updated to new version, switched to Sun CC.
