%define name    nano
%define ver     2.1.4
%define rel     1

Summary: 	Nano: GNU version of pico
Name: 		%{name}
Version: 	%{ver} 
Release: 	%{rel}
Copyright: 	GPL
Group: 		Applications/Editors
Source: 	http://www.nano-editor.org/dist/v2.0/%{name}-%{ver}.tar.gz
URL: 		http://www.nano-editor.org
Distribution: 	RU-Solaris
Vendor: 	NBCS-OSS
Packager:       Brian Schubert <schubert@nbcs.rutgers.edu>
BuildRoot: 	%{_tmppath}/%{name}-root
Requires: aspell aspell-en
BuildConflicts: ncurses ncurses-devel

%description
GNU Nano is designed to be a free replacement for the Pico text editor,
part of the PINE email suite from The University of Washington.  It aims
to emulate Pico as closely as possible and perhaps include extra functionality.

%prep
%setup -q

%build
PATH="/opt/SUNWspro/bin:${PATH}" \
CC="cc" CXX="CC" CPPFLAGS="-I/usr/local/include" \
LD="/usr/ccs/bin/ld" \
LDFLAGS="-L/usr/local/lib -R/usr/local/lib" \
export PATH CC CXX CPPFLAGS LD LDFLAGS

./configure --prefix=/usr/local --enable-all --disable-nls \
	    --mandir=/usr/local/man --infodir=/usr/local/info

gmake

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT
gmake install DESTDIR=$RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/local/etc
cat $RPM_BUILD_ROOT/usr/local/share/nano/* >> $RPM_BUILD_ROOT/usr/local/etc/nanorc

#We want aspell to be the spellchecker used by default at Rutgers
#so we need to append the following information to the nanorc file
echo '#RUTGERS addded config for aspell
set speller "aspell -c"' >> $RPM_BUILD_ROOT/usr/local/etc/nanorc

%post
if [ -x /usr/local/bin/install-info ] ; then
	/usr/local/bin/install-info --info-dir=/usr/local/info \
	         /usr/local/info/nano.info
fi
cat<<EOF

                   :::
     iLE88Dj.  :jD88888Dj:                                           
   .LGitE888D.f8GjjjL8888E;        .d8888b.  888b    888 888     888 
   iE   :8888Et.     .G8888.      d88P  Y88b 8888b   888 888     888 
   ;i    E888,        ,8888,      888    888 88888b  888 888     888 
         D888,        :8888:      888        888Y88b 888 888     888 
         D888,        :8888:      888  88888 888 Y88b888 888     888 
         D888,        :8888:      888    888 888  Y88888 888     888 
         D888,        :8888:      Y88b  d88P 888   Y8888 Y88b. .d88P 
         888W,        :8888:       "Y8888P88 888    Y888  "Y88888P"  
         W88W,        :8888:                                         
         W88W:        :8888:      88888b.   8888b.  88888b.   .d88b. 
         DGGD:        :8888:      888 "88b     "88b 888 "88b d88""88b
                      :8888:      888  888 .d888888 888  888 888  888
                      :W888:      888  888 888  888 888  888 Y88..88P
                      :8888:      888  888 "Y888888 888  888  "Y88P" 
                       E888i                                         
                       tW88D

Note: At Rutgers aspell is the spell checking program of choice.
If you wish to use spell or some other spell checker you need
to alter or remove the last line of /usr/local/etc/nanorc or create
your own ~/.nanorc file.
EOF

%preun
if [ -x /usr/local/bin/install-info ] ; then
	/usr/local/bin/install-info --delete --info-dir=/usr/local/info \
	         /usr/local/info/nano.info
fi

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
/usr/local/bin/nano
/usr/local/bin/rnano
/usr/local/etc/*
/usr/local/info/nano.info
/usr/local/man/man1/nano.1
/usr/local/man/man1/rnano.1
/usr/local/man/man5/nanorc.5
/usr/local/share/nano/*

%changelog
* Thu Aug 14 2008 Brian Schubert <schubert@nbcs.rutgers.edu> - 2.1.4-1
- Fixed man/info paths and bumped to 2.1.4
* Tue Mar 11 2008 David Diffenbaugh <davediff@nbcs.rutgers.edu> - 2.0.7-2
- added config to allow aspell, added BuildConflicts: ncurses ncurses-devel 
* Mon Jan 07 2008 David Diffenbaugh <davediff@nbcs.rutgers.edu> - 2.0.7-1
- Updated to 2.0.7
* Sun Apr 29 2007 Kevin Mulvey <kmulvey@nbcs.rutgers.edu> - 2.0.6-1
- Updated to 2.0.6
* Wed Apr 25 2007 Kevin Mulvey <kmulvey@nbcs.rutgers.edu> - 2.0.5-1
- Updated to 2.0.5
* Mon Nov 20 2006 Leo Zhadanovsky <leozh@nbcs.rutgers.edu> - 2.0.1-1
- Updated to 2.0.1
* Wed Sep 13 2006 David Lee Halik <dhalik@nbcs.rutgers.edu> - 1.3.12-2
- Updated to latest devel version. Fixed info path.

