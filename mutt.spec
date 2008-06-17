Summary: Mutt mailer
Name: mutt
Version: 1.4.2.3
Release: 1
Group: Applications/Internet
Copyright: GPL
Source: mutt-%{version}.tar.gz
Patch: mutt-1.4-nosetgid.patch
BuildRoot: /var/tmp/%{name}-root
Requires: slang
BuildRequires: openssl, slang-devel

%description
Mutt is a small but very powerful text-based MIME mail client.  Mutt
is highly configurable, and is well suited to the mail power user with
advanced features like key bindings, keyboard macros, mail threading,
regular expression searches and a powerful pattern matching language
for selecting groups of messages.

"All mail clients suck. This one just sucks less." -The Author, circa 1995

%prep
%setup -q -n mutt-%{version}
%patch -p1 -b .nosetgid

%build

PATH="/opt/SUNWspro/bin:${PATH}" \
CC="cc" \
CXX="CC" \
CFLAGS="-I/usr/local/ssl/include -I/usr/local/include -I/usr/include \
 -L/usr/local/ssl/lib -L/usr/local/lib \
 -R/usr/local/ssl/lib -R/usr/local/lib" \
LDFLAGS="-L/usr/lib -L/usr/local/ssl/lib -L/usr/local/lib \
 -R/usr/lib -R/usr/local/ssl/lib -R/usr/local/lib" \
export CC CXX CFLAGS LDFLAGS SHELL PATH
./configure --enable-pop \
            --enable-imap \
            --with-mailpath=/var/mail \
            --sysconfdir=/usr/local/etc/mutt \
            --with-ssl \
            --prefix=/usr/local \
	    --with-slang \
	    --with-curses=/usr \
            --disable-nls
gmake

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/local
gmake install DESTDIR=$RPM_BUILD_ROOT
mv $RPM_BUILD_ROOT/usr/local/doc/mutt \
   $RPM_BUILD_ROOT/usr/local/doc/mutt-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%post

%files
%defattr(-,root,other)
/usr/local/bin/flea
/usr/local/bin/mutt
/usr/local/bin/muttbug
/usr/local/bin/pgpewrap
/usr/local/bin/pgpring
/usr/local/share/man/man1/*.1
/usr/local/share/man/man5/*.5
%doc /usr/local/doc/mutt-%{version}
%config(noreplace) /usr/local/etc/mutt/Muttrc
%config(noreplace) /usr/local/etc/mutt/mime.types

%changelog
* Tue Jun 17 2008 Brian Schubert <schubert@nbcs.rutgers.edu> - 1.4.2.3-1
- Updated to version 1.4.2.3
* Fri Oct 20 2006 John M. Santel <jmsl@nbcs.rutgers.edu>
 - Updated to 1.4.2.2i and applied dotlock removal hack from rawhide
* Tue Aug 30 2005 Eric Rivas <kc2hmv@nbcs.rutgers.edu>
 - Updated to 1.4.2.1i

