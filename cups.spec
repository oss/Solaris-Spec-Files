# This is based on the included specfile.

%include machine-header.spec

Summary: Common Unix Printing System
Name: cups
Version: 1.1.14
Release: 1
Copyright: GPL
Group: System Environment/Daemons
Source: ftp://ftp.easysw.com/pub/cups/1.1.14/cups-1.1.14-source.tar.bz2
Url: http://www.cups.org
Vendor: Easy Software Products
BuildRoot: /var/tmp/%{name}-root
Conflicts: lpr, LPRng
Provides: libcups.so.2
Provides: libcupsimage.so.2
Requires: openssl
BuildRequires: openssl
BuildRequires: fileutils
BuildRequires: vpkg-SPROcc

%package devel
Summary: Common Unix Printing System - development environment
Group: Development/Libraries

%package pstoraster
Summary: Common Unix Printing System - PostScript RIP
Group: System Environment/Daemons
Provides: pstoraster

%description
The Common UNIX Printing System provides a portable printing layer for 
UNIX® operating systems. It has been developed by Easy Software Products 
to promote a standard printing solution for all UNIX vendors and users. 
CUPS provides the System V and Berkeley command-line interfaces. 

%description devel
The Common UNIX Printing System provides a portable printing layer for 
UNIX® operating systems. This is the development package for creating
additional printer drivers, and other CUPS services.

%description pstoraster
The Common UNIX Printing System provides a portable printing layer for 
UNIX® operating systems. This is the PostScript RIP package for
supporting non-PostScript printer drivers.

%prep
%setup -q

%build
%ifarch sparc64
DSOFLAGS="-xarch=v9" \
LDFLAGS="-L/usr/local/lib -R/usr/local/lib -L/usr/local/ssl/sparcv9/lib -R/usr/local/ssl/sparcv9/lib" \
LIBS="-lsocket" \
CC=cc CFLAGS="-I/usr/local/include -I/usr/local/ssl/sparcv9/include -xarch=v9" \
CXX=CC CXXFLAGS="-I/usr/local/include -I/usr/local/ssl/sparcv9/include -xarch=v9" \
INSTALL="/usr/local/gnu/bin/install" \
./configure --enable-ssl --enable-pam
make DSOFLAGS="-G -xarch=v9 -L../cups -L../filter -L/usr/local/lib -R/usr/local/lib -L/usr/local/ssl/sparcv9/lib -R/usr/local/ssl/sparcv9/lib" \
     SSLLIBS="-lnsl -lsocket -lssl -lcrypto -lgen" \
     LDFLAGS="-xarch=v9 -L../cups -L../filter -L/usr/local/lib -R/usr/local/lib -L/usr/local/ssl/sparcv9/lib -R/usr/local/ssl/sparcv9/lib"
%else
LDFLAGS="-L/usr/local/lib -R/usr/local/lib -L/usr/local/ssl/lib -R/usr/local/ssl/lib" \
LIBS="-lsocket" \
CC=gcc CFLAGS="-I/usr/local/include -I/usr/local/ssl/include" \
CXX=g++ CXXFLAGS="-I/usr/local/include -I/usr/local/ssl/include" \
INSTALL="/usr/local/gnu/bin/install" \
./configure --enable-ssl --enable-pam
make DSOFLAGS="-G -L../cups -L../filter -L/usr/local/lib -R/usr/local/lib -L/usr/local/ssl/lib -R/usr/local/ssl/lib" \
     SSLLIBS="-lnsl -lsocket -lssl -lcrypto -lgen" \
     LDFLAGS="-L../cups -L../filter -L/usr/local/lib -R/usr/local/lib -L/usr/local/ssl/lib -R/usr/local/ssl/lib"
%endif

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}
make  prefix=%{buildroot} \
      exec_prefix=%{buildroot}/usr/local \
      AMANDIR=%{buildroot}/usr/local/man \
      BINDIR=%{buildroot}/usr/local/bin \
      DATADIR=%{buildroot}/usr/local/share/cups \
      DOCDIR=%{buildroot}/usr/local/share/doc/cups \
      INCLUDEDIR=%{buildroot}/usr/local/include \
      LIBDIR=%{buildroot}/usr/local/lib \
      LOGDIR=%{buildroot}/var/log/cups \
      LOCALEDIR=%{buildroot}/usr/local/share/locale \
      MANDIR=%{buildroot}/usr/local/man \
      PMANDIR=%{buildroot}/usr/local/man \
      AMANDIR=%{buildroot}/usr/local/man \
      PAMDIR=%{buildroot}/etc/pam.d \
      REQUESTS=%{buildroot}/var/spool/cups \
      SBINDIR=%{buildroot}/usr/local/sbin \
      SERVERBIN=%{buildroot}/usr/local/lib/cups \
      BUILDROOT=%{buildroot}
      SERVERROOT=%{buildroot}/etc/cups \
      CUPS_USER=`whoami` CUPS_GROUP=`id | sed 's/.*gid=.*(\(.*\))/\1/'` \
      INSTALL_BIN=/usr/local/gnu/bin/install \
      install
for i in `find %{buildroot}/etc -type f`; do
    mv $i $i.rpm
done

%post
cat <<EOF
Edit and move:

   /etc/cups/classes.conf.rpm
   /etc/cups/client.conf.rpm
   /etc/cups/cupsd.conf.rpm
   /etc/cups/printers.conf.rpm
   /etc/cups/mime.convs.rpm
   /etc/cups/mime.types.rpm
   /etc/pam.d/cups.rpm
   /etc/init.d/cups.rpm
   /etc/rc0.d/K00cups.rpm
   /etc/rc2.d/S99cups.rpm
   /etc/rc3.d/S99cups.rpm
   /etc/rc5.d/S99cups.rpm

EOF

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
/usr/local/bin/lpq
/usr/local/bin/lpr
/usr/local/bin/lprm
/usr/local/bin/cancel
/usr/local/bin/disable
/usr/local/bin/enable
/usr/local/bin/lp
/usr/local/bin/lpoptions
/usr/local/bin/lpstat
%attr(4755, lp, sys) /usr/local/bin/lppasswd
/usr/local/lib/*.so*
/usr/local/lib/cups
/usr/local/sbin/*
/usr/local/man/*/*
/usr/local/share/cups
/usr/local/share/doc/cups
/usr/local/share/locale/*/*
%attr(711, lp, sys) /etc/cups/certs
/etc/cups/interfaces
/etc/cups/ppd
/etc/cups/classes.conf.rpm
/etc/cups/client.conf.rpm
/etc/cups/cupsd.conf.rpm
/etc/cups/printers.conf.rpm
/etc/cups/mime.convs.rpm
/etc/cups/mime.types.rpm
/etc/pam.d/cups.rpm
/etc/init.d/cups.rpm
/etc/rc0.d/K00cups.rpm
/etc/rc2.d/S99cups.rpm
/etc/rc3.d/S99cups.rpm
/etc/rc5.d/S99cups.rpm
/var/log/cups
%attr(700, lp, sys) %dir /var/spool/cups
%attr(1700, lp, sys) /var/spool/cups/tmp

%files devel
%defattr(-,root,root)
/usr/local/include/cups
/usr/local/lib/libcups.a

%files pstoraster
%defattr(-,root,root)
/usr/local/lib/cups/filter
/usr/local/share/cups/fonts
/usr/local/share/cups/pstoraster
