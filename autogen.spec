Name:		autogen
Version:	5.11
License:	GPLv3+
Group:		Development/Tools
Summary:	GNU autogen
Release:	1
URL:            http://www.gnu.org/software/autogen/
Source:		http://ftp.gnu.org/gnu/autogen/rel%{version}/autogen-%{version}.tar.bz2
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
Requires:	m4
Conflicts:	vpkg-SFWagen
Requires:	guile
BuildRequires:  guile gmp-devel

%description
AutoGen is a tool designed to simplify the creation and maintenance of 
programs that contain large amounts of repetitious text. It is 
especially valuable in programs that have several blocks of text that 
must be kept synchronized.

%package libopts
Summary:        Automated option processing library based on %{name}
# Although sources are dual licensed with BSD, some autogen generated files
# are only under LGPLv3+. We drop BSD to avoid multiple licensing scenario.
License:        LGPLv3+
Group:          System Environment/Libraries

%description libopts
Libopts is very powerful command line option parser consisting of a set of
AutoGen templates and a run time library that nearly eliminates the hassle of
parsing and documenting command line options.

%package libopts-devel
Summary:        Development files for libopts
# Although sources are dual licensed with BSD, some autogen generated files
# are only under LGPLv3+. We drop BSD to avoid multiple licensing scenario.
License:        LGPLv3+
Group:          Development/Libraries
Requires:       automake
Requires:       %{name}-libopts = %{version}-%{release}
Requires:       pkgconfig

%description libopts-devel
This package contains development files for libopts.


%prep
%setup -q

sed -i '\|/mk-agen-texi.sh|d' doc/Makefile.in

%build
CPPFLAGS="-I/usr/local/include/gmp32 -I/usr/local/include/guile"
export CPPFLAGS

%configure \
	--with-libguile \
	--with-libguile-cflags \
	--with-libguile-libs
	
gmake

%install
rm -rf $RPM_BUILD_ROOT

gmake install DESTDIR=$RPM_BUILD_ROOT
rm %{buildroot}/%{_infodir}/dir
rm %{buildroot}/%{_libdir}/*.la
rm %{buildroot}/%{_libdir}/*.a
rm %{buildroot}/%{_datadir}/%{name}/autoopts.m4
rm %{buildroot}/%{_datadir}/%{name}/libopts-*.tar.gz


%clean
rm -rf $RPM_BUILD_ROOT

%post
if [ -x /usr/local/bin/install-info ] ; then
        /usr/local/bin/install-info --info-dir=/usr/local/share/info \
                 /usr/local/share/info/%{name}.info
fi

%preun
if [ -x /usr/local/bin/install-info ] ; then
        /usr/local/bin/install-info --delete --info-dir=/usr/local/share/info \
                 /usr/local/share/info/%{name}.info
fi



%files
%defattr(-,root,root,-)
%doc AUTHORS
%doc ChangeLog
%doc COPYING
%doc NEWS
%doc README
%doc THANKS
%doc TODO
%doc pkg/libopts/COPYING.gplv3
%{_bindir}/columns
%{_bindir}/getdefs
%{_bindir}/%{name}
%{_bindir}/xml2ag
%{_infodir}/%{name}.info*
%{_mandir}/man1/%{name}.1*
%{_mandir}/man1/columns.1*
%{_mandir}/man1/getdefs.1*
%{_mandir}/man1/xml2ag.1*

%dir %{_datadir}/%{name}
%{_datadir}/%{name}/stdoptions.def
%{_datadir}/%{name}/*.tpl


%files libopts
%defattr(-,root,root,-)
%doc pkg/libopts/COPYING.mbsd
%doc pkg/libopts/COPYING.lgplv3
%{_libdir}/libopts.so.*

%files libopts-devel
%defattr(-,root,root,-)
%{_bindir}/autoopts-config
%{_datadir}/aclocal/*.m4
%{_libdir}/libopts.so
%{_libdir}/pkgconfig/autoopts.pc
%{_mandir}/man1/autoopts-config.1*
%{_mandir}/man3/*

%dir %{_includedir}/autoopts
%{_includedir}/autoopts/options.h
%{_includedir}/autoopts/usage-txt.h



%changelog
* Thu Aug 05 2010 Orcan Ogetbil <orcan@nbcs.rutgers.edu> - 5.11-1
- Latest version
* Mon Sep 28 2009 Dan Gopstein <dgop@nbcs.rutgers.edu> - 5.9.8-1
- Updated to latest version, updated syntax
* Wed May 28 2008 David Diffenbaugh <davediff@nbcs.rutgers.edu> - 5.9.5-1
- bumped to latest version
* Fri Feb 08 2008 David Diffenbaugh <davediff@nbcs.rutgers.edu> - 5.9.4-2
  removed info post and pre scripts, updated files section, removed info/dir
* Tue Feb 05 2008 David Diffenbaugh <davediff@nbcs.rutgers.edu> - 5.9.4-1
- updated to 5.9.4
* Sat Oct 20 2007 David Lee Halik <dhalik@nbcs.rutgers.edu> - 5.9.3-1
- Bump to 5.9.3
* Wed Aug 22 2007 Naveen Gavini <ngavini@nbcs.rutgers.edu> - 5.9.2-1
- Updated to the latest version.
