%{!?python_sitelib: %global python_sitelib %(%{__python} -c "from distutils.sysconfig import get_python_lib; print get_python_lib()")}

Name:           disk2html
Version:        0.1
Release:        1%{?dist}
Summary:        Convert disk input to html output
Group:          Applications/System
License:        GPLv2+
URL:            http://centos.rutgers.edu
Source0:        %{name}-%{version}.tar.bz2
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:      noarch
BuildRequires:  python >= 2.4
Requires:       python >= 2.4

%description
This program converts disk input into html output

%prep
%setup -q

%build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{python_sitelib}

cp -pR %{name} %{buildroot}%{_bindir}
cp -pR pyHTML.py %{buildroot}%{python_sitelib}

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc COPYING ChangeLog
%{python_sitelib}/pyHTML.py
%{_bindir}/%{name}

%changelog
* Thu Jun 11 2009 Orcan Ogetbil <orcan@ncbs.rutgers.edu> - 0.1-1
- Initial release

