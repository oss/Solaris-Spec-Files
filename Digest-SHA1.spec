%include perl-header.spec

Summary: The Digest::SHA1 module allows you to use the NIST SHA-1 message digest algorithm from within Perl programs.
Name: perl-module-Digest-SHA1
Version: 2.01
Release: 2
Group: Libraries/Perl
Copyright: GPL/Artistic
Source: Digest-SHA1-%{version}.tar.gz
BuildRoot: /var/tmp/%{name}-root
Requires: perl = %{perl_version}
BuildRequires: perl = %{perl_version}


%description
The Digest::SHA1 module allows you to use the NIST SHA-1 message
digest algorithm from within Perl programs.  The algorithm takes as
input a message of arbitrary length and produces as output a 160-bit
"fingerprint" or "message digest" of the input.

SHA1 is described at <http://www.itl.nist.gov/fipspubs/fip180-1.htm>

%prep
%setup -q -n Digest-SHA1-%{version}

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
%{perl_prefix}/*