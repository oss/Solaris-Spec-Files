%include perl-header.spec

Summary: Spam Assassin perl module
Name: perl-module-Mail-SpamAssassin
Version: 2.54
Release: 0
Group: System Environment/Base
Copyright: Unknown
Source: Mail-SpamAssassin-%{version}.tar.gz
BuildRoot: /var/tmp/%{name}-root
Requires: perl = %{perl_version}  perl-module-HTML-Parser
BuildRequires: perl = %{perl_version} perl-module-HTML-Parser

%description
Yet another allegedly useful module from CPAN.

%prep

%setup -n Mail-SpamAssassin-%{version}

%build
# perl is ridiculous
LDFLAGS='-L/usr/local/lib -R/usr/local/lib'
export LDFLAGS
perl Makefile.PL PREFIX=/usr/local/spam SYSCONFDIR=/usr/local/spam/conf LDFLAGS='-L/usr/local/lib -R/usr/local/lib'
make LDFLAGS='-L/usr/local/lib -R/usr/local/lib'
make test

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{perl_prefix}
%{pmake_install} SYSCONFDIR=%{buildroot}/usr/local/spam/conf PKG_DEF_RULES_DIR=%{buildroot}/usr/local/spam/share/spamassassin

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,bin,bin)
%doc README Changes
%{site_perl_arch}/*
%{site_perl}/*
%{perl_prefix}/man/man3/*
%{perl_prefix}/man/man1/*
%{perl_prefix}/bin/*
#this may require a symlink
#%{perl_prefix}/share/spamassassin
/usr/local/spam/conf
/usr/local/spam/share/spamassassin
