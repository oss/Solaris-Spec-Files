Name: pam
Version: 3.0
Copyright: Rutgers
Group: System Environment/Base
Summary: pam libraries
Release: 3
Source: pam-3.0.tar.gz
BuildRoot: /var/tmp/%{name}-root
Provides: libru.so pam_ru.so.1

%description
This RPM is just a binary container of the old tint package.
Its DESCRIPTION follows:


This is a version of RU PAM support for Solaris 2.6.  It includes all
Rutgers features:

  links to Kerberos and Enigma
  checking logginable groups
  setting the envrionment from /etc/default/login
  rhosts checking that uses /etc/localhosts

To install, copy all files from etc to /etc and all files from
usr to /usr, in corresponding positions.  You may want to save
the old /etc/pam.conf first.

Be sure that pam_ru.so.1 is protected 755.  (libpam will refuse to
use pam_ru.so if it is group writable.)

Be aware that a full man page is installed to /usr/man/man5.
If for some reason you don't want your users to see it, remove it.

The pam.conf included here has all Rutgers features enabled.  That may
not be appropriate.  See pam_ru.5 for a detailed description of the
options.  The file /etc/pam.conf.ru-minimal is an example that has fewer
Rutgers-specific features enabled.  You might want to consider using
that as /etc/pam.conf, or some compromise.

  -------

Unlike the older version, this was done without access to source.
Thus it should be freely distributable, except for rcmd_sol.c.  While
I have access to additional overview documentation, the man pages and
include files appear to be complete.  rcmd_sol.c needs to be
rewritten to be free.

Currently this implements only about half the possible functions, just
those associated with authentication.  That's OK, since pam.conf only
lists it to be used for authentication and account management.

ru_auth is a fairly clean implementation of pam_sm_authenticate,
except that the various flags and options aren't implemented.

ru_setcred does the rutgers group handling.  The man page suggests
that setcred is to be used for managing things like Kerberos tickets.
However the example login code suggests that setcred may change the
groups, and the debugging output for dtlogin shows the groups before
and after.  So it appears that de facto Sun expects that setcred might
do what I'm doing.

ru_acctmgt handles the check for a valid shell.  Eventually it will
do Kerberos password expiration.

   -------------

Options in pam.conf.

See the man page, pam_ru.5 or pam_ru.0, for details.

It makes sense to list pam_ru.so.1 in both the auth and account
sections.

In the auth section, there are a number of possible options.  All the
special Rutgers features have now been made into options.  This allows
groups that want to do so to move to a more standard environment, but
still get Kerberos and Enigma handling.  With no options, you will get
password processing using libru's conventions for Kerberos, Enigma,
etc, but nothing else.

   debug=/dev/pts/8
   enb
   path=envinit+8
   ruser
   localhosts
   localhosts=/usr/local/etc/localhosts
   groups
   rshx

The debug option enables debugging messages.  Since most of the code
that uses this is in daemons, output to stderr isn't very useful.
Thus I require a device to be specified.

The env option enable Rutgers environment handling.  See the man page.

The path option is a hack needed because PAM's handling of environment
variables is wierd.  PAM can set environment variables.  This is used
for EDITOR and MANPATH.  However certain variables won't work.  PATH
is one.  Unfortunately PATH is the most critical one for us.  The
path= specification causes PAM to put the path environment variable in
the location specified.  This is disgusting: we're deposting a string
pointer into the middle of the running program.  It happens that rshd
and rexec always put the path at that one specific location.  This
should only be needed for rshd and rexecd.  Login processes the path
from /etc/default/login on its own.  Dtlogin can be done using its
startup scripts.

The ruser option causes a check of .rhosts and /etc/hosts.equiv.  This
occurs in place of the usual password check.  It's intended for rshd
and rlogin, where a password check is not appropriate.

