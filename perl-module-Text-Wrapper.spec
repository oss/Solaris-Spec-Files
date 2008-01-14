%include perl-header.spec

Summary: Text::Wrapper
Name: perl-module-Text-Wrapper
Version: 1.000
Release: 2
Group: System Environment/Base
Copyright: GPL/Artistic
Source: Text-Wrapper-%{version}.tar.gz
BuildRoot: /var/tmp/%{name}-root
Requires: perl = %{perl_version}
BuildRequires: perl = %{perl_version}

%description
This module provides simple word wrapping.  It breaks long lines,
    but does not alter spacing or remove existing line breaks.  If
    you're looking for more sophisticated text formatting, try the
    Text::Format module.

    Reasons to use Text::Wrapper instead of Text::Format:

    *   Text::Wrapper is significantly smaller.

    *   It does not alter existing whitespace or combine short lines.
        It only breaks long lines.  By design, Text::Format removes
        all whitespace and then adds whitespace where it thinks
        appropriate.


%prep

%setup -q -n Text-Wrapper-%{version}

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
%{site_perl}/Text/Wrapper.pm
%{site_perl_arch}/auto/Text/Wrapper
%{perl_prefix}/man/man3/*
