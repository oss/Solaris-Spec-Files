%include machine-header.spec

Name: emacs
License: GPL
Version: 21.2
Release: 1.1
Group: Applications/Editors
Summary: The extensible self-documenting text editor
Source0: emacs-%{version}.tar.gz 
Source1: leim-%{version}.tar.gz
Patch: emacs-21.1-sol9.patch
BuildRoot: %{_tmppath}/%{name}-root
Requires: info Xaw3d xpm libjpeg tiff libungif libpng
BuildRequires: Xaw3d xpm libjpeg tiff libungif-devel libpng
Conflicts: SFWemacs
Obsoletes: emacs21

%description
Emacs is a real-time text editor that uses lisp as an extension language.
This is the base package; you need to install it whether you want emacs
with or without X support.

%package info
Group: Applications/Editors
Summary: Emacs info
Requires: emacs
%description info
Emacs info files

%package libexec
Group: Applications/Editors
Summary: Emacs libexec
Requires: emacs
%description libexec
Emacs libexec files


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
%setup -q -n emacs-%{version}
%setup -D -T -b 1 -n emacs-%{version}

#%ifos solaris2.9
%patch -p1
#%endif

%build
#CC=/opt/SUNWSpro/bin/cc
#CXX=/opt/SUNWspro/bin/CC
#export CC
#export CXX
LDFLAGS="-L/usr/local/lib -R/usr/local/lib" CPPFLAGS="-I/usr/local/include" \
./configure --prefix=/usr/local --srcdir=`pwd` \
--with-png --with-xpm --with-jpeg --with-png --with-gif --with-tiff\
--with-x-toolkit=athena
make

%clean
rm -rf $RPM_BUILD_ROOT

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/local
ed Makefile <<EOF
    /^install-leim/
    .+1s/install/install prefix=\${prefix}/
    w
    q
EOF
make install prefix=$RPM_BUILD_ROOT/usr/local

%post
cat <<EOF

If /mail is the mail directory on your system, you should run this as
root to enable movemail:

  cd /usr/local/emacs21/libexec/emacs/%{version}/%{sparc_arch}
  chgrp 6 movemail && chmod g+s movemail

EOF


%files
%defattr(-, root, bin)
/usr/local/share/emacs/%{version}/etc
/usr/local/share/emacs/%{version}/lisp
/usr/local/share/emacs/%{version}/site-lisp
/usr/local/share/emacs/site-lisp
/usr/local/bin/b2m
/usr/local/bin/ebrowse
/usr/local/bin/emacs
/usr/local/bin/emacs-21.2
/usr/local/bin/emacsclient
/usr/local/man/man1/emacs.1
#/usr/local/bin/grep-changelog
#/usr/local/bin/rcs-checkin

%files info
%defattr(-, root, bin)
/usr/local/info/*

%files libexec
%defattr(-, root, bin)
/usr/local/libexec/emacs

%files ctags
%defattr(-, root, bin)
/usr/local/bin/etags
/usr/local/bin/ctags
/usr/local/man/man1/etags.1
/usr/local/man/man1/ctags.1

%files leim
%defattr(-, root, bin)
/usr/local/share/emacs/%{version}/leim

