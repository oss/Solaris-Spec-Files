Name: opie
Version: 2.4
Release: 1ru
Summary: One time passwords in everything
Copyright: BSD-like
Group: System/Authentication
BuildRoot: %{_tmppath}/%{name}-root
Source0: http://www.inner.net/pub/opie/opie-2.4.tar.gz
Source1: pam_opie-0.21.tar.gz
Patch: pam_opie.patch

%description
One time passwords in everything

%prep
%setup -c -n opie -T

%setup -q -D -n opie -T -a 0
%setup -q -D -n opie -T -a 1
%patch

%build
cd opie-2.4
./configure --enable-insecure-override --prefix=/usr/local
make
#make install prefix=
cp libopie/*.o ../pam_opie/libopie/
cd ../pam_opie/
#apply patch
make

%install
TOPDIR=`pwd`

rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/local/bin %{buildroot}/usr/local/man/man1 %{buildroot}/usr/local/man/man4 %{buildroot}/usr/local/man/man5 %{buildroot}/usr/local/man/man8 %{buildroot}/usr/lib/security
cd opie-2.4
cp *.1 %{buildroot}/usr/local/man/man1
cp *.4 %{buildroot}/usr/local/man/man4
cp *.5 %{buildroot}/usr/local/man/man5
cp *.8 %{buildroot}/usr/local/man/man8
#chown root opieftpd opiegen opieinfo opiekey opielogin opiepasswd opieserv opiesu opietest
#chmod u+s opieftpd opiegen opieinfo opiekey opielogin opiepasswd opieserv opiesu
cp opieftpd opiegen opieinfo opiekey opielogin opiepasswd opieserv opiesu opietest %{buildroot}/usr/local/bin

#cd opie-2.4
#make install prefix=%{buildroot}/usr/local
cp ../pam_opie/pam_opie.so %{buildroot}/usr/lib/security

%clean
rm -rf %{buildroot}

%post

cat <<EOF
To begin using OPIE, you must tell pam to use the pam_opie module.
Edit /etc/pam.conf. For ssh, have something like:

    sshd auth  sufficient pam_opie.so
    sshd auth  required   pam_unix.so.1 try_first_pass

The system will try the user's OPIE key first, which if correct 
is sufficient to authenticate the login. It will fall back on 
unix login, trying the password you gave to the first module.

To give users OPIE passwords, the user should run opiepasswd in
a secure session. To force this to run, try `opiepasswd -c -f`

There are Response Key generators available for various 
platforms at:
http://www.nas.nasa.gov/Groups/Security/OPIE/opie_login.html
EOF

%preun
cat<<EOF

EOF

%files
%defattr(4755, root, other)
/usr/local/bin/opiepasswd
%defattr(-, root, other)
#/usr/local/bin/opieftpd 
/usr/local/bin/opiegen 
/usr/local/bin/opieinfo 
/usr/local/bin/opiekey 
#/usr/local/bin/opielogin 
/usr/local/bin/opiepasswd 
/usr/local/bin/opieserv 
/usr/local/bin/opiesu 
/usr/local/bin/opietest
/usr/lib/security
/usr/local/man
