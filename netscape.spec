Summary: Netscape web browser
Name: netscape
Version: 4.75
Release: 3
Group: Applications/Internet
Copyright: free beer (Netscape Client Products License Agreement)
Source: communicator-v475-us.sparc-sun-solaris2.5.1.tar.gz 
BuildRoot: /var/tmp/%{name}-root

%description
Netscape Communicator offers the complete set of tools for browsing
dynamic web content, plus full-strength email and easy-to-use
groupware.

%prep
%setup -q -n communicator-v475.sparc-sun-solaris2.5.1

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/local/netscape-4.75/java/classes

mv vreg *.nif $RPM_BUILD_ROOT/usr/local/netscape-4.75
mv *.jar $RPM_BUILD_ROOT/usr/local/netscape-4.75/java/classes

cd $RPM_BUILD_ROOT/usr/local/netscape-4.75
for i in *.nif ; do 
    gzip -dc $i | tar -xf -
    rm -f $i
done

%clean
rm -rf $RPM_BUILD_ROOT

%post
cat <<EOF
To use netscape's updater program, run:

  echo 'Communicator,4.75.0.20000814,/usr/local/netscape' > /tmp/infile
  /usr/local/netscape/vreg /tmp/infile

You might want to run

  /sos/config/master -f /usr/local/etc/netscape.config
  /sos/config/master -f /usr/local/etc/netscape.preferences.js

EOF

[ -f /usr/local/netscape/movemail ] && rm /usr/local/netscape/movemail

if [ `/bin/ls -d1 /usr/local/netscape* |wc -l` -gt 2 ]
then
    cat <<EOF
There are old versions of netscape still installed in /usr/local You
might want to clean them up...  You only want /usr/local/netscape and
/usr/local/netscape-4.75.
EOF
   /bin/ls -d1 /usr/local/netscape*
fi 
   
rm /usr/local/netscape
ln -s /usr/local/netscape-4.75 /usr/local/netscape

cat <<EOF > /usr/local/bin/netscape
#!/bin/sh

REAL_NETSCAPE=/usr/local/netscape/netscape
MOZILLA_HOME=/usr/local/netscape

export MOZILLA_HOME

[ -x /usr/local/etc/netscape.config ] && . /usr/local/etc/netscape.config

exec \$REAL_NETSCAPE -name netscape \$*
EOF
chmod 755 /usr/local/bin/netscape

mkdir -p /usr/local/etc
cat <<EOF > /usr/local/etc/netscape.config.example
#! /bin/sh

if [ -f /usr/local/etc/netscape.preferences.js ]
then
  if [ ! -d \$HOME/.netscape ]
  then
     mkdir \$HOME/.netscape
  fi
 
  if [ ! -f =$HOME/.netscape/preferences.js -a -f /usr/local/etc/netscape.preferences.js ] 
  then
     cp /usr/local/etc/netscape.preferences.js $HOME/.netscape/preferences.js
  fi
fi
EOF

cat <<EOF > /usr/local/etc/netscape.preferences.js.example
// Netscape User Preferences
// This is a generated file!  Do not edit.

user_pref("browser.startup.homepage", "http://www.rci.rutgers.edu");
user_pref("mail.auto_quote", false);
user_pref("mail.html_compose", false);
user_pref("mail.server_type", 1);
user_pref("mail.use_movemail", false);
user_pref("network.hosts.nntp_server", "news-nb-rci.rutgers.edu");
user_pref("network.hosts.pop_server", "email.rci.rutgers.edu");
user_pref("network.hosts.smtp_server", "email.rci.rutgers.edu");
# exit
EOF
chmod 644 /usr/local/etc/netscape.preferences.js.example \
    /usr/local/etc/netscape.config.example

%preun
rm -f /usr/local/bin/netscape

%files
%defattr(-,bin,bin)
/usr/local/netscape-4.75

