%include perl-header.spec

Summary: XML-Parser is a Perl extension interface to James Clark's XML parser, expat.
Name: perl-module-XML-Parser
Version: 2.31
Release: 3
Group: System Environment/Base
Copyright: GPL/Artistic
Source: XML-Parser-%{version}.tar.gz
BuildRoot: /var/tmp/%{name}-root
Requires: perl = %{perl_version} expat
BuildRequires: perl = %{perl_version} expat


%description


%prep
%setup -q -n XML-Parser-%{version}

%build
perl Makefile.PL EXPATLIBPATH=/usr/local/lib EXPATINCPATH=/usr/local/include
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