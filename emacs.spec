%include machine-header.spec
%define emacsversion 22.2
#%define emacsversionletter a
%define leimversion 21.4

Name:		emacs
License:	GPL
Version:	%{emacsversion}
Release:	1
Packager:	Rutgers University
Group:		Applications/Editors
Summary:	The extensible self-documenting text editor
Source0:	emacs-%{emacsversion}.tar.gz 
#Source1:	leim-%{leimversion}.tar.gz
BuildRoot:	%{_tmppath}/%{name}-root
Requires:	xpm libjpeg libtiff >= 3.5.7 libungif libpng3
BuildRequires:	xpm libjpeg-devel libtiff >= 3.5.7 libungif-devel libpng3-devel
Conflicts:	SFWemacs xemacs-b2m
Obsoletes:	emacs21 emacs-leim emacs-libexec


%description
Emacs is a real-time text editor that uses lisp as an extension language.
This is the base package; you need to install it whether you want emacs
with or without x support.

%package info
Group: Applications/Editors
Summary: Emacs info
Requires: emacs = %{emacsversion}, info
%description info
Emacs info files

%package ctags
Group: Applications/Editors
Summary: Emacs ctags
Requires: emacs = %{emacsversion}
%description ctags
Ctags (and etags) makes editing programs with emacs a lot easier.


%prep
%setup -q -n emacs-%{emacsversion}
#%setup -q -D -T -b 1 -n emacs-%{leimversion}

%build
PATH="/opt/SUNWspro/bin:${PATH}" \
CC="cc" CXX="CC" CPPFLAGS="-I/usr/local/include" \
LD="/usr/ccs/bin/ld" \
LDFLAGS="-L/usr/local/lib -R/usr/local/lib"
export PATH CC CXX CPPFLAGS LD LDFLAGS

./configure \
	--prefix=/usr/local \
	--srcdir=`pwd` \
	--with-png \
	--with-xpm \
	--with-jpeg \
	--with-png \
	--with-gif \
	--with-tiff \
	--with-x-toolkit=athena
gmake

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

gmake install prefix=$RPM_BUILD_ROOT/usr/local

#rm $RPM_BUILD_ROOT/usr/local/info/dir
# owned by info package, which is a Requires STUPID
# avoid Requires  rpmlib(PartialHardlinkSets) = 4.0.4-1 by changing to sym
#rm $RPM_BUILD_ROOT/usr/local/bin/emacs

# hardlink badness GO AWAY
cd %{buildroot}/usr/local
/usr/local/bin/unhardlinkify.py ./

%post
# Commented out. This should be done in cfengine!
#if [ ! -r /usr/local/bin/emacs ]; then
#        ln -s /usr/local/bin/emacs-%{emacsversion} /usr/local/bin/emacs
#        echo /usr/local/bin/emacs now points to /usr/local/bin/emacs-%{emacsversion}
#else
#	echo WARNING: You already have /usr/local/bin/emacs but this RPM put 
#	echo down /usr/local/bin/emacs-%{version}
#	echo You may wish to verify a symlink emacs to emacs-%{emacsversion}
#fi
cat <<EOF

If /mail is the mail directory on your system, you should run this as
root to enable movemail:

  cd /usr/local/libexec/emacs/%{emacsversion}/%{sparc_arch}/movemail
  chgrp 6 movemail && chmod g+s movemail

============================================================================

In order to use emacs you must symlink the binary as such:

  ln -s /usr/local/bin/emacs-%{emacsversion} /usr/local/bin/emacs

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
/usr/local/share/emacs/%{emacsversion}/etc
/usr/local/share/emacs/%{emacsversion}/lisp
/usr/local/share/emacs/%{emacsversion}/site-lisp
/usr/local/share/emacs/site-lisp
/usr/local/bin/b2m
/usr/local/bin/ebrowse
#/usr/local/bin/emacs
/usr/local/bin/emacs-%{emacsversion}
/usr/local/bin/emacsclient
/usr/local/bin/grep-changelog
/usr/local/bin/rcs-checkin
/usr/local/share/man/man1/emacsclient.1
/usr/local/share/man/man1/emacs.1
#/usr/local/share/man/man1/gfdl.1
/usr/local/libexec/emacs
/usr/local/share/emacs/%{emacsversion}/leim

%files info
%defattr(-, root, bin)
/usr/local/share/info/ada-mode
/usr/local/share/info/autotype
/usr/local/share/info/calc
/usr/local/share/info/calc-1
/usr/local/share/info/calc-2
/usr/local/share/info/calc-3
/usr/local/share/info/calc-4
/usr/local/share/info/calc-5
/usr/local/share/info/calc-6
/usr/local/share/info/ccmode
/usr/local/share/info/ccmode-1
/usr/local/share/info/cl
/usr/local/share/info/dired-x
/usr/local/share/info/ebrowse
/usr/local/share/info/ediff
/usr/local/share/info/efaq
/usr/local/share/info/eintr
/usr/local/share/info/eintr-1
/usr/local/share/info/eintr-2
/usr/local/share/info/eintr-3
/usr/local/share/info/elisp
/usr/local/share/info/elisp-1
/usr/local/share/info/elisp-10
/usr/local/share/info/elisp-2
/usr/local/share/info/elisp-3
/usr/local/share/info/elisp-4
/usr/local/share/info/elisp-5
/usr/local/share/info/elisp-6
/usr/local/share/info/elisp-7
/usr/local/share/info/elisp-8
/usr/local/share/info/elisp-9
/usr/local/share/info/emacs
/usr/local/share/info/emacs-1
/usr/local/share/info/emacs-2
/usr/local/share/info/emacs-3
/usr/local/share/info/emacs-4
/usr/local/share/info/emacs-5
/usr/local/share/info/emacs-6
/usr/local/share/info/emacs-7
/usr/local/share/info/emacs-8
/usr/local/share/info/emacs-mime
/usr/local/share/info/erc
/usr/local/share/info/eshell
/usr/local/share/info/eudc
/usr/local/share/info/flymake
/usr/local/share/info/forms
/usr/local/share/info/gnus
/usr/local/share/info/gnus-1
/usr/local/share/info/gnus-2
/usr/local/share/info/gnus-3
/usr/local/share/info/gnus-4
/usr/local/share/info/gnus-5
/usr/local/share/info/idlwave
/usr/local/share/info/info
/usr/local/share/info/message
/usr/local/share/info/mh-e
/usr/local/share/info/mh-e-1
/usr/local/share/info/mh-e-2
/usr/local/share/info/newsticker
/usr/local/share/info/org
/usr/local/share/info/org-1
/usr/local/share/info/org-2
/usr/local/share/info/pcl-cvs
/usr/local/share/info/pgg
/usr/local/share/info/rcirc
/usr/local/share/info/reftex
/usr/local/share/info/sc
/usr/local/share/info/ses
/usr/local/share/info/sieve
/usr/local/share/info/smtpmail
/usr/local/share/info/speedbar
/usr/local/share/info/tramp
/usr/local/share/info/url
/usr/local/share/info/vip
/usr/local/share/info/viper
/usr/local/share/info/widget
/usr/local/share/info/woman


%files ctags
%defattr(-, root, bin)
/usr/local/bin/etags
/usr/local/bin/ctags
/usr/local/share/man/man1/etags.1
/usr/local/share/man/man1/ctags.1

%Changelog
* Wed Apr 9 2008 Naveen Gavini <ngavini@nbcs.rutgers.edu> - 22.2-2
- Updated to the latest version.
* Mon Aug 13 2007 David Lee Halik <dhalik@nbcs.rutgers.edu> - 22.1-2
- Fixed Post path for emacs movemail
* Fri Aug 10 2007 David Lee Halik <dhalik@nbcs.rutgers.edu> - 22.1-1
- Bumped to 22
- Removed auto symlink in preference of cfengine

