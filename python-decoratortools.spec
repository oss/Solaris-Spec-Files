%{!?python_sitelib: %define python_sitelib %(%{__python} -c "from distutils.sysconfig import get_python_lib; print get_python_lib()")}
%{!?pyver: %define pyver %(%{__python} -c "import sys ; print sys.version[:3]")}

%define module DecoratorTools

Name:           python-decoratortools
Version:        1.7
Release:        2.ru
Summary:        Use class and function decorators -- even in Python 2.3
Group:          Development/Languages
License:        Python or ZPLv2.1
URL:            http://cheeseshop.python.org/pypi/DecoratorTools
Source0:        http://cheeseshop.python.org/packages/source/D/DecoratorTools/%{module}-%{version}.zip
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires:  python-setuptools

%description
Want to use decorators, but still need to support Python 2.3? Wish you could
have class decorators, decorate arbitrary assignments, or match decorated
function signatures to their original functions? Then you need "DecoratorTools"


%prep
%setup -q -n %{module}-%{version}


%build
%{__python} setup.py build


%install
rm -rf %{buildroot}
%{__python} setup.py install --skip-build --root %{buildroot}


%clean
rm -rf %{buildroot}


%files
%defattr(-,root,root,-)
%doc README.txt
%{python_sitelib}/peak
%{python_sitelib}/%{module}-%{version}-py%{pyver}.egg-info
%{python_sitelib}/%{module}-%{version}-py%{pyver}-nspkg.pth


%changelog
* Mon Nov 09 2009 Orcan Ogetbil <orcan@nbcs.rutgers.edu> - 1.7-2
- Solaris port
- Build against python 2.6

* Thu Feb 28 2008 Luke Macken <lmacken@redhat.com> - 1.7-1
- Update to 1.7

* Tue Nov 27 2007 Luke Macken <lmacken@redhat.com> - 1.6-1
- 1.6

* Sat Sep 01 2007 Toshio Kuratomi <a.badger@gmail.com> - 1.5-2
- Verify that .pth files are correct.
- Update license tag for new guidelines.
- Update setuptools BR for changes in rawhide.

* Tue Aug 21 2007 Luke Macken <lmacken@redhat.com> - 1.5-1
- 1.5

* Tue May  8 2007 Luke Macken <lmacken@redhat.com>  - 1.4-2
- Own the peak namespace, for now.

* Thu May  3 2007 Luke Macken <lmacken@redhat.com> - 1.4-1
- Initial creation
