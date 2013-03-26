%global info_files ada-mode auth autotype calc ccmode cl dbus dired-x ebrowse ede ediff edt efaq eieio eintr elisp emacs emacs-mime epa erc eshell eudc flymake forms gnus idlwave info mairix-el message mh-e newsticker nxml-mode org pcl-cvs pgg rcirc reftex remember sasl sc ses sieve smtpmail speedbar tramp url vip viper widget woman
%global site_lisp %{_datadir}/emacs/site-lisp

Name:		emacs
License:	GPL
Version:	24.1
Release:	2
Packager:	Rutgers University
Group:		Applications/Editors
Summary:	The extensible self-documenting text editor
URL:            http://www.gnu.org/software/emacs/
Source0:	http://ftp.gnu.org/pub/gnu/emacs/emacs-%{version}.tar.gz

# Useful stuff from Fedora
Source4:        site-start.el
Source7:        http://php-mode.svn.sourceforge.net/svnroot/php-mode/tags/php-mode-1.4.0/php-mode.el
Source8:        php-mode-init.el
Source9:        ssl.el
Source10:       rpm-spec-mode.el
Source11:       rpm-spec-mode-init.el
Source13:       focus-init.el
Source18:       default.el
Patch1:         rpm-spec-mode.patch
Patch3:         rpm-spec-mode-utc.patch
#Patch5:         emacs-23.2-m17ncheck.patch
#Patch6:         emacs-23.2-hideshow-comment.patch
#Patch7:         emacs-23.2-spacing.patch

# OSS: unsetenv() doesn't exist on Solaris 9:
Patch100:         emacs-solaris-build.patch

BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:	xpm libjpeg libtiff >= 3.5.7 libungif libpng3 xrender
BuildRequires:	xpm libjpeg-devel libtiff >= 3.5.7 libungif-devel libpng3-devel
Conflicts:	SFWemacs xemacs-b2m
Obsoletes:	emacs21 emacs-leim emacs-libexec


%description
Emacs is a real-time text editor that uses lisp as an extension language.
This is the base package; you need to install it whether you want emacs
with or without x support.

%package info
Group:          Applications/Editors
Summary:        Emacs info
Requires:       emacs = %{version}-%{release}
Requires:       info

%description info
Emacs info files

%package ctags
Group:          Applications/Editors
Summary:        Emacs ctags
Requires:       emacs = %{version}-%{release}
%description ctags
Ctags (and etags) makes editing programs with emacs a lot easier.


%prep
%setup -q
#%patch5 -p1 -b .m17ncheck
#%patch6 -p0 -b .hideshow-comment
#%patch7 -p1 -b .spacing
%patch100 -p1

cp %SOURCE7 %SOURCE9 %SOURCE10 site-lisp
cd site-lisp
%patch1 -p0
%patch3 -p0
cd ../

# We want -R/usr/local/lib passed first to the linker:
sed -i -e 's|\(X11_LDFLAGS =\)|\1 -L/usr/local/lib -R/usr/local/lib|' \
       -e 's|\(TEMACS_LDFLAGS =\)|\1 -L/usr/local/lib -R/usr/local/lib|' \
       src/Makefile.in

%build

%configure \
	CFLAGS='-O2 -g -m32 -mcpu=ultrasparc' \
	CXXFLAGS='-O2 -g -m32 -mcpu=ultrasparc' \
	FFLAGS='-O2 -g -m32 -mcpu=ultrasparc' \
	--srcdir=`pwd` \
	--with-png \
	--with-xpm \
	--with-jpeg=no \
	--with-png=no \
	--with-gif=no \
	--with-tiff=no \
	--with-x-toolkit=athena \
	--without-makeinfo \
    --without-dbus

gmake -j3

%clean
rm -rf $RPM_BUILD_ROOT

%install
rm -rf $RPM_BUILD_ROOT

gmake install DESTDIR=$RPM_BUILD_ROOT

# owned by info package, which is a Requires STUPID
rm -f $RPM_BUILD_ROOT/%{_infodir}/dir

# avoid Requires  rpmlib(PartialHardlinkSets) = 4.0.4-1 by changing to sym
#rm $RPM_BUILD_ROOT/usr/local/bin/emacs

mkdir -p %{buildroot}%{site_lisp}
install -p -m 0644 %SOURCE4 %{buildroot}%{site_lisp}/site-start.el
install -p -m 0644 %SOURCE18 %{buildroot}%{site_lisp}

mkdir -p %{buildroot}%{site_lisp}/site-start.d
install -p -m 0644 %SOURCE8 %SOURCE11 %SOURCE13 %{buildroot}%{site_lisp}/site-start.d

