%include perl-header.spec

Summary: Perl interface to the PAM library
Name: perl-module-Authen-PAM
Version: 0.10
Release: 3
Group: System Environment/Base
Copyright: GPL/Artistic
Source: Authen-PAM-%{version}.tar.gz
BuildRoot: /var/tmp/%{name}-root
Requires: perl = %{perl_version}
BuildRequires: perl = %{perl_version}

%description
The Authen::PAM module provides a Perl interface to the PAM
library. The only difference with the standard PAM interface is that
instead of passing a pam_conv struct which has an additional context
parameter appdata_ptr, you must only give an address to a conversation
function written in Perl (see below).  If you use the 3 argument
version of pam_start then a default conversation function is used
(Authen::PAM::pam_default_conv).

%prep
%setup -q -n Authen-PAM-%{version}

%build
perl Makefile.PL
make

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{perl_prefix}
%{pmake_install}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,bin,bin)
%doc README Changes
%{site_perl_arch}/auto/Authen/PAM
%{site_perl_arch}/Authen/*
%{perl_prefix}/man/man3/*
