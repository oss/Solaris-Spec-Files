%include perl-header.spec

Summary: Perl GUI module
Name: perl-module-Tk
Version: 800.023
Release: 1
Group: System Environment/Base
Copyright: GPL/Artistic
Source: Tk%{version}.tar.gz
BuildRoot: /var/tmp/%{name}-root
Requires: perl = %{perl_version}
BuildRequires: perl = %{perl_version}

%description
Tk is a graphical user interface module for Perl.

%prep
%setup -q -n Tk%{version}

%build
perl Makefile.PL
make
# Since it opens connections to the X server, don't run
# make test.

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{perl_prefix}
%{pmake_install}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,bin,bin)
%doc README* Changes COPYING
%{site_perl_arch}/Tk
%{site_perl_arch}/auto/Tk
%{site_perl_arch}/fix_4_os2.pl
%{site_perl_arch}/Tk.pod
%{site_perl_arch}/Tk.pm
%{perl_prefix}/man/man3/*
%{perl_prefix}/man/man1/*
%{perl_prefix}/bin/*
