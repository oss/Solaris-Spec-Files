%include perl-header.spec

Summary: XML::Simple - Easy API to read/write XML (esp config files)
Name: perl-module-XML-Simple
Version: 1.08_01
Release: 3
Group: Libraries/Perl
Copyright: GPL/Artistic
Source: XML-Simple-%{version}.tar.gz
BuildRoot: /var/tmp/%{name}-root
Requires: perl = %{perl_version} XML-Parser = 2.31
BuildRequires: perl = %{perl_version} 


%description
   This release (1.08_01) is a beta release to allow the new SAX code to be tested on as many platforms as possible.  Please try it out if you can and report success/failure to the author.


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
