Name:		bison
Version:	2.4.2
License:	GPL
Group:		Development/Tools
Summary:	A GNU general-purpose parser generator
Release:	2
Source:		ftp://ftp.gnu.org/gnu/bison/bison-%{version}.tar.gz
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root
BuildRequires:	m4
Conflicts:	vpkg-SFWbison

%description
Bison is a general-purpose parser generator that converts an annotated 
context-free grammar into an LALR(1) or GLR parser for that grammar. Once you 
are proficient with Bison, you can use it to develop a wide range of language 
parsers, from those used in simple desk calculators to complex programming 
languages.

Bison is upward compatible with Yacc: all properly-written Yacc grammars ought 
to work with Bison with no change. Anyone familiar with Yacc should be able to 
use Bison with little trouble. You need to be fluent in C or C++ programming in 
order to use Bison. 

%prep
%setup -q

%build
PATH="/opt/SUNWspro/bin:/usr/local/gnu/bin:${PATH}"
CC="cc" CXX="CC"
CPPFLAGS="-I/usr/local/include"
LD="/usr/ccs/bin/ld"
LDFLAGS="-L/usr/local/lib -R/usr/local/lib"
export PATH CC CXX CPPFLAGS LD LDFLAGS

./configure \
		--prefix=%{_prefix}	\
		--infodir=%{_infodir}	\
		--mandir=%{_mandir}	\
		--disable-nls
gmake

%install
rm -rf %{buildroot}
gmake install DESTDIR=%{buildroot}
rm -f %{buildroot}%{_infodir}/dir
rm -f %{buildroot}%{_libdir}/charset.alias

%clean
rm -rf %{buildroot}

%post
if [ -x %{_bindir}/install-info ] ; then
	%{_bindir}/install-info --info-dir=%{_infodir} \
		 %{_infodir}/bison.info
fi

%preun
if [ -x %{_bindir}/install-info ] ; then
	%{_bindir}/install-info --delete --info-dir=%{_infodir} \
		 %{_infodir}/bison.info
fi

%files
%defattr(-,root,root)
%doc README COPYING AUTHORS 
%doc TODO THANKS *ChangeLog
%{_bindir}/*
%{_datadir}/bison/
%{_datadir}/aclocal/bison-i18n.m4
%{_libdir}/*
%{_infodir}/*
%{_mandir}/man1/*

%changelog
* Thu Aug 05 2010 Steven Lu <sjlu@nbcs.rutgers.edu> -2.4.2-1
- bump
* Tue May 19 2009 Brian Schubert <schubert@nbcs.rutgers.edu> - 2.4.1-2
- Removed some files that conflict with other packages
* Tue Mar 02 2009 Brian Schubert <schubert@nbcs.rutgers.edu> - 2.4.1-1
- Updated to version 2.4.1
* Tue Nov 13 2007 David Lee Halik <dhalik@nbcs.rutgers.edu> - 2.3-2
- Disable NLS
* Sat Aug 11 2007 David Lee Halik <dhalik@nbcs.rutgers.edu> - 2.3
- Bump to 2.3
