Summary: Relevance logging tool
Name: relevance
Version: 1.0
Release: 1
Group: System Environment/Base
Copyright: Rutgers
Source: %{name}-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-root

%description
Relevance logging tool

%prep
%setup -q -n relevance

%build
rm loginlog
cc -o loginlog loginlog.c

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/local/sbin
install loginlog %{buildroot}/usr/local/sbin/relevance

%clean
rm -rf %{buildroot}

%files
%attr(0700, root, bin) /usr/local/sbin/relevance
