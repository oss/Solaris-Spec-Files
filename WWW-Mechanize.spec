%include perl-header.spec

Summary: WWW::Mechanize - automate interaction with websites

Name: perl-module-WWW-Mechanize
Version: 0.55
Release: 1
Group: System Environment/Base
Copyright: GPL/Artistic
Source: WWW-Mechanize-%{version}.tar.gz
BuildRoot: /var/tmp/%{name}-root
Requires: perl = %{perl_version}
BuildRequires: perl = %{perl_version}

%description
WWW::Mechanize, or Mech for short, was designed to help you automate interaction with a website. It supports performing a sequence of page fetches including following links and submitting forms. Each fetched page is parsed and its links and forms are extracted. A link or a form can be selected, form fields can be filled and the next page can be fetched. Mech also stores a history of the URLs you've visited, which can be queried and revisited.

%prep

%setup -q -n WWW-Mechanize-%{version}

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
%{perl_prefix}/bin/mech-forms
%{site_perl}/WWW/Mechanize.pm
%{site_perl}/WWW/Mechanize
%{site_perl_arch}/auto/WWW/Mechanize
%{perl_prefix}/man/man3/*
