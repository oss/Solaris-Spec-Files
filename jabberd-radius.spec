Summary: Jabber IM Server with Radius Authentication  
Name: jabberd-radius
Version: 1.4.2
Release: 7
Group: Applications/Internet 
Copyright: GPL
Source0: jabber-1.4.2.tar.gz
Source1: jabberd-mod_auth_radius-RU.tar.gz
Source2: jabberd-extras-0.2.tar.gz
Source3: ru-mu-conference-0.5.2.tar.gz
Source4: xdb_sql-1.3.tar.gz

Patch: rutgers-mu-conference.patch
BuildRoot: /var/tmp/%{name}-root
Requires: radiusclient openssl mysql mysql-devel

%description
This is the server for the Jabber Instant Messaging system.  It has been altered by cwawak to allow for radius support.  It has been tested and known to work on 64 Bit Solaris 9 installations.  If you need it to work on anything besides Solaris 9, contact OSS at oss@nbcs.rutgers.edu.


%prep
%setup -n jabber-1.4.2  
%setup -D -T -a 1 -n jabber-1.4.2
%setup -D -T -a 2 -n jabber-1.4.2
%setup -D -T -a 3 -n jabber-1.4.2
%setup -D -T -a 4 -n jabber-1.4.2

%build
#PATH="/usr/openwin/bin:/usr/local/bin:/usr/local/gnu/bin:/usr/ccs/bin:/usr/bin:/usr/ucb:/usr/sbin"
#LD_LIBRARY_PATH="/usr/local/ssl/lib:/usr/local/radiusclient/lib:/usr/local/mysql/lib"
#LD_RUN_PATH="/usr/local/ssl/lib:/usr/local/radiusclient/lib:/usr/local/mysql/lib"
#LDFLAGS="-L/usr/local/ssl/lib -R/usr/local/ssl/lib -L/usr/local/radiusclient/lib -R/usr/local/radiusclient/lib -L/usr/local/mysql/lib -R/usr/local/mysql/lib"
#CPPFLAGS="-I/usr/local/ssl/include/openssl -I/usr/local/radiusclient/include -I/usr/local/mysql/include/mysql"
#LIBS="-lssl -lcrypto -ldl -lsocket -lnsl -lresolv -lradiusclient -lmysqlclient"
#LD="/usr/local/gnu/bin/ld"
#export CPPFLAGS LD_LIBRARY_PATH LD_RUN_PATH LDFLAGS LIBS LD
#cd /usr/local/src/rpm-packages/BUILD/
#cd jabber-1.4.2
./configure --enable-ssl
mv platform-settings.new platform-settings
cp platform-settings xdb_sql
gmake
cd mu-conference-0.5.2/src
patch < /usr/local/src/rpm-packages/SOURCES/rutgers-mu-conference.patch
gmake
cd ../..
cd jsm/modules
gmake
cd ../..
gmake
cd xdb_sql
gmake

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
rm Makefile configure platform-settings
rm -rf cygwin
rm `/usr/local/gnu/bin/find . -iname \*.h`
rm `/usr/local/gnu/bin/find . -iname \*.c`
rm `/usr/local/gnu/bin/find . -iname \*.o`
rm `/usr/local/gnu/bin/find . -iname Makefile`
rm `/usr/local/gnu/bin/find . -iname platform-settings`
rm -rf xdb_file
rm -rf spool

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

* Mon May 19 2003 Christopher Wawak <cwawak@nbcs.rutgers.edu>
 - Initial build.

