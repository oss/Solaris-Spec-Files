%include perl-header.spec
%define module_name Test-Simple

Summary: 	Test::Simple, Test::Builder and Test::More perl modules
Name: 		perl-module-%{module_name}
Version: 	0.74
Release: 	1
Group: 		System Environment/Base
License	: 	Perl (Artistic and GPL-2)
Source: 	%{module_name}-%{version}.tar.gz
URL: 		http://search.cpan.org/~mschwern/%{module_name}-%{version}/lib/Test/Simple.pm
BuildRoot: 	%{_tmppath}/%{name}-root
Requires: 	perl = %{perl_version}, perl-module-ExtUtils-MakeMaker
BuildRequires: 	perl = %{perl_version}, perl-module-ExtUtils-MakeMaker, perl-module-Test-Harness >= 2.03

%description
Test writing utilities

%prep
%setup -qn %{module_name}-%{version}

%build
# @INC has Sun's Test-Harness at a higher precedence
PERL5LIB="/usr/perl5/5.6.1/:$PERL5LIB"
export PERL5LIB
%{perl_binary} Makefile.PL
gmake
gmake test

%install
PERL5LIB="/usr/perl5/5.6.1/:$PERL5LIB"
export PERL5LIB
rm -rf %{buildroot}
mkdir -p %{buildroot}%{perl_prefix}
%{pmake_install}
rm -f `/usr/local/gnu/bin/find %{buildroot} -iname perllocal.pod`
rm -f %{buildroot}/%{global_perl_arch}/perllocal.pod

%clean
rm -rf %{buildroot}

%files
%defattr(-, bin, bin)
%doc Changes README TODO
%{site_perl}/Test/*
%{site_perl_arch}/auto/*
%{perl_prefix}/man/man3/*

%changelog
* Thu Jan 17 2008 Naveen Gavini <ngavini@nbcs.rutgers.edu> - 0.74-1
- Updated to the latest version.
* Thu Apr 20 2006 Jonathan Kaczynski <jmkacz@oss.rutgers.edu> - 0.62-3
- Removed perl-module-Test-Harness from the Requires
* Wed Apr 19 2006 Jonathan Kaczynski <jmkacz@oss.rutgers.edu> - 0.62-2
- Fixed the requires.
