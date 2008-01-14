%include perl-header.spec

Summary:	Compress-Zlib perl module
Name:		perl-module-CompressZlib
Version:	2.008
Release:	1
Group:		System Environment/Base
Copyright:	GPL
Source:		Compress-Zlib-%{version}.tar.gz
Packager:	David Diffenbaugh <davediff@nbcs.rutgers.edu>
BuildRoot:	/var/tmp/%{name}-root
Requires:	perl = %{perl_version}, perl-module-CompressRawZlib >= 2.008, perl-module-IO-Compress-Base >= 2.008, perl-module-IO-Compress-Zlib >= 2.008, perl-module-Scalar-List-Util
BuildRequires:	perl = %{perl_version}, perl-module-CompressRawZlib >= 2.008, perl-module-IO-Compress-Base >= 2.008, perl-module-IO-Compress-Zlib >= 2.008, perl-module-Scalar-List-Util
%description
Yet another allegedly useful module from CPAN.

%prep

%setup -n Compress-Zlib-%{version}

%build
perl Makefile.PL
gmake
gmake test

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{perl_prefix}
%{pmake_install}
rm %{buildroot}/%{global_perl_arch}/perllocal.pod

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,bin,bin)
%doc README Changes
%{site_perl}/Compress/*
%{site_perl}/auto/Compress/*
%{site_perl_arch}/*
%{perl_prefix}/man/man3/*

%changelog
* Fri Jan 11 2008 David Diffenbaugh <davediff@nbcs.rutgers.edu> - 2.008-1
- Updated to latest version
