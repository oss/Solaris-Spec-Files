Summary:   sleephost, naphost, host based timedelay
Name:      sleephost
Version:   2.0
Release:   1
Group:     System Environment/Base
License:   Public Domain
Source:    sleephost-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

%description
sleephost, sleep the host based on machine IP
naphost, sleep the host for a short period based on machine IP

%prep
%setup -q

%build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{_sbindir}
cp -pr sleephost %{buildroot}%{_sbindir}
cp -pr naphost %{buildroot}%{_sbindir}

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc ChangeLog
%{_sbindir}/sleephost
%{_sbindir}/naphost

%changelog
* Fri Nov 19 2010 Orcan Ogetbil <orcan@nbcs.rutgers.edu> - 2.0
- Update to 2.0. Includes naphost
