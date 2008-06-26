%include perl-header.spec

Summary: Text::Reform -- Manual text wrapping and reformatting
Name: perl-module-Text-Reform
Version: 1.12.2
Release: 1
Group: System Environment/Base
Copyright: GPL/Artistic
Source: Text-Reform-v%{version}.tar.gz
BuildRoot: /var/tmp/%{name}-root
Requires: perl = %{perl_version}
BuildRequires: perl = %{perl_version}, perl-module-version

%description
   The form() subroutine may be exported from the module. It takes a series of format (or
   "picture") strings followed by replacement values, interpolates those values into each
   picture string, and returns the result. The effect is similar to the inbuilt perl format
   mechanism, although the field specification syntax is simpler and some of the formatting
   behaviour is more sophisticated.

%prep

%setup -q -n Text-Reform-v%{version}

%build
perl Makefile.PL
make

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{perl_prefix}
%{pmake_install}
rm -f %{buildroot}%{global_perl_arch}/perllocal.pod

%clean
rm -rf %{buildroot}

%files
%defattr(-,bin,bin)
%doc README Changes
%{site_perl}/Text/*
%{site_perl_arch}/auto/Text/Reform
%{perl_prefix}/man/man3/*

%changelog
* Thu Jun 26 2008 Brian Schubert <schubert@nbcs.rutgers.edu> - 1.12.2-1
- Added changelog and updated to version 1.12.2
