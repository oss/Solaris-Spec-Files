Summary: Jabber IM Server with PAM Authentication  
Name: jabberd-PAM 
Version: 1.4.2
Release: 15
Group: Applications/Internet 
Copyright: GPL
Source0: jabber-1.4.2.tar.gz
Source1: jabberd-pamauth-0.1.tar.gz
Source2: jabberd-extras-0.2.tar.gz
Source3: ru-mu-conference-0.5.2.tar.gz
BuildRoot: /var/tmp/%{name}-root
Requires: perl-module-Jabber-Connection openssl

Patch: rutgers-mu-conference.patch

%description
This is the server for the Jabber Instant Messaging system.  It has been hacked by cwawak to allow for RU PAM support, through the use of many diverse Perl modules.  It has been tested and known to work on 64 Bit Solaris 9 installations.  Other platforms would require more work.  If you need it to work on anything besides Solaris 9, contact OSS at oss@nbcs.rutgers.edu. 


%prep
%setup -q -n jabber-1.4.2  
%setup -D -T -a 1 -n jabber-1.4.2
%setup -D -T -a 2 -n jabber-1.4.2
%setup -D -T -a 3 -n jabber-1.4.2

%build
PATH="/usr/openwin/bin:/usr/local/bin:/opt/SUNWspro/bin:/usr/local/gnu/bin:/usr/ccs/bin:/usr/bin:/usr/ucb:/usr/sbin"
./configure --enable-ssl
mv platform-settings.new platform-settings
CFLAGS="-I/usr/local/ssl/include/openssl -I/usr/local/ssl/include -DHAVE_SSL -I/usr/local/jabber-1.4pre2/jabberd/pth-1.3.7 -g -Wall -" make 

cd mu-conference-0.5.2/src
patch < /usr/local/src/rpm-packages/SOURCES/rutgers-mu-conference.patch
gmake
cd ../..

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/local/doc
cd ..
mkdir -p %{buildroot}/etc/init.d/
mv jabber-1.4.2/jabberd.startup %{buildroot}/etc/init.d/jabberd
mv jabber-1.4.2 %{buildroot}/usr/local/
mkdir jabber-1.4.2
cd %{buildroot}/usr/local/jabber-1.4.2
mv jabber.xml.example jabber.xml.example.ru
mv jabber.xml jabber.xml.example

rm -rf cygwin
rm `/usr/local/gnu/bin/find . -iname \*.h`
rm `/usr/local/gnu/bin/find . -iname \*.c`
rm `/usr/local/gnu/bin/find . -iname \*.o`
rm `/usr/local/gnu/bin/find . -iname Makefile`
rm `/usr/local/gnu/bin/find . -iname platform-settings`

%clean
rm -rf %{buildroot}

%post
cat <<EOF
Read the README file before you go any further!

EOF


%files
%defattr(-,jabberd,nobody)
/usr/local/jabber-1.4.2/*
%attr(755, root, root) /usr/local/doc
/etc/init.d/jabberd
%attr(755, root, root) /etc/init.d/jabberd
%changelog

* Mon Jan 27 2003 Christopher Wawak <cwawak@nbcs.rutgers.edu>
 - OpenSSL is still required.  Jabberd is built with SSL support ONLY.
    Also added conferencing.

* Fri Dec  6 2002 Christopher Wawak <cwawak@nbcs.rutgers.edu>
 - Implemented preliminary SSL support.  Package now requires 
    OpenSSL.

* Mon Dec  2 2002 Christopher Wawak <cwawak@nbcs.rutgers.edu>
 - Fixed RPM Issues

* Mon Nov 25 2002 Christopher Wawak <cwawak@nbcs.rutgers.edu>
 - Changed structure of package.

* Fri Nov 08 2002 Christopher Wawak <cwawak@nbcs.rutgers.edu>
 - Changed minor scripting issues.

* Mon Nov 04 2002 Christopher Wawak <cwawak@nbcs.rutgers.edu>
 - Added changelog, built new package with documentation per roy's
         request
