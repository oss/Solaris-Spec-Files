Summary:	amavisd-new is a high-performance interface between mailer (MTA) and content checkers: virus scanners, and/or SpamAssasin.
Name:		amavisd-new
Version:	2.6.1
Release:	2
Group:		Applications/Internet 
License:	GPL
Distribution:   RU-Solaris
Vendor:         NBCS-OSS
Packager:       Brian Schubert <schubert@nbcs.rutgers.edu>
Source:		%{name}-%{version}.tar.gz 
#Patch:		amavisd-2.5.2-language.patch
BuildRoot:	%{_tmppath}/%{name}-root
Requires:	perl 
Requires:	file >= 4.21
Requires:	perl-module-ArchiveTar >= 1.30
Requires:	perl-module-ArchiveZip >= 1.14
Requires:	perl-module-CompressZlib >= 1.35
Requires:	perl-module-Convert-TNEF >= 0.17
Requires:	perl-module-Convert-UUlib >= 1.05
Requires:	perl-module-MIME-Base64 >= 3.07
Requires:	perl-module-MIME-tools >= 5.423
Requires:	perl-module-MailTools >= 1.74
Requires:	perl-module-Net-Server >= 0.94
Requires:	perl-module-libnet >= 1.16
Requires:	perl-module-Digest-MD5 >= 2.22
Requires:	perl-module-IO-stringy >= 2.110
Requires:	perl-module-Time-HiRes >= 1.97
Requires:	perl-module-Unix-Syslog >= 0.100-1
Requires:	perl-module-BerkeleyDB >= 0.32
Requires:	perl-module-HTML-Parser >= 3.56
Requires:	perl-module-Mail-SpamAssassin >= 3.2.3

%description
amavisd-new is a high-performance interface between mailer (MTA) and content
checkers: virus scanners, and/or SpamAssasin. It is written in Perl for
maintainability, without paying a significant price for speed. It talks to
MTA via (E)SMTP or LMTP, or by using helper programs. Best with Postfix, fine
with dual-sendmail setup and Exim v4, works with sendmail/milter, or with any
MTA as a SMTP relay. 'Howto' for qmail available as well.

%prep
%setup -q -n %{name}-%{version}

#%patch -p1

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
%doc
/usr/local/amavisd/*

%changelog
* Thu Sep 04 2008 David Diffenbaugh <davediff@nbcs.rutgers.edu> 2.6.1-2
- changed Requires: perl-module-MIME-tools to >= 5.423
* Mon Jun 30 2008 Brian Schubert <schubert@nbcs.rutgers.edu> 2.6.1-1
- Updated to version 2.6.1
* Thu Apr 24 2008 David Diffenbaugh <davediff@nbcs.rutgers.edu> 2.6.0-1
- bumped to latest version
* Thu Apr 10 2008 David Diffenbaugh <davediff@nbcs.rutgers.edu> 2.5.4-2
- added requires file >= 4.21 which corrects security vulnerability
* Thu Mar 13 2008 David Diffenbaugh <davediff@nbcs.rutgers.edu> 2.5.4-1
- updated to latest version, changed version system, removed patch
* Wed Dec 12 2007 Naveen Gavini <ngavini@nbcs.rutgers.edu> - 20070627-1
- Updated to the latest version.
* Tue Nov 06 2007 David Lee Halik <dhalik@nbcs.rutgers.edu> - 20070627-1
- Change version back to dated form for dependencies
- Added perl requires
* Tue Nov 06 2007 David Lee Halik <dhalik@nbcs.rutgers.edu> - 2.5.2-2
- Added amavisd-textcat-2.5.2.patch
* Wed Jun 27 2007 Kevin Mulvey <kmulvey@nbcs.rutgers.edu>
- Updated to 2.5.2
* Thu May 31 2007 David Lee Halik <dhalik@nbcs.rutgers.edu>
- Updated to 2.5.1
- Fixed crazy version system
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
