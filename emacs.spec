%include machine-header.spec

Name: emacs
License: GPL
Version: 21.2
Release: 9
Packager: Rutgers University
Group: Applications/Editors
Summary: The extensible self-documenting text editor
Source0: emacs-%{version}.tar.gz 
Source1: leim-%{version}.tar.gz
Patch: emacs-21.1-sol9.patch
BuildRoot: %{_tmppath}/%{name}-root
Requires: xpm libjpeg62 tiff libungif libpng3
BuildRequires: xpm libjpeg62-devel tiff libungif-devel libpng3-devel
Conflicts: SFWemacs xemacs-b2m
Obsoletes: emacs21 emacs-leim emacs-libexec


%description
Emacs is a real-time text editor that uses lisp as an extension language.
This is the base package; you need to install it whether you want emacs
with or without X support.

%package info
Group: Applications/Editors
Summary: Emacs info
Requires: emacs info
%description info
Emacs info files

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
LDFLAGS="-L/usr/local/lib -R/usr/local/lib" CPPFLAGS="-I/usr/local/include" CFLAGS="-O3"
export LDFLAGS CPPFLAGS CFLAGS
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
rm $RPM_BUILD_ROOT/usr/local/info/dir
# owned by info package, which is a Requires STUPID
# avoid Requires  rpmlib(PartialHardlinkSets) = 4.0.4-1 by changing to sym
rm $RPM_BUILD_ROOT/usr/local/bin/emacs

%post
if [ ! -r /usr/local/bin/emacs ]; then
        ln -s /usr/local/bin/emacs-%{version} /usr/local/bin/emacs
        echo /usr/local/bin/emacs now points to /usr/local/bin/emacs-%{version}
else
	echo WARNING: You already have /usr/local/bin/emacs but this RPM put 
	echo down /usr/local/bin/emacs-%{version}
	echo You may wish to verify a symlink emacs -> emacs-%{version}
fi
cat <<EOF

If /mail is the mail directory on your system, you should run this as
root to enable movemail:

  cd /usr/local/emacs21/libexec/emacs/%{version}/%{sparc_arch}
  chgrp 6 movemail && chmod g+s movemail

EOF


%post info
echo Adding info directory...
for i in `ls /usr/local/info/`; do
    if [ -x /usr/local/bin/install-info ] ; then
        /usr/local/bin/install-info --info-dir=/usr/local/info \
             /usr/local/info/$i &>1 > /dev/null
    fi
done


%postun info
echo Rebuilding info directory...
rm /usr/local/info/dir > /dev/null
for i in `ls /usr/local/info/`; do
    if [ -x /usr/local/bin/install-info ] ; then
        /usr/local/bin/install-info --info-dir=/usr/local/info \
             /usr/local/info/$i &> /dev/null
    fi
done


%files
%defattr(-, root, bin)
/usr/local/share/emacs/%{version}/etc
/usr/local/share/emacs/%{version}/lisp
/usr/local/share/emacs/%{version}/site-lisp
/usr/local/share/emacs/site-lisp
/usr/local/bin/b2m
/usr/local/bin/ebrowse
#/usr/local/bin/emacs
/usr/local/bin/emacs-%{version}
/usr/local/bin/emacsclient
/usr/local/man/man1/emacs.1
#/usr/local/bin/grep-changelog
#/usr/local/bin/rcs-checkin
/usr/local/libexec/emacs
/usr/local/share/emacs/%{version}/leim

%files info
%defattr(-, root, bin)
/usr/local/info/*

%files ctags
%defattr(-, root, bin)
/usr/local/bin/etags
/usr/local/bin/ctags
/usr/local/man/man1/etags.1
/usr/local/man/man1/ctags.1
