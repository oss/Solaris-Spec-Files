%include perl-header.spec

Summary: Freeze Thaw

Name: perl-module-Freeze-Thaw
Version: 0.43
Release: 1
Group: System Environment/Base
Copyright: GPL/Artistic
Source: FreezeThaw-%{version}.tar.gz
BuildRoot: /var/tmp/%{name}-root
Requires: perl = %{perl_version}
BuildRequires: perl = %{perl_version}

%description
With this module from this moment on you are on your own ;-). Good luck.
(No Kidding, this is the real live description of the package.  What are you doing to me?

%prep

%setup -q -n FreezeThaw-%{version}

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
%{site_perl_arch}/*
%{perl_prefix}/man/man3/*
