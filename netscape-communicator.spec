Summary: Netscape Communicator web browsing suite
Name: netscape
Version: 4.79
Release: 1
Group: Applications/Internet
Copyright: free beer (Netscape Client Products License Agreement)
Source: communicator-v479-us.sparc-sun-solaris2.5.1.tar.gz
BuildRoot: /var/tmp/%{name}-root

%description
Netscape Communicator offers the complete set of tools for browsing
dynamic web content, plus full-strength email and easy-to-use
groupware.

%prep
%setup -q -n communicator-v479.sparc-sun-solaris2.5.1

%install
rm -rf $RPM_BUILD_ROOT
for i in netscape-%{version}/java/classes bin etc ; do
    mkdir -p $RPM_BUILD_ROOT/usr/local/$i
done

mv vreg *.nif $RPM_BUILD_ROOT/usr/local/netscape-%{version}
mv *.jar $RPM_BUILD_ROOT/usr/local/netscape-%{version}/java/classes

cd $RPM_BUILD_ROOT/usr/local/netscape-%{version}
for i in *.nif ; do 
    gzip -dc $i | tar -xf -
    rm -f $i
done

cat <<EOF > $RPM_BUILD_ROOT/usr/local/etc/netscape.config.example
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
cat <<EOF > $RPM_BUILD_ROOT/usr/local/etc/netscape.preferences.js.example
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
cat <<EOF > $RPM_BUILD_ROOT/usr/local/bin/netscape-4.79
#!/bin/sh

REAL_NETSCAPE=/usr/local/netscape-4.79/netscape
MOZILLA_HOME=/usr/local/netscape-4.79

export MOZILLA_HOME

[ -x /usr/local/etc/netscape.config ] && . /usr/local/etc/netscape.config

exec \$REAL_NETSCAPE -name netscape \$*
EOF
chmod 755 $RPM_BUILD_ROOT/usr/local/bin/netscape-%{version}
chmod 644 $RPM_BUILD_ROOT/usr/local/etc/netscape.preferences.js.example \
    $RPM_BUILD_ROOT/usr/local/etc/netscape.config.example

%clean
rm -rf $RPM_BUILD_ROOT

%post
cat <<EOF
To use netscape's updater program, run:

    echo 'Communicator,4.79.0.20011017,/usr/local/netscape-4.79' > /tmp/infile
    vreg /usr/local/netscape-4.79/registry /tmp/infile

You may wish to symlink /usr/local/bin/netscape-4.79 
                     to /usr/local/bin/netscape

EOF


%preun
rm -f /usr/local/bin/netscape

%files
%defattr(-,bin,bin)
/usr/local/netscape-%{version}/*
/usr/local/bin/*
/usr/local/etc/*
