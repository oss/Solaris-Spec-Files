Name:		flex
Version:	2.5.35
Copyright:	GPL
Group:		Development/Tools
Summary:	Flex is a scanner generator
Release:	2
Source:		flex-%{version}.tar.gz
BuildRoot:	/var/tmp/%{name}-root
Conflicts:	vpkg-SFWflex

%description
Flex is a lex replacement that is used to generate scanners in C or C++.
Along with yacc, flex is often used in the front end of compilers.
Install flex if you are writing something that needs a scanner, or if
you are trying to compile software from source that requires lex.

%prep
%setup -q

%build
PATH="/opt/SUNWspro/bin:${PATH}" \
CC="cc" CXX="CC" CPPFLAGS="-I/usr/local/include" \
LD="/usr/ccs/bin/ld" \
LDFLAGS="-L/usr/local/lib -R/usr/local/lib"
export PATH CC CXX CPPFLAGS LD LDFLAGS

./configure --prefix=/usr/local --disable-nls
gmake

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/local/share/info
gmake DESTDIR=%{buildroot} install

%clean
rm -rf $RPM_BUILD_ROOT

%post
if [ -x /usr/local/bin/install-info ] ; then
	/usr/local/bin/install-info --info-dir=/usr/local/share/info \
		 /usr/local/info/flex.info
fi

%preun
if [ -x /usr/local/bin/install-info ] ; then
	/usr/local/bin/install-info --delete --info-dir=/usr/local/share/info \
		 /usr/local/info/flex.info
fi

%files
%defattr(-,root,root)
%doc COPYING
/usr/local/bin/*
/usr/local/lib/libfl.a
/usr/local/include/FlexLexer.h
/usr/local/man/man1/flex.1
/usr/local/info/flex.info*

%changelog
* Tue Aug 26 2008 David Diffenbaugh <davediff@nbcs.rutgers.edu> 2.5.35-2
- fixed broken install-info crap
* Tue May 27 2008 Brian Schubert <schubert@nbcs.rutgers.edu> - 2.5.35-1
- Updated to 2.5.35
* Tue Nov 13 2007 David Lee Halik <dhalik@nbcs.rutgers.edu> - 2.5.33-2
- Disable NLS
* Tue Aug 28 2007 David Lee Halik <dhalik@nbcs.rutgers.edu> 2.5.33-1
- Bumped to 2.5.33
- Cleaned up spec
