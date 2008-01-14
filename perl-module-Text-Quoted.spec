%include perl-header.spec

Summary: Text::Quoted - Extract the structure of a quoted mail message
Name: perl-module-Text-Quoted
Version: 1.2
Release: 2
Group: System Environment/Base
Copyright: GPL/Artistic
Source: Text-Quoted-%{version}.tar.gz
BuildRoot: /var/tmp/%{name}-root
Requires: perl = %{perl_version}
BuildRequires: perl = %{perl_version}

%description
Text::Quoted examines the structure of some text which may contain multiple different levels of quoting, and turns the text into a nested data structure.

The structure is an array reference containing hash references for each paragraph belonging to the same author. Each level of quoting recursively adds another list reference. So for instance, this: 

%prep

%setup -q -n Text-Quoted-%{version}

%build
perl Makefile.PL
make


%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{perl_prefix}
%{pmake_install}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,bin,bin)
%doc README Changes
%{site_perl}/Text/Quoted.pm
%{site_perl_arch}/auto/Text/Quoted
%{perl_prefix}/man/man3/*
