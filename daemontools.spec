Summary: D. J. Bernstein's unix utilities
Name: daemontools
Version: 0.70
Release: 2
Group: Applications/Productivity
Copyright: BSD
Source: %{name}-%{version}.tar.gz
BuildRoot: /var/tmp/%{name}-root

%description
Daemontools is a collection of system administration tools.

%prep
%setup -q
# conf-home has /usr/local but no programs depend on this at build time.
perl -i -p -e "s(/usr/local)($RPM_BUILD_ROOT/usr/local)" conf-home

%build

make

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/local
make setup check

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,bin,bin)
%doc README TODO VERSION CHANGES
/usr/local/bin/*
