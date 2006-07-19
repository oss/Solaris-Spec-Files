
%define __libtoolize /bin/true

Summary: maildrop mail filter/mail delivery agent
Name: maildrop
Version: 2.0.2
Release: 2
Copyright: GPL
Group: Applications/Mail
Source: http://www.flounder.net/~mrsam/maildrop/maildrop-%{version}.tar.bz2
Patch0: maildrop-2.0.2-maildir.patch
Patch1: maildrop-2.0.2-subject.patch
Url: http://www.flounder.net/~mrsam/maildrop/
Packager: Rutgers University
BuildRoot: /var/tmp/maildrop-build
BuildRequires: perl
BuildRequires: pcre
Requires: pcre

%package devel
Summary: development tools for handling E-mail messages
Group: Applications/Mail

%description

Maildrop is a combination mail filter/mail delivery agent.
Maildrop reads the message to be delivered to your mailbox,
optionally reads instructions from a file how filter incoming
mail, then based on these instructions may deliver mail to an
alternate mailbox, or forward it, instead of dropping the
message into your mailbox.

Maildrop uses a structured, real, meta-programming language in
order to define filtering instructions.  Its basic features are
fast and efficient.  At sites which carry a light load, the
more advanced, CPU-demanding, features can be used to build
very sophisticated mail filters.  Maildrop deployments have
been reported at sites that support as many as 30,000
mailboxes.

Maildrop mailing list -- http://maildropl.listbot.com

This version is compiled with support for GDBM database files,
maildir enhancements (folders+quotas), and userdb.

%description devel
The maildrop-devel package contains the libraries and header files
that can be useful in developing software that works with or processes
E-mail messages.

Install the maildrop-devel package if you want to develop applications
which use or process E-mail messages.

%prep

%setup -q
%patch0 -p1
%patch1 -p1

%build

PATH="/opt/SUNWspro/bin:/usr/ccs/bin:${PATH}"
CC="cc" CXX="CC"
CPPFLAGS="-I/usr/local/include -I/usr/local/pcre/include"
LDFLAGS="-L/usr/local/lib -R/usr/local/lib"
LDFLAGS="${LDFLAGS} -L/usr/local/pcre/lib -R/usr/local/pcre/lib"
export PATH CC CXX CPPFLAGS LDFLAGS

./configure \
    --enable-use-dotlock=0 \
    --with-devel \
    --enable-userdb \
    --enable-maildirquota \
    --enable-syslog=1 \
    --enable-restrict-trusted=0 \
    --enable-sendmail=/usr/lib/sendmail \
    --prefix=/usr/local \
    --with-default-maildrop=./Maildir \
    --enable-trusted-users='root mail daemon postmaster qmaild mmdf' 

gmake

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT
gmake install DESTDIR=$RPM_BUILD_ROOT MAILDROPUID='' MAILDROPGID=''

#gzip man pages is a Linuxism? -amr
#find $RPM_BUILD_ROOT%{_mandir} ! -type d -print | perl -e '
# while (<>)
#  {
#    $f=$_;  
#    chop $f;
#    next if $f =~ /\.gz$/;
#    if (-l $f)
#    {
#        $f2=readlink($f);
#        unlink($f);
#        symlink "$f2.gz", "$f.gz";
#    }
#    else
#    {
#        system("gzip <$f >$f.gz");
#        unlink($f);
#    }
# } '

mkdir htmldoc
cp $RPM_BUILD_ROOT%{_datadir}/maildrop/html/* htmldoc
rm -rf $RPM_BUILD_ROOT%{_datadir}/maildrop/html

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

