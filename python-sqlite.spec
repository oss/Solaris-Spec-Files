%define real_name pysqlite

Summary: Python bindings for sqlite.
Name: python-sqlite
Version: 1.1.7
Release: 1%{?dist}
License: GPL
Group: Development/Libraries
URL: http://pysqlite.org/
Source: http://initd.org/pub/software/pysqlite/releases/1.1/%{version}/pysqlite-%{version}.tar.gz
Obsoletes: python-sqlite3
BuildRequires: sqlite-devel 
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

%description
This packages allows you to use sqlite with python.
sqlite is a simple database engine.

%prep
%setup -q -n pysqlite
rm -f doc/rest/.*swp

%build
python ./setup.py build 

%install
rm -rf ${RPM_BUILD_ROOT}
python ./setup.py install --prefix="${RPM_BUILD_ROOT}/%{_prefix}"

%clean
rm -rf ${RPM_BUILD_ROOT}

%files
%defattr(-, root, root, 0755)
%doc LICENSE README doc/ examples/
%{_libdir}/python*/site-packages/*

%changelog
* Wed Dec 02 2009 Orcan Ogetbil <orcan@nbcs.rutgers.edu> - 1.1.7-1
- I will not publish unsigned packages again

* Mon Nov 09 2009 Orcan Ogetbil <orcan@nbcs.rutgers.edu> - 1.1.7-0.1.2.3
- Solaris port 

* Tue Aug 28 2007 Jeff Sheltren <sheltren@cs.ucsb.edu> - 1.1.7-0.1.2.2
- Official EPEL rebuild

* Wed Jul 25 2007 Jeff Sheltren <sheltren@cs.ucsb.edu> - 1.1.7-0.1.2.1
- Prepend 0 to release
- Rebuild for EPEL

* Wed Jul 12 2006 Jesse Keating <jkeating@redhat.com> - 1.1.7-1.2.1
- rebuild

* Fri Feb 10 2006 Jesse Keating <jkeating@redhat.com> - 1.1.7-1.2
- bump again for double-long bug on ppc(64)

* Tue Feb 07 2006 Jesse Keating <jkeating@redhat.com> - 1.1.7-1.1
- rebuilt for new gcc4.1 snapshot and glibc changes

* Fri Feb 03 2006 Paul Nasrat <pnasrat@redhat.com> - 1.1.7-1
- Upgrade to latest upstream 1.1.x series
- sqlite_prepare fix now upstream
- Update url information

* Wed Feb 01 2006 Paul Nasrat <pnasrat@redhat.com> - 1.1.6-3
- Pass valid parameter to prepare (#179547)
- Temporarily remove %%check

* Wed Feb 01 2006 Paul Nasrat <pnasrat@redhat.com> - 1.1.6-2
- Rebuild

* Fri Dec 09 2005 Jesse Keating <jkeating@redhat.com>
- rebuilt

* Wed Mar  9 2005 Jeff Johnson <jbj@redhat.com> 1.1.6-1
- rename to "sqlite" from "sqlite3" (#149719).

* Sat Feb  5 2005 Jeff Johnson <jbj@jbj.org> 1.1.6-1
- repackage for fc4.
- upgrade to 1.1.6.

* Sat May 01 2004 Dag Wieers <dag@wieers.com> - 0.5.0-1
- Initial package. (using DAR)
