Summary: Nano: GNU version of pico
Name: nano
Version: 1.0.5
Release: 1
Copyright: GPL
Group: Applications/Editors
Source: http://www.nano-editor.org/dist/v1.0/nano-1.0.5.tar.gz
URL: http://www.nano-editor.org
Distribution: RU-Solaris
Vendor: NBCS-OSS
Packager: Christopher J. Suleski <chrisjs@nbcs.rutgers.edu>
BuildRoot: %{_tmppath}/%{name}-root


%description
GNU Nano is designed to be a free replacement for the Pico text editor, part of the PINE email suite from The University of Washington.  It aims to emulate Pico as closely as possible and perhaps include extra functionality.

%prep
 mkdir -p $RPM_BUILD_ROOT
 cd $RPM_BUILD_ROOT/
 rm -rf *
 zcat $RPM_SOURCE_DIR/nano-1.0.5.tar.gz | tar -xvf -

%setup -q -n nano-1.0.5

%build
 LD="/usr/ccs/bin/ld -L/usr/local/lib -R/usr/local/lib" \
  LDFLAGS="-L/usr/local/lib -R/usr/local/lib" ./configure --with-history \
  --with-readline
 make

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/local
make install prefix=$RPM_BUILD_ROOT/usr/local sysconfdir=$RPM_BUILD_ROOT/etc

%clean
rm -rf $RPM_BUILD_ROOT

%files
/usr/local/lib/locale/*/LC_MESSAGES/nano.mo
/usr/local/bin/nano
/usr/local/info/nano.info
/usr/local/man/man1/nano.1




