Summary: Sun's office suite
Name: staroffice
Version: 5.2
Release: 2
Group: Applications/Productivity
Copyright: Sun
Source: %{name}-%{version}.tar.gz
BuildRoot: /var/tmp/%{name}-root
%description
Staroffice is a collection of office programs for Solaris.

%prep
%setup -q -n opt

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/opt/office52
find . | cpio -pdmuv $RPM_BUILD_ROOT/opt

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
/opt/office52
