%include perl-header.spec

Summary: XML::Simple - Easy API to read/write XML (esp config files)
Name: perl-module-XML-Simple
Version: 2.08
Release: 1
Group: Libraries/Perl
Copyright: GPL/Artistic
Source: XML-Simple-%{version}.tar.gz
BuildRoot: /var/tmp/%{name}-root
Requires: perl = %{perl_version} perl-module-XML-Parser >= 2.31
BuildRequires: perl = %{perl_version} perl-module-XML-Parser >= 2.31


%description
  This version (2.08) is the current stable release.
	Please send any feedback to the author: grantm@cpan.org
		

%prep
%setup -q -n XML-Simple-%{version}

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
%doc README Changes
%{perl_prefix}/*
