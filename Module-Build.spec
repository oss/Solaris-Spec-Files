%include perl-header.spec

Summary: Module::Build - Build and install Perl modules

Name: perl-module-Module-Build
Version: 0.18
Release: 1
Group: System Environment/Base
Copyright: GPL/Artistic
Source: Module-Build-%{version}.tar.gz
BuildRoot: /var/tmp/%{name}-root
Requires: perl
Requires: perl-module-ExtUtils-ParseXS >= 2.02-1
Requires: perl-module-YAML >= 0.35-1
BuildRequires: perl
BuildRequires: perl-module-ExtUtils-ParseXS >= 2.02-1
BuildRequires: perl-module-YAML >= 0.35-1

%description
    This is a beta version of a new module I've been working on,
    "Module::Build". It is meant to be a replacement for "ExtUtils::MakeMaker".

    To install "Module::Build", and any other module that uses "Module::Build"
    for its installation process, do the following:

      perl Build.PL       # 'Build.PL' script creates the 'Build' script
      ./Build             # Need ./ to ensure we're using this "Build" script
      ./Build test        # and not another one that happens to be in the PATH
      ./Build install

    This illustrates initial configuration and the running of three 'actions'.
    In this case the actions run are 'build' (the default action), 'test', and
    'install'. Actions defined so far include:

      build                          help        
      clean                          install     
      diff                           manifest    
      dist                           manifypods  
      distcheck                      realclean   
      distclean                      skipcheck   
      distdir                        test        
      distsign                       testdb      
      disttest                       versioninstall
      fakeinstall

    You can run the 'help' action for a complete list of actions.

%prep

%setup -q -n Module-Build-%{version}

%build
%{pbuild}

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{perl_prefix}
%{pbuild_install}
#rm -f `/usr/local/gnu/bin/find $RPM_BUILD_ROOT -iname perllocal.pod`
#rm -f %{global_perl_arch}/perllocal.pod

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,bin,bin)
%doc README Changes
%{site_perl}/Module/Build
