#Depricated/EOL package
IgnoreOS: Solaris

Name: task-generic-production
Version: 1.0
Release: 1ru
Summary: Default packages to install on a generic machine.
Group: Administration
License: ---

Requires: bash
Requires: become
Requires: bind
Requires: bind-dnstools
Requires: cops
Requires: cpdir
Requires: emacs-X11
Requires: fvwm
Requires: gnu-standards
Requires: grubs
Requires: info
Requires: ispell
Requires: less
Requires: m4
Requires: mail.local
Requires: maillock
Requires: mlock
Requires: netscape
Requires: nn
Requires: pam
Requires: pgp
Requires: pine
Requires: plp
Requires: procmail
Requires: qmail
Requires: ru-rdist
Requires: ru-rsh
Requires: slide
Requires: sos-utils
Requires: tcp_wrappers
Requires: tcsh
Requires: teTeX
Requires: texinfo
Requires: traceroute
Requires: tvtwm
Requires: wpwhois
Requires: xanim
Requires: xpm
Requires: xrsh
Requires: xv
Requires: zap

%description
This package contains no actual files.  It is used with apt to automatically
install all required subpackages.

These packages comprise the suggested generic install.  Used in the automated
install process at Rutgers University.

# nothing to do 
# files section required or no rpm will be built

%prep

%build

%install

%clean

%files

