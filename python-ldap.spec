%{!?python_sitelib: %define python_sitelib %(%{__python} -c "from distutils.sysconfig import get_python_lib; print get_python_lib()")}

Summary:       python LDAP bindings
Name:          python-ldap
Version:       2.3.10
Release:       1
Group:         Development/Libraries
Source0:       http://prdownloads.sf.net/python-ldap/python-ldap-%{version}.tar.gz
Source1:       setup.cfg
License:       Python-style
BuildRoot:     %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
URL:           http://python-ldap.sf.net/

BuildRequires: openldap-devel >= 2.4 cyrus-sasl python >= 2.6 openssl > 0.9.8 openssl < 0.9.9
Requires:      openldap-lib >= 2.4 python >= 2.6 cyrus-sasl openssl > 0.9.8 openssl < 0.9.9



%description
This module provides access to the LDAP (C language) library.

%prep
%setup -q
cp %{SOURCE1} setup.cfg

%build
PATH="/opt/SUNWspro/bin:/usr/ccs/bin:${PATH}"
export PATH

python setup.py build

%clean
rm -rf %{buildroot}

%install
rm -rf %{buildroot}

PYTHONPATH=%{buildroot}%{python_sitelib}
export PYTHONPATH

python setup.py install --optimize=2 --root=%{buildroot}

%files
%defattr(644,root,bin,755)
%doc CHANGES README LICENCE TODO Demo/
%{python_sitelib}/*.py*
%{python_sitelib}/*.so*
%{python_sitelib}/ldap


%changelog
* Fri Dec 04 2009 Orcan Ogetbil <orcan@nbcs.rutgers.edu> - 2.3.10-1
- Update to 2.3.10
- Build against python 2.6

* Wed Oct 29 2008 Brian Schubert <schubert@nbcs.rutgers.edu> - 2.3.5-1
- Built against openldap 2.4 and updated to version 2.3.5
