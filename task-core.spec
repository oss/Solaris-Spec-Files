Name: task-core
Version: 1.3
Release: 2ru
Summary: Default packages to install on a generic machine.
Group: Administration
License: ---

Requires: bash
Requires: bind-dnstools
Requires: binutils
Requires: cleanpath
Requires: cpdir
Requires: diffutils
Requires: emacs
Requires: emacs-X11
Requires: expect
Requires: fileutils
Requires: findutils
Requires: gawk
Requires: grep
Requires: gzip
Requires: less
Requires: lsof
Requires: m4
Requires: md5
Requires: pam
Requires: patchdiag
Requires: sh-utils
Requires: sharutils
Requires: slide
Requires: sos-utils
Requires: tar
Requires: task-ssh
Requires: tcp_wrappers
Requires: tcsh
Requires: time
Requires: top
Requires: rpm-tools



%description
This package contains no actual files.  It is used with apt to automatically
install all required subpackages.

These packages comprise the suggested "core" install.  They will be part of
every install.  Used in the automated install process at Rutgers University.

# nothing to do 
# files section required or no rpm will be built

%prep

%build

%install

%post
cat<<EOF
NOTICE NOTICE NOTICE NOTICE NOTICE NOTICE NOTICE NOTICE NOTICE NOTICE
NOTICE NOTICE NOTICE NOTICE NOTICE NOTICE NOTICE NOTICE NOTICE NOTICE
NOTICE NOTICE NOTICE NOTICE NOTICE NOTICE NOTICE NOTICE NOTICE NOTICE

     You are installing packages from the Solaris 8 64-bit
     sun-perl sun-gnome repository. This repository is deprecated
     and will no longer continue to be updated with new packages.
     
     From now on, the Solaris 8 64-bit repository is the only
     one for this OS and arch. It is built using a newer version
     of Perl and Sun's GNOME 1.4 Preview.
     
     Update your /usr/local/etc/apt/sources.list by changing:
         rpm-packages/sparc64-sun-solaris2.8_sun-perl,gnome
     to:
         rpm-packages/sparc64-sun-solaris2.8

     Complete an apt-get update. You may receive a few errors about
     the same version of a package having different dependencies.
     For this, run:
         apt-get install --reinstall packagename 
     Make sure to run this command for the task-core package, too.

NOTICE NOTICE NOTICE NOTICE NOTICE NOTICE NOTICE NOTICE NOTICE NOTICE
NOTICE NOTICE NOTICE NOTICE NOTICE NOTICE NOTICE NOTICE NOTICE NOTICE
NOTICE NOTICE NOTICE NOTICE NOTICE NOTICE NOTICE NOTICE NOTICE NOTICE
EOF
%clean

%files

