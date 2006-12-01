Summary: amavisd-new is a high-performance interface between mailer (MTA) and content checkers: virus scanners, and/or SpamAssasin.
Name: amavisd-new
Version: 2.4.4
Release: 3
Group: Applications/Internet 
Copyright: GPL
Source: %{name}-%{version}.tar.gz 
BuildRoot: /var/tmp/%{name}-root
Requires: perl 
Requires: perl-module-ArchiveTar >= 1.30
Requires: perl-module-ArchiveZip >= 1.14
Requires: perl-module-CompressZlib >= 1.35
Requires: perl-module-Convert-TNEF >= 0.17
Requires: perl-module-Convert-UUlib >= 1.05
Requires: perl-module-MIME-Base64
Requires: perl-module-MIME-tools >= 5.417
Requires: perl-module-MailTools >= 1.58
Requires: perl-module-Net-Server >= 0.88
Requires: perl-module-libnet >= 1.16
Requires: perl-module-Digest-MD5 >= 2.22
Requires: perl-module-IO-stringy
Requires: perl-module-Time-HiRes >= 1.49
Requires: perl-module-Unix-Syslog

%description
amavisd-new is a high-performance interface between mailer (MTA) and content
checkers: virus scanners, and/or SpamAssasin. It is written in Perl for
maintainability, without paying a significant price for speed. It talks to
MTA via (E)SMTP or LMTP, or by using helper programs. Best with Postfix, fine
with dual-sendmail setup and Exim v4, works with sendmail/milter, or with any
MTA as a SMTP relay. 'Howto' for qmail available as well.

%prep
%setup

%build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/local/amavisd
cp -r * %{buildroot}/usr/local/amavisd

%clean
rm -rf %{buildroot}

%post
cat <<EOF
Remember to read the README files, and make sure you have a group set up for
amavisd!
EOF


%files
%defattr(-,root,root)
/usr/local/amavisd/*

%changelog
* Wed Nov 29 2006 Leo Zhadanovsky <leozh@nbcs.rutgers.edu>
- Updated to 2.4.4
* Mon Sep 13 2004 Jonathan Kaczynski <jmkacz@nbcs.rutgers.edu>
 - Updated to 20040906 (aka latest version of 2.1.2)
* Fri Apr  9 2004 Christopher Wawak <cwawak@nbcs.rutgers.edu>
 - Updated to -p9
* Wed Mar 17 2004 Christopher Wawak <cwawak@nbcs.rutgers.edu>
 - Updated to -p8
* Fri May 16 2003 Christopher Wawak <cwawak@nbcs.rutgers.edu>
 - Initial version.
 
