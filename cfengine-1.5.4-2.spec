Summary: attempting to build an RPM of cfengine
Name: cfengine
Version: 1.5.4
Release: 3
Copyright: GPL
Group: System Admin
Source: cfengine-1.5.4.tar.gz
BuildRoot: /var/tmp/%{name}-buildroot

%description
configure many machines from a central location
"less work ; more play"

%prep						#???
%setup 						#??? 

./configure

%build

LD="/usr/ccs/bin/ld -L/usr/local/lib -R/usr/local/lib" \
 
  LDFLAGS="-L/usr/local/lib -R/usr/local/lib" ./configure --with-history \
  --with-readline

make RPM_OPT_FLAGS="$RPM_OPT_FLAGS"

cd doc;
make;

%install
rm -rf SRPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/local/sbin/
mkdir -p $RPM_BUILD_ROOT/usr/local/share/
mkdir -p $RPM_BUILD_ROOT/usr/local/info/
mkdir -p $RPM_BUILD_ROOT/usr/local/man/man8/
mkdir -p $RPM_BUILD_ROOT/usr/local/share/cfengine/html/

make install prefix=$RPM_BUILD_ROOT/usr/local/

cd doc

make install prefix=$RPM_BUILD_ROOT/usr/local/


%clean

rm -rf $RPM_BUILD_ROOT

%post

echo  >> /etc/services "\ncfengine\t5308/tcp\t  #cfd"



if 
   [ -x /usr/local/bin/install-info ] ;   then

     for i in /usr/local/info/cfengine*.info
     do  /usr/local/bin/install-info --quiet $i /usr/local/info/dir;
     chmod 644 /usr/local/info/dir
     
     done  
   
fi 


%files
%defattr (-,root,root)
/usr/local/sbin/cfengine
/usr/local/sbin/cfd
/usr/local/sbin/cfrun
/usr/local/sbin/cfkey
/usr/local/sbin/cfdoc
/usr/local/share/cfengine/cfdaily
/usr/local/share/cfengine/cfwrap
/usr/local/share/cfengine/cfmail
/usr/local/share/cfengine/cf.linux.example
/usr/local/share/cfengine/cf.motd.example
/usr/local/share/cfengine/cf.preconf.example
/usr/local/share/cfengine/cf.site.example
/usr/local/share/cfengine/cf.solaris.example
/usr/local/share/cfengine/cf.sun4.example
/usr/local/share/cfengine/cf.users.example
/usr/local/share/cfengine/cfengine.conf.example
/usr/local/share/cfengine/cf.main.example
/usr/local/share/cfengine/cf.groups.example
/usr/local/share/cfengine/cfd.conf.example
/usr/local/share/cfengine/cf.services.example
/usr/local/share/cfengine/cf.ftp.example
/usr/local/share/cfengine/cfrc.example
/usr/local/info/cfengine-Tutorial.info
/usr/local/info/cfengine-Tutorial.info-1
/usr/local/info/cfengine-Tutorial.info-2
/usr/local/info/cfengine-Tutorial.info-3
/usr/local/info/cfengine-Tutorial.info-4
/usr/local/info/cfengine-Tutorial.info-5
/usr/local/info/cfengine-Reference.info
/usr/local/info/cfengine-Reference.info-1
/usr/local/info/cfengine-Reference.info-2
/usr/local/info/cfengine-Reference.info-3
/usr/local/info/cfengine-Reference.info-4
/usr/local/info/cfengine-Reference.info-5
/usr/local/info/cfengine-Reference.info-6
/usr/local/info/cfengine-Reference.info-7
/usr/local/man/man8/cfengine.8
/usr/local/share/cfengine/html/cfengine-Tutorial.html
/usr/local/share/cfengine/html/cfengine-Reference.html
/usr/local/share/cfengine/html/cf-security.html
 



%changelog


