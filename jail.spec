Summary: Utilities for producing a chroot jail
Name: jail
Version: 1.9
Release: 8
License: GPL
Group: System/Utilities
Source: jail_1.9.tar.gz
Patch0: jail-solaris.patch
Patch1: jail-roy-20020204.patch
Patch2: jail-makeinstallpath.patch
BuildRoot: /var/tmp/%{name}-root
URL: http://www.gsyc.inf.uc3m.es/~assman/jail
Requires: perl

%description
Jail is a login tool. Jail works as a wrapper to the user shell, so when
the user log in the machine Jail is launched, and the chrooted environment
is activated. Then, Jail execs the real user shell, so he gets his session
in the server.

%prep 
PATH=/usr/local/gnu/bin:$PATH
export PATH
%setup -q -n jail_1-9_stable
PATH=/usr/local/gnu/bin:$PATH
export PATH
# these used to be all %patch -p1
%patch -p1 
%patch1 -p1
%patch2 -p1

# The patch0 changes Makefile to use __SOLARIS__ and /usr/local/bin/perl.
# The patch1 makes changes that Roy wants in the Perl scripts.

%build
cd src
make

%install
cd src
rm -rf $RPM_BUILD_ROOT
make install INSTALL_DIR=$RPM_BUILD_ROOT/usr/local
cd $RPM_BUILD_ROOT/usr/local


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
/usr/local/etc/jail.conf
/usr/local/lib/libjail.pm
/usr/local/lib/arch

%changelog
* Tue Oct 8 2002 Aaron Richton <richton@nbcs.rutgers.edu>
export PATH to make sure that GNU patch is used

* Thu Feb 4 2002 Christopher Suleski <chrisjs@nbcs.rutgers.edu>
- Changed path patch to patch the install script and not the 
  actual program after installation. Updated Roy's patched.

* Thu Jan 31 2002 Christopher Suleski <chrisjs@nbcs.rutgers.edu>
- Added jail-path.patch that fixed the hard paths encoded in the
  perl scripts not to be inside the build root. Also fixed the 
  SPEC and patch file so Roy's fixed got in.
