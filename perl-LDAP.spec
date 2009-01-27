%include perl-header.spec

Name:		perl-LDAP
Version:	0.39
Release:	1
Summary:        Perl client interface to LDAP servers

Group:		Development/Libraries
License:	GPL/Artistic
Source:		perl-ldap-%{version}.tar.gz
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires:	perl = %{perl_version}
BuildRequires:	perl-module-Convert-ASN1, perl-module-URI 
BuildRequires:	perl-module-Authen-SASL, perl-module-Digest-MD5 
BuildRequires:	perl-module-IO-Socket-SSL, perl-module-MIME-Base64

Requires:	perl = %{perl_version}
Requires:	perl-module-Convert-ASN1, perl-module-URI 
Requires:	perl-module-Authen-SASL, perl-module-Digest-MD5 
Requires:	perl-module-IO-Socket-SSL, perl-module-MIME-Base64

%description
Net::LDAP is a collection of modules that implements a LDAP 
services API for Perl programs. The module may be used to 
search directories or perform maintenance functions such as 
adding, deleting or modifying entries.

%prep
%setup -q -n perl-ldap-%{version}

%build
%{perl_binary} Makefile.PL < /dev/null
make
make test

%install
rm -rf %{buildroot}
%{pmake_install}
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -type f -name perllocal.pod -exec rm -f {} ';'
find %{buildroot} -type d -depth -exec rmdir {} 2>/dev/null ';'

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc Changes CREDITS
%doc contrib/ bin/
%{site_perl}/Bundle/
%{site_perl}/LWP/
%{site_perl}/Net/
%{perl_prefix}/man/man3/*

%changelog
* Tue Jan 27 2009 Brian Schubert <schubert@nbcs.rutgers.edu> - 0.39-1
- Initial RU-Solaris build

