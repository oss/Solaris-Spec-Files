%include perl-header.spec
%define module_name Mail-SpamAssassin

Summary: Spam Assassin perl module
Name: perl-module-%{module_name}
Version: 3.2.0
Release: 1
Group: System Environment/Base
License: Apache
Source: %{module_name}-%{version}.tar.bz2
URL: http://search.cpan.org/~felicity/%{module_name}-%{version}/lib/spamassassin-run.pod
BuildRoot: %{_tmppath}/%{name}-root
Requires:      perl = %{perl_version} perl-module-HTML-Parser perl-module-Digest-MD5 >= 2.33-2ru perl-module-Digest-SHA1 perl-module-Net-DNS perl-module-Storable perl-module-MIME-Base64 perl-module-Mail-SPF-Query perl-module-Getopt-Long >= 2.35 perl-module-DB_File perl-module-Mail-DomainKeys perl-module-IP-Country perl-module-Mail-DKIM
BuildRequires: perl = %{perl_version} perl-module-HTML-Parser perl-module-Digest-MD5 >= 2.33-2ru perl-module-Digest-SHA1 perl-module-Net-DNS perl-module-Storable perl-module-MIME-Base64 perl-module-Mail-SPF-Query perl-module-Getopt-Long >= 2.35 perl-module-ExtUtils-MakeMaker >= 6.17 perl-module-DB_File perl-module-Mail-DomainKeys perl-module-IP-Country perl-module-Mail-DKIM

%description
Yet another allegedly useful module from CPAN.

%prep
%setup -qn %{module_name}-%{version}

%build
PERL5LIB="/usr/perl5/5.6.1/"
export PERL5LIB
perl Makefile.PL \
    DESTDIR=%{buildroot} \
    SYSCONFDIR=/usr/local/etc \
    INSTALLBIN=/usr/local/bin \
    INSTALLSCRIPT=/usr/local/bin \
    DATADIR=/usr/local/share/spamassassin \
    INSTALLMAN1DIR=/usr/local/man/man1 \
    INSTALLMAN3DIR=/usr/local/man/man3 \
    CONTACT_ADDRESS=root@jla.rutgers.edu
make
#make test

%install
PERL5LIB="/usr/perl5/5.6.1/"
export PERL5LIB
rm -rf %{buildroot}
mkdir -p %{buildroot}%{perl_prefix}
make install

# Get rid of *.pod and .packlist files
rm -rf %{buildroot}/usr/perl5/5.6.1
rm -rf %{buildroot}/usr/perl5/site_perl/5.6.1/sun4-solaris-64int
rm -f  %{buildroot}/usr/perl5/site_perl/5.6.1/spamassassin-run.pod

%clean
rm -rf %{buildroot}

%files
%defattr(-,bin,bin)
%doc BUGS Changes CREDITS INSTALL LICENSE NOTICE PACKAGING README STATUS TRADEMARK UPGRADE USAGE
/usr/local/bin/*
%dir /usr/local/etc/mail
%dir /usr/local/etc/mail/spamassassin
/usr/local/etc/mail/spamassassin/*
/usr/local/man/man1/*.1
/usr/local/man/man3/*.3
%dir /usr/local/share/spamassassin
/usr/local/share/spamassassin/*
/usr/perl5/site_perl/5.6.1/Mail/*

%changelog
* Mon Oct 23 2006 Eric Rivas <kc2hmv@nbcs.rutgers.edu> - 3.1.7-2
 - Update to 3.1.7.
* Wed Jun 21 2006 Jonathan Kaczynski <jmkacz@nbcs.rutgers.edu> - 3.1.3-3
 - Changed the file locations to sort of mirror the way Debian has it set up
 - All future spamassassin packages should use this format
* Tue Jun 06 2006 Jonathan Kaczynski <jmkacz@nbcs.rutgers.edu> - 3.1.3-2
 - Upgraded to version 3.1.3
 - It does not belong in /usr/local/spam
* Mon Apr 24 2006 Jonathan Kaczynski <jmkacz@nbcs.rutgers.edu> - 3.1.1-1
 - Upgraded to version 3.1.1
 - Added perl-module-Mail-SPF-Query to Requires and BuildRequires
* Tue Jan 10 2006 Eric Rivas <kc2hmv@nbcs.rutgers.edu> - 3.1.0-1
 - Upgraded to version 3.1.0
* Mon Apr 14 2005 Leonid Zhadanovsky <leozh@nbcs.rutgers.edu> - 3.0.2-1
 - Upgraded to version 3.02, fixed requires

