Name:           check
Version:        0.9.6
Release:        2%{?dist}
Summary:        A unit test framework for C
Source0:        http://download.sourceforge.net/check/%{name}-%{version}.tar.gz
Patch0: 	check.Makefile.am.patch
Patch1:		check.setenv.patch
Group:          Development/Tools
License:        LGPLv2+
URL:            http://check.sourceforge.net/
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

%description
Check is a unit test framework for C. It features a simple interface for 
defining unit tests, putting little in the way of the developer. Tests 
are run in a separate address space, so Check can catch both assertion 
failures and code errors that cause segmentation faults or other signals. 
The output from unit tests can be used within source code editors and IDEs.

%package devel
Summary:        Libraries and headers for developing programs with check
Group:          Development/Libraries
Requires:       pkgconfig
Requires:       %{name} = %{version}-%{release}

%description devel
Libraries and headers for developing programs with check

%package static
Summary:        Static libraries of check
Group:          Development/Libraries

%description static
Static libraries of check.

%prep
%setup -q
cd tests
%patch1 -p0
cd ..

%build
PATH="/usr/local/gnu/bin:/usr/local/bin:/opt/SUNWspro/bin:/usr/ccs/bin:$PATH" \
CC="cc" \
CXX="CC" \
CFLAGS="-kPIC" \
CPPFLAGS="-I/usr/local/include -I/usr/local/mysql-5.0.67/include/mysql " \
LDFLAGS="-L/usr/local/lib -R/usr/local/lib -lm -ldl" \
LUA_LIBS="-L/usr/local/lib -llua" \
LUA_CFLAGS="-I /usr/local/include" \
export PATH CC CXX CPPFLAGS LDFLAGS 
./configure

cd src
sed -e 's/\-ansi \-pedantic//' Makefile > Makefile.new
mv Makefile.new Makefile
cd ..

gmake

%install
rm -rf $RPM_BUILD_ROOT
gmake DESTDIR=$RPM_BUILD_ROOT install
rm -f $RPM_BUILD_ROOT%{_libdir}/*.la
rm -rf $RPM_BUILD_ROOT%{_infodir}/dir
rm -rf $RPM_BUILD_ROOT%{_defaultdocdir}/%{name}

%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
%doc AUTHORS COPYING.LESSER ChangeLog ChangeLogOld NEWS README SVNChangeLog
%doc THANKS TODO
%{_libdir}/libcheck.so.*

%files devel
%defattr(-,root,root,-)
%doc COPYING.LESSER doc/example
%{_includedir}/check.h
%{_libdir}/libcheck.so
%{_libdir}/pkgconfig/check.pc
%{_datadir}/aclocal/check.m4

#check used to be static only, hence this.
%files static
%defattr(-,root,root,-)
%{_libdir}/libcheck.a

%changelog
* Mon Jan 12 2009 Dave Diffenbaugh <davediff@nbcs.rutgers.edu> - 0.9.6-2
- updated spec file for solaris
- added sun cc

* Tue Jan  6 2009 Tom "spot" Callaway <tcallawa@redhat.com> - 0.9.6-1
- update to 0.9.6

* Mon Dec  1 2008 Jerry James <loganjerry@gmail.com> - 0.9.5-3
- Fix unowned directory (bz 473635)
- Drop unnecessary BuildRequires
- Replace patches with addition of -fPIC to CFLAGS in the spec file
- Add some more documentation files

* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 0.9.5-2.1
- Autorebuild for GCC 4.3

* Thu Aug  2 2007 Tom "spot" Callaway <tcallawa@redhat.com> 0.9.5-1
- 0.9.5 bump

* Fri Jul 14 2006 Jesse Keating <jkeating@redhat.com> - 0.9.3-5
- rebuild

* Fri Feb 10 2006 Jesse Keating <jkeating@redhat.com> - 0.9.3-4.fc5.2
- bump again for double-long bug on ppc(64)

* Tue Feb 07 2006 Jesse Keating <jkeating@redhat.com> - 0.9.3-4.fc5.1
- rebuilt for new gcc4.1 snapshot and glibc changes

* Mon Dec 19 2005 Warren Togami <wtogami@redhat.com> 0.9.2-4
- import into FC5 for gstreamer-0.10

* Fri Dec  2 2005 Tom "spot" Callaway <tcallawa@redhat.com> 0.9.2-3
- enabled -fPIC to resolve bz 174313

* Sat Sep 17 2005 Tom "spot" Callaway <tcallawa@redhat.com> 0.9.2-2
- get rid of the so file (not needed)
- only make devel package

* Sun Aug 14 2005 Tom "spot" Callaway <tcallawa@redhat.com> 0.9.2-1
- initial package for Fedora Extras
