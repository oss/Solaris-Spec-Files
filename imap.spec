Name: imap
Version: 4.7
Release: 4
Copyright: Rutgers
Summary: University of Washington imap
Source0: imap-4.7-RU.tar.gz
Source1: imap-utils-RU.tar.gz
Source2: pine4.21-RU.tar.gz
Group: Applications/Internet
Requires: mlock
BuildRoot: /var/tmp/%{name}-root

%description
Imap, the Internet Message Access Protocol, lets people access their
mail from far away.  Install this package if you are running an imap
server.

You may want to edit inetd.conf and /etc/services after you install
this package.  Check the documentatin for details.  You need to
install mlock.

%package utils
Summary: Mailbox locking tool
Group: Applications/Internet
Provides: mlock

%description utils
Imap-utils include mlock, which is necessary for pine and imap.  Here
is what it includes:

chkmail mailbox - check for new mail (mail with Recent) set
dmail - deliver mail for procmail
icat mailbox - print mailbox to stdout
ifrom mailbox - one line/msg summary
imapcopy host [mailbox] - get inbox, copy to local, remove from original
imapxfer mailbox mailbox - copy whole mailboxes
mbxcopy mailbox mailbox - move messages to new mailbox
mbxmove mailbox mailbox - move message to new mailbox, remove from original
mbxcreat mailbox - create a mailbox
mbxcvt mailbox format mailbox - convert from one format to another
mlock fd# file - create lock file
tmail user - deliver mail to user's INBOX, for sendmail

%package -n pine
Summary: University of Washington pine
Group: Applications/Internet
Version: 4.21

%description -n pine
Pine is a user-friendly terminal-based mail reader.  You need to
install imap if you want to use this package.

The pine package includes pico, a text editor.

%prep
%setup -T -c -n imap-4.7
%setup -D -T -a 0
%setup -D -T -a 1
%setup -D -T -a 2

# This package expects 3 tarballs:
#
# imap-4.7-RU.tar.gz
# pine4.21-RU.tar.gz
# imap-utils-RU.tar.gz
#
# All of those should be patched.  rpm has the capability of applying
# a patch to a clean source tree, but there's no point in this case.
# The Rutgers-specific patches might break imap from time to time.  I
# looked at the compressed files in the source tree but they seemed to
# have nontrivial diffs against the source tree.
#
# As long as the build procedure doesn't change, this specfile should
# continue to work.


%build
cd imap-4.7
make gso
cd ../imap-utils
for i in * ; do
    [ -d $i ] && (cd $i && make)
done
cd ../pine4.21
./build

%install
umask 022
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/local/bin
mkdir -p $RPM_BUILD_ROOT/usr/local/sbin
mkdir -p $RPM_BUILD_ROOT/usr/local/man/man1
mkdir -p $RPM_BUILD_ROOT/etc

cp imap-4.7/ipopd/ipop2d $RPM_BUILD_ROOT/usr/local/sbin/ipop2d
cp imap-4.7/ipopd/ipop3d $RPM_BUILD_ROOT/usr/local/sbin/ipop3d
cp imap-4.7/imapd/imapd $RPM_BUILD_ROOT/usr/local/sbin/imapd

for i in pico pine pilot ; do
    cp pine4.21/bin/$i $RPM_BUILD_ROOT/usr/local/bin/$i
    cp pine4.21/doc/$i.1 $RPM_BUILD_ROOT/usr/local/man/man1/$i.1
done

for i in chkmail dmail icat ifrom imapcopy imapxfer \
         mbxcopy mbxcreat mbxcvt tmail ; do
    cp imap-utils/$i/$i $RPM_BUILD_ROOT/usr/local/bin/$i
    cp imap-utils/$i/$i.1 $RPM_BUILD_ROOT/usr/local/man/man1/$i.1
done

cp imap-utils/imapcopy/imapmove $RPM_BUILD_ROOT/usr/local/bin/imapmove
cp imap-utils/mbxcopy/mbxmove $RPM_BUILD_ROOT/usr/local/bin/mbxmove
cp imap-utils/mlock/mlock $RPM_BUILD_ROOT/etc/mlock

cd $RPM_BUILD_ROOT/etc
ln -s ../usr/local/sbin/imapd rimapd

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(0755, root, other)
%doc imap-4.7/docs/* imap-4.7/README imap-4.7/RUTGERS
/usr/local/sbin/ipop2d
/usr/local/sbin/ipop3d
/usr/local/sbin/imapd

%files utils
%defattr(-, bin, bin)
/etc/rimapd
/usr/local/bin/chkmail
/usr/local/bin/dmail
/usr/local/bin/icat
/usr/local/bin/ifrom
/usr/local/bin/imapcopy
/usr/local/bin/imapxfer
/usr/local/bin/mbxcopy
/usr/local/bin/mbxcreat
/usr/local/bin/mbxcvt
%attr(3711, root, mail) /etc/mlock
/usr/local/bin/tmail
/usr/local/bin/imapmove
/usr/local/bin/mbxmove
/usr/local/man/man1/chkmail.1
/usr/local/man/man1/dmail.1
/usr/local/man/man1/icat.1
/usr/local/man/man1/ifrom.1
/usr/local/man/man1/imapcopy.1
/usr/local/man/man1/imapxfer.1
/usr/local/man/man1/mbxcopy.1
/usr/local/man/man1/mbxcreat.1
/usr/local/man/man1/mbxcvt.1
/usr/local/man/man1/tmail.1

%files -n pine
%defattr(-, bin, bin)
%doc pine4.21/doc/brochure.txt pine4.21/doc/mailcap.unx 
%doc pine4.21/doc/mime.types pine4.21/doc/tech-notes.txt
%doc pine4.21/doc/tech-notes/*
%attr(755, root, other) /usr/local/bin/pico
%attr(755, root, other) /usr/local/bin/pilot
%attr(755, root, other) /usr/local/bin/pine
/usr/local/man/man1/pico.1
/usr/local/man/man1/pilot.1
/usr/local/man/man1/pine.1



