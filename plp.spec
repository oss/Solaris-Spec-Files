%define psversion 1.0.6

Summary: Public Line Printer Spooler
Name: plp
Version: 4.0.3
Release: 3
Group: Applications/Printing
License: Rutgers
Source0: plp.tar.gz
Source1: plp-psfilter-%{psversion}.tar.gz
Source2: plp-RU-support.tar.gz
Source3: plp-scripts.tar.gz
BuildRoot: /var/tmp/%{name}-root
BuildRequires: vpkg-SPROcc

%description
PLP is a reverse engineered version of the Berkeley 4.3BSD Line
Printer Spooler system. It has many advanced features, which are
described in PLP - The Public Line Printer Spooler by Patrick Powell,
San Diego State University (papowell@sdsu.edu), et al.  It is
available from ftp.iona.ie:/pub/plp.

%prep
%setup -c -n plp -T
%setup -q -D -n plp -T -a 0
%setup -q -D -n plp -T -a 1
%setup -q -D -n plp -T -a 2
%setup -q -D -n plp -T -a 3

%build
PATH="/opt/SUNWspro/bin:$PATH"
export PATH
ROOT=`pwd`
cd $ROOT/plp-%{version}/src
make

cd $ROOT/psfilter-%{psversion}
make

cd $ROOT/RU-support
make ifnotps
make lptcp

%install
PATH="/opt/SUNWspro/bin:$PATH"
export PATH
ROOT=`pwd`

rm -rf $RPM_BUILD_ROOT
for i in bin man/man1 man/man5 man/man8 sbin etc \
         doc/psfilter-%{psversion} ; do
    mkdir -p $RPM_BUILD_ROOT/usr/local/$i
done
mkdir -p $RPM_BUILD_ROOT/etc/init.d

cd $ROOT/plp-%{version}/src
for i in lpq lprm lpr ; do
# for some reason, -m 4711 doesn't work ...
    install -m 4711 $i $RPM_BUILD_ROOT/usr/local/bin/$i.PLP
    chmod 4711 $RPM_BUILD_ROOT/usr/local/bin/$i.PLP
done
install -m 4711 lpc $RPM_BUILD_ROOT/usr/local/sbin/lpc
chmod 4711 $RPM_BUILD_ROOT/usr/local/sbin/lpc


for i in lpd pac setstatus ; do
    install -m 0755 $i $RPM_BUILD_ROOT/usr/local/sbin
done
for i in lp lpstat printers ; do
    install -m 0755 $i $RPM_BUILD_ROOT/usr/local/bin/$i.PLP
done

cd ../doc/man
for j in 1 5 8 ; do
    for i in *.$j ; do
        install -m 0644 $i $RPM_BUILD_ROOT/usr/local/man/man$j/$i
    done
done
cd ..
rm -rf man

cd $ROOT/RU-support
for i in h2 ifnotps lptcp plpsetup plpunsetup checkpc ; do
    install -m 0755 $i $RPM_BUILD_ROOT/usr/local/sbin
done

install -m 0755 init.d-lpd $RPM_BUILD_ROOT/etc/init.d/lpd

cd $ROOT/psfilter-%{psversion}
install -m 0555 psfilter $RPM_BUILD_ROOT/usr/local/sbin
install -m 0644 psfilter.1 $RPM_BUILD_ROOT/usr/local/man/man1
for i in LICENSE COPYING README* ; do
    install -m 0644 $i $RPM_BUILD_ROOT/usr/local/doc/psfilter-%{psversion}
done

cd $ROOT/files
for i in `find . -type f | sed 's/^\.\///` ; do
    install $i $RPM_BUILD_ROOT/$i
done

cd $ROOT

# Why wasn't this in the source tree?  Oh well ...
cat <<EOF > README.RUTGERS
See RU-dist for a hierarchy suitable to copy to your machine.

The postscript filter is in psfilter-1.0.6.  See README.operations there
for documentation of the Rutgers operator status messages.  I'm still
actively working on this program, though I believe that this copy
works.

I've tried to minimize changes, but have had to make them to support
the -B, -N, and -S options.  The maintainer has taken back all my bug
fixes.  I haven't submitted these changes though.  The changes are
localized and fairly clean.  The sources are all rcs'ed.

You'll want to look at documentation, which is fairly complete.
PLP-Manual in this directory is a good starting point, together with
recommended printcap's below.  

