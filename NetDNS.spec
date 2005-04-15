%include perl-header.spec

Summary: Perl interface to the DNS resolver
Name: perl-module-Net-DNS
Version: 0.49
Release: 1ru
Group: System Environment/Base
Copyright: GPL/Artistic
Source: Net-DNS-%{version}.tar.gz
BuildRoot: /var/tmp/%{name}-root
Requires: perl = %{perl_version}
BuildRequires: perl = %{perl_version}
Obsoletes: perl-Net-DNS

%description
Net::DNS is a collection of Perl modules that act as a Domain Name
System (DNS) resolver.  It allows the programmer to perform DNS
queries that are beyond the capabilities of `gethostbyname' and
`gethostbyaddr'.

%prep
%setup -q -n Net-DNS-%{version}

%build
perl Makefile.PL<<EOF


EOF
make
#make test

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{perl_prefix}
%{pmake_install}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,bin,bin)
%doc README Changes
%{site_perl}/*
%{site_perl_arch}/*
%{perl_prefix}/*
