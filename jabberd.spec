Summary: Jabber IM Server 
Name: jabberd-PAM 
Version: 1.4.2
Release: 6 
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
mkdir -p %{buildroot}/etc/init.d/
mv jabberd/jabberd.startup %{buildroot}/etc/init.d/jabberd
mv jabberd %{buildroot}/usr/local/
mkdir jabberd

%clean
rm -rf %{buildroot}

%post
cat <<EOF
Read the README file before you go any further!

EOF


%files
%defattr(-,jabberd,nobody)
/*

%changelog
* Fri Nov 08 2002 Christopher Wawak <cwawak@nbcs.rutgers.edu>
 - Changed minor scripting issues.

* Mon Nov 04 2002 Christopher Wawak <cwawak@nbcs.rutgers.edu>
 - Added changelog, built new package with documentation per roy's
         request
	 
