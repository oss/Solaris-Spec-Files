%include perl-header.spec

Summary: DES encryption support for Perl
Name: perl-module-Des
Version: a2
Release: 2
Group: System Environment/Base
Copyright: GPL/Artistic
Source: Des-%{version}.tar.gz
BuildRoot: /var/tmp/%{name}-root
Requires: perl = %{perl_version}
Requires: openssl
BuildRequires: perl = %{perl_version}
BuildRequires: openssl

%description

%prep
%setup -q -n Des-%{version}

%build
perl Makefile.PL
make
make test

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{perl_prefix}
%{pmake_install}

%clean
rm -rf %{buildroot}

%files
%defattr(-,bin,bin)
%doc README
%{site_perl_arch}/auto/Des
%{site_perl_arch}/Des*
%{perl_prefix}/man/*/*


