Summary: Process monitoring tool
Name: keep-alive
Version: 0.1
Release: 2
Group: System Environment/Base
Copyright: Rutgers
Source: keep-alive-%{version}.tar.gz
BuildRoot: /var/tmp/%{name}-root

%description
Keep-alive is used to to monitor and restart a process.

%prep
%setup -q -n files

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT
find . -print | cpio -pdm $RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(700,root,other)
/usr/local/sbin/keep-alive