Summary: Problem shell
Name: probshell
Version: 1.0
Release: 4
Copyright: Rutgers
Group: System Environment/Shells
Source: probshell.tar.gz
BuildRoot: /var/tmp/%{name}-root
BuildRequires: rcs

%description
This is a "problem shell" for users whose account should be
temporarily closed.  It prints out a message if it can find a file
with filename == username.  If not, it prints out a generic banner or
backs down to the generic message string in this program.  This
program will also call syslog when it is run.  By Kaveh Ghazi
(ghazi@noc.rutges.edu) 11/23/93.

modified to support better logging and multiple use messages [Roy] Now
derives the message directory based on the users shell (from getpwuid)
If shell is of the form .../foo/bar the program will look in .../foo
for messages and log and use foo as the program name.

  [ from probsh.c ]

%prep
%setup -q -n probshell

%build
chmod -x *
rm -f kerbshell probsh probsh.c probsh.c~ probsh.OLD
co probsh.c
gcc -o probsh probsh.c

%install
rm -rf $RPM_BUILD_ROOT

for i in probshell kerbshell closedshell ; do
    mkdir -p $RPM_BUILD_ROOT/usr/local/bin/$i/bannerdir
done

install -m 0755 probsh $RPM_BUILD_ROOT/usr/local/bin/probshell/sh
cat <<EOF > $RPM_BUILD_ROOT/usr/local/bin/probshell/generic_banner.example

 
There is a problem with your account.  Please contact the Information
Center in person at Hill Center Room 128, Busch Campus for assistance.
Telephone: 732-445-HELP(4357) and Please bring a valid photo ID with you.
 
 
EOF
cat <<EOF > $RPM_BUILD_ROOT/usr/local/bin/kerbshell/generic_banner.example


 You must change your password.  Point your web browser to

             www.eden.rutgers.edu/rats/kerbshell_change.cgi

 to authenticate and change your password.  Please wait
 15 minutes to allow the change to update on all of eden.

 Please contact the Information Center either in person or via
 telephone if you need further assistance.  Please bring a valid photo
 ID with you.

                           Information Center
                          Hill Center Room 128
                              Busch Campus
                Telephone:  732-445-HELP (732-445-4357)

EOF
cat <<EOF > $RPM_BUILD_ROOT/usr/local/bin/closedshell/generic_banner.example


 Your account has been CLOSED.
 
 If you had a guest account it was probably NOT renewed on time.

 Please contact the Information Center either in person or via
 telephone if you need further assistance.  Please bring a valid photo
 ID with you.

                           Information Center
                          Hill Center Room 128
                              Busch Campus
                Telephone:  732-445-HELP (732-445-4357)


EOF
for i in closedshell kerbshell probshell ; do
    chmod 644 $RPM_BUILD_ROOT/usr/local/bin/$i/generic_banner.example
done

SHELLS="tcsh ksh csh bash"

cd $RPM_BUILD_ROOT/usr/local/bin/probshell
for i in $SHELLS ; do
    ln -s sh $i
done

cd ../closedshell
for i in $SHELLS sh ; do
    ln -s ../probshell/sh $i
done

cd ../kerbshell
for i in $SHELLS sh ; do
    ln -s ../probshell/sh $i
done

cd ..
ln -s kerbshell kerbsh
ln -s closedshell closedsh

%clean
rm -rf $RPM_BUILD_ROOT

%post
cat <<EOF
You may wish to edit /etc/shells at this point.
EOF

%files
%defattr(-,root,other)
/usr/local/bin/kerbsh
/usr/local/bin/closedsh
/usr/local/bin/kerbshell
/usr/local/bin/probshell
/usr/local/bin/closedshell
