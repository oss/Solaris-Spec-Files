%include perl-header.spec

Summary: Authen SASL perm module
Name: perl-module-Authen-SASL
Version: 2.09
Release: 2
Group: System Environments/Base
License: Perl (Artistic and GPL)
Source: Authen-SASL-%{version}.tar.gz
BuildRoot: /var/tmp/%{name}-root
#Requires:
#BuildRequires:

%description
SASL Authentication framework in perl

%prep

%setup -qn Authen-SASL-%{version}

%build
perl Makefile.PL
make
make test

%install
mkdir -p $RPM_BUILD_ROOT%{perl_prefix}
%{pmake_install}
rm $RPM_BUILD_ROOT%{global_perl_arch}/perllocal.pod

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,bin,bin)
%{site_perl}/*
%{perl_prefix}/man/man3/*
