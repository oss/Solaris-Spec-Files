%include perl-header.spec

Summary:	ArchiveZip perl module
Name:		perl-module-ArchiveZip
Version:	1.23
Release:	2
Group:		System Environment/Base
Copyright:	GPL
Source:		Archive-Zip-%{version}.tar.gz
Packager: 	David Diffenbaugh <davediff@nbcs.rutgers.edu>
BuildRoot:	/var/tmp/%{name}-root
Requires:	perl = %{perl_version}, perl-module-File-Which >= 0.05, perl-module-CompressZlib
BuildRequires:	perl = %{perl_version}, perl-module-File-Which >= 0.05, perl-module-CompressZlib 

%description
Archive::Zip etc.

%prep

%setup -n Archive-Zip-%{version}

%build
perl Makefile.PL
gmake
gmake test

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{perl_prefix}
%{pmake_install}
cd %{buildroot}
rm usr/perl5/5.6.1/lib/sun4-solaris-64int/perllocal.pod

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,bin,bin)
%doc README Changes
%{site_perl}/*
%{perl_prefix}/man/man3/*
%{perl_prefix}/bin/crc32

%changelog
* Fri Jan 11 2008 David Diffenbaugh <davediff@nbcs.rutgers.edu> - 1.23-2
- Updated to version 1.23 added changelog
