Summary: Script to check file permissions
Name: check-files
Version: 1.0
Release: 2
Group: System Environment/Base
Copyright: Rutgers
Source: check-files.tar.gz
BuildRoot: /var/tmp/%{name}-root
BuildRequires: rcs

%description
Check-files is a perl script that checks files' permissions, owners,
and groups against what you specify in a configuration file.  It can
also correct the differences.

%prep
%setup -q -n check-files

%build
rm -f check-files check-files.config.example
co check-files
co check-files.config.example

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/local/sbin
install -m 0755 check-files $RPM_BUILD_ROOT/usr/local/sbin/check-files

%files
%defattr(-, root, other)
%doc check-files.config.example
/usr/local/sbin/check-files
