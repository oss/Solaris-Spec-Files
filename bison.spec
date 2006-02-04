Name: bison
Version: 2.1
Copyright: GPL
Group: Development/Tools
Summary: Bison generates LALR parsers
Release: 1
Source: ftp://ftp.gnu.org/gnu/bison/bison-%{version}.tar.bz2
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
CC='/opt/SUNWspro/bin/cc'
CXX='/opt/SUNWspro/bin/CC'
CFLAGS='-g -xs'
CPPFLAGS='-I/usr/local/include -I/usr/sfw/include'
LDFLAGS='-L/usr/local/lib -R/usr/local/lib -L/usr/sfw/lib -R/usr/sfw/lib'
export CC CXX CFLAGS CPPFLAGS LDFLAGS
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
/usr/local/share/*
/usr/local/bin/bison
/usr/local/bin/yacc
/usr/local/info/*
/usr/local/lib/*
/usr/local/man/man1/bison.1
