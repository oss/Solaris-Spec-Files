%include perl-header.spec

Summary: MLDMB Perl Module - store multi-level hash structure in single level tied hash

Name: perl-module-MLDBM
Version: 2.01
Release: 2
Group: System Environment/Base
Copyright: GPL/Artistic
Source: MLDBM-%{version}.tar.gz
BuildRoot: /var/tmp/%{name}-root
Requires: perl
BuildRequires: perl

%description
This module can serve as a transparent interface to any TIEHASH package that is required to 
store arbitrary perl data, including nested references. Thus, this module can be used for 
storing references and other arbitrary data within DBM databases.

It works by serializing the references in the hash into a single string. In the underlying 
TIEHASH package (usually a DBM database), it is this string that gets stored. When the value 
is fetched again, the string is deserialized to reconstruct the data structure into memory.

For historical and practical reasons, it requires the Data::Dumper package, available at any 
CPAN site. Data::Dumper gives you really nice-looking dumps of your data structures, in case 
you wish to look at them on the screen, and it was the only serializing engine before version 
2.00. However, as of version 2.00, you can use any of Data::Dumper, FreezeThaw or Storable to 
perform the underlying serialization, as hinted at by the SYNOPSIS overview above. Using 
Storable is usually much faster than the other methods. 

%prep

%setup -q -n MLDBM-%{version}

%build
perl Makefile.PL
make
make test

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{perl_prefix}
%{pmake_install}
%{clean_common_files}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,bin,bin)
%doc README Changes
%{site_perl}/MLDBM.pm
%{site_perl}/MLDBM/Serializer/*
%{site_perl_arch}/auto/MLDBM
%{perl_prefix}/man/man3/*