# hardlink badness GO AWAY
cd %{buildroot}/usr/local
/usr/local/bin/unhardlinkify.py ./

%post
#the build proccess puts a symlink in /usr/local/bin/emacs, we don't want this
if [ -L /usr/local/bin/emacs ]; then
	rm /usr/local/bin/emacs
fi
	
# Commented out. This should be done in cfengine!
#if [ ! -r /usr/local/bin/emacs ]; then
#        ln -s /usr/local/bin/emacs-%{version} /usr/local/bin/emacs
#        echo /usr/local/bin/emacs now points to /usr/local/bin/emacs-%{version}
#else
#	echo WARNING: You already have /usr/local/bin/emacs but this RPM put 
#	echo down /usr/local/bin/emacs-%{version}
#	echo You may wish to verify a symlink emacs to emacs-%{version}
#fi
cat <<EOF

If /mail is the mail directory on your system, you should run this as
root to enable movemail:

  cd /usr/local/libexec/emacs/%{version}/%{sparc_arch}/movemail
  chgrp 6 movemail && chmod g+s movemail

============================================================================

In order to use emacs you must symlink the binary as such:

  ln -s /usr/local/bin/emacs-%{version} /usr/local/bin/emacs

EOF


%post info
if [ -x /usr/local/bin/install-info ] ; then
    for i in %{info_files}; do
        /usr/local/bin/install-info --info-dir=%{_infodir} \
             %{_infodir}/$i &> /dev/null ||:
    done
fi


%preun info
if [ -x /usr/local/bin/install-info ] ; then
    for i in %{info_files}; do
        /usr/local/bin/install-info --delete --info-dir=%{_infodir} \
             %{_infodir}/$i &> /dev/null ||:
    done
fi


%files
%defattr(-, root, root, -)
%doc BUGS COPYING ChangeLog INSTALL README
%{_datadir}/emacs/
%{_bindir}/ebrowse
%{_bindir}/emacs
%{_bindir}/emacs-%{version}
%{_bindir}/emacsclient
%{_bindir}/grep-changelog
%{_bindir}/rcs-checkin
%{_libexecdir}/emacs
%{_datadir}/applications/emacs.desktop
%{_datadir}/icons/hicolor/*/*/*
%{_mandir}/man1/emacsclient.1.gz
%{_mandir}/man1/emacs.1.gz
%{_mandir}/man1/ebrowse.1.gz
%{_mandir}/man1/grep-changelog.1.gz
%{_mandir}/man1/rcs-checkin.1.gz
%{_localstatedir}/games/emacs/


%files info
%defattr(-, root, root, -)
%{_infodir}/*


%files ctags
%defattr(-, root, root, -)
%{_bindir}/etags
%{_bindir}/ctags
%{_mandir}/man1/etags.1.gz
%{_mandir}/man1/ctags.1.gz

%changelog
* Mon Mar 25 2013 Kaitlin Poskaitis <katiepru@nbcs.rutgers.edu> - 24.1-1
- Requiring xrender

* Mon Aug 27 2012 Josh Matthews <jmatth@nbcs.rutgers.edu> - 24.1-1
- version bump
- disabling jpeg and tiff support
- fixing patch 100 for new source code
- removing patches 5, 6, and 7

* Wed Aug 25 2010 Orcan Ogetbil <orcan@nbcs.rutgers.edu>
- Rebuild using --without-dbus

* Tue Aug 24 2010 Orcan Ogetbil <orcan@nbcs.rutgers.edu> - 23.2-1
- Major clean-up in the specfile
- Import some Fedora patches
- Update to the latest version

* Wed Aug 04 2010 Orcan Ogetbil <orcan@nbcs.rutgers.edu> - 23.1-3
- Remove /usr/local/share/info/dir

* Mon Oct 19 2009 Jarek Sedlacek <jarek@nbcs.rutgers.edu> - 23.1-2
- added post install script to make sure /usr/local/bin/emacs not exist
* Tue Oct 06 2009 Jarek Sedlacek <jarek@nbcs.rutgers.edu> - 23.1-1
- update to latest version
* Wed Sep 24 2008 David Diffenbaugh <davediff@nbcs.rutgers.edu> - 22.3-1
- bump
* Wed Apr 9 2008 Naveen Gavini <ngavini@nbcs.rutgers.edu> - 22.2-2
- Updated to the latest version.
* Mon Aug 13 2007 David Lee Halik <dhalik@nbcs.rutgers.edu> - 22.1-2
- Fixed Post path for emacs movemail
* Fri Aug 10 2007 David Lee Halik <dhalik@nbcs.rutgers.edu> - 22.1-1
- Bumped to 22
- Removed auto symlink in preference of cfengine

