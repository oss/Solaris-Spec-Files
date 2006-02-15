%define name nagios-plugins
%define version 1.4.2
%define release 2
%define prefix  /usr/local 
%define nppath  %{prefix}/%{name}

Summary: Host/service/network monitoring program plugins for Nagios 
Name: %{name}
Version: %{version}
Release: %{release}
Copyright: GPL
Group: Applications/System
Source0: %{name}-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-root
Requires: nagios coreutils gmp openssl openldap-client openldap-lib cyrus-sasl


%description
Nagios is a program that will monitor hosts and services on your
network, and to email or page you when a problem arises or is
resolved. Nagios runs on a unix server as a background or daemon
process, intermittently running checks on various services that you
specify. The actual service checks are performed by separate "plugin"
programs which return the status of the checks to Nagios.

This package contains the basic plugins necessary for use with the
Nagios package.  This package should install cleanly on almost any
RPM-based system.


%prep
%setup -n %{name}-%{version}


%build
LD_RUN_PATH=/usr/local/lib
PATH_TO_FPING=/usr/local/sbin/fping 
LDFLAGS="-L/usr/local/lib"
CPPFLAGS="-I/usr/local/include"
export LD_RUN_PATH PATH_TO_FPING LDFLAGS CPPFLAGS
./configure --with-df-command="/usr/local/gnu/bin/df -Pkh" --with-openssl="/usr/local/ssl" --prefix=%{nppath}
make all


%install
PATH="/usr/local/gnu/bin:/usr/local/bin:$PATH"
export PATH
make DESTDIR=%{buildroot} AM_INSTALL_PROGRAM_FLAGS="" INSTALL_OPTS="" install
mkdir -p %{buildroot}%{nppath}/etc
install -m 0644 command.cfg %{buildroot}%{nppath}/etc/command.cfg-example


%clean
rm -rf %{buildroot}


%files
%defattr(-,nagios,nagios)
%doc AUTHORS COPYING ChangeLog INSTALL NEWS README REQUIREMENTS 
%{nppath}/libexec
%{nppath}/lib
%{nppath}/share
%config(noreplace)%{nppath}/etc/*


%changelog
* Wed Feb 15 2005 Jonathan Kaczynski <jmkacz@oss.rutgers.edu> - 1.4.2-2
- Changed the install directory from /usr/local/nagios to /usr/local/nagios-plugins
