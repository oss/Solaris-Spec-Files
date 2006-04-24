%include perl-header.spec
%define module_name Mail-SpamAssassin

Summary: Spam Assassin perl module
Name: perl-module-%{module_name}
Version: 3.1.1
Release: 1
Group: System Environment/Base
License: Apache
Source: %{module_name}-%{version}.tar.gz
URL: http://search.cpan.org/~felicity/%{module_name}-%{version}/lib/spamassassin-run.pod
BuildRoot: %{_tmppath}/%{name}-root
Requires:      perl = %{perl_version} perl-module-HTML-Parser perl-module-Digest-MD5 >= 2.33-2ru perl-module-Digest-SHA1 perl-module-Net-DNS perl-module-Storable perl-module-MIME-Base64, perl-module-Mail-SPF-Query perl-module-Getopt-Long >= 2.35 perl-module-ExtUtils-MakeMaker >= 6.17
BuildRequires: perl = %{perl_version} perl-module-HTML-Parser perl-module-Digest-MD5 >= 2.33-2ru perl-module-Digest-SHA1 perl-module-Net-DNS perl-module-Storable perl-module-MIME-Base64, perl-module-Mail-SPF-Query perl-module-Getopt-Long >= 2.35

%description
Yet another allegedly useful module from CPAN.

%prep
%setup -qn %{module_name}-%{version}

%build
# perl is ridiculous
###LDFLAGS='-L/usr/local/lib -R/usr/local/lib'
###export LDFLAGS
PERL5LIB="/usr/perl5/5.6.1/:$PERL5LIB"
export PERL5LIB
perl Makefile.PL PREFIX=/usr/local/spam SYSCONFDIR=/usr/local/spam/conf LDFLAGS='-L/usr/local/lib -R/usr/local/lib' DESTDIR=%{buildroot}
###make LDFLAGS='-L/usr/local/lib -R/usr/local/lib'
make
make test

%install
PERL5LIB="/usr/perl5/5.6.1/:$PERL5LIB"
export PERL5LIB
rm -rf %{buildroot}
mkdir -p %{buildroot}%{perl_prefix}
#%{pmake_install} SYSCONFDIR=%{buildroot}/usr/local/spam/conf PKG_DEF_RULES_DIR=%{buildroot}/usr/local/spam/share/spamassassin
# only with Perl would you set DESTDIR BEFORE you compile!
make install

%clean
rm -rf %{buildroot}

%files
%defattr(-,bin,bin)
%doc BUGS Changes CREDITS INSTALL LICENSE NOTICE PACKAGING README STATUS TRADEMARK UPGRADE USAGE
/usr/local/spam

%changelog
* Mon Apr 24 2006 Jonathan Kaczynski <jmkacz@nbcs.rutgers.edu> - 3.1.1-1
 - Upgraded to version 3.1.1
 - Added perl-module-Mail-SPF-Query to Requires and BuildRequires
* Tue Jan 10 2006 Eric Rivas <kc2hmv@nbcs.rutgers.edu> - 3.1.0-1
 - Upgraded to version 3.1.0
* Mon Apr 14 2005 Leonid Zhadanovsky <leozh@nbcs.rutgers.edu> - 3.0.2-1
 - Upgraded to version 3.02, fixed requires

