# When updating perl, be sure to update this file and reuse perl.spec
# instead of rewriting it.  This file is (or will be) %included in all
# the perl-related specfiles, so upgrading should be relatively
# painless.

%include machine-header.spec

%if %{which_perl} == "REPOSITORY"
%define perl_version      5.6.1
%define perl_prefix       /usr/local/perl5
%define perl_arch         sun4-solaris-thread-multi
%define global_perl       %{perl_prefix}/lib/%{perl_version}
%define global_perl_arch  %{global_perl}/%{perl_arch}
%define site_perl         %{perl_prefix}/lib/site_perl/%{perl_version}
%define site_perl_arch    %{site_perl}/%{perl_arch}

%define perl_binary       %{perl_prefix}/bin/perl

%define pmake_install     make install PREFIX=%{buildroot}%{perl_prefix}
%endif

%if %{which_perl} == "SOLARIS"

%ifos solaris2.9
%define perl_version      5.6.1
%define perl_prefix       /usr/perl5
%define perl_arch         sun4-solaris-64int
%define global_perl       %{perl_prefix}/%{perl_version}
%define global_perl_arch  %{global_perl}/%{perl_arch}
%define site_perl         %{perl_prefix}/site_perl/5.6.1
%define site_perl_arch    %{site_perl}/%{perl_arch}

%define perl_binary       %{perl_prefix}/bin/perl

%define pmake_install   make install INSTALLARCHLIB=%{buildroot}/%{global_perl_arch} INSTALLSITEARCH=%{buildroot}/%{site_perl_arch} INSTALLPRIVLIB=%{buildroot}/%{global_perl} INSTALLSITELIB=%{buildroot}/%{site_perl} INSTALLBIN=%{buildroot}/%{perl_prefix}/bin INSTALLSCRIPT=%{buildroot}/%{perl_prefix}/bin INSTALLMAN1DIR=%{buildroot}/usr/perl5/man/man1 INSTALLMAN3DIR=%{buildroot}/usr/perl5/man/man3
%endif

%ifos solaris2.8
%define perl_version      5.00503
%define perl_prefix       /usr/perl5
%define perl_arch         sun4-solaris
%define global_perl       %{perl_prefix}/%{perl_version}
%define global_perl_arch  %{global_perl}/%{perl_arch}
%define site_perl         %{perl_prefix}/site_perl/5.005
%define site_perl_arch    %{site_perl}/%{perl_arch}

%define perl_binary       %{perl_prefix}/bin/perl

%define pmake_install	make install INSTALLARCHLIB=%{buildroot}/%{global_perl_arch} INSTALLSITEARCH=%{buildroot}/%{site_perl_arch} INSTALLPRIVLIB=%{buildroot}/%{global_perl} INSTALLSITELIB=%{buildroot}/%{site_perl} INSTALLBIN=%{buildroot}/%{perl_prefix}/bin INSTALLSCRIPT=%{buildroot}/%{perl_prefix}/bin INSTALLMAN1DIR=%{buildroot}/usr/perl5/man/man1 INSTALLMAN3DIR=%{buildroot}/usr/perl5/man/man3
%endif
%endif
