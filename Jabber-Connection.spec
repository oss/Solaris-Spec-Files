%include perl-header.spec

Summary: Jabberd Connection Modules
Name: perl-module-Jabber-Connection
Version: 0.04
Release: 6
Group: Libraries/Perl
Copyright: GPL/Artistic
Source: Jabber-Connection-%{version}.tar.gz
BuildRoot: /var/tmp/%{name}-root
Requires: perl = %{perl_version} perl-module-Digest-MD5 expat perl-module-Authen-PAM perl-module-Scalar-List-Util perl-module-XML-Parser perl-module-XML-Simple
BuildRequires: perl = %{perl_version} perl-module-Digest-MD5 expat perl-module-Authen-PAM perl-module-Scalar-List-Util perl-module-XML-Parser perl-module-XML-Simple


%description
The Jabber::Connection package provides basic functions
for connecting clients and components to a Jabber server.

%prep
%setup -q -n Jabber-Connection-%{version}

%build
perl Makefile.PL
make
make test

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{perl_prefix}
%{pmake_install}
find $RPM_BUILD_ROOT -name .packlist -exec rm -f {} \;
find $RPM_BUILD_ROOT -name perllocal.pod -exec rm -f {} \;

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,bin,bin)
%{perl_prefix}/*


