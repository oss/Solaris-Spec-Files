Summary: Process viewer
Name: top
Version: 3.5beta9
Release: 3
Group: System Environment/Base
License: Freely distributable
Source: %{name}-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-root

%description
"top" is a program that will give continual reports about the state of
the system, including a list of the top cpu using processes.  Version
3 of "top" has three primary design goals: provide an accurate
snapshot of the system and process state, not be one of the top
processes itself, be as portable as possible.

%prep
%setup -q

%build
/bin/echo "sunos5\n\n\n\n/opt/SUNWspro/bin/cc\n\n\n\n-1\n\n5\n\n\n\n\n" | ./Configure
make

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/local/man/man1
mkdir %{buildroot}/usr/local/bin
install -m 0755 top %{buildroot}/usr/local/bin/top
install -m 0444 top.1 %{buildroot}/usr/local/man/man1/top.1

%clean
rm -rf %{buildroot}

%files
%defattr(-, root, bin)
%doc ADVERTISEMENT DISCLAIMER FAQ INSTALL README SYNOPSIS
/usr/local/bin/top
/usr/local/man/man1/top.1
