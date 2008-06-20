Summary:	GTK Monitoring Tool 
Name:		gkrellm
Version:	2.3.1
Release:        1
Copyright:	GPL
Group:		Applications/Multimedia
Source:		%{name}-%{version}.tar.gz
Patch:		%{name}.patch
Distribution: 	RU-Solaris
Vendor: 	NBCS-OSS
Packager: 	Brian Schubert <schubert@nbcs.rutgers.edu>
BuildRoot:	/var/tmp/%{name}-%{version}-root
BuildRequires:	atk-devel, gtk2-devel, glib2-devel, cairo-devel, pango-devel

%description
GKrellM is a single process stack of system monitors which supports 
applying themes to match its appearance to your window manager, Gtk, or 
any other theme.

    *  Hostname/systemname display.
    * Clock/calendar.
    * SMP CPU monitor that can chart individual CPUs and/or a composite 
CPU.
    * Temperature, fan, and voltage sensor monitors if supported by the 
kernel and the mainboard hardware. Linux requires lm_sensors modules, 
sysfs sensors for kernels >= 2.6.0 or a running mbmon daemon. Sensors 
can also be read from mbmon on FreeBSD. On Linux, you can also monitor 
disk temperatures from the hddtemp daemon and nvidia GPU temperatures 
if nvidia-settings is installed.
      Each sensor monitor has a configurable alarm and warning.
    * Process monitor with a chart for load and forks and a display of 
number of current processes and users.
    * Disk monitor that can chart individual disks or a composite disk.
    * Internet monitor (http, ftp, ...) that displays current tcp port 
connections and charts historical port hits for over two days.
    * Net interface monitors with charts for all routed net interfaces. 
Data rx/tx LEDs and a timer button that can be linked to a ppp or isdn 
net interface and displays on line time.
    * Memory and swap space usage meters, and a swap page in/out chart.
    * File system meters which show capacity/free space and can 
mount/umount.
    * A mailbox monitor which can launch a mail reader, a mail 
fetch/check program, and a sound notify command. Builtin new mail 
message checking for mbox, maildir, MH, POP3, and IMAP mailboxes.
    * APM laptop battery meter with a configurable alarm and warning 
for low battery time left.
    * Uptime display.

    * Multiple monitors managed by a single process to reduce system 
load.
    * Charts have auto scaling or fixed scaling modes.
    * Commands can be configured to run when monitor labels are 
clicked.
    * gkrellm can run in client mode and collect data from a gkrellmd 
server running on a remote machine.
    * Both gkrellm and the gkrellmd server are plugin capable so 
special interest monitors can be coded.

%package devel 
Summary: Libraries, includes to develop applications with %{name}.
Group: Applications/Libraries
Requires: %{name} = %{version}

%description devel
The %{name}-devel package contains the header files and static libraries
for building applications which use %{name}.

%prep
%setup -q
%patch -p1

%build
PATH="/opt/SUNWspro/bin:${PATH}" \
CC="cc" CXX="CC" CPPFLAGS="-I/usr/local/include" \
LD="/usr/ccs/bin/ld" \
LDFLAGS="-L/usr/local/lib -R/usr/local/lib -lnsl" \
export PATH CC CXX CPPFLAGS LD LDFLAGS

for i in `find . -name Makefile`
do mv $i $i.wrong
sed -e 's/$(MAKE) install INSTALL=\/usr\/ucb\/install/$(MAKE) install INSTALL=\/usr\/local\/gnu\/bin\/install/g' \
-e 's/chgrp sys $(INSTALLDIR)\/$(PACKAGE)//g' \
-e 's/chgrp sys $(SINSTALLDIR)\/$(PACKAGE_D)//g' \
-e 's/enable_nls=1/enable_nls=0/g' \
-e 's/gcc/cc/g' \
-e 's/-Wall//g' \
-e 's/-Wno-implicit-int//g' \
-e 's/-O2/-xO2/g' \
-e 's/-lsocket/-lsocket -lnsl/g' \
-e 's/-lintl//g' \
$i.wrong > $i; rm $i.wrong; done

gmake solaris

%install
rm -rf $RPM_BUID_ROOT

gmake install_solaris DESTDIR=$RPM_BUILD_ROOT/usr/local

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,bin,bin)
/usr/local/bin/*
/usr/local/share/*

%files devel
%defattr(-,root,root)
/usr/local/include/*
/usr/local/lib/pkgconfig/*

%changelog
* Fri Jun 20 2008 Brian Schubert <schubert@nbcs.rutgers.edu> - 2.3.1-1
- Modified gkrellm.patch, Updated to version 2.3.1
* Sat Nov 17 2007 David Lee Halik <dhalik@nbcs.rutgers.edu> - 2.3.0-1
- Bump to 2.3.0
- Disable NLS
* Tue May 30 2006 Leo Zhadanovsky <leozh@nbcs.rutgers.edu> - 2.2.9-1
- Initial Rutgers release
