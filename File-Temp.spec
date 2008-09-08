%include perl-header.spec

Summary: File-Temp
Name: perl-module-File-Temp
Version: 0.17
Release: 1
Group: System Environment/Base
Copyright: GPL/Artistic
Source: File-Temp-%{version}.tar.gz
BuildRoot: /var/tmp/%{name}-root
Requires: perl = %{perl_version}
BuildRequires: perl = %{perl_version}

%description
File::Temp rules at making temp files.

%prep

%setup -q -n File-Temp-%{version}

%build
perl Makefile.PL
gmake
gmake test

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{perl_prefix}
%{pmake_install}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,bin,bin)
%doc ChangeLog MANIFEST README
/usr/perl5/5.6.1/File/Temp.pm
/usr/perl5/5.6.1/lib/sun4-solaris-64int/auto/File/Temp/.packlist
/usr/perl5/man/man3/File::Temp.3


%changelog
* Thu Sep 04 2008 David Diffenbaugh <davediff@nbcs.rutgers.edu> - 0.17-1
- updated to latest version
