%define gprefix %{_prefix}/gnu

Name: 		findutils
Version: 	4.4.2
Release: 	1
Group: 		System Environment/Base
License:	GPL
URL:		http://www.gnu.org/software/findutils	
Source: 	http://ftp.gnu.org/pub/gnu/findutils/findutils-%{version}.tar.gz
BuildRoot: 	%{_tmppath}/%{name}-%{version}-%{release}-root

Summary:	Directory searching utilities	

%description
The GNU Find Utilities are the basic directory searching utilities of the 
GNU operating system. These programs are typically used in conjunction 
with other programs to provide modular and powerful directory search and 
file locating capabilities to other commands. 

This package contains the find, xargs, updatedb, and locate tools.

%prep
%setup -q

%build
PATH="/opt/SUNWspro/bin:/usr/ccs/bin:${PATH}"
CC="cc" CXX="CC"
CPPFLAGS="-I/usr/local/include"
LDFLAGS="-L/usr/local/lib -R/usr/local/lib"
export PATH CC CXX CPPFLAGS LDFLAGS

./configure \
	--prefix=%{gprefix}		\
	--infodir=%{gprefix}/info	\
	--mandir=%{gprefix}/man		\
	--disable-nls			

gmake -j3

%install
rm -rf %{buildroot}

gmake install DESTDIR=%{buildroot}

# Get rid of unpackaged files
rm -f %{buildroot}%{gprefix}/info/dir
rm -f %{buildroot}%{gprefix}/lib/charset.alias

%clean
rm -rf %{buildroot}

%post
if [ -x %{_bindir}/install-info ] ; then 
	%{_bindir}/install-info --info-dir=%{gprefix}/info %{gprefix}/info/find.info
fi

mkdir -p %{gprefix}/var

cat << EOF

If you run 'updatedb' in cron, make sure to run it as user 'nobody'
instead of 'root'.

EOF

%preun
if [ -x %{_bindir}/install-info ] ; then
        %{_bindir}/install-info --info-dir=%{gprefix}/info --delete %{gprefix}/info/find.info
fi

%files
%defattr(-, root, root)
%doc COPYING NEWS
%{gprefix}/bin/*
%{gprefix}/libexec/*
%{gprefix}/info/*.info*
%{gprefix}/man/man*/*

%changelog
* Thu Aug 13 2009 Brian Schubert <schubert@nbcs.rutgers.edu> - 4.4.2-1
- Updated to version 4.4.2
- Added (fixed) post and preun scriptlets

* Tue Apr 15 2008 David Diffenbaugh <davediff@nbcs.rutgers.edu> - 4.4.0-2
- bumped to latest version

* Mon Feb 11 2008 David Diffenbaugh <davediff@nbcs.rutgers.edu> - 4.2.32-1
- updated to latest version 4.2.32, removed install-info preun and post scripts

* Tue Nov 13 2007 David Lee Halik <dhalik@nbcs.rutgers.edu> - 4.2.31-3
- Disable NLS

* Tue Aug 14 2007 David Lee Halik <dhalik@nbcs.rutgers.edu> - 4.2.31
- Fixed charset.alias conflict

* Tue Aug 14 2007 David Lee Halik <dhalik@nbcs.rutgers.edu> - 4.2.31
- Updated to 4.2.31

* Mon Sep 18 2006 David Lee Halik <dhalik@nbcs.rutgers.edu> - 4.2.28
- Updated to latest version. Patched Regex bug.

* Thu Feb 02 2006 Jonathan Kaczynski <jmkacz@oss.rutgers.edu> - 4.2.27-2
- Made /usr/local/gnu/var in %post because updatedb stores the locate database there.

* Thu Feb 02 2006 Jonathan Kaczynski <jmkacz@oss.rutgers.edu> - 4.2.27-1
- Updated to latest version.

* Fri Sep 14 2001 Samuel Isaacson <sbi@nbcs.rutgers.edu>
- Fixed `locate' getshort() bug, added note on updatedb user.
