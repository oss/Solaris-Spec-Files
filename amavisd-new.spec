Summary: amavisd-new is a high-performance interface between mailer (MTA) and content checkers: virus scanners, and/or SpamAssasin.
Name: amavisd-new
Version: 20040906
Release: 1
Group: Applications/Internet 
Copyright: GPL
Source: amavisd-new-20040906.tar.gz 
BuildRoot: /var/tmp/%{name}-root
Requires: perl perl-module-ArchiveTar perl-module-ArchiveZip perl-module-CompressZlib perl-module-Convert-TNEF perl-module-Convert-UUlib perl-module-MIME-Base64 perl-module-MIME-tools perl-module-MailTools perl-module-Net-Server perl-module-libnet perl-module-Digest-MD5 perl-module-IO-stringy perl-module-Time-HiRes perl-module-Unix-Syslog

%description
amavisd-new is a high-performance interface between mailer (MTA) and content checkers: virus scanners, and/or SpamAssasin. It is written in Perl for maintainability, without paying a significant price for speed. It talks to MTA via (E)SMTP or LMTP, or by using helper programs. Best with Postfix, fine with dual-sendmail setup and Exim v4, works with sendmail/milter, or with any MTA as a SMTP relay. 'Howto' for qmail available as well.

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
Remember to read the README files, and make sure you have a group set up for amavisd!
EOF


%files
%defattr(-,root,root)
/usr/local/amavisd/*

%changelog
* Mon Sep 13 2004 Jonathan Kaczynski <jmkacz@nbcs.rutgers.edu>
 - Updated to 20040906 (aka latest version of 2.1.2)
* Fri Apr  9 2004 Christopher Wawak <cwawak@nbcs.rutgers.edu>
 - Updated to -p9
* Wed Mar 17 2004 Christopher Wawak <cwawak@nbcs.rutgers.edu>
 - Updated to -p8
* Fri May 16 2003 Christopher Wawak <cwawak@nbcs.rutgers.edu>
 - Initial version.
 
