Summary: Netscape web browser
Name: netscape6
Version: 6.2.3
Release: 1ru
Group: Applications/Internet
Copyright: NPL
Source: ns6-sol9.tar.bz2
Source1: http://download.macromedia.com/pub/shockwave/flash/english/solaris/5.0r55/flash_solaris.tar.gz
BuildRoot: /var/tmp/%{name}-root
Patch: netscape6-startscript.patch

%description
Netscape Communicator offers the complete set of tools for browsing
dynamic web content, plus full-strength email and easy-to-use
groupware.

%prep
%setup -q -n usr
%patch -p1

%install
cp  ../../SOURCES/flash_solaris.tar.gz ./
gunzip flash_solaris.tar.gz
tar xvf flash_solaris.tar
mv flash_solaris/libflashplayer.so flash_solaris/ShockwaveFlash.class dt/appconfig/SUNWns6/plugins/
cd dt/appconfig
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/local $RPM_BUILD_ROOT/usr/local/bin
mv -f SUNWns6 $RPM_BUILD_ROOT/usr/local/netscape-6.2.3
#mv -f * $RPM_BUILD_ROOT/usr/local/netscape-6.2.3
cd $RPM_BUILD_ROOT/usr/local/netscape-6.2.3
rm java components/libjavaplugin_oji.so
ln -sf ../../../j2se/jre java
ln -sf ../../../j2se/jre/plugin/sparc/ns610/libjavaplugin_oji.so components/libjavaplugin_oji.so
cd $RPM_BUILD_ROOT/usr/local/bin
ln -sf ../netscape-6.2.3/netscape netscape6 

%files
%defattr(-,bin,bin)
/usr/local/netscape-6.2.3
%config(noreplace)/usr/local/bin/netscape6
