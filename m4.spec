%define gnu_prefix %{_prefix}/gnu

Name: 		m4
Version: 	1.4.13
Release:	1
Group: 		System Environment/Base
License:        GPL
URL:		http://www.gnu.org/software/m4
Source: 	ftp://ftp.gnu.org/gnu/m4/m4-%{version}.tar.bz2
BuildRoot: 	%{_tmppath}/%{name}-%{version}-%{release}-root

Conflicts:	vpkg-SFWgm4

Summary:        The GNU implementation of the traditional Unix macro processor

%description
GNU M4 is a macro processor in the sense that it copies its input to the output 
expanding macros as it goes. Macros are either builtin or user-defined and can 
take any number of arguments. Besides just doing macro expansion, m4 has builtin 
functions for including named files, running UNIX commands, doing integer arithmetic, 
manipulating text in various ways, recursion etc... m4 can be used either as a 
front-end to a compiler or as a macro processor in its own right. 

%prep
%setup -q

%build
PATH="/opt/SUNWspro/bin:/usr/ccs/bin:${PATH}"
CC="cc" CXX="CC" CPPFLAGS="-I/usr/local/include"
LDFLAGS="-L/usr/local/lib -R/usr/local/lib"
export PATH CC CXX CPPFLAGS LDFLAGS

./configure \
	--prefix=%{gnu_prefix}		\
	--infodir=%{gnu_prefix}/info	\
	--mandir=%{gnu_prefix}/man

gmake -j3

%install
rm -rf %{buildroot}

gmake install DESTDIR=%{buildroot}

# Remove unpackaged files
rm %{buildroot}%{gnu_prefix}/info/dir
rm %{buildroot}%{gnu_prefix}/lib/charset.alias

%clean
rm -rf %{buildroot}

%post
[ -x %{_bindir}/install-info ] && %{_bindir}/install-info --info-dir=%{gnu_prefix}/info %{gnu_prefix}/info/m4.info

%preun
[ -x %{_bindir}/install-info ] && %{_bindir}/install-info --info-dir=%{gnu_prefix}/info --delete %{gnu_prefix}/info/m4.info

%files
%defattr(-, root, root)
%doc README COPYING AUTHORS THANKS
%doc NEWS TODO BACKLOG ChangeLog
%{gnu_prefix}/bin/*
%{gnu_prefix}/man/man1/*
%{gnu_prefix}/info/*.info*

%changelog
* Wed Sep 09 2009 Brian Schubert <schubert@nbcs.rutgers.edu> - 1.4.13-1
- Updated to version 1.4.13
- Fixed man, info paths
- Added post and preun scriptlets

* Tue Apr 15 2008 David Diffenbaugh <davediff@nbcs.rutgers.edu> - 1.4.11-4
- fixed charset.alias conflict, removed install-info stuff

* Thu Apr 08 2008 David Diffenbaugh <davediff@nbcs.rutgers.edu> - 1.4.11-1
- bumped

* Tue Aug 28 2007 David Lee Halik <dhalik@nbcs.rutgers.edu> - 1.4.9-1
- Updated to 1.4.9

* Thu May 04 2006 Leo Zhadanovsky <leozh@nbcs.rutgers.edu> - 1.4.4-1
- Cleaned up spec file, updated to 1.4.4
