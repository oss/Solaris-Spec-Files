Summary: The GNU Core Utilities are the basic file, shell and text manipulation utilities of the GNU operating system.
Name: coreutils
Version: 5.2.1
Release: 1
Group: General/Tools
Copyright: GPL
Source: %{name}-%{version}.tar.gz
BuildRoot: /var/tmp/%{name}-root
Obsoletes: textutils fileutils sh-utils
Provides: textutils fileutils sh-utils

%description
The GNU Core Utilities are the basic file, shell and text manipulation utilities of the GNU operating system. These are the core utilities which are expected to exist on every operating system.

Previously these utilities were offered as three individual sets of GNU utilities, fileutils, shellutils, and textutils. Those three have been combined into a single set of utilities called the coreutils.

%prep
%setup -q

%build
./configure --prefix=/usr/local/gnu
make 

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/local/gnu
make install prefix=%{buildroot}/usr/local/gnu

%clean
rm -fr %{buildroot}

%post
if [ -x /usr/local/bin/install-info ]; then
    /usr/local/bin/install-info --info-dir=/usr/local/gnu/info \
        --entry="* Time: (time).        GNU time" \
        /usr/local/gnu/info/time.info
fi

%preun
if [ -x /usr/local/bin/install-info ]; then
    /usr/local/bin/install-info --info-dir=/usr/local/gnu/info --delete \
        /usr/local/gnu/info/time.info
fi

