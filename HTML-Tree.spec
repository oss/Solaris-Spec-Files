%include perl-header.spec

Summary: HTML-Tree

Name: perl-module-HTML-Tree
Version: 3.17
Release: 1
Group: System Environment/Base
Copyright: GPL/Artistic
Source: HTML-Tree-%{version}.tar.gz
BuildRoot: /var/tmp/%{name}-root
Requires: perl = %{perl_version}
BuildRequires: perl = %{perl_version}

%description
This distribution contains a suite of modules for representing,
creating, and extracting information from HTML syntax trees; there is
also relevent documentation.  These modules used to be part of the
libwww-perl distribution, but are now unbundled in order to facilitate
a separate development track.  Bug reports and discussions about these
modules can still be sent to the <libwww@perl.org> mailing list, or to
<sburke@cpan.org>.

%prep

%setup -q -n HTML-Tree-%{version}

%build
perl Makefile.PL
make


%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{perl_prefix}
%{pmake_install}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,bin,bin)
%doc README Changes
%{site_perl_arch}/*
%{perl_prefix}/man/man3/*
