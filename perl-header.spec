# When updating perl, be sure to update this file and reuse perl.spec
# instead of rewriting it.  This file is (or will be) %included in all
# the perl-related specfiles, so upgrading should be relatively
# painless.

# Added new: 6/27/03 by mcgrof 
# pbuild and pbuild_install for Module::Build
# Other modules that support this type of building can use this as well. 
# Note: only pbuild's flags are passed since Module::Build only supports
# that flag so far. The author of Module::Build told me they would soon
# be adding support for the flags in pbuild_install as well.

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

# Note: the commented pmake_install wasn't working for ExtUtils-MakeMaker so I 
# changed it. I'll be testing it thoroughly with some more modules now.
#%define pmake_install     make install PREFIX=%{buildroot}%{perl_prefix}
%define pmake_install   make install INSTALLARCHLIB=%{buildroot}/%{global_perl_arch} INSTALLSITEARCH=%{buildroot}/%{site_perl_arch} INSTALLPRIVLIB=%{buildroot}/%{global_perl} INSTALLSITELIB=%{buildroot}/%{site_perl} INSTALLBIN=%{buildroot}/%{perl_prefix}/bin INSTALLSCRIPT=%{buildroot}/%{perl_prefix}/bin INSTALLMAN1DIR=%{buildroot}/usr/perl5/man/man1 INSTALLMAN3DIR=%{buildroot}/%{perl_prefix}/man/man3
%define pmake_pure_install     make pure_install PREFIX=%{buildroot}%{perl_prefix}

# The following line needs testing
%define pbuild	perl Build.PL destdir=%{buildroot}
%define pbuild_install     perl Build install PREFIX=%{buildroot}%{perl_prefix}

%endif # REPOSITORY



%if %{which_perl} == "SOLARIS"

%ifos solaris2.9
%define perl_version      5.6.1
%define perl_prefix       /usr/perl5
%define perl_arch         sun4-solaris-64int
%define global_perl       %{perl_prefix}/%{perl_version}
%define global_perl_arch  %{global_perl}/lib/%{perl_arch}
%define site_perl         %{perl_prefix}/site_perl/5.6.1
%define site_perl_arch    %{site_perl}/%{perl_arch}

%define perl_binary       %{perl_prefix}/bin/perl

# NOTE: pmake_install variables reduce to these values:
#INSTALLARCHLIB=         /var/tmp/blah-root/usr/perl5/5.6.1/lib/sun4-solaris-64int
#INSTALLSITEARCH=        /var/tmp/blah-root/usr/perl5/site_perl/5.6.1/sun4-solaris-64int 
#INSTALLALLPRIVLIB=      /var/tmp/blah-root/usr/perl5/5.6.1 
#INSTALLSITELIB=         /var/tmp/blah-root/usr/perl5/site_perl/5.6.1/
#INSTALLBIN=             /var/tmp/blah-root/usr/perl5/bin
#INSTALLSCRIPT=          /var/tmp/blah-root/usr/perl5/bin
#INSTALLMAN1DIR=         /var/tmp/blah-root/usr/perl5/man/man1
#INSTALLMAN3DIR=         /var/tmp/blah-root/usr/perl5/man/man3

%define pmake_install   make install INSTALLARCHLIB=%{buildroot}/%{global_perl_arch} INSTALLSITEARCH=%{buildroot}/%{site_perl_arch} INSTALLPRIVLIB=%{buildroot}/%{global_perl} INSTALLSITELIB=%{buildroot}/%{site_perl} INSTALLBIN=%{buildroot}/%{perl_prefix}/bin INSTALLSCRIPT=%{buildroot}/%{perl_prefix}/bin INSTALLMAN1DIR=%{buildroot}/usr/perl5/man/man1 INSTALLMAN3DIR=%{buildroot}/usr/perl5/man/man3
%define pmake_pure_install   make pure_install INSTALLARCHLIB=%{buildroot}/%{global_perl_arch} INSTALLSITEARCH=%{buildroot}/%{site_perl_arch} INSTALLPRIVLIB=%{buildroot}/%{global_perl} INSTALLSITELIB=%{buildroot}/%{site_perl} INSTALLBIN=%{buildroot}/%{perl_prefix}/bin INSTALLSCRIPT=%{buildroot}/%{perl_prefix}/bin INSTALLMAN1DIR=%{buildroot}/usr/perl5/man/man1 INSTALLMAN3DIR=%{buildroot}/usr/perl5/man/man3

# The following lines *have* been tested
%define pbuild  perl Build.PL destdir=%{buildroot}/
%define pbuild_install	perl Build install INSTALLARCHLIB=%{buildroot}/%{global_perl_arch} INSTALLSITEARCH=%{buildroot}/%{site_perl_arch} INSTALLPRIVLIB=%{buildroot}/%{global_perl} INSTALLSITELIB=%{buildroot}/%{site_perl} INSTALLBIN=%{buildroot}/%{perl_prefix}/bin INSTALLSCRIPT=%{buildroot}/%{perl_prefix}/bin INSTALLMAN1DIR=%{buildroot}/usr/perl5/man/man1 INSTALLMAN3DIR=%{buildroot}/usr/perl5/man/man3

%endif # solaris2.9


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
%define pmake_pure_install   make pure_install INSTALLARCHLIB=%{buildroot}/%{global_perl_arch} INSTALLSITEARCH=%{buildroot}/%{site_perl_arch} INSTALLPRIVLIB=%{buildroot}/%{global_perl} INSTALLSITELIB=%{buildroot}/%{site_perl} INSTALLBIN=%{buildroot}/%{perl_prefix}/bin INSTALLSCRIPT=%{buildroot}/%{perl_prefix}/bin INSTALLMAN1DIR=%{buildroot}/usr/perl5/man/man1 INSTALLMAN3DIR=%{buildroot}/usr/perl5/man/man3

# The following line needs testing
%define pbuild  perl Build.PL destdir=%{buildroot}
%define pbuild_install	perl Build install INSTALLARCHLIB=%{buildroot}/%{global_perl_arch} INSTALLSITEARCH=%{buildroot}/%{site_perl_arch} INSTALLPRIVLIB=%{buildroot}/%{global_perl} INSTALLSITELIB=%{buildroot}/%{site_perl} INSTALLBIN=%{buildroot}/%{perl_prefix}/bin INSTALLSCRIPT=%{buildroot}/%{perl_prefix}/bin INSTALLMAN1DIR=%{buildroot}/usr/perl5/man/man1 INSTALLMAN3DIR=%{buildroot}/usr/perl5/man/man3

%endif # solaris2.8


%endif # SOLARIS
