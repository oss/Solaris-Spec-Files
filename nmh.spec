Summary: Email handling system
Name: nmh
Version: 1.0
Release: 2
Group: Applications/Internet
Copyright: BSD type
Source: %{name}.tar.gz
BuildRoot: /var/tmp/%{name}-root

%description
nmh (new MH) is an electronic mail handling system.  It was originally
based on the package MH-6.8.3, and is intended to be a (mostly)
compatible drop-in replacement for MH.

%prep
%setup -q

%build
# We need to clean the path.  GNU tsort and Solaris tsort both report
# cycles in the output of lorder, but Solaris tsort gives a more
# correct list of libraries.  So correct, in fact, that nmh actually
# compiles ... is this a feature or a bug?
PATH="/usr/openwin/bin:/opt/SUNWspro/bin:/usr/ccs/bin:/usr/bin:/usr/ucb:/usr/sbin"
export PATH
CC="/opt/SUNWspro/bin/cc" ./configure --prefix=/usr/local
make

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/local
make install prefix=$RPM_BUILD_ROOT/usr/local

for i in $RPM_BUILD_ROOT/usr/local/etc/* ; do
    mv $i $i.rpm
done

%post
cat <<EOF
You need to edit and copy the following files:

/usr/local/etc/components.rpm
/usr/local/etc/digestcomps.rpm
/usr/local/etc/distcomps.rpm
/usr/local/etc/forwcomps.rpm
/usr/local/etc/MailAliases.rpm
/usr/local/etc/mhl.body.rpm
/usr/local/etc/mhl.digest.rpm
/usr/local/etc/mhl.format.rpm
/usr/local/etc/mhl.forward.rpm
/usr/local/etc/mhl.headers.rpm
/usr/local/etc/mhl.reply.rpm
/usr/local/etc/mhn.defaults.rpm
/usr/local/etc/mts.conf.rpm
/usr/local/etc/rcvdistcomps.rpm
/usr/local/etc/replcomps.rpm
/usr/local/etc/replgroupcomps.rpm
/usr/local/etc/scan.default.rpm
/usr/local/etc/scan.mailx.rpm
/usr/local/etc/scan.nomime.rpm
/usr/local/etc/scan.size.rpm
/usr/local/etc/scan.time.rpm
/usr/local/etc/scan.timely.rpm
/usr/local/etc/scan.unseen.rpm
/usr/local/etc/tmac.h.rpm

(To get this list of files, run 

  rpm -q nmh -l | egrep '^/usr/local/etc'.)
EOF


%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,bin,bin)
/usr/local/bin/*
/usr/local/lib/*
/usr/local/etc/*
/usr/local/man/man1/*
/usr/local/man/man5/*
/usr/local/man/man8/*
