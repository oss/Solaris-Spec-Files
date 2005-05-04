%define version 0.55

Summary: Courier Authentication Library
Name: courier-authlib
Version: %{version}
Release: 1
Copyright: GPL
Group: Applications/Mail
Source: courier-authlib-%{version}.tar.bz2
Distribution: RU-Solaris
Vendor: NBCS-OSS
Packager: Leonid Zhadanovsky <leozh@nbcs.rutgers.edu>
BuildRoot: %{_tmppath}/%{name}-root
BuildPreReq: openssl coreutils rpm >= 4.0.2 sed perl gdbm 
Patch0: courier-authlib-rhost.0.55.patch

%description
This is the Courier authentication library. Copies of this library code used to exist in other tarballs: Courier, Courier-IMAP, and SqWebMail. Building and installing any of these packages would've automatically installed this authentication code.

The authentication library is now a separate, standalone package. This authentication library must now be installed, separately, before upgrading to the following builds (or if installing them for the first time): Courier 0.48, Courier-IMAP 4.0, and SqWebMail 5.0.

The Courier authentication library provides authentication services for other Courier applications. In this context, the term "authentication" refers to the following functions:

   1. Take a userid or a loginid, and a password. Determine whether the loginid and the password are valid.
   2. Given a userid, obtain the following information about the userid:
         1. The account's home directory.
         2. The numeric system userid and groupid that owns all files associated with this account.
         3. The location of the account's maildir.
         4. Any maildir quota defined for this account. See the Courier documentation for more information on maildir quotas.
         5. Other miscellaneous account-specific options.
   3. Change the password associated with a loginid.
   4. Obtain a complete list of all loginids.

The Courier authentication library provides alternative implementations 
of these authentication services:

   1. Use the traditional system password files: /etc/passwd and /etc/shadow, possibly in conjunction with the PAM library.
   2. Maintain all this information in a GDBM or a DB database. The GDBM or the DB database is compiled from plain text files. Perl scripts provide a simple interface for creating and editing the authentication information, then a script compiles the plain text files into a database.
   3. Use an LDAP server for authentication.
   4. Use a table in a MySQL database for authentication.
   5. Use a table in a PostgreSQL database for authentication.

All Courier components that use this authentication library, therefore, 
will be able to authenticate E-mail accounts using any of the above 
methods.

%prep
%setup -q

%patch -p1

%build

CC='cc' CXX='CC' \
CFLAGS='' CXXFLAGS='' \
LDFLAGS='-L/usr/local/ssl/lib -L/usr/local/lib -R/usr/local/lib' \
CPPFLAGS='-I/usr/local/ssl/include -I/usr/local/include' \
PATH=/opt/SUNWspro/bin:/usr/ccs/bin:$PATH \
./configure --localstatedir=/var/run \
--without-authdaemon --with-db=gdbm --without-ipv6 \
--prefix=/usr/local/lib/courier-authlib \
--enable-workarounds-for-imap-client-bugs
# --with-authdaemonvar=/var/run/authdaemon.courier-imap 

make 

%install

%{__rm} -rf $RPM_BUILD_ROOT
%{__mkdir_p} $RPM_BUILD_ROOT/etc/pam.d
make install DESTDIR=$RPM_BUILD_ROOT
make install-configure DESTDIR=$RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%config /usr/local/lib/courier-authlib/etc/authlib/*
/usr/local/lib/courier-authlib/etc/*
/usr/local/lib/courier-authlib/lib/courier-authlib/*
/usr/local/lib/courier-authlib/libexec/courier-authlib/*
/usr/local/lib/courier-authlib/include/*
/usr/local/lib/courier-authlib/man/*
/usr/local/lib/courier-authlib/bin/*
/usr/local/lib/courier-authlib/sbin/*
/var/*

%clean
rm -rf $RPM_BUILD_ROOT

%changelog
* Tue May 03 2005 Leonid Zhadanovsky <leozh@nbcs.rutgers.edu>
 - New package, version 0.55
