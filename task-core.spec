Name: task-core
Version: 1.3
Release: 1ru
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

%clean

%files

