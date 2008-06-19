%include perl-header.spec

Summary: Text::Wrapper
Name: perl-module-Text-Wrapper
Version: 1.02
Release: 1
Packager: Brian Schubert <schubert@nbcs.rutgers.edu>
Group: System Environment/Base
Copyright: GPL/Artistic
Source: Text-Wrapper-%{version}.tar.gz
BuildRoot: /var/tmp/%{name}-root
Requires: perl = %{perl_version}
BuildRequires: perl = %{perl_version}, perl-module-Module-Build

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
%{pbuild}

%install
rm -rf %{buildroot}
%{pbuild_install}

%clean
rm -rf %{buildroot}

%files
%defattr(-,bin,bin)
%doc README Changes
%{site_perl}/Text/Wrapper.pm
%{site_perl_arch}/auto/Text/Wrapper
%{global_perl}/man/man3/*

%changelog
* Thu Jun 19 2008 Brian Schubert <schubert@nbcs.rutgers.edu> - 1.02-1
- Added changelog, updated to version 1.02
