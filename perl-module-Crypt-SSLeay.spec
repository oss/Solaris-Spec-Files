%include perl-header.spec

Summary: OpenSSL glue that provides LWP https support.

%define module_name Crypt-SSLeay

Name: perl-module-%{module_name}
Version: 0.58
Release: 1.ru
Group: System Environment/Base
License: GPL/Artistic
Source: %{module_name}-%{version}.tar.gz
BuildRoot: /var/tmp/%{name}-root
Requires: perl
BuildRequires: perl
Requires: perl-module-MIME-Base64

%description
This Perl module provides support for the HTTPS protocol under LWP, to allow an LWP::UserAgent object to perform GET, HEAD and POST requests. Please see LWP for more information on POST requests.

The Crypt::SSLeay package provides Net::SSL, which is loaded by LWP::Protocol::https for https requests and provides the necessary SSL glue.

%prep

%setup -q -n %{module_name}-%{version}

%build
perl Makefile.PL
make


%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{perl_prefix}
%{pmake_install}

#Remove the packlist file
#rm -f /usr/perl5/site_perl/%{perl_version}/%{perl_arch}/auto/REST/Google/Apps/EmailSettings/.packlist
find $RPM_BUILD_ROOT -name .packlist | xargs rm
find $RPM_BUILD_ROOT -name perllocal.pod | xargs rm

%clean
rm -rf $RPM_BUILD_ROOT



%files
%defattr(-,bin,bin)
%doc Changes MANIFEST MANIFEST.SKIP
%{site_perl_arch}/Crypt/SSLeay.pm
%{site_perl_arch}/Crypt/SSLeay/CTX.pm
%{site_perl_arch}/Crypt/SSLeay/Conn.pm
%{site_perl_arch}/Crypt/SSLeay/Err.pm
%{site_perl_arch}/Crypt/SSLeay/MainContext.pm
%{site_perl_arch}/Crypt/SSLeay/X509.pm
%{site_perl_arch}/Net/SSL.pm
%{site_perl_arch}/auto/Crypt/SSLeay/SSLeay.bs
%{site_perl_arch}/auto/Crypt/SSLeay/SSLeay.so
%{perl_prefix}/man/man3/*

%changelog
* Fri Mar 31 2011 Vaibhav Verma <vverna@nbcs.rutgers.edu> 0.58-1.ru 
- Initial Rutgers build