The big trick is to get Solaris to get its hands off the port used by
lpd.  Here's Casper Dik's explanation:

  >Feb 28 15:43:55 bienne lpd[1146]: bind: Address already in use

  You need to remove the lpd listener from pmadm.

  pmadm -l will show something like:
  PMTAG          PMTYPE         SVCTAG         FLGS ID       <PMSPECIFIC>
  tcp            listen         lpd            -    root     \x00020203000000000000000000000000 - p - /var/spool/lp/fifos/listenBSD # 
  tcp            listen         0              -    root     \x00020ACE000000000000000000000000 - c - /usr/lib/saf/nlps_server # 
  tcp            listen         lp             -    root     - - p - /var/spool/lp/fifos/listenS5 # 
 
  Remove lpd line with ``pmadm -r -p tcp -s lpd'' and the lp line
  with ``pmadm -r -p tcp -s lp''.

Here's an explanation of my example printcap:

Note that :tc: lets you refer to another entry, so I recommend putting
most of your parameters in a model entry that you use for all printers
of a given type.  That makes maintenance easier.  Here's the model
for a networked postscript printer:

   modelps|model for local postscript printers:\
	:nu:\

nu says this isn't a real printer

	:mx#0:lf=/usr/adm/lpd-errs:\
	:bp=/usr/local/sbin/h2 %n %h %C %N %J:\

bp is the banner generation program.  Note the % escapes to pass it
various information about the file being printed

	:cl:\

cl means to close the connection after every file.  This is needed to
get stacking right on the newer printers.

	:if=/usr/local/sbin/ifnotps /usr/lib/lp/postscript/postprint -l %l - :\

filter for normal files.  ifnotps checks the file to see if it's already
postscript, and makes a pipe using the next command if not.

	:gf=/usr/lib/lp/postscript/postplot %_:\
	:rf=/usr/local/sbin/postfort $l :\

postfort is a simple script that calls asa to do carriage control
interpretation and then postprint.

	:tf=/usr/lib/lp/postscript/dpost %_:\
	:ld=:

   lp8|New Test PostScript Printer:\
	:tc=modelps:\
        :sd=/usr/spool/lpd/lp8:\
	:lp=|/usr/local/sbin/psfilter -m%s -Tdev=lcsr-gw@5020:

psfilter is a Postscript printer controller.  It can handle printers
on serial lines or on a network connection.  I assume our printers are
all on network connections.  The example should be fairly clear.  -m%s
causes PLP to supply the name of the device status file, which is
usually prstatus.  That's the file that "lpc status" shows.  Psfilter
is in a subdirectory here.

   core3|core3l|3rd floor HP LJIIIsi Postscript, CoRE Room 342:\
	:tc=modelps:\
	:sd=/usr/spool/lpd/core3:\
	:lx=/usr/local/sbin/setduplex %C:\

For a printer that's capable of duplex, I recommend using this script.
(The lx printcap entry is a RU modification.  It calls a program to
generate a string that gets stuck at the beginning of each file.  It's
called right before the banner.  You can't use the banner program
because the user can request no banner.)  It checks for ;s in the
class field, and sets duplex or simpler accordingly.  This is the
place to put any special Postscript initialization, if it depends upon
information about the job.  The ld property can be used if it's a
constant for the printer.

	:lp=|/usr/local/sbin/psfilter -m%s -Tdev=core3@9100:
EOF

%post
cat <<EOF
You should probably do this:

  [ ! -f /usr/local/etc/plp.conf ] && cp -p /usr/local/etc/plp.conf.example /usr/local/etc/plp.conf
  [ ! -f /usr/local/etc/plpsetup ] && cp -p /usr/local/etc/plpsetup.example /usr/local/etc/plpsetup
  /usr/local/sbin/checkpc -f
  /usr/local/etc/plpsetup

EOF
mkdir -p /var/spool/lpd
chown daemon.daemon /var/spool/lpd
chmod 0755 /var/spool/lpd

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,other)
%doc plp-%{version}/doc/*
%doc README.RUTGERS
/usr/local/doc/psfilter-%{psversion}
/usr/local/sbin/*
/usr/local/bin/*
/usr/local/etc/*
/usr/local/man/man1/*
/usr/local/man/man5/*
/usr/local/man/man8/*
/etc/init.d/lpd
