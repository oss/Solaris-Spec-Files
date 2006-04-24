# This file is deprecated.
# Now using perl-module-Mail-SpamAssasin.spec

%include perl-header.spec

Summary: Spam Assassin perl module
Name: perl-module-Mail-SpamAssassin
Version: 3.1.0
Release: 1
Group: System Environment/Base
Copyright: Unknown
Source: Mail-SpamAssassin-%{version}.tar.bz2
BuildRoot: /var/tmp/%{name}-root
Requires: perl = %{perl_version} perl-module-HTML-Parser perl-module-Digest-MD5 >= 2.33-2ru perl-module-Digest-SHA1 perl-module-Net-DNS perl-module-Storable perl-module-MIME-Base64
BuildRequires: perl = %{perl_version} perl-module-HTML-Parser perl-module-Digest-MD5 >= 2.33-2ru perl-module-Digest-SHA1 perl-module-Net-DNS perl-module-Storable perl-module-MIME-Base64
 %ifos solaris2.9
# Rutgers perl-5.6.1-1 provides an appropriate MakeMaker. Sun does not.
BuildRequires: perl-module-ExtUtils-MakeMaker >= 6.17
%endif

%description
Yet another allegedly useful module from CPAN.

%prep

%setup -q -n Mail-SpamAssassin-%{version}

%build
# perl is ridiculous
LDFLAGS='-L/usr/local/lib -R/usr/local/lib'
export LDFLAGS
perl Makefile.PL PREFIX=/usr/local/spam SYSCONFDIR=/usr/local/spam/conf LDFLAGS='-L/usr/local/lib -R/usr/local/lib' DESTDIR=%{buildroot}
make LDFLAGS='-L/usr/local/lib -R/usr/local/lib'
# make test

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{perl_prefix}
#%{pmake_install} SYSCONFDIR=%{buildroot}/usr/local/spam/conf PKG_DEF_RULES_DIR=%{buildroot}/usr/local/spam/share/spamassassin
# only with Perl would you set DESTDIR BEFORE you compile!
make install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,bin,bin)
%doc README Changes
/usr/local/spam
%ifos solaris2.9
%{site_perl_arch}/*
%{site_perl}/*
%endif

%changelog
* Tue Jan 10 2006 Eric Rivas <kc2hmv@nbcs.rutgers.edu>
 - Upgraded to version 3.1.0
* Mon Apr 14 2005 Leonid Zhadanovsky <leozh@nbcs.rutgers.edu>
 - Upgraded to version 3.02, fixed requires

