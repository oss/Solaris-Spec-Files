# Inspired by the redhat emacs spec file

Name: emacs
License: GPL
Version: 20.7
Release: 12
Group: Applications/Editors
Summary: The extensible self-documenting text editor
Source0: emacs-%{version}.tar.gz 
Source1: leim-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-root
Requires: info
Conflicts: SFWemacs

%description
Emacs is a real-time text editor that uses lisp as an extension language.
This is the base package; you need to install it whether you want emacs
with or without X support.

%package nox
Group: Applications/Editors
Summary: Emacs without X11 support
Requires: emacs
%description nox
Emacs is a real-time text editor that uses lisp as an extension language.
If you want emacs without X11 support, install this package (as well as
the emacs package).

%package X11
Group: Applications/Editors
Summary: Emacs with X11 support
Requires: emacs
%description X11
Emacs is a real-time text editor that uses lisp as an extension language.
If you want emacs with X11 support (this package works on ttys as well),
install this package (as well as the emacs package).

%package leim
Group: Applications/Editors
Summary: Emacs Lisp for international characters
Requires: emacs
%description leim
Emacs is a real-time text editor that uses lisp as an extension language.
This package adds international support for emacs.  You may want to
install intlfonts as well. 

%package ctags
Group: Applications/Editors
Summary: Emacs ctags
%description ctags
Ctags (and etags) makes editing programs with emacs a lot easier.

%prep
%setup -q
%setup -D -T -b 1

%build
rm -rf without-x
mkdir without-x
cd without-x
../configure --prefix=/usr/local/emacs20 --with-pop --with-kerberos \
    --with-x=no --infodir=/usr/local/info
make
cd ..

rm -rf with-x
mkdir with-x
cd with-x
../configure --prefix=/usr/local/emacs20 --with-pop --with-kerberos \
    --with-x-toolkit --infodir=/usr/local/info
make
cd ..


%clean
rm -rf $RPM_BUILD_ROOT
rm -rf with-x
rm -rf without-x

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/local/emacs20
make install -C with-x prefix=$RPM_BUILD_ROOT/usr/local/emacs20 \
    infodir=$RPM_BUILD_ROOT/usr/local/info
install -m755 without-x/src/emacs $RPM_BUILD_ROOT/usr/local/emacs20/bin/emacs-nox
rm -f $RPM_BUILD_ROOT/usr/local/info/dir

%post
# sanity check:
if [ -x /usr/local/bin/install-info ]; then
    for i in emacs ediff dired-x cl ccmode forms gnus message mh-e sc vip \
	    viper widget ; do
	/usr/local/bin/install-info --info-dir=/usr/local/info /usr/local/info/$i
    done
fi
cat <<EOF

If /mail is the mail directory on your system, you should run this as
root to enable movemail:

  cd /usr/local/emacs20/libexec/emacs/20.7/sparc-sun-solaris2.7
  chgrp 6 movemail && chmod g+s movemail

In order to run emacs you must install emacs-X11 or emacs-nox.

EOF

%post X11
echo "You may wish to link /usr/local/emacs20/bin/emacs to /usr/local/bin/emacs."

%post nox
echo "You may wish to link /usr/local/emacs20/bin/emacs-nox to /usr/local/bin/emacs."

%preun
if [ -x /usr/local/bin/install-info ]; then
    for i in emacs ediff dired-x cl ccmode forms gnus message mh-e sc vip \
	    viper widget ; do
	/usr/local/bin/install-info --delete --info-dir=/usr/local/info \
	    /usr/local/info/$i
    done
fi

%files
%defattr(-, root, bin)
/usr/local/emacs20/share/emacs/%{version}
/usr/local/emacs20/share/emacs/site-lisp
/usr/local/info/*
/usr/local/emacs20/man/man1/emacs.1
/usr/local/emacs20/bin/b2m
/usr/local/emacs20/bin/emacsclient
/usr/local/emacs20/bin/rcs-checkin
/usr/local/emacs20/libexec/emacs/%{version}

%files leim
%defattr(-, root, bin)
/usr/local/emacs20/share/emacs/%{version}/leim
/usr/local/emacs20/share/emacs/site-lisp/subdirs.el

%files X11
%defattr(-, root, bin)
/usr/local/emacs20/bin/emacs-%{version}
/usr/local/emacs20/bin/emacs

%files nox
%defattr(-, root, bin)
/usr/local/emacs20/bin/emacs-nox

%files ctags
%defattr(-, root, bin)
/usr/local/emacs20/bin/etags
/usr/local/emacs20/bin/ctags
/usr/local/emacs20/man/man1/etags.1
/usr/local/emacs20/man/man1/ctags.1
