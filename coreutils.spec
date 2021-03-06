Summary: 	The basic file, shell and text manipulation utilities of the GNU operating system.
Name: 		coreutils
Version: 	8.9
Release: 	1
Group: 		System Environment/Base
License: 	GPLv3+
Source: 	ftp://ftp.gnu.org/gnu/coreutils/%{name}-%{version}.tar.gz
URL:		http://www.gnu.org/software/coreutils/
BuildRoot: 	%{_tmppath}/%{name}-%{version}-%{release}-root
Obsoletes: 	textutils fileutils sh-utils
Provides: 	textutils fileutils sh-utils

%description
The GNU Core Utilities are the basic file, shell and text manipulation utilities of the GNU operating system. 
These are the core utilities which are expected to exist on every operating system.

Previously these utilities were offered as three individual sets of GNU  utilities, fileutils, shellutils, 
and textutils. Those three have been combined into a single set of utilities called the coreutils.

%prep
%setup -q

%build
export LDFLAGS="-lgen"
%configure 				\
	--prefix=%{_prefix}/gnu		\
	--bindir=/usr/local/gnu/bin     \
	--libdir=/usr/local/gnu/lib     \
	--mandir=%{_prefix}/gnu/man	\
	--infodir=%{_prefix}/gnu/info	\
	--enable-install-program=hostname,arch \
	--disable-silent-rules          \
	--disable-nls			\
	--without-gmp
gmake 

%install
rm -rf %{buildroot}
gmake install DESTDIR=%{buildroot}
rm %{buildroot}%{_prefix}/gnu/info/dir  

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,bin)
%doc README COPYING AUTHORS NEWS
%doc ChangeLog* TODO THANKS
%{_prefix}/gnu/info/coreutils.info
%{_prefix}/gnu/man/man1/*
%{_prefix}/gnu/bin/*
%{_prefix}/gnu/lib/charset.alias

%changelog
* Wed Aug 17 2011 Steven Lu <sjlu@nbcs.rutgers.edu> - 8.9-1
- Update to version 8.9
* Mon Aug 02 2010 Orcan Ogetbil <orcan@nbcs.rutgers.edu> - 8.5-1
- Updated to version 8.5
* Wed Sep 16 2009 Dan Gopstein <dgop@nbcs.rutgers.edu> - 7.6-1
- Updated to version 7.6
* Fri May 08 2009 Brian Schubert <schubert@nbcs.rutgers.edu> - 7.4-1
- Updated to version 7.4
* Mon Apr 13 2009 Brian Schubert <schubert@nbcs.rutgers.edu> - 7.2-1
- Updated to version 7.2
- Added --disable-nls configure option
* Tue Mar 17 2009 Brian Schubert <schubert@nbcs.rutgers.edu> - 7.1-1
- Updated to version 7.1
- Added --without-gmp configure option
- Cleaned up SPEC file
* Tue Jun 17 2008 David Diffenbaugh <davediff@nbcs.rutgers.edu> - 6.12-1
- bumped
* Wed May 21 2008 Brian Schubert <schubert@nbcs.rutgers.edu> - 6.11-1
- Updated to 6.11
* Fri Feb 08 2008 David Diffenbaugh <davediff@nbcs.rutgers.edu> -  6.10-1
- updated to 6.10, changed /usr/local/gnu/bin/make to gmake, removed install-info preun/post scripts
* Thu Jun 07 2007 Naveen Gavini <ngavini@nbcs.rutgers.edu> - 5.97-1
- Upgraded to 6.9
* Mon Sep 18 2006 David Lee Halik <dhalik@nbcs.rutgers.edu> - 5.97-1
- Rebuilt tainted package
