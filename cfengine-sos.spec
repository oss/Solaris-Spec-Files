%include machine-header.spec

Summary: Tools for remotely configuring several machines
Name: cfengine-sos
Version: 1.6.5
Release: 1
Copyright: GPL
Group: System Admin
Source0: cfengine-%{version}.tar.gz
# Source1: RU_cfengine.tar.gz
BuildRoot: /var/tmp/%{name}-buildroot
BuildRequires: tcp_wrappers
BuildRequires: teTeX
BuildRequires: openssl >= 0.9.8
BuildRequires: db
Requires: tcp_wrappers
Requires: openssl >= 0.9.8
Requires: db

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

%prep
%setup -q -n cfengine-%{version}
# %setup -q -D -T -a 1

%build
#PATH="$PATH:/usr/local/teTeX/bin/%{sparc_arch}"; export PATH

#LD="/usr/ccs/bin/ld -L/usr/local/lib -R/usr/local/lib -L/usr/local/ssl/lib" \
#LDFLAGS="-L/usr/local/lib -R/usr/local/lib -L/usr/local/ssl/lib" \
PATH="/opt/SUNWspro/bin:/usr/local/teTeX/bin:${PATH}" \
CC="cc" CXX="CC" CPPFLAGS="-I/usr/local/include -I/usr/local/ssl/include" \
LD="/usr/ccs/bin/ld" \
LDFLAGS="-L/usr/local/lib -R/usr/local/lib -L/usr/local/ssl/lib" \
export PATH CC CXX CPPFLAGS LD LDFLAGS
./configure --prefix=/sos/cfengine --with-history --with-readline --with-lockdir=/var/log/cfengine  --with-logdir=/var/log/cfengine
rm depcomp
rm ylwrap
ln -s /usr/local/share/automake-1.9/ylwrap ylwrap
ln -s /usr/local/share/automake-1.9/depcomp depcomp
make MAKEINFO="/usr/local/teTeX/bin/makeinfo" \
     LATEX="/usr/local/teTeX/bin/latex" \
     DVIPS="/usr/local/teTeX/bin/dvips"

#cd doc;
#make;

%install
PATH="$PATH:/usr/local/teTeX/bin/%{sparc_arch}"; export PATH

rm -rf %{buildroot}
#mkdir -p %{buildroot}/sos/cfengine/sbin/
#mkdir -p %{buildroot}/sos/cfengine/share/
#mkdir -p %{buildroot}/sos/cfengine/info/
#mkdir -p %{buildroot}/sos/cfengine/man/man8/
#mkdir -p %{buildroot}/sos/cfengine/share/cfengine/html/
#mkdir -p %{buildroot}/etc/cfengine/
#mkdir -p %{buildroot}/etc/rc2.d/
#mkdir -p %{buildroot}/var/log/cfengine

make install DESTDIR=%{buildroot}
#cd doc
#make install prefix=%{buildroot}/sos/cfengine/

# cd $RPM_BUILD_DIR/cfengine-1.6.0.b3/RU_cfengine/
# ./INSTALL

%clean
rm -rf %{buildroot}

%post
grep cfengine /etc/services >/dev/null 2>&1
if [ $? -eq 1 ]; then
    echo  >> /etc/services "\ncfengine\t5308/tcp\t  #cfd"
fi
# echo  >> /etc/profile "\nexport CFINPUTS=/etc/cfengine/ \t  #so cfengine/cfd know where to look for their conf files"
#if [ -x /sos/cfengine/bin/install-info ] ;   then
#     for i in /sos/cfengine/info/cfengine*.info
#         do  /sos/cfengine/bin/install-info --quiet $i /sos/cfengine/info/dir;
#         chmod 644 /sos/cfengine/info/dir
#     done  
#fi 
# echo "\nPlease look at RU_README in /etc/cfengine in order to get started with cfengine." 

%postun
if [ -d /sos/cfengine/share/cfengine/ ] ;   then
    rm -rf /sos/cfengine/share/cfengine/
fi
if [ -d /etc/cfengine/ ] ;   then
   rm -rf /etc/cfengine/
fi
if [ -d /var/log/cfengine/ ] ;   then
   rm -rf /var/log/cfengine/
fi

   
%files
%defattr (-,root,root)
%doc COPYING AUTHORS README SURVEY TODO NEWS
/sos/cfengine/bin/*
/sos/cfengine/sbin/*
/sos/cfengine/share/cfengine
#/sos/cfengine/info/*info*
#/sos/cfengine/man/*/*
# /var/log/cfengine/ 
# /etc/cfengine/cfengine.conf.RPM.NEW
# /etc/cfengine/cf.groups
# /etc/cfengine/cf.download
# /etc/rc2.d/DONTS99start-cfd
# /etc/cfengine/RU_README


%changelog
* Thu Aug 2 2001 Sam Isaacson <sbi@nbcs.rutgers.edu>
- Upgraded to 1.6.3; removed RU-specific files.

* Thu Dec 14 2000 John Wieczorek <vieczore@nbcs.rutgers.edu>
- added %{version} to Source0

* Wed Dec 13 2000  John Wieczorek <vieczore@nbcs.rutgers.edu>
- added RU specific files in Source1 

