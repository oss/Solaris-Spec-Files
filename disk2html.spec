%{!?python_sitelib: %global python_sitelib %(%{__python} -c "from distutils.sysconfig import get_python_lib; print get_python_lib()")}

Name:           disk2html
Version:        0.3.13
Release:        1%{?dist}
Summary:        Convert disk input to html output
Group:          Applications/System
License:        GPLv2+
URL:            http://cvs.rutgers.edu/cgi-bin/viewvc.cgi/trunk/orcan/disk2html/
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
* Wed Jan 23 2013 Josh Matthews <jmatth@nbcs.rutgers.edu> - 0.3.13-1
- Update to 0.3.13

* Wed Jan 17 2013 Josh Matthews <jmatth@nbcs.rutgers.edu> - 0.3.12-1
- Update to 0.3.12

* Wed Jan 16 2013 Josh Matthews <jmatth@nbcs.rutgers.edu> - 0.3.11-1
- Update to 0.3.11

* Thu Aug 16 2010 Orcan Ogetbil <orcan@nbcs.rutgers.edu> - 0.3.10-1
- Update to 0.3.10

* Tue Aug 03 2010 Orcan Ogetbil <orcan@nbcs.rutgers.edu> - 0.3.9-1
- Update to 0.3.9

* Thu Jul 22 2010 Orcan Ogetbil <orcan@nbcs.rutgers.edu> - 0.3.8.1-1
- Update to 0.3.8.1

* Wed Jul 21 2010 Orcan Ogetbil <orcan@nbcs.rutgers.edu> - 0.3.8-1
- Update to 0.3.8

* Wed Jul 21 2010 Orcan Ogetbil <orcan@nbcs.rutgers.edu> - 0.3.7-1
- Update to 0.3.7

* Wed Jun 16 2010 Orcan Ogetbil <orcan@nbcs.rutgers.edu> - 0.3.6-1
- Update to 0.3.6

* Tue May 25 2010 Orcan Ogetbil <orcan@nbcs.rutgers.edu> - 0.3.5-1
- Update to 0.3.5

* Mon May 24 2010 Orcan Ogetbil <orcan@nbcs.rutgers.edu> - 0.3.4-1
- Update to 0.3.4

* Thu May 20 2010 Orcan Ogetbil <orcan@nbcs.rutgers.edu> - 0.3.3-1
- Update to 0.3.3

* Fri May 07 2010 Orcan Ogetbil <orcan@nbcs.rutgers.edu> - 0.3.2-1
- Update to 0.3.2

* Wed Mar 03 2010 Orcan Ogetbil <orcan@nbcs.rutgers.edu> - 0.3.1-1
- Update to 0.3.1

* Mon Feb 15 2010 Orcan Ogetbil <orcan@nbcs.rutgers.edu> - 0.3-1
- Update to 0.3

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

