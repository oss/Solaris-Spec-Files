Name: bison
Version: 1.28
Copyright: GPL
Group: Development/Tools
Summary: Bison generates LALR parsers
Release: 3
Source: bison-%{version}.tar.gz
BuildRequires: make
BuildRoot: /var/tmp/%{name}-root
Conflicts: vpkg-SFWbison

%description
Bison is a yacc replacement.  It is used to create parsers.  Along with
lex, it is commonly used to create the front-end of a compiler.  Install
this if you need a parser in C, or if you need to compile software from
source with bison or yacc grammars. 

%prep
%setup -q

%build
./configure --prefix=/usr/local
gmake

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/local
make install prefix=$RPM_BUILD_ROOT/usr/local

%clean
rm -rf $RPM_BUILD_ROOT

%post
if [ -x /usr/local/bin/install-info ] ; then
	/usr/local/bin/install-info --info-dir=/usr/local/info \
		 /usr/local/info/bison.info
fi

%preun
if [ -x /usr/local/bin/install-info ] ; then
	/usr/local/bin/install-info --delete --info-dir=/usr/local/info \
		 /usr/local/info/bison.info
fi

%files
%defattr(-,root,root)
%doc COPYING
/usr/local/lib/locale/*/LC_MESSAGES/*
/usr/local/bin/bison
/usr/local/share/bison.simple
/usr/local/share/bison.hairy
/usr/local/info/bison.info
/usr/local/man/man1/bison.1
