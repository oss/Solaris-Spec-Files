%include perl-header.spec

Summary: Class::ReturnValue - A return-value object that lets you treat it as as a boolean, array or object

Name: perl-module-Class-ReturnValue
Version: 0.51
Release: 2
Group: System Environment/Base
Copyright: GPL/Artistic
Source: Class-ReturnValue-%{version}.tar.gz
BuildRoot: /var/tmp/%{name}-root
Requires: perl = %{perl_version}
BuildRequires: perl = %{perl_version}

%description
Class::ReturnValue - A return-value object that lets you treat it as as a boolean, array or object. Class::ReturnValue is a "clever" return value object that can allow code calling your routine to expect: a boolean value (did it fail) or a list (what are the return values)

%prep

%setup -q -n Class-ReturnValue-%{version}

%build
perl Makefile.PL
make


%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{perl_prefix}
%{pmake_install}
%{clean_common_files}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,bin,bin)
%doc Changes
%{site_perl}/Class/ReturnValue.pm
%{site_perl_arch}/auto/Class/ReturnValue
%{perl_prefix}/man/man3/*
