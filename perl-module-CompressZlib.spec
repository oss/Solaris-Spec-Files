%include perl-header.spec

Summary: Compress-Zlib perl module
Name: perl-module-CompressZlib
Version: 2.001
Release: 2
Group: System Environment/Base
Copyright: Unknown
Source: Compress-Zlib-%{version}.tar.gz
BuildRoot: /var/tmp/%{name}-root
Requires: perl = %{perl_version}, perl-module-CompressRawZlib >= 2.001, perl-module-IO-Compress-Base >= 2.001, perl-module-IO-Compress-Zlib >= 2.001, perl-module-Scalar-List-Util
BuildRequires: perl = %{perl_version}, perl-module-CompressRawZlib >= 2.001, perl-module-IO-Compress-Base >= 2.001, perl-module-IO-Compress-Zlib >= 2.001, perl-module-Scalar-List-Util
%description
Yet another allegedly useful module from CPAN.

%prep

%setup -n Compress-Zlib-%{version}

%build
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
%{site_perl}/Compress/*
%{site_perl}/auto/Compress/*
%{site_perl_arch}/*
%{perl_prefix}/man/man3/*
