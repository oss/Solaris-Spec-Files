%include perl-header-unstable.spec

Summary: parse directory listing

%define module_name File-Listing

Name: perl-module-%{module_name}
Version: 6.02
Release: 1.ru
Group: System Environment/Base
License: GPL/Artistic
Source: %{module_name}-%{version}.tar.gz
BuildRoot: /var/tmp/%{name}-root
Requires: perl
BuildRequires: perl >= 5.8.8
BuildRequires: perl-devel >= 5.8.8
Requires: perl-module-HTTP-Date >= 6

%description
This module exports a single function called parse_dir(), which can be used to parse directory listings.

The first parameter to parse_dir() is the directory listing to parse. It can be a scalar, a reference to an array of directory lines or a glob representing a filehandle to read the directory listing from.

The second parameter is the time zone to use when parsing time stamps in the listing. If this value is undefined, then the local time zone is assumed.

The third parameter is the type of listing to assume. Currently supported formats are 'unix', 'apache' and 'dosftp'. The default value 'unix'. Ideally, the listing type should be determined automatically.

The fourth parameter specifies how unparseable lines should be treated. Values can be 'ignore', 'warn' or a code reference. Warn means that the perl warn() function will be called. If a code reference is passed, then this routine will be called and the return value from it will be incorporated in the listing. The default is 'ignore'.

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
find $RPM_BUILD_ROOT -name *.pod | xargs rm

%clean
rm -rf $RPM_BUILD_ROOT



%files
%defattr(-,bin,bin)
%doc README Changes

%{site_perl}/File/Listing.pm

%changelog
* Fri Mar 31 2011 Vaibhav Verma <vverna@nbcs.rutgers.edu> 6.02-1.ru 
- Initial Rutgers build
