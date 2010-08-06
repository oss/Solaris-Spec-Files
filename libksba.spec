
Summary: X.509 library
Name:    libksba
Version: 1.0.8
Release: 1%{?dist}

License: GPLv3
Group:   System Environment/Libraries
URL:     http://www.gnupg.org/
Source0: ftp://ftp.gnupg.org/gcrypt/libksba/libksba-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

# quick-n-dirty hack to ksba-config, TODO: consider using pkgconfig instead
Patch1: libksba-1.0.3-multilib.patch

BuildRequires: gawk
# >= 1.4 preferred
BuildRequires: libgpg-error-devel >= 1.2 
BuildRequires: libgcrypt-devel >= 1.2.0

%description
KSBA is a library designed to build software based on the X.509 and
CMS protocols.

%package devel
Summary: Development headers and libraries for %{name}
Group:   Development/Libraries
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires(post): info
Requires(preun): info
%description devel
%{summary}.


%prep
%setup -q

%patch1 -p1 -b .multilib


%build
PATH="/opt/SUNWspro/bin:/usr/ccs/bin:${PATH}"
CC="cc" CXX="CC" CFLAGS="-I/usr/local/include -O2 -g" \
LD="/usr/ccs/bin/ld" \
LDFLAGS="-L/usr/local/lib/sparcv9 -R/usr/local/lib/sparcv9" \
export PATH CC CXX CFLAGS LD LDFLAGS
%configure \
  --disable-dependency-tracking \
  --disable-static

gmake %{?_smp_mflags}


%install
rm -rf $RPM_BUILD_ROOT

gmake install DESTDIR=$RPM_BUILD_ROOT

rm -f $RPM_BUILD_ROOT%{_infodir}/dir
rm -f $RPM_BUILD_ROOT%{_libdir}/lib*.la


%check
make check


%clean
rm -rf $RPM_BUILD_ROOT


%post devel
/usr/local/bin/install-info %{_infodir}/ksba.info %{_infodir}/dir ||:

%preun devel
if [ $1 -eq 0 ]; then
  /usr/local/bin/install-info --delete %{_infodir}/ksba.info %{_infodir}/dir ||:
fi


%files
%defattr(-,root,root,-)
%doc AUTHORS ChangeLog COPYING NEWS README* THANKS TODO VERSION
%{_libdir}/libksba.so.8*

%files devel
%defattr(-,root,root,-)
%{_bindir}/ksba-config
%{_libdir}/libksba.so
%{_includedir}/*
%{_datadir}/aclocal/*
%{_infodir}/*


%changelog
* Wed Aug 04 2010 Steven Lu <sjlu@nbcs.rutgers.edu> - 1.0.8-1
- bump!

* Wed Dec 02 2009 Orcan Ogetbil <orcan@nbcs.rutgers.edu> - 1.0.6-5
- I will not publish unsigned packages again

* Mon Nov 02 2009 Orcan Ogetbil <orcan@ncbs@rutgers.edu> - 1.0.6-4
- Solaris port

* Mon Aug 10 2009 Ville Skyttä <ville.skytta@iki.fi> - 1.0.6-3
- Convert specfile to UTF-8.

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Sat Jun 20 2009 Rex Dieter <rdieter@fedorproject.org> - 1.0.6-1
- libksba-1.0.6
- -devel: fix info scriptlet

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Fri Jan 09 2009 Rex Dieter <rdieter@fedoraproject.org> 1.0.5-1
- libksba-1.0.5

* Thu Sep 23 2008 Rex Dieter <rdieter@fedoraproject.org> 1.0.4-1
- libksba-1.0.4

* Thu Apr 03 2008 Rex Dieter <rdieter@fedoraproject.org> 1.0.3-2
- multiarch conflicts (#342201)

* Tue Feb 12 2008 Rex Dieter <rdieter@fedoraproject.org> 1.0.3-1
- libksba-1.0.3

* Fri Feb 08 2008 Rex Dieter <rdieter@fedoraproject.org> 1.0.2-4
- respin (gcc43)

* Sat Aug 25 2007 Rex Dieter <rdieter[AT]fedoraproject.org> 1.0.2-3
- BR: gawk

* Sat Aug 25 2007 Rex Dieter <rdieter[AT]fedoraproject.org> 1.0.2-2
- respin (ppc32, BuildID)
- License: GPLv3

* Fri Jul 06 2007 Rex Dieter <rdieter[AT]fedoraproject.org> 1.0.2-1
- libksba-1.0.2

* Fri Dec 01 2006 Rex Dieter <rexdieter[AT]users.sf.net> 1.0.1-1
- libksba-1.0.1

* Mon Oct 02 2006 Rex Dieter <rexdieter[AT]users.sf.net> 1.0.0-1.1
- respin

* Thu Aug 31 2006 Rex Dieter <rexdieter[AT]users.sf.net> 1.0.0-1
- libksba-1.0.0

* Tue Aug 29 2006 Rex Dieter <rexdieter[AT]users.sf.net> 0.9.15-3
- fc6 respin

* Thu Jun 20 2006 Rex Dieter <rexdieter[AT]users.sf.net> 0.9.15-2
- 0.9.15

* Wed Mar 1 2006 Rex Dieter <rexdieter[AT]users.sf.net> 0.9.13-2.1
- fc5: gcc/glibc respin

* Wed Nov 30 2005 Rex Dieter <rexdieter[AT]users.sf.net> 0.9.13-2
- remove hacks
- drop self Obsoletes

* Wed Nov 30 2005 Rex Dieter <rexdieter[AT]users.sf.net> 0.9.13-1
- 0.9.13

* Fri Aug 26 2005 Rex Dieter <rexdieter[AT]users.sf.net> 0.9.11-3
- botched Obsoletes good, let's try again.

* Fri Aug 26 2005 Rex Dieter <rexdieter[AT]users.sf.net> 0.9.11-2
- revert to 0.9.11 (0.9.12 makes gnupg2 fail on x86_64) using Obsoletes
  to avoid Epoch or other ugly means.

* Mon Aug  8 2005 Rex Dieter <rexdieter[AT]users.sf.net> 0.9.12-1
- 0.9.12
- --disable-static

* Thu Apr 21 2005 Rex Dieter <rexdieter[AT]users.sf.net> 0.9.11-1
- 0.9.11
- drop upstreamed acquote patch

* Fri Apr  7 2005 Michael Schwendt <mschwendt[AT]users.sf.net> - 0.9.9-2
- rebuilt

* Tue Feb  1 2005 Michael Schwendt <mschwendt[AT]users.sf.net> - 0:0.9.9-1
- Minus BR libtool, add epoch to -devel req, fix underquoted ksba.m4.

* Fri Oct 22 2004 Rex Dieter <rexdieter[AT]users.sf.net> 0:0.9.9-0.fdr.2
- remove hard-coded .gz from %%post/%%postun
- add %%check section

* Tue Oct 19 2004 Rex Dieter <rexdieter[AT]users.sf.net> 0:0.9.9-0.fdr.1
- 0.9.9

* Thu Mar 20 2003 Ville Skyttä <ville.skytta@iki.fi> - 0.4.7-0.fdr.1
- Update to 0.4.7, and to current Fedora guidelines.
- Exclude %%{_libdir}/*.la.

* Tue Feb 12 2003 Warren Togami <warren@togami.com> 0.4.6-1.fedora.3
- temporary workaround to lib/dir conflict problem

* Sat Feb  8 2003 Ville Skyttä <ville.skytta@iki.fi> - 0.4.6-1.fedora.1
- First Fedora release.
