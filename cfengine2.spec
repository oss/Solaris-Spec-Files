%include machine-header.spec

Summary: Tools for remotely configuring several machines
Name: cfengine2
Version: 2.1.3
Release: 1
Copyright: GPL
Group: System Admin
Source0: cfengine-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-buildroot
BuildRequires: tcp_wrappers
BuildRequires: teTeX
BuildRequires: openssl >= 0.9.6b
BuildRequires: db3.3
Requires: tcp_wrappers
Requires: openssl >= 0.9.6b
Requires: db3.3

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
another.  Cfengine uses a flexible system of "classes" which helps
you to single out a specific group of hosts with a single statement.

%prep
%setup -q -n cfengine-%{version}

%build

%ifarch sparc64
%ifos solaris2.9
PATH="/usr/local/bin:/usr/local/teTeX/bin/%{sparc_arch}:$PATH"; export PATH
%else
PATH="$PATH:/usr/local/teTeX/bin/%{sparc_arch}"; export PATH
%endif 
%else
PATH="$PATH:/usr/local/teTeX/bin/%{sparc_arch}"; export PATH
%endif

which texi2dvi
echo $PATH
LDFLAGS="-L/usr/local/lib -L/usr/local/ssl/lib -L/usr/local/BerkeleyDB.3.3 -R/usr/local/lib -R/usr/local/ssl/lib -R?usr/local/BerkeleyDB.3.3" \
./configure --with-history --with-readline --with-lockdir=/var/log/cfengine  --with-logdir=/var/log/cfengine
make MAKEINFO="/usr/local/bin/makeinfo" \
     LATEX="/usr/local/teTeX/bin/%{sparc_arch}/latex" \
     DVIPS="/usr/local/teTeX/bin/%{sparc_arch}/dvips" \
     TEX="/usr/local/teTeX/bin/%{sparc_arch}/tex"

%install
PATH="$PATH:/usr/local/teTeX/bin/%{sparc_arch}"; export PATH

rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/local
make install prefix=%{buildroot}/usr/local

%clean
rm -rf %{buildroot}

%post
grep cfengine /etc/services >/dev/null 2>&1
if [ $? -eq 1 ]; then
    echo "Add a line in /etc/services for cfengine (5308 tcp)."
fi
if [ -x /usr/local/bin/install-info ] ;   then
     for i in /usr/local/info/cfengine*.info
         do  /usr/local/bin/install-info --quiet $i /usr/local/info/dir;
         chmod 644 /usr/local/info/dir
     done  
fi 

%postun
if [ -d /usr/local/share/cfengine ]; then
    rm -rf /usr/local/share/cfengine
fi
if [ -d /etc/cfengine ]; then
   rm -rf /etc/cfengine
fi
if [ -d /var/log/cfengine ]; then
   rm -rf /var/log/cfengine
fi

%files
%defattr (-,root,bin)
%doc COPYING AUTHORS README SURVEY TODO NEWS
/usr/local/sbin/*
/usr/local/share/cfengine
# move these to docs subpackage?
/usr/local/info/*info*
/usr/local/man/man8/*




