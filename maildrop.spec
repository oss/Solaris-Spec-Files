%define __libtoolize /bin/true

Name:		maildrop
Version:	2.1.0
Release:	1
License:	GPL
Group:		Applications/Mail
Source:		http://prdownloads.sourceforge.net/courier/maildrop-%{version}.tar.bz2
URL:            http://www.courier-mta.org/maildrop
Patch0:		maildrop-2.0.4-maildir.patch
Patch1:		maildrop-2.0.2-subject.patch
Patch2:		maildrop-2.0.2-errwritefail.patch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: pcre-devel

Summary:        Mail filter/mail delivery agent

%description
Maildrop is a combination mail filter/mail delivery agent.
It reads a mail message from standard input, then delivers 
the message to your mailbox. Maildrop knows how to deliver 
mail to mbox-style mailboxes, and maildirs.

Maildrop optionally reads instructions from a file, which 
describes how to filter incoming mail. These instructions 
can direct maildrop to deliver the message to an alternate 
mailbox, or forward it somewhere else. Unlike procmail, 
maildrop uses a structured filtering language.

Maildrop is written in C++, and is significantly larger than 
procmail. However, it uses resources much more efficiently.

This version is compiled with support for GDBM database files,
maildir enhancements (folders), and userdb.

%package devel
Summary:        Development tools for handling E-mail messages
Group:          Applications/Mail

%description devel
The maildrop-devel package contains the libraries and header files
that can be useful in developing software that works with or processes
E-mail messages.

You may want to install the maildrop-devel package if you intend to 
develop applications that use or process E-mail messages.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1

%build
PATH="/opt/SUNWspro/bin:/usr/ccs/bin:${PATH}"
CC="cc" CXX="CC"
CPPFLAGS="-I/usr/local/include"
LDFLAGS="-L/usr/local/lib -R/usr/local/lib"
export PATH CC CXX CPPFLAGS LDFLAGS

./configure \
	--prefix=%{_prefix}			\
	--mandir=%{_mandir}			\
	--enable-use-dotlock=0			\
	--with-devel 				\
	--enable-userdb 			\
	--enable-maildirquota 			\
	--enable-syslog=1			\
	--enable-restrict-trusted=0		\
	--enable-sendmail=/usr/lib/sendmail 	\
    	--with-default-maildrop=./Maildir 	\
    	--enable-trusted-users='root mail daemon postmaster qmaild mmdf' 

gmake -j3

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}
gmake install DESTDIR=%{buildroot} MAILDROPUID='' MAILDROPGID=''

mkdir htmldoc
cp %{buildroot}%{_datadir}/maildrop/html/* htmldoc
rm -rf %{buildroot}%{_datadir}/maildrop/html

%files
%defattr(-, bin, bin)
%{_datadir}/maildrop

%doc htmldoc/*

%attr(555, root, mail) %{_bindir}/maildrop
%{_bindir}/mailbot
%{_bindir}/maildirmake
%{_bindir}/deliverquota
%{_bindir}/reformail
%{_bindir}/makemime
%{_bindir}/reformime
%{_bindir}/lockmail
%{_bindir}/makedat
%{_bindir}/makedatprog
%defattr(-, bin, bin)
%{_mandir}/man[1578]/*

%doc maildir/README.maildirquota.html maildir/README.maildirquota.txt
%doc COPYING README README.postfix INSTALL NEWS UPGRADE ChangeLog maildroptips.txt

%files devel
%defattr(-, bin, bin)
%{_mandir}/man3/*
%{_includedir}/*
%{_libdir}/*

%clean
rm -rf $RPM_BUILD_ROOT

%post
cat << EOF

To have maildir directories created, use "-F" when starting maildrop.

EOF

%changelog
* Wed May 27 2009 Brian Schubert <schubert@nbcs.rutgers.edu> - 2.1.0-1
- Updated to version 2.1.0

* Tue May 22 2007 Eric Rivas <kc2hmv@nbcs.rutgers.edu> - 2.0.4-1
- Update to 2.0.4
- Modified patches to apply to 2.0.4

