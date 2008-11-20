Summary: python LDAP bindings
Name: python-ldap
Version: 2.3.5
Release: 1
Group: Development/Libraries
Source0: http://prdownloads.sf.net/python-ldap/python-ldap-%{version}.tar.gz
Source1: setup.cfg
License: Python-style
BuildRoot: %{_tmppath}/%{name}-root
URL: http://python-ldap.sf.net/
Prefix: %{_prefix}
BuildRequires: openldap-devel >= 2.4 cyrus-sasl python >= 2.4 python < 2.5 openssl > 0.9.8 openssl < 0.9.9
Requires: openldap-lib >= 2.4 python cyrus-sasl openssl > 0.9.8 openssl < 0.9.9

%define py_sitedir /usr/local/lib/python2.4/site-packages

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

PYTHONPATH=%{buildroot}%{py_sitedir}
export PYTHONPATH

python setup.py install --optimize=2 --root=%{buildroot}

%files
%defattr(644,root,bin,755)
%doc CHANGES README INSTALL TODO Demo/
%{py_sitedir}/*.py*
%{py_sitedir}/*.so*
%dir %{py_sitedir}/ldap
%{py_sitedir}/ldap/*

%changelog
* Wed Oct 29 2008 Brian Schubert <schubert@nbcs.rutgers.edu> - 2.3.5-1
- Built against openldap 2.4 and updated to version 2.3.5
