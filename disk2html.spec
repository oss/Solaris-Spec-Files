%{!?python_sitelib: %global python_sitelib %(%{__python} -c "from distutils.sysconfig import get_python_lib; print get_python_lib()")}

Name:           disk2html
Version:        0.2
Release:        3%{?dist}
Summary:        Convert disk input to html output
Group:          Applications/System
License:        GPLv2+
URL:            http://centos.rutgers.edu
Source0:        %{name}-%{version}.tar.bz2
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
#BuildArch:      noarch
BuildRequires:  python >= 2.6
Requires:       python >= 2.6

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
* Wed Dec 02 2009 Orcan Ogetbil <orcan@nbcs.rutgers.edu> - 0.2-3
- I will not publish unsigned packages again

* Mon Nov 30 2009 Orcan Ogetbil <orcan@nbcs.rutgers.edu> - 0.2-2
- Rebuild against python 2.6

* Mon Nov 02 2009 Orcan Ogetbil <orcan@nbcs.rutgers.edu> - 0.2-1
- Update to 0.2

* Mon Nov 02 2009 Orcan Ogetbil <orcan@nbcs.rutgers.edu> - 0.1-2
- Comment out BuildArch: noarch

* Fri Oct 30 2009 Orcan Ogetbil <orcan@nbcs.rutgers.edu> - 0.1-1
- Initial release

