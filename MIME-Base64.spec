%include perl-header.spec

Summary: MIME base64 encoder/decoder
Name: perl-module-MIME-Base64
Version: 2.11
Release: 3
Group: System Environment/Base
Copyright: GPL/Artistic
Source: MIME-Base64-%{version}.tar.gz
BuildRoot: /var/tmp/%{name}-root
Requires: perl = %{perl_version}
BuildRequires: perl = %{perl_version}

%description
This package contains a base64 encoder/decoder and a quoted-printable
encoder/decoder.  These encoding methods are specified in RFC 2045 -
MIME (Multipurpose Internet Mail Extensions).

The Base64 encoding is designed to represent arbitrary sequences of
octets in a form that need not be humanly readable. A 65-character
subset ([A-Za-z0-9+/=]) of US-ASCII is used, enabling 6 bits to be
represented per printable character.

The quoted-printable encoding is intended to represent data that
largely consists of bytes that correspond to printable characters in
the ASCII character set.  Non-printable characters are represented by
a triplet consisting of the character "=" followed by two hexadecimal
digits.

%prep
%setup -q -n MIME-Base64-%{version}

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
%{site_perl_arch}/auto/MIME/Base64
%{site_perl_arch}/MIME/*
%{perl_prefix}/man/man3/*
