%define name    nano
%define ver     1.3.11
%define rel     2

Summary: 	Nano: GNU version of pico
Name: 		%{name}
Version: 	%{ver} 
Release: 	%{rel}
Copyright: 	GPL
Group: 		Applications/Editors
Source: 	http://www.nano-editor.org/dist/v1.3/%{name}-%{ver}.tar.gz
URL: 		http://www.nano-editor.org
Distribution: 	RU-Solaris
Vendor: 	NBCS-OSS
Packager:       Leo Zhadanovsky <leozh@nbcs.rutgers.edu>
BuildRoot: 	%{_tmppath}/%{name}-root


%description
GNU Nano is designed to be a free replacement for the Pico text editor,
part of the PINE email suite from The University of Washington.  It aims
to emulate Pico as closely as possible and perhaps include extra functionality.

%prep
%setup -q

%build
#CC="gcc" CFLAGS="-I/usr/local/include" \
#LDFLAGS="-R/usr/local/lib -L/usr/local/lib" \
#  ./configure --prefix=/usr/local
#gmake

PATH="/opt/SUNWspro/bin:${PATH}" \
CC="cc" CXX="CC" CPPFLAGS="-I/usr/local/include" \
LD="/usr/ccs/bin/ld" \
LDFLAGS="-L/usr/local/lib -R/usr/local/lib" \
export PATH CC CXX CPPFLAGS LD LDFLAGS

./configure --prefix=/usr/local

gmake

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}
gmake install DESTDIR=%{buildroot}
rm %{buildroot}/usr/local/info/dir

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
EOF

%preun
if [ -x /usr/local/bin/install-info ] ; then
	/usr/local/bin/install-info --delete --info-dir=/usr/local/info \
	         /usr/local/info/nano.info
fi

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
/usr/local/bin/nano
/usr/local/info/nano.info
/usr/local/man/man1/nano.1
/usr/local/man/man1/rnano.1
/usr/local/man/man5/nanorc.5
/usr/local/man/fr/man1/nano.1
/usr/local/man/fr/man5/nanorc.5
/usr/local/share/locale/*

%changelog
* Thu Apr 27 2006 Leo Zhadanovsky <leozh@nbcs.rutgers.edu> - 1.3.11-1
- Changed over to Sun CC, cleaned up spec file, updated to latest devel version
