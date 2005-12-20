# This is heavily inspired by the qmail spec from qmail's site. 

URL: ftp://koobera.math.uic.edu/www/qmail.html
Summary: qmail Mail Transfer Agent
Name: qmail 
Version: 1.03
Release: 8ru
Group: Utilities/System
Copyright: Check with djb@koobera.math.uic.edu
Source0: qmail-%{version}.tar.gz
Source1: rutgers-qmail-additions.tar.gz
Patch0: qmail.patch
Patch1: patch-qmail-1.03-rfc2821.diff
Patch2: patch-qmail-1.03-rfc1652.diff
Buildroot: /var/tmp/qmail-root
Conflicts: sendmail exim smail
Provides: MTA smtpdaemon
BuildRequires: perl

%description
qmail is a small, fast, secure replacement for the sendmail package,
which is the program that actually receives, routes, and delivers
electronic mail.  *** Note: Be sure and read the documentation as there
are some small but very significant differences between sendmail and
qmail and the programs that interact with them.

%prep
%setup -q
%setup -D -T -a 1
# Patch 0 fixes the hier.c file so install works correctly.
%patch  -p1
# Patch 1 deals with rfc 2821
%patch1 -p0
# Patch 2 deals with rfc 1652
%patch2 -p0
perl -i -p -e 's(/var/qmail)(/usr/local/qmail)' conf-qmail
perl -i -p -e 's/cc/gcc/' conf-cc
perl -i -p -e 's/cc/gcc/' conf-ld


%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/local/qmail/bin
mkdir -p $RPM_BUILD_ROOT/etc/qmail

echo "255" > conf-spawn

# Two builds are done here to make both binaries:

# make secure
perl -i -p -e 's/002/022/' conf-patrn
make 
make setup

mv $RPM_BUILD_ROOT/usr/local/qmail/bin/qmail-local \
   $RPM_BUILD_ROOT/usr/local/qmail/bin/qmail-local.secure
for i in control alias users ; do
    mv $RPM_BUILD_ROOT/usr/local/qmail/$i $RPM_BUILD_ROOT/etc/qmail/$i
done
 
# make insecure
perl -i -p -e 's/022/000/' conf-patrn
make
mv qmail-local $RPM_BUILD_ROOT/usr/local/qmail/bin/qmail-local.insecure
cp config config-fast $RPM_BUILD_ROOT/usr/local/qmail/bin

(cd files && find . | cpio -pdmu $RPM_BUILD_ROOT)
perl -e '
  %qmailu = ( 30296 => "alias", 30297 => "qmaild", 30298 => "qmaill",
              0 => "root", 30300 => "qmailp", 30301 => "qmailq",
              30302 => "qmailr", 30303 => "qmails" ); 
  %qmailg = ( 2036 => "nofiles", 2035 => "qmail" );
  %moved  = ( "/usr/local/qmail/control" => "/etc/qmail/control",
              "/usr/local/qmail/alias"   => "/etc/qmail/alias",
              "/usr/local/qmail/users"   => "/etc/qmail/users" );
  open(MANIFEST, "RPM_MANIFEST")   or die "Cannot open RPM_MANIFEST: $!";
  open(FILELIST, "> RPM_FILELIST") or die "Cannot open RPM_FILELIST: $!";
  print FILELIST "\%defattr(-,root,root)\n";
  while (<MANIFEST>) {
      chomp; @f = split /:/;
      $fn = "/usr/local/qmail" . ($f[0] eq "" ? "" : "/$f[0]")
                               . ($f[1] eq "" ? "" : "/$f[1]");
      $fn = $moved{$fn} if (defined $moved{$fn});
      next if ($fn =~ m(bin/qmail-local));
      print FILELIST "\%attr(-,$qmailu{ $f[2] },$qmailg{ $f[3] }) ";
      print FILELIST "%dir " if ($f[1] eq "");
      print FILELIST "$fn\n";
      $seen{$fn} = 1;
  }
  close MANIFEST;
  open(REST, "find /var/tmp/qmail-root/ \! -type d |")
      or die "Pipe error: $!";
  while (<REST>) {
      chomp; s(/var/tmp/qmail-root)();
      unless ($seen{$_}) {
          print FILELIST "\%attr(755,root,qmail) " if (m/qmail-local/);
          print FILELIST "$_\n";
      }
  }
  close FILELIST;'

sed "s/\/etc/\%config\(noreplace\)\/etc/" RPM_FILELIST > RPM_FILELIST2
mv RPM_FILELIST2 RPM_FILELIST
  
%clean
rm -rf $RPM_BUILD_ROOT

%pre
echo "Checking uids..."
if [   "id -a qmailq | grep \
        \"uid=30301(qmailq) gid=199(users) groups=2035(qmail)\"" \
    -a "id -a qmailr | grep \
        \"uid=30302(qmailr) gid=199(users) groups=2035(qmail)\"" \
    -a "id -a qmails | grep \
       \"uid=30303(qmails) gid=199(users) groups=2035(qmail)\"" ]; then
    echo "okay."
else
    echo -e "FAILED!" \
"\nCheck id -a qmailq == uid=30301(qmailq) gid=199(users) groups=2035(qmail)" \
"\n      id -a qmailr == uid=30302(qmailr) gid=199(users) groups=2035(qmail)" \
"\n      id -a qmails == uid=30303(qmails) gid=199(users) groups=2035(qmail)" \
"\nYou may need to recompile qmail.\n"
sleep 60
fi

%post
PATH=/usr/bin
QHOME=/usr/local/qmail

# Shamelessly cribbed from the tint package

addlink () {
    # $1 is the target name
    # $2 is the real location
    [ ! -d "$1" ] && [ ! -h "$1" ] && [ ! -f "$1" ] && ln -s "$2" "$1"
}

# people may want to move these around

addlink $QHOME/boot/rc          rutgers
addlink $QHOME/bin/qmail-local  qmail-local.secure

addlink $QHOME/control          /etc/qmail/control
addlink $QHOME/alias            /etc/qmail/alias
addlink $QHOME/users            /etc/qmail/users

echo "Don't forget /usr/local/qmail/bin/setup for first time installs"
echo "Don't forget /usr/local/qmail/bin/finish_qmail to enable qmail"

%preun

QHOME=/usr/local/qmail
for i in boot/rc bin/qmail-local control alias users ; do
    rm $QHOME/$i
done

%files -f RPM_FILELIST
