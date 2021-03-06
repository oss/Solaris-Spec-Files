Name:      autoconf
Version:   2.67
License:   GPL
Group:     Development/Tools
Summary:   GNU autoconf
Release:   1
URL:       http://ftp.gnu.org/gnu/autoconf/
Source:    http://ftp.gnu.org/gnu/autoconf/autoconf-%{version}.tar.xz
BuildRoot: /var/tmp/%{name}-root
Requires:  m4
Conflicts: vpkg-SFWaconf

%description
GNU autoconf generates shell scripts used to configure programs.  Install
this package if you are writing Unix software for several platforms and
you want GNU-style configure scripts.

%prep
%setup -q

%build
%configure
gmake

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/local
gmake install DESTDIR=$RPM_BUILD_ROOT
rm -f $RPM_BUILD_ROOT/usr/local/share/info/dir

#I don't really think we need this emacs/lisp stuff
rm -rf %{buildroot}/usr/local/share/emacs/site-lisp

%clean
rm -rf $RPM_BUILD_ROOT

%post
if [ -x /usr/local/bin/install-info ] ; then
	/usr/local/bin/install-info --info-dir=/usr/local/info \
		 /usr/local/share/info/autoconf.info
fi
if [ -x /usr/local/bin/install-info ] ; then
        /usr/local/bin/install-info --info-dir=/usr/local/info \
                 /usr/local/share/info/standards.info
fi

%preun
if [ -x /usr/local/bin/install-info ] ; then
	/usr/local/bin/install-info --delete --info-dir=/usr/local/info \
		 /usr/local/share/info/autoconf.info
fi
if [ -x /usr/local/bin/install-info ] ; then
        /usr/local/bin/install-info --delete --info-dir=/usr/local/info \
                 /usr/local/share/info/standards.info
fi 

%files
%defattr(-,root,root)
%doc COPYING
/usr/local/bin/*
/usr/local/share/autoconf/*
/usr/local/share/info/*
/usr/local/share/man/man1/*
#/usr/local/share/emacs/site-lisp/*

%changelog
* Thu Aug 05 2010 Orcan Ogetbil <orcan@nbcs.rutgers.edu - 2.67-1
- latest version
* Wed Sep 23 2009 Dan Gopstein <dgop@nbcs.rutgers.edu> - 2.64-1
- bumped to latest version, updated spec file syntax
* Tue Apr 15 2008 David Diffenbaugh <davediff@nbcs.rutgers.edu> - 2.62-3
- changed info-dir to /usr/local/info
* Thu Apr 10 2008 David Diffenbaugh <davediff@nbcs.rutgers.edu> - 2.62-2
- fixed info path
* Thu Apr 10 2008 David Diffenbaugh <davediff@nbcs.rutgers.edu> - 2.62-2
- bumped to latest version
* Wed Sep 12 2007 Eric Rivas <kc2hmv@nbcs.rutgers.edu> - 2.61-2
 - Compiler with Sun Studio.
 - Remove annoying file.
* Tue Aug 21 2007 Naveen Gavini <ngavini@nbcs.rutgers.edu> - 2.61-1
 - Updated to 2.61-1
