%include machine-header.spec

Name: emacs
Obsoletes: emacs21
License: GPL
Version: 21.2
Release: 1
Group: Applications/Editors
Summary: The extensible self-documenting text editor
Source0: emacs-%{version}.tar.gz 
Source1: leim-%{version}.tar.gz
Patch: emacs-21.1-sol9.patch
BuildRoot: %{_tmppath}/%{name}-root
Requires: info Xaw3d xpm libjpeg tiff libungif libpng
BuildRequires: Xaw3d xpm libjpeg tiff libungif-devel libpng
Conflicts: SFWemacs

%description
Emacs is a real-time text editor that uses lisp as an extension language.
This is the base package; you need to install it whether you want emacs
with or without X support.

%prep
%setup -q -n emacs-%{version}
%setup -D -T -b 1 -n emacs-%{version}
%patch -p1

%build
#CC=/opt/SUNWSpro/bin/cc
#CXX=/opt/SUNWspro/bin/CC
#export CC
#export CXX
LDFLAGS="-L/usr/local/lib -R/usr/local/lib" CPPFLAGS="-I/usr/local/include" \
./configure --prefix=/usr/local/emacs21 --srcdir=`pwd` \
--with-png --with-xpm --with-jpeg --with-png --with-gif --with-tiff
make

%clean
rm -rf $RPM_BUILD_ROOT

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/local/emacs21
ed Makefile <<EOF
    /^install-leim/
    .+1s/install/install prefix=\${prefix}/
    w
    q
EOF
make install prefix=$RPM_BUILD_ROOT/usr/local/emacs21

%post
cat <<EOF

If /mail is the mail directory on your system, you should run this as
root to enable movemail:

  cd /usr/local/emacs21/libexec/emacs/%{version}/%{sparc_arch}
  chgrp 6 movemail && chmod g+s movemail

EOF

%files
%defattr(-, root, bin)
/usr/local/emacs21
