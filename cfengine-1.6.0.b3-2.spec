Summary: attempting to build an RPM of cfengine
Name: cfengine
Version: 1.6.0.b3
Release: 3
Copyright: GPL
Group: System Admin
Source0: cfengine-%{version}.tar.gz
Source1: RU_cfengine-%{version}.tar.gz
BuildRoot: /var/tmp/%{name}-buildroot

%description
Cfengine is a tool for setting up and maintaining BSD and
System-5-like operating system optionally attached to a TCP/IP
network.  You can think of cfengine as a very high level
language---much higher level than Perl or shell: a single statement
can result in many hundreds of operations being performed on multiple
hosts. Cfengine is good at performing a lot of common system
administration tasks, and allows you to build on its strengths with
your own scripts. You can also use it as a netwide front-end for cron.
Once you have set up cfengine, you'll be free to use your time being
like a human being, instead of playing R2-D2 with the system.

The main purpose of cfengine is to allow you to create a single,
central system configuration which will define how every host on your
network should be configured in an intuitive way.  An interpreter runs
on every host on your network and parses the master file (or
file-set); the configuration of each host is checked against this file
and then, if you request it, any deviations from the defined
configuration are fixed automatically.  You do not have to mention
every host specifically by name in order to configure them : instead
you can refer to the properties which distinguish hosts from one
another.  Cfengine uses a flexible system of ``classes'' which helps
you to single out a specific group of hosts with a single statement.



%prep						#???
%setup 						#??? 
%setup -q -D -T -a 1

./configure --with-lockdir=/var/log/cfengine  --with-logdir=/var/log/cfengine

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
mkdir -p $RPM_BUILD_ROOT/etc/cfengine/
mkdir -p $RPM_BUILD_ROOT/etc/rc2.d/
mkdir -p $RPM_BUILD_ROOT/var/log/cfengine

make install prefix=$RPM_BUILD_ROOT/usr/local/

cd doc

make install prefix=$RPM_BUILD_ROOT/usr/local/

cd $RPM_BUILD_DIR/cfengine-1.6.0.b3/RU_cfengine/

./INSTALL

%clean

#rm -rf $RPM_BUILD_ROOT

%post

echo  >> /etc/services "\ncfengine\t5308/tcp\t  #cfd"

echo  >> /etc/profile "\nexport CFINPUTS=/etc/cfengine/ \t  #so cfengine/cfd know where to look for their conf files"

if 
   [ -x /usr/local/bin/install-info ] ;   then

     for i in /usr/local/info/cfengine*.info
     do  /usr/local/bin/install-info --quiet $i /usr/local/info/dir;
     chmod 644 /usr/local/info/dir
     
     done  
   
fi 

echo "\nPlease look at RU_README in /etc/cfengine in order to get started with cfengine." 

%postun

if 
   [ -d /usr/local/share/cfengine/ ] ;   then

   rm -rf /usr/local/share/cfengine/
  
fi

if 
   [ -d /etc/cfengine/ ] ;   then

   rm -rf /etc/cfengine/
  
fi

if 
   [ -d /var/log/cfengine/ ] ;   then

   rm -rf /var/log/cfengine/
  
fi

   
%files
%defattr (-,root,root)
/usr/local/sbin/cfengine
/usr/local/sbin/cfd
/usr/local/sbin/cfrun
/usr/local/sbin/cfkey
/usr/local/sbin/cfwrap
/usr/local/sbin/cfmail
/usr/local/sbin/cfmailfilter
/usr/local/sbin/cfcron
/usr/local/sbin/vicf
/usr/local/sbin/cfdoc
/usr/local/share/cfengine/cfdaily
/usr/local/share/cfengine/start-cfd
/usr/local/share/cfengine/cfengine.el
/usr/local/share/cfengine/cf.chflags.example
/usr/local/share/cfengine/cf.freebsd.example
/usr/local/share/cfengine/cf.ftp.example
/usr/local/share/cfengine/cf.groups.example
/usr/local/share/cfengine/cf.linux.example
/usr/local/share/cfengine/cf.main.example
/usr/local/share/cfengine/cf.motd.example
/usr/local/share/cfengine/cf.preconf.example
/usr/local/share/cfengine/cf.services.example
/usr/local/share/cfengine/cf.site.example
/usr/local/share/cfengine/cf.solaris.example
/usr/local/share/cfengine/cf.sun4.example
/usr/local/share/cfengine/cf.users.example
/usr/local/share/cfengine/cfd.conf.example
/usr/local/share/cfengine/cfengine.conf.example
/usr/local/share/cfengine/cfrc.example
/usr/local/share/cfengine/cfrun.hosts.example
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
 
/etc/cfengine/cfengine.conf.RPM.NEW
/etc/cfengine/cf.groups
/etc/cfengine/cf.download
/etc/rc2.d/DONTS99start-cfd
/etc/cfengine/RU_README
/var/log/cfengine/

%changelog

*Thu Dec 14 2000 John Wieczorek <vieczore@nbcs.rutgers.edu
- added %{version} to Source0 and Source1

*Wed Dec 13 2000  John Wieczorek <vieczore@nbcs.rutgers.edu>
- added RU specific files in Source1 
