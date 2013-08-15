# Rutgers build note: make sure you grab the perl-header file from someone
# and include it in ~/rpmbuild/SPECS/
%include perl-header.spec

%define perl_arch         sun4-solaris-64int
%define site_perl         %{perl_prefix}/site_perl/%{perl_version}


Summary: RATS encryption module
Name: perl-module-RATSdes
Version: 4
Release: 1
Group: System Environment/Base
License: Rutgers University
Source: RATSdes-%{version}.tar
BuildRoot: /var/tmp/%{name}-root
Requires: perl = %{perl_version}
Requires: openssl >= 0.9.8
BuildRequires: perl = %{perl_version}
BuildRequires: openssl >= 0.9.8

%description

%prep
%setup -q -n RATSdes

# Fix shebangs
sed -i 's|/usr/local/bin/perl|%{perl_binary}|' Makefile* src/Makefile* blib/lib/vtest.pl vtest.pl

%build
# Changed as per arichton's sherlockery
#export PATH=$PATH:/usr/bin:/usr/ccs/bin:/usr/local/gnu/bin:/opt/SUNWspro/bin
perl Makefile.PL CCFLAGS="-DOPENSSL_DES_LIBDES_COMPATIBILITY" CC="/opt/SUNWspro/bin/cc"
make
make test

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{perl_prefix}
%{pmake_install}

%clean
rm -rf %{buildroot}

%files
%defattr(-,bin,bin)
%doc README CHANGELOG
%{site_perl_arch}/*
%{perl_prefix}/man/*/*
%{site_perl_arch}/vtest.pl
##%{global_perl_arch}/perllocal.pod



%changelog
* Thu Aug 15 2013 Kyle Suarez <kds124@nbcs.rutegrs.edu> 4.0-1
- Upgrade to the latest version
- 'Changes' has been renamed to 'CHANGELOG'

* Tue Mar 09 2010 Jarek Sedlacek <jarek@nbcs.rutgers.edu> 3.0-3
- included perl-header.spec instead of manually defining all perl prefixes/methods/etc
- overrode default site_perl and perl_arch definitions

* Mon Mar 01 2010 Orcan Ogetbil <orcan@nbcs.rutgers.edu> 3.0-2
 - Change perl prefix to /usr/perl5
 - Fix shebangs

* Mon Nov 02 2009 Jarek Sedlacek <jarek@nbcs.rutgers.edu> 3.0-1
 - Added changelog section to specfile
 - Updated to latest source
 - Changed specfile from using %{cvsdate} to %{version}
