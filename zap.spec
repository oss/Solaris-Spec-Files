Summary: Interactively kill processes
Name: zap
Version: 3.0
Release: 1
Group: System Environment/Base
Copyright: Rutgers
Source: %{name}-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-root
Requires: perl

%description
Zap is a self-contained perl script that lets you interactively kill
processes from groups that you specify.

%prep
%setup -q 

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}
find . -print | cpio -pdm %{buildroot}

%clean
rm -rf %{buildroot}

%files
%attr(0755, root, bin) /usr/local/bin/zap
%attr(0644, root, bin) /usr/local/man/man1/zap.1
