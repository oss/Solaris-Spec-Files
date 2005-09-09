%define actual_version 1.4.2.1i
%define source_dir_version 1.4.2.1

Summary: Mutt mailer
Name: mutt
Version: %{actual_version}
Release: 1
Group: Applications/Internet
Copyright: GPL
Source0: mutt-%{version}.tar.gz
#Patch0: mutt.makefileam.patch
#Patch1: mutt.muttrc.patch
BuildRoot: /var/tmp/%{name}-root
BuildRequires: autoconf automake openssl

%description
Mutt is a small but very powerful text-based MIME mail client.  Mutt
is highly configurable, and is well suited to the mail power user with
advanced features like key bindings, keyboard macros, mail threading,
regular expression searches and a powerful pattern matching language
for selecting groups of messages.

"All mail clients suck. This one just sucks less." -The Author, circa 1995

%prep
%setup -q -n mutt-%{source_dir_version}

#%patch0 -p1
#%patch1 -p1

%build

#aclocal
#automake
#autoconf

CC="cc"
CXX="CC"
CFLAGS="-I/usr/local/ssl/include -I/usr/local/include \
 -L/usr/local/ssl/lib -L/usr/local/lib \
 -R/usr/local/ssl/lib -R/usr/local/lib"
LDFLAGS="-L/usr/local/ssl/lib -L/usr/local/lib \
 -R/usr/local/ssl/lib -R/usr/local/lib"
export CC CXX CFLAGS LDFLAGS

./configure --enable-pop \
            --enable-imap \
            --enable-external-dotlock \
            --with-mailpath=/var/mail \
            --sysconfdir=/usr/local/etc/mutt \
            --with-ssl \
            --prefix=/usr/local
make

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/local
make install DESTDIR=$RPM_BUILD_ROOT
mv $RPM_BUILD_ROOT/usr/local/doc/mutt \
   $RPM_BUILD_ROOT/usr/local/doc/mutt-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%post

%files
%defattr(-,root,other)
/usr/local/share/locale/*/LC_MESSAGES/mutt.mo
#/usr/local/share/locale/locale.alias
#/usr/local/lib/charset.alias
/usr/local/man/man1/*
/usr/local/man/man5/*
/usr/local/bin/flea
/usr/local/bin/mutt
/usr/local/bin/muttbug
/usr/local/bin/pgpewrap
/usr/local/bin/pgpring
%attr(2755,root,mail) /usr/local/bin/mutt_dotlock
%doc /usr/local/doc/mutt-%{version}
%config(noreplace) /usr/local/etc/mutt/Muttrc
%config(noreplace) /usr/local/etc/mutt/mime.types

%changelog
* Tue Aug 30 2005 Eric Rivas <kc2hmv@nbcs.rutgers.edu>
 - Updated to 1.4.2.1i

