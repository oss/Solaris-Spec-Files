%define __python /usr/local/bin/python
%{!?python_sitelib_platform: %define python_sitelib_platform %(%{__python} -c "from distutils.sysconfig import get_python_lib; print get_python_lib(1)")}

Summary:	A fast metadata parser for yum
Name:		yum-metadata-parser
Version:	1.1.2
Release:	2
Source0:	%{name}-%{version}.tar.gz
License:	GPL
Group:		Development/Libraries
URL:		http://devel.linux.duke.edu/cgi-bin/viewcvs.cgi/yum-metadata-parser/
Requires:	yum >= 3.2.5
BuildRequires:	python, glib2-devel, libxml2-devel, sqlite-devel, pkgconfig
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root

%description
Fast metadata parser for yum implemented in C.

%prep
%setup -q

%build
PATH="/opt/SUNWspro/bin:${PATH}" \
CC="cc" CXX="CC" CPPFLAGS="-I/usr/local/include `pkg-config --cflags glib-2.0`" \
LD="/usr/ccs/bin/ld" \
LDFLAGS="-L/usr/local/lib -R/usr/local/lib `pkg-config --libs glib-2.0`"
export PATH CC CXX CPPFLAGS LD LDFLAGS

%{__python} setup.py build

%install
%{__python} setup.py install -O1 --root=%{buildroot}

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-,root,root)
%doc README AUTHORS ChangeLog
%{python_sitelib_platform}/_sqlitecache.so
%{python_sitelib_platform}/sqlitecachec.py
%{python_sitelib_platform}/sqlitecachec.pyc
%{python_sitelib_platform}/sqlitecachec.pyo

%changelog
* Fri Nov 06 2009 Orcan Ogetbil <orcan@nbcs.rutgers.edu> - 1.1.2-2
- Build against python 2.6

* Thu Sep 27 2007 David Lee Halik <dhalik@nbcs.rutgers.edu> - 1.1.2-1
- Initial build