%files
%defattr(-,root,bin)
/usr/local/gnu/bin/basename
/usr/local/gnu/bin/cat
/usr/local/gnu/bin/chgrp
/usr/local/gnu/bin/chmod
/usr/local/gnu/bin/chown
/usr/local/gnu/bin/chroot
/usr/local/gnu/bin/cksum
/usr/local/gnu/bin/comm
/usr/local/gnu/bin/cp
/usr/local/gnu/bin/csplit
/usr/local/gnu/bin/cut
/usr/local/gnu/bin/date
/usr/local/gnu/bin/dd
/usr/local/gnu/bin/df
/usr/local/gnu/bin/dir
/usr/local/gnu/bin/dircolors
/usr/local/gnu/bin/dirname
/usr/local/gnu/bin/du
/usr/local/gnu/bin/echo
/usr/local/gnu/bin/env
/usr/local/gnu/bin/expand
/usr/local/gnu/bin/expr
/usr/local/gnu/bin/factor
/usr/local/gnu/bin/false
/usr/local/gnu/bin/fmt
/usr/local/gnu/bin/fold
/usr/local/gnu/bin/groups
/usr/local/gnu/bin/head
/usr/local/gnu/bin/hostid
/usr/local/gnu/bin/hostname
/usr/local/gnu/bin/id
/usr/local/gnu/bin/install
/usr/local/gnu/bin/join
/usr/local/gnu/bin/kill
/usr/local/gnu/bin/link
/usr/local/gnu/bin/ln
/usr/local/gnu/bin/logname
/usr/local/gnu/bin/ls
/usr/local/gnu/bin/md5sum
/usr/local/gnu/bin/mkdir
/usr/local/gnu/bin/mkfifo
/usr/local/gnu/bin/mknod
/usr/local/gnu/bin/mv
/usr/local/gnu/bin/nice
/usr/local/gnu/bin/nl
/usr/local/gnu/bin/nohup
/usr/local/gnu/bin/od
/usr/local/gnu/bin/paste
/usr/local/gnu/bin/pathchk
/usr/local/gnu/bin/pinky
/usr/local/gnu/bin/pr
/usr/local/gnu/bin/printenv
/usr/local/gnu/bin/printf
/usr/local/gnu/bin/ptx
/usr/local/gnu/bin/pwd
/usr/local/gnu/bin/readlink
/usr/local/gnu/bin/rm
/usr/local/gnu/bin/rmdir
/usr/local/gnu/bin/seq
/usr/local/gnu/bin/sha1sum
/usr/local/gnu/bin/shred
/usr/local/gnu/bin/sleep
/usr/local/gnu/bin/sort
/usr/local/gnu/bin/split
/usr/local/gnu/bin/stat
/usr/local/gnu/bin/stty
/usr/local/gnu/bin/sum
/usr/local/gnu/bin/sync
/usr/local/gnu/bin/tac
/usr/local/gnu/bin/tail
/usr/local/gnu/bin/tee
/usr/local/gnu/bin/test
/usr/local/gnu/bin/touch
/usr/local/gnu/bin/tr
/usr/local/gnu/bin/true
/usr/local/gnu/bin/tsort
/usr/local/gnu/bin/tty
/usr/local/gnu/bin/uname
/usr/local/gnu/bin/unexpand
/usr/local/gnu/bin/uniq
/usr/local/gnu/bin/unlink
/usr/local/gnu/bin/uptime
/usr/local/gnu/bin/users
/usr/local/gnu/bin/vdir
/usr/local/gnu/bin/wc
/usr/local/gnu/bin/who
/usr/local/gnu/bin/whoami
/usr/local/gnu/bin/yes
/usr/local/gnu/info/coreutils.info
/usr/local/gnu/lib/charset.alias
/usr/local/gnu/man/man1/basename.1
/usr/local/gnu/man/man1/cat.1
/usr/local/gnu/man/man1/chgrp.1
/usr/local/gnu/man/man1/chmod.1
/usr/local/gnu/man/man1/chown.1
/usr/local/gnu/man/man1/chroot.1
/usr/local/gnu/man/man1/cksum.1
/usr/local/gnu/man/man1/comm.1
/usr/local/gnu/man/man1/cp.1
/usr/local/gnu/man/man1/csplit.1
/usr/local/gnu/man/man1/cut.1
/usr/local/gnu/man/man1/date.1
/usr/local/gnu/man/man1/dd.1
/usr/local/gnu/man/man1/df.1
/usr/local/gnu/man/man1/dir.1
/usr/local/gnu/man/man1/dircolors.1
/usr/local/gnu/man/man1/dirname.1
/usr/local/gnu/man/man1/du.1
/usr/local/gnu/man/man1/echo.1
/usr/local/gnu/man/man1/env.1
/usr/local/gnu/man/man1/expand.1
/usr/local/gnu/man/man1/expr.1
/usr/local/gnu/man/man1/factor.1
/usr/local/gnu/man/man1/false.1
/usr/local/gnu/man/man1/fmt.1
/usr/local/gnu/man/man1/fold.1
/usr/local/gnu/man/man1/groups.1
/usr/local/gnu/man/man1/head.1
/usr/local/gnu/man/man1/hostid.1
/usr/local/gnu/man/man1/hostname.1
/usr/local/gnu/man/man1/id.1
/usr/local/gnu/man/man1/install.1
/usr/local/gnu/man/man1/join.1
/usr/local/gnu/man/man1/link.1
/usr/local/gnu/man/man1/ln.1
/usr/local/gnu/man/man1/logname.1
/usr/local/gnu/man/man1/ls.1
/usr/local/gnu/man/man1/md5sum.1
/usr/local/gnu/man/man1/mkdir.1
/usr/local/gnu/man/man1/mkfifo.1
/usr/local/gnu/man/man1/mknod.1
/usr/local/gnu/man/man1/mv.1
/usr/local/gnu/man/man1/nice.1
/usr/local/gnu/man/man1/nl.1
/usr/local/gnu/man/man1/nohup.1
/usr/local/gnu/man/man1/od.1
/usr/local/gnu/man/man1/paste.1
/usr/local/gnu/man/man1/pathchk.1
/usr/local/gnu/man/man1/pinky.1
/usr/local/gnu/man/man1/pr.1
/usr/local/gnu/man/man1/printenv.1
/usr/local/gnu/man/man1/printf.1
/usr/local/gnu/man/man1/ptx.1
/usr/local/gnu/man/man1/pwd.1
/usr/local/gnu/man/man1/readlink.1
/usr/local/gnu/man/man1/rm.1
/usr/local/gnu/man/man1/rmdir.1
/usr/local/gnu/man/man1/seq.1
/usr/local/gnu/man/man1/sha1sum.1
/usr/local/gnu/man/man1/shred.1
/usr/local/gnu/man/man1/sleep.1
/usr/local/gnu/man/man1/sort.1
/usr/local/gnu/man/man1/split.1
/usr/local/gnu/man/man1/stat.1
/usr/local/gnu/man/man1/stty.1
/usr/local/gnu/man/man1/su.1
/usr/local/gnu/man/man1/sum.1
/usr/local/gnu/man/man1/sync.1
/usr/local/gnu/man/man1/tac.1
/usr/local/gnu/man/man1/tail.1
/usr/local/gnu/man/man1/tee.1
/usr/local/gnu/man/man1/test.1
/usr/local/gnu/man/man1/touch.1
/usr/local/gnu/man/man1/tr.1
/usr/local/gnu/man/man1/true.1
/usr/local/gnu/man/man1/tsort.1
/usr/local/gnu/man/man1/tty.1
/usr/local/gnu/man/man1/uname.1
/usr/local/gnu/man/man1/unexpand.1
/usr/local/gnu/man/man1/uniq.1
/usr/local/gnu/man/man1/unlink.1
/usr/local/gnu/man/man1/uptime.1
/usr/local/gnu/man/man1/users.1
/usr/local/gnu/man/man1/vdir.1
/usr/local/gnu/man/man1/wc.1
/usr/local/gnu/man/man1/who.1
/usr/local/gnu/man/man1/whoami.1
/usr/local/gnu/man/man1/yes.1
