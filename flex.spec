Name: flex
Version: 2.5.4a
Copyright: GPL
Group: Development/Tools
Summary: Flex is a scanner generator
Release: 5
Source: flex-%{version}.tar.gz
BuildRoot: /var/tmp/%{name}-root
Conflicts: vpkg-SFWflex

%description
Flex is a lex replacement that is used to generate scanners in C or C++.
Along with yacc, flex is often used in the front end of compilers.
Install flex if you are writing something that needs a scanner, or if
you are trying to compile software from source that requires lex.

%prep
%setup -q -n flex-2.5.4

%build
./configure --prefix=/usr/local
make

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/local/info
make install prefix=$RPM_BUILD_ROOT/usr/local
cp MISC/texinfo/flex.info $RPM_BUILD_ROOT/usr/local/info

%clean
rm -rf $RPM_BUILD_ROOT

%post
if [ -x /usr/local/bin/install-info ] ; then
	/usr/local/bin/install-info --info-dir=/usr/local/info \
		 /usr/local/info/flex.info
fi

%preun
if [ -x /usr/local/bin/install-info ] ; then
	/usr/local/bin/install-info --delete --info-dir=/usr/local/info \
		 /usr/local/info/flex.info
fi

%files
%defattr(-,root,root)
%doc COPYING
/usr/local/bin/*
/usr/local/lib/libfl.a
/usr/local/include/FlexLexer.h
/usr/local/man/man1/flex.1
/usr/local/info/flex.info
