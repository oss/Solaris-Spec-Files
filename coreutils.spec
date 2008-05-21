Summary: 	The GNU Core Utilities are the basic file, shell and text manipulation utilities of the GNU operating system.
Name: 		coreutils
Version: 	6.11
Release: 	1
Distribution:   RU-Solaris
Vendor:         NBCS-OSS
Packager:       Brian Schubert	<schubert@nbcs.rutgers.edu>
Group: 		General/Tools
Copyright: 	GPL
Source: 	%{name}-%{version}.tar.gz
BuildRoot: 	%{_tmppath}/%{name}-root
Obsoletes: 	textutils fileutils sh-utils
Provides: 	textutils fileutils sh-utils

%description
The GNU Core Utilities are the basic file, shell and text manipulation utilities of the GNU operating system. These are the core utilities which are expected to exist on every operating system.

Previously these utilities were offered as three individual sets of GNU  utilities, fileutils, shellutils, and textutils. Those three have been combined into a single set of utilities called the coreutils.

%prep
%setup -q

%build
PATH="/opt/SUNWspro/bin:/usr/ccs/bin:/usr/local/gnu/bin:/usr/local/bin:/usr/local/bin:$PATH"
CC=/opt/SUNWspro/bin/cc
CXX=/opt/SUNWspro/bin/CC
export CC CXX PATH
./configure --prefix=/usr/local/gnu
gmake 

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/local/gnu
/usr/local/gnu/bin/gmake install prefix=%{buildroot}/usr/local/gnu
rm %{buildroot}/usr/local/gnu/share/info/dir  
mv %{buildroot}/usr/local/gnu/share/info %{buildroot}/usr/local/gnu
mv %{buildroot}/usr/local/gnu/share/man %{buildroot}/usr/local/gnu
rmdir %{buildroot}/usr/local/gnu/share

%clean
rm -rf %{buildroot}


%files
%defattr(-,root,bin)
%doc AUTHORS COPYING INSTALL NEWS README THANKS TODO ABOUT-NLS 
/usr/local/gnu/info/coreutils.info
/usr/local/gnu/man/man1/*
/usr/local/gnu/bin/*
/usr/local/gnu/lib/charset.alias

%changelog
* Fri Feb 08 2008 David Diffenbaugh <davediff@nbcs.rutgers.edu> -  6.10-1
- updated to 6.10, changed /usr/local/gnu/bin/make to gmake, removed install-info preun/post scripts
* Thu Jun 07 2007 Naveen Gavini <ngavini@nbcs.rutgers.edu> - 5.97-1
- Upgraded to 6.9
* Mon Sep 18 2006 David Lee Halik <dhalik@nbcs.rutgers.edu> - 5.97-1
- Rebuilt tainted package