The localhosts option (which can be abbreviated lh) causes
/etc/localhosts to be checked in addition to .rhosts and
/etc/hosts.equiv.  It implies ruser.  That is, normally you would
specify lh and not also ruser.  localhosts= lets you specify a
different location for the file to be checked.

The groups option specifies Rutgers group handling.

The rshx option indicates that the special Rutgers version of the rsh
protocol should be used.  If there is a failure, this prompts the user
for a password.  That only works with special Rutgers versions of rsh
and rdist, of course.  We would prefer not to use this, but instead to
move to versions of rsh and rdist that use rexec if they fail.
rshx implies ruser.

Note that pam.conf for rlogin has two entries, both using pam_ru.so
but with different options.  First it tries .rhosts processing.  If
that fails, it does normal password processing, which will prompt for
a password.

In the account section of pam.conf, there is only one possible option:

   shells

Without this option, pam_ru.so is a no-op when listed in the account
section of pam.conf.

Shells enables the check for a valid shell (a shell in /etc/shells).

You should also use the normal Unix module if you want Unix account
expiration checks.

  ------------

Here's an outline of the organization:

pam_ru.so.1 is the sharable library, invoked by /etc/pam.conf.

It is made up of these pieces:

  ru_auth: defines pam_sm_authenticate and its major subroutines

    ru_crypt:  check passwords for normal authentication (essentially the
	      same code appears in libru)

       becomeok:  standard routine used to process become accounts

    rcmd_sol:  contains _validuser, a common routine used to process
              localhosts.  This is actually in the Sun libraries, but
	      as of 2.6 it is declared local, so it can't be called.

    ru_setupenv:  reads /etc/default/login and sets up environment

  ru_setcred: defines pam_sm_setcred

  ru_acctmgt: defines pam_sm_acct_mgmt



Note to second RUSOS version:


Date: Tue, 29 Sep 1998 22:30:17 -0000
From: Charles Hedrick <hedrick@GENEVA.RUTGERS.EDU>
Reply-To: General discussion list for Unix administrators and development       
    staff <UNIX_ADMIN@EMAIL.RUTGERS.EDU>
To: UNIX_ADMIN@EMAIL.RUTGERS.EDU
Subject: problem with 2.6 PAM handling and cron patch

For Solaris 2.6:


Problem:

  You install the current recommended and security patches.  You
start seeing the following in /var/adm/messages:

    Sep 29 17:45:07 geneva.rutgers.edu cron[19352]: load_modules: can not open
module /usr/lib/security/pam_test.so.1


Diagnosis:

  /usr/lib/security/pam_ru.so.1 needs to be linked with -lsocket in order
to get ruserok.  For some reason this was never a problem before.  It's
now become one.


Fix:

  A new pam_ru.so.1 has been submitted to Track.  You can also find it
in /rutgers/ref/ru-dist/ru-pam-2.6/usr/lib/security.  Note that the
copy in /rutgers/ref is version numbered.  I.e. pam_ru.so.1 is a
symlink to pam_ru.so.1.4.  The copy in track is simply pam_ru.so.1.
They're the same thing.

md5sum pam_ru.so.1
fd36bbd4685c77ff9d0bd6b146c20737  pam_ru.so.1

%prep
%setup -q -n files

%build

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT
tar cvf - * | (cd $RPM_BUILD_ROOT && tar xf -)
for i in $RPM_BUILD_ROOT/etc/* ; do
    mv $i $i.rpm
done

%clean
rm -rf $RPM_BUILD_ROOT

%post
os=`uname -r`
if [ -f /etc/pam.conf.ru.$os ]; then
	/usr/bin/cp /etc/pam.conf.ru.$os /etc/pam.conf
	/usr/bin/chmod 644 /etc/pam.conf
	/usr/bin/chgrp sys /etc/pam.conf
fi

%files
%defattr(-,root,root)
%attr(644, root, sys) /etc/*.rpm
/usr/lib/security/*
%attr(644, bin, bin) /usr/man/man5/*
%attr(755, root, other) /usr/local/lib/*
