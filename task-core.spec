Name: task-core
Version: 1.0
Release: 1ru
Summary: Default packages to install on a generic machine.
Group: Administration
License: ---

Requires: bash
Requires: cpdir
Requires: pam
Requires: slide
Requires: tcp_wrappers
Requires: tcsh

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

