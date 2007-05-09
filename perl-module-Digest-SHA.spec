%include perl-header.spec

Summary: SHA
Name: perl-module-Digest-SHA
Version: 5.44
Release: 1
Group: System Environment/Base
Copyright: Unknown
Source: Digest-SHA-%{version}.tar.gz
BuildRoot: /var/tmp/%{name}-root
Requires: perl = %{perl_version}
BuildRequires: perl = %{perl_version}

%description
This perl module implements Digest-SHA

%prep
%setup -q -n Digest-SHA-%{version}

%build
%{perl_binary} Makefile.PL
make

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{perl_prefix}
%{pmake_install}

%clean
rm -rf %{buildroot}

%files
%defattr(-,bin,bin)
/usr/perl5/bin/*
%{perl_prefix}/man/*
%{site_perl_arch}
%{site_perl}
