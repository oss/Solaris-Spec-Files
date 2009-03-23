Summary:	Curses Emulation Library
Name:		ncurses
Version:	5.7
Release:        1
License:	MIT
Group:		System Environment/Libraries
Source:		%{name}-%{version}.tar.gz
Distribution: 	RU-Solaris
Vendor: 	NBCS-OSS
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root

%description
The Ncurses (new curses) library is a free software emulation of curses in 
System V Release 4.0, and more. It uses Terminfo format, supports pads and 
color and multiple highlights and forms characters and function-key 
mapping, and has all the other SYSV-curses enhancements over BSD Curses.

The ncurses code was developed under GNU/Linux. It should port easily to 
any ANSI/POSIX-conforming UNIX. It has even been ported to OS/2 Warp!

The distribution includes the library and support utilities, including a 
terminfo compiler tic, a decompiler infocmp, clear, tput, tset, and a 
termcap conversion tool captoinfo. Full manual pages are provided for the 
library and tools.

The Ncurses distribution is available via anonymous FTP at the GNU 
distribution site http://ftp.gnu.org/pub/gnu/ncurses.
It is also available at ftp://invisible-island.net/ncurses/.

%package devel 
Summary:	Development files for the ncurses library
Group:		System Environment/Libraries
Requires:	ncurses = %{version}-%{release}

%description devel
The ncurses-devel package contains the header files and developer 
documentation for the ncurses library

%package static
Summary:	Static libraries for the ncurses library
Group:		System Environment/Libraries
Requires:	ncurses-devel = %{version}-%{release}

%description static
The ncurses-static package includes static libraries of the ncurses library.

%prep
%setup -q

%build
PATH="/opt/SUNWspro/bin:${PATH}" 
CC="cc" CXX="CC"
CPPFLAGS="-I/usr/local/include" 
LD="/usr/ccs/bin/ld" 
LDFLAGS="-L/usr/local/lib -R/usr/local/lib"
export PATH CC CXX CPPFLAGS LD LDFLAGS

./configure \
	--prefix=%{_prefix}			\
	--mandir=%{_mandir}			\
	--with-shared 				\
	--enable-termcap 			\
	--enable-symlinks 			\
	--enable-bsdpad 			\
	--with-rcs-ids 				\
	--enable-sigwinch 			\
	--enable-tcap-names 			\
	--enable-widec 				\
	--enable-ext-colors 			\
	--with-install-prefix=%{buildroot}

gmake

%install
rm -rf %{buildroot}

make install DESTDIR=%{buildroot}

cd %{buildroot}%{_libdir}

ln -s libformw.so libform.so; ln -s libformw.so.6 libform.so.6; ln -s libformw.so.6.0 libform.so.6.0

ln -s libmenuw.so libmenu.so; ln -s libmenuw.so.6 libmenu.so.6; ln -s libmenuw.so.6.0 libmenu.so.6.0

ln -s libncursesw.so libncurses.so; ln -s libncursesw.so.6 libncurses.so.6; ln -s libncursesw.so.6.0 libncurses.so.6.0

ln -s libpanelw.so libpanel.so; ln -s libpanelw.so.6 libpanel.so.6; ln -s libpanelw.so.6.0 libpanel.so.6.0

cd ../include
ln -s ncursesw ncurses

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc README NEWS AUTHORS ANNOUNCE
%{_bindir}/*
%{_libdir}/*.so.*
%{_libdir}/terminfo
%{_datadir}/*
%{_mandir}/man1/*
%{_mandir}/man5/*
%{_mandir}/man7/*

%files devel
%defattr(-,root,root)
%{_includedir}/*
%{_libdir}/*.so
%{_mandir}/man3/*

%files static
%defattr(-,root,root)
%{_libdir}/*.a

%changelog
* Mon Mar 23 2009 Brian Schubert <schubert@nbcs.rutgers.edu> - 5.7-1
- Updated to version 5.7
- Moved symlinks to devel package
- Created a separate static package
* Mon Nov 20 2006 Leo Zhadanovsky <leozh@nbcs.rutgers.edu> - 5.5-1
- Made a whole new file for 5.5
