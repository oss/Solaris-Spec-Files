Summary: UNIX security tools
Name: cops
Version: 1.04
Release: 2
Group: System Environment/Base
License: Freely distributable
Source: cops.1.04.tar.gz
Patch: cops.patch
BuildRoot: /var/tmp/%{name}-root

%prep
%setup -q -n cops_104
%patch -p1

%build
make clean
make all CC=gcc

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/local/cops
mkdir -p $RPM_BUILD_ROOT/usr/local/man/man1

FILES="home.chk user.chk pass.chk is_writable crc crc_check addto clearfiles \
    filewriters members tilde is_able chk_strings root.chk dev.chk cron.chk \
    is_able.chk cops group.chk rc.chk passwd.chk ftp.chk crc.chk misc.chk \
    suid.chk kuang init_kuang reconfig res_diff yp_pass.chk bug.chk \
    bug.chk.aix bug.chk.apollo bug.chk.dec bug.chk.next bug.chk.sgi \
    bug.chk.sun bug.chk.svr4 bug_cmp is_able.lst suid.stop crc_list"

for i in $FILES ; do
    install -m 0700 $i $RPM_BUILD_ROOT/usr/local/cops/$i
done

DOCS="cops cron.chk dev.chk group.chk is_able.chk  passwd.chk \
    home.chk user.chk pass.chk root.chk rc.chk pass_diff.chk misc.chk \
    is_writable bug.chk"

install -m 0644 docs/kuang.man $RPM_BUILD_ROOT/usr/local/man/man1/kuang.1

for i in $DOCS ; do
    install -m 0644 docs/$i $RPM_BUILD_ROOT/usr/local/man/man1/$i.1
done

%clean
rm -rf $RPM_BUILD_ROOT

%description
   The heart of COPS is a collection of about a dozen (actually, a few
more, but a dozen sounds so good) programs that each attempt to tackle
a different problem area of UNIX security.  Here is what the programs
currently check, more or less (they might check more, but never less,
actually):

o  file, directory, and device permissions/modes.

o  poor passwords.

o  content, format, and security of password and group files.

o  the programs and files run in /etc/rc* and cron(tab) files.

o  existance of root-SUID files, their writeability, and whether or not
   they are shell scripts.

o  a CRC check against important binaries or key files to report any
   changes therein. 

o  writability of users home directories and startup files (.profile,
   .cshrc, etc.) 

o  anonymous ftp setup.

o  unrestricted tftp, decode alias in sendmail, SUID uudecode problems, 
   hidden shells inside inetd.conf, rexd running in inetd.conf.

o  miscellaneous root checks -- current directory in the search path,
   a "+" in /etc/host.equiv, unrestricted NFS mounts, ensuring root is 
   in /etc/ftpusers, etc.

o  dates of CERT advisories vs. key files.  This checks the dates that
   various bugs and security holes were reported by CERT against the
   actual date on the file in question.  A positive result doesn't
   always mean that a bug was found, but it is a good indication that
   you should look at the advisory and file for further clues.  A
   negative result, obviously, does not mean that your software has no
   holes, merely that it has been modified in SOME way (perhaps merely
   "touch"'ed) since the advisory was sent out.

o  the Kuang expert system.  This takes a set of rules and tries to
   determine if your system can be compromised (for a more complete list 
   of all of the checks, look at the file "release.notes" or
   "cops.report"; for more on Kuang, look at at "kuang.man".)

   All of the programs merely warn the user of a potential problem --
COPS DOES NOT ATTEMPT TO CORRECT OR EXPLOIT ANY OF THE POTENTIAL
PROBLEMS IT FINDS!  COPS either mails or creates a file (user
selectable) of any of the problems it finds while running on your
system.  Because COPS does not correct potential hazards it finds, it
does _not_ have to be run by a privileged account (i.e. root or
whomever.)  The only security check that should be run by root to get
maximum results is the SUID checker: although it can be run as an
unprivileged user, it should be run as root so that it can find all the
SUID files in a system.  In addition, if key binaries are not
world-readable, only executable, the CRC checking program ("crc.chk")
needs to be run as a privileged user to read the files in question to
get the result.)  Also note that COPS cannot used to probe a host
remotely; all the tests and checks made require a shell that is on the
host being tested.

   The programs that make up COPS were originally written primarily in
Bourne shell (using awk, sed, grep, etc.) for (hopefully) maximum
portability, with a few written in C for speed (most notably parts of
the Kuang expert system and the implementation of fast user home
directory searching), but the entire system should run on most BSD and
System V machines with a minimum of tweaking.  In addition, a perl
version is included that, while perhaps not as portable as the shell/C
version, has some advantages.

   COPS includes various support programs as well.  The primary one is
CARP (COPS Analysis and Report Program).  CARP is a results interpreter
that is designed to analyze and generate a summary on various COPS reports
from a complete network or set of hosts.


%files
%defattr(-,root,other)
%doc disclaimer 
%doc docs/*ms
/usr/local/cops
/usr/local/man/man1/*
