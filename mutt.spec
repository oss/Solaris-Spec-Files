%define actual_version 1.2.5i
%define source_dir_version 1.2.5

Summary: Mutt mailer
Name: mutt
Version: %{actual_version}
Release: 2
Group: Applications/Internet
Copyright: GPL
Source: mutt-%{version}.tar.gz
Patch: mutt.patch
BuildRoot: /var/tmp/%{name}-root
BuildRequires: autoconf automake

%description
Mutt is a small but very powerful text-based MIME mail client.  Mutt
is highly configurable, and is well suited to the mail power user with
advanced features like key bindings, keyboard macros, mail threading,
regular expression searches and a powerful pattern matching language
for selecting groups of messages.

%prep
%setup -q -n mutt-%{source_dir_version}
%patch -p1

%build
automake
autoconf
./configure --enable-pop --enable-imap --enable-external-dotlock \
 --with-mailpath=/var/mail --sysconfdir=/etc
make

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/local
make install DESTDIR=$RPM_BUILD_ROOT
mv $RPM_BUILD_ROOT/usr/local/doc/mutt \
   $RPM_BUILD_ROOT/usr/local/doc/mutt-%{version}
for i in $RPM_BUILD_ROOT/etc/* ; do
    mv $i $i.rpm
done

%post
cat <<EOF
You need to edit and copy /etc/Muttrc.rpm and /etc/mime.types.rpm.
EOF


%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,other)
/usr/local/doc/mutt-%{version}
/usr/local/lib/locale/*/LC_MESSAGES/mutt.mo
/usr/local/man/man1/*
/usr/local/man/man5/muttrc.5
%attr(2755,root,mail) /usr/local/bin/mutt_dotlock
/usr/local/bin/mutt
/usr/local/bin/muttbug
/usr/local/bin/pgpewrap
/usr/local/bin/pgpring
/etc/Muttrc.rpm
/etc/mime.types.rpm
