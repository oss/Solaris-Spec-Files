Name: Pyrex
Version: 0.9.3.1
Release: 2
Copyright: GPL
Group: Applications/Python
Summary: Pyrex
Packager: Rutgers University
Source: %{name}-%{version}.tar.gz
BuildRoot: /var/tmp/%{name}-root
Requires: python >= 2.4

%description
Pyrex lets you write code that mixes Python and C data types any way you 
want, and compiles it into a C extension for Python. 

%prep
%setup -q

%build

%install
rm -rf $RPM_BUILD_ROOT

mkdir -p $RPM_BUILD_ROOT/usr/local
python setup.py install --prefix=$RPM_BUILD_ROOT/usr/local

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,bin,bin)
/usr/local/*
