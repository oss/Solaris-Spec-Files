Summary: Jabber IM Server 
Name: jabberd-PAM 
Version: 1.4.2
Release: 1 
Group: Applications/Internet 
Copyright: GPL
Source: jabberd-1.4.2_RU1.tar.gz
BuildRoot: /var/tmp/%{name}-root
Requires: perl-module-Jabber-Connection

%description
This is the server for the Jabber Instant Messaging system.  It has been hacked by cwawak to allow for RU PAM support, through the use of many diverse Perl modules.  It has been tested and known to work on 64 Bit Solaris 9 installations.  Other platforms would require more work.  If you need it to work on anything besides Solaris 9, contact OSS at oss@nbcs.rutgers.edu. 


%prep
%setup -n jabberd  

%build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/local/
cd ..
mv jabberd %{buildroot}/usr/local/
mkdir jabberd

%clean
rm -rf %{buildroot}

cat <<EOF
Before you start jabberd, make sure you have an appropriate jabberd
entry in your pam.conf file. Something like this may be appropriate:

jabberd auth    required        /usr/lib/security/pam_ru.so.2 debug become

Also, you must change the jabber.xml file to your requirements.  At the least, 
replace all "localhost" entries with the name of the hostname that you are
running the server on.  Finally, create a directory in /usr/local/jabberd/spool
that is the name of your hostname, such as eden.rutgers.edu if this would be
installed on eden.  This is where the XML spool files are stored, so make sure
that the directory can be read and written to by the jabberd user.  Finally,
to start jabberd:

#(make sure the pid files are gone)
rm /usr/local/jabberd/*pid
#(start the jabberd binary)
/usr/local/jabberd/jabberd -h . -c ./jabber.xml &
#(start the pam authentication layer)
/usr/local/jabberd/jabberdpamauth.pl &


EOF


%files
%defattr(-,jabberd,nobody)
/*
