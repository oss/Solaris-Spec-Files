Summary: Time out execution of shell commands
Name: timeout
Version: 1.0
Release: 1
Group: System Environment/Base
Copyright: Rutgers (?)
Source: timeout-%{version}.tar.gz
BuildRoot: /var/tmp/%{name}-root

%description
Timeout is a simple command that will exit with a ETIMEDOUT if a
command does return in a given time.  The command will be executed
with 'sh -c' and killed when the timeout period expires.  Timeoutio is
a simple command that will exit with a ETIMEDOUT if a command does
produce any output in a given time.  The command will be executed with
'sh -c'.

  (from the manpages)

%prep
%setup -q -n timeout

%build
gcc -g -o timeout timeout.c
gcc -g -o timeoutio timeoutio.c

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/local/bin %{buildroot}/usr/local/man/man1
install -m 0755 timeout timeoutio     %{buildroot}/usr/local/bin
install -m 0644 timeout.1 timeoutio.1 %{buildroot}/usr/local/man/man1

%clean
rm -rf %{buildroot}

%files
%defattr(-, root, bin)
/usr/local/bin/*
/usr/local/man/*/*
