%define perl_version   5.6.0
%define perl_arch      sun4-solaris-thread-multi
%define site_perl      /usr/local/lib/perl5/site_perl/%{perl_version}
%define site_perl_arch %{site_perl}/%{perl_arch}

Summary: Perl interface to the DNS resolver
Name: perl-module-Net-DNS
Version: 0.12
Release: 2
Group: System Environment/Base
Copyright: GPL/Artistic
Source: Net-DNS-%{version}.tar.gz
BuildRoot: /var/tmp/%{name}-root
Requires: perl = %{perl_version}
BuildRequires: perl = %{perl_version}

%description
Net::DNS is a collection of Perl modules that act as a Domain Name
System (DNS) resolver.  It allows the programmer to perform DNS
queries that are beyond the capabilities of `gethostbyname' and
`gethostbyaddr'.

%prep
%setup -q -n Net-DNS-%{version}

%build
perl Makefile.PL
make
make test

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/local
make install PREFIX=$RPM_BUILD_ROOT/usr/local
x=$RPM_BUILD_ROOT%{site_perl_arch}/auto/Net/DNS/.packlist
mv $x $x.tmp
sed "s#$RPM_BUILD_ROOT##" < $x.tmp > $x
rm $x.tmp

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,bin,bin)
%doc README Changes
%{site_perl}/Net/DNS
%{site_perl_arch}/auto/Net/DNS
/usr/local/man/man3/*
