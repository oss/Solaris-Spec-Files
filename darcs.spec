Summary: David's advanced revision control system
Name: darcs
Version: 1.0.3
Release: 1
License: GPL
Group: Development/Tools
URL: http://www.darcs.net
Source0: %{name}-%{version}.tar.gz
Buildrequires: ghc
BuildRoot: %{_tmppath}/%{name}-%{version}-root

%description 
Darcs is a revision control system, along the lines of CVS
or arch. That means that it keeps track of various revisions
and branches of your project, allows for changes to
propogate from one branch to another. Darcs is intended to
be an ``advanced'' revision control system. Darcs has two
particularly distinctive features which differ from other
revision control systems: 1) each copy of the source is a
fully functional branch, and 2) underlying darcs is a
consistent and powerful theory of patches.

%package server
Summary: David's advanced revision control system Server
Group: Development/Tools
Requires: httpd

%description server
Darcs is a revision control system, along the lines of CVS
or arch. That means that it keeps track of various revisions
and branches of your project, allows for changes to
propogate from one branch to another. Darcs is intended to
be an ``advanced'' revision control system. Darcs has two
particularly distinctive features which differ from other
revision control systems: 1) each copy of the source is a
fully functional branch, and 2) underlying darcs is a
consistent and powerful theory of patches.

This package contains the darcs cgi server program.

# the debuginfo subpackage is currently empty anyway, so don't generate it
%define debug_package %{nil}
%define __spec_install_post /usr/lib/rpm/brp-compress

%prep
%setup -q

%build
LDFLAGS="-L/usr/local/lib -R/usr/local/lib"
LD_LIBRARY_PATH="/usr/local/lib"
export LDFLAGS LD_LIBRARY_PATH

./configure --libexecdir=/srv/www --without-curses --disable-profile
gmake all
#make check

%install
rm -rf $RPM_BUILD_ROOT
gmake DESTDIR=%buildroot installbin installserver

rm -r %buildroot%{_sysconfdir}/bash_completion.d

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%{_bindir}/darcs
%{_mandir}/man1/*
%doc AUTHORS COPYING ChangeLog manual darcs_completion zsh_completion_*

%files server
%defattr(-,root,root,-)
/srv/www/cgi-bin
%{_sbindir}/darcs-createrepo
%{_sysconfdir}/darcs
%{_datadir}/darcs

