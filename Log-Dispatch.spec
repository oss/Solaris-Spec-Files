%include perl-header.spec

Summary: Log-Dispatch

Name: perl-module-Log-Dispatch
Version: 2.06
Release: 1
Group: System Environment/Base
Copyright: GPL/Artistic
Source: Log-Dispatch-%{version}.tar.gz
BuildRoot: /var/tmp/%{name}-root
Requires: perl
BuildRequires: perl
Requires: perl-module-Module-Build >= 0.18-1 
BuildRequires: perl-module-Module-Build >= 0.18-1

%description
Log::Dispatch is a suite of OO modules for logging messages to
multiple outputs, each of which can have a minimum and maximum log
level.  It is designed to be easily subclassed, both for creating a
new dispatcher object and particularly for creating new outputs.

It also allows both global (dispatcher level) and local (logging
object) message formatting callbacks which allows greater flexibility
and should reduce the need for subclassing.

Subclassing is only needed to send a message to a different output,
not to change the message format.

Please see the Log::Dispatch documentation for more details.

%prep

%setup -q -n Log-Dispatch-%{version}

%build
%{pbuild}

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{perl_prefix}
%{pbuild_install}
rm -f `/usr/local/gnu/bin/find $RPM_BUILD_ROOT -iname perllocal.pod`
rm -f $RPM_BUILD_ROOT/%{global_perl_arch}/perllocal.pod

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,bin,bin)
%doc README Changes LICENSE
%{site_perl}/Log/*
