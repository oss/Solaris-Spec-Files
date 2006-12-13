%include perl-header.spec

Summary: List::Util and Scalar::Util perl modules
Name: perl-module-Scalar-List-Util
Version: 1.19
Release: 1
Group: Libraries/Perl
Copyright: GPL/Artistic
Source: Scalar-List-Utils-%{version}.tar.gz
BuildRoot: /var/tmp/%{name}-root
Requires: perl = %{perl_version}
BuildRequires: perl = %{perl_version}


%description
This package contains a selection of subroutines that people have expressed would be nice to have in the perl core, but the usage would not really be high enough to warrant the use of a keyword, and the size so small such that being individual extensions would be wasteful.

%prep
%setup -q -n Scalar-List-Utils-%{version}

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
%{perl_prefix}/man/man3/*
%doc Change* README
%dir %{site_perl_arch}/List
%{site_perl_arch}/List/*.pm
%dir %{site_perl_arch}/Scalar
%{site_perl_arch}/Scalar/*.pm
%dir %{site_perl_arch}/auto/List
%dir %{site_perl_arch}/auto/List/Util
%attr(755,root,root) %{site_perl_arch}/auto/List/Util/*.so
/usr/perl5/site_perl/5.6.1/sun4-solaris-64int/auto/List/Util/.packlist
%{site_perl_arch}/auto/List/Util/*.bs
