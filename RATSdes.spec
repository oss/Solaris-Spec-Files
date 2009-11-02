#%include perl-header.spec
#%define perl_version 5.6.1
%define perl_version      5.6.1
%define perl_prefix       /usr/local/perl5
%define perl_arch         sun4-solaris-thread-multi
%define global_perl       %{perl_prefix}/lib/%{perl_version}
%define global_perl_arch  %{global_perl}/%{perl_arch}
%define site_perl         %{perl_prefix}/lib/site_perl/%{perl_version}
%define site_perl_arch    %{site_perl}/%{perl_arch}
%define perl_binary       %{perl_prefix}/bin/perl


%define pmake_install make install INSTALLARCHLIB=%{buildroot}/%{global_perl_arch} INSTALLSITEARCH=%{buildroot}/%{site_perl_arch} INSTALLPRIVLIB=%{buildroot}/%{global_perl} INSTALLSITELIB=%{buildroot}/%{site_perl} INSTALLBIN=%{buildroot}/%{perl_prefix}/bin INSTALLSCRIPT=%{buildroot}/%{perl_prefix}/bin INSTALLMAN1DIR=%{buildroot}/usr/perl5/man/man1 INSTALLMAN3DIR=%{buildroot}/%{perl_prefix}/man/man3


Summary: RATS encryption module
Name: perl-module-RATSdes
Version: 3
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

%build
# Changed as per arichton's sherlockery
#export PATH=$PATH:/usr/bin:/usr/ccs/bin:/usr/local/gnu/bin:/opt/SUNWspro/bin
perl Makefile.PL CCFLAGS="-DOPENSSL_DES_LIBDES_COMPATIBILITY" CC="/opt/SUNWspro/bin/cc"
make clean
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
%doc README Changes
%{site_perl_arch}/*
%{perl_prefix}/man/*/*
%{site_perl_arch}/vtest.pl
%{global_perl_arch}/perllocal.pod



%changelog
* Mon Nov 02 2009 Jarek Sedlacek <jarek@nbcs.rutgers.edu> 3.0-1
 - Added changelog section to specfile
 - Updated to latest source
 - Changed specfile from using %{cvsdate} to %{version}
