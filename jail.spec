Summary: Utilities for producing a chroot jail
Name: jail
Version: 1.9
Release: 2
License: GPL
Group: System/Utilities
Source: jail_1.9.tar.gz
Patch0: jail-solaris.patch
Patch1: jail-roy.patch
BuildRoot: /var/tmp/%{name}-root
URL: http://www.gsyc.inf.uc3m.es/~assman/jail
Requires: perl

%description
Jail is a login tool. Jail works as a wrapper to the user shell, so when
the user log in the machine Jail is launched, and the chrooted environment
is activated. Then, Jail execs the real user shell, so he gets his session
in the server.

%prep 
%setup -q -n jail_1-9_stable
%patch -p1

# The patch0 changes Makefile to use __SOLARIS__ and /usr/local/bin/perl.
# The patch1 makes changes that Roy wants in the Perl scripts.

%build
cd src
make

%install
cd src
rm -rf $RPM_BUILD_ROOT
make install INSTALL_DIR=$RPM_BUILD_ROOT/usr/local

%clean
rm -rf $RPM_BUILD_ROOT

%post
cat <<EOF
Make sure to run the scripts to setup /var/chroot and other important
items. See the webpage http://www.gsyc.inf.uc3m.es/~assman/jail for
details.

/usr/local/bin/jail has been installed setuid root.
EOF

%files
# The permissions that jail's make install uses are pretty crazy.
%defattr(4711,root,root)
/usr/local/bin/jail
%defattr(755,root,root)
/usr/local/bin/addjailsw
/usr/local/bin/addjailuser
/usr/local/bin/mkjailenv
%defattr(644,root,root)
/usr/local/etc/*
/usr/local/lib/libjail.pm
/usr/local/lib/arch/*
