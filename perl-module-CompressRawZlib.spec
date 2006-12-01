%include perl-header.spec

Summary: Compress-Raw-Zlib perl module
Name: perl-module-CompressRawZlib
Version: 2.001
Release: 1
Group: System Environment/Base
Copyright: Unknown
Source: Compress-Raw-Zlib-%{version}.tar.gz
BuildRoot: /var/tmp/%{name}-root
Requires: perl = %{perl_version}
BuildRequires: perl = %{perl_version}

%description
Yet another allegedly useful module from CPAN.

%prep

%setup -n Compress-Raw-Zlib-%{version}

%build
CC=/opt/SUNWspro/bin/cc
export CC
perl Makefile.PL
make
make test

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{perl_prefix}
%{pmake_install}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,bin,bin)
%doc README Changes
%{site_perl_arch}/*
%{perl_prefix}/man/man3/*
