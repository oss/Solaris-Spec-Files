%{!?python_sitearch: %define python_sitearch %(%{__python} -c "from distutils.sysconfig import get_python_lib; print get_python_lib(1)")} 

Summary: 	File type information tool
Name: 		file
Version:	5.04
Release:	2
Group:		System Environment/Base
License:	GPL
URL:		http://www.darwinsys.com/file
Source:		ftp://ftp.astron.com/pub/file/%{name}-%{version}.tar.gz
Patch0:		file-5.04-warnings.patch
# Add rpath to python library:
Patch1:         file-python-magic-5.04.patch
Packager:	Brian Schubert <schubert@nbcs.rutgers.edu>
BuildRequires:	autoconf >= 2.62
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root

%description
File tests each argument in an attempt to classify it.  There are
three sets of tests, performed in this order: filesystem tests, magic 
numbertests, and language tests. The first test that succeeds causes the
file type to be printed.

%package devel
Summary:	Libraries and header files for file development
Group:		Development/Headers
Requires:	%{name} = %{version}-%{release}

%description devel
The file-devel package contains the header files and libmagic library
necessary for developing programs using libmagic.

%package -n python-magic
Summary: Python bindings for the libmagic API
Group: Development/Libraries
BuildRequires: python
Requires: %{name} = %{version}-%{release}

%description -n python-magic
This package contains the Python bindings to allow access to the
libmagic API. The libmagic library is also used by the familiar
file(1) command. 


%prep
%setup -q
%patch0 -p1
%patch1 -p1
autoreconf

%build
export GCC="no"
%configure

gmake -j3

cd python
%{__python} setup.py build 

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{_prefix}
gmake install DESTDIR=%{buildroot}
rm %{buildroot}%{_libdir}/libmagic.la

cd python
%{__python} setup.py install -O1 --skip-build --root %{buildroot}
%{__install} -d ${RPM_BUILD_ROOT}%{_datadir}/%{name}
%{__install} -D example.py %{buildroot}/%{_docdir}/python-magic-%{version}

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,bin)
%doc README COPYING ChangeLog
%{_bindir}/file
%{_libdir}/libmagic.so.*
%{_datadir}/misc/magic.mgc
%{_mandir}/man1/file.1
%{_mandir}/man4/magic.4

%files devel
%defattr(-,root,bin)
%{_includedir}/magic.h
%{_libdir}/libmagic.so
%{_libdir}/libmagic.a
%{_mandir}/man3/libmagic.3

%files -n python-magic
%defattr(-, root, root, -)
%doc python/README COPYING python/example.py
%{python_sitearch}/magic.so
%{python_sitearch}/*egg-info


%changelog
* Fri Sep 10 2010 Orcan Ogetbil <orcan@nbcs.rutgers.edu> - 5.04-2
- Include the magic.mgc file in the main RPM
* Tue Sep 07 2010 Russ Frank <rfranknj@nbcs.rutgers.edu> - 5.04-1
- Updated to version 5.04
- Added debugging flags
* Fri Dec 18 2009 Orcan Ogetbil <orcan@nbcs.rutgers.edu> - 5.00-2
- Build the python-magic subpackage.
* Mon Feb 09 2009 Brian Schubert <schubert@nbcs.rutgers.edu> - 5.00-1
- Updated to version 5.00
- Added separate devel package
* Thu Aug 28 2008 Brian Schubert <schubert@nbcs.rutgers.edu> - 4.25-1
- Added a patch needed to compile with Sun cc, bumped to version 4.25
* Thu Apr 10 2008 David Diffenbaugh <davediff@nbcs.rutger.edu> - 4.23-1
- bumped to latest version
* Wed Apr 09 2008 David Diffenbaugh <davediff@nbcs.rutgers.edu> - 4.21-1
- bumped to latest version, added LD env variable, to correct linking issues
