Summary: Interactive, three-dimensional ps
Name: psdoom
Version: 2000.05.03
Release: 2
Group: Applications/Productivity
License: GPL
Source0: %{name}-%{version}-src.tar.gz
Source1: %{name}-%{version}-data.tar.gz
Source2: doom-1.8.wad.gz
Patch: psdoom.patch
BuildRequires: make patch
Requires: perl
BuildRoot: /var/tmp/%{name}-root
%description
psDooM is a process monitor and manager for *nix systems.
It could be considered a graphical interface to the 'ps', 'renice', and
'kill' commands.
psDooM is based on XDoom, which is based on id Software's 'Doom'.

This project started out as a proof-of-concept program for the web page
"Doom as a tool for system administration" at
http://www.cs.unm.edu/~dlchao/flake/doom by Dennis Chao at the University
of New Mexico.  Dennis took the GPL'd sources of XDoom and added code so
that processes running on the system would be instantiated as monsters,
and wounding and killing them corresponds to renicing and killing the
processes.

I (David Koppenhofer) loved the idea of combining two of my favorite
computer subjects (Linux and Doom).  Therefore, I began to enhance and
customize the program.

Goals of this project include:
1) Add even more functionality to the process manager such as the ability
   to send various kill signals and a way to shut down the machine
   _cleanly_ from the program.
2) Add networking support so multiple admins can work the machine at the
   same time and/or remotely administer a machine.
3) Everything else in the TODO file.
4) Possibly make other interfaces besides one to 'ps', such as a file
   management module.
5) Make psDooM the de-facto standard for graphical process manipulation
   on the *nix platform. :-)

%prep
%setup -q -n psdoom-src
%setup -D -T -a 1 -n psdoom-src
%patch -p1
gzip -dc $RPM_SOURCE_DIR/doom-1.8.wad.gz > doom1.wad

%build
cd xdoomsrc
make solsparc

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/local/man/man6
(cd xdoomsrc &&
 make install-solsparc DESTDIR=$RPM_BUILD_ROOT/usr)
cp psdoom-data/*wad $RPM_BUILD_ROOT/usr/local/games/psdoom
cp doom1.wad $RPM_BUILD_ROOT/usr/local/games/psdoom
cp xdoomsrc/doc/xdoom.6 $RPM_BUILD_ROOT/usr/local/man/man6
cp solaris/psxdoom-ps $RPM_BUILD_ROOT/usr/local/bin
chmod 755 $RPM_BUILD_ROOT/usr/local/bin/psxdoom-ps

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc psdoomdoc/*
%doc xdoomsrc/doc/COPYING xdoomsrc/doc/CREDITS xdoomsrc/doc/INSTALL
%doc xdoomsrc/doc/INSTRUCTIONS xdoomsrc/doc/PORTING xdoomsrc/doc/README
%doc xdoomsrc/doc/RELEASE.NOTES
/usr/local/bin/*
/usr/local/games/psdoom/*
/usr/local/lib/acc/xdoom
/usr/local/man/man6/*
