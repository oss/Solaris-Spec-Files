Summary: GPG Keyserver
Name: pks
Version: 0.9.4
Release: 1ru
Group: Applications/Internet
Copyright: Unique
Source: http://www.mit.edu/people/marc/pks/pks-%{version}.tar.gz
Source1: pks-init.d
Source2: pks-html.tar.bz2
BuildRoot: /var/tmp/%{name}-root

%description
GPG KeyServer


%prep
%setup -q

%build
LD="/usr/ccs/bin/ld -L/usr/local/lib -R/usr/local/lib" \
  DFLAGS="-L/usr/local/lib -R/usr/local/lib" \
  CFLAGS="-I/usr/local/include" 
CC="cc" ./configure --prefix=/usr/local/pks
make

%install
rm -rf $RPM_BUILD_ROOT
make install prefix=$RPM_BUILD_ROOT/usr/local/pks
mv $RPM_BUILD_ROOT/usr/local/pks/man $RPM_BUILD_ROOT/usr/local/
mkdir -p $RPM_BUILD_ROOT/usr/local/etc $RPM_BUILD_ROOT/etc/init.d $RPM_BUILD_ROOT/var/local/pks/db
mv $RPM_BUILD_ROOT/usr/local/pks/etc/pksd.conf $RPM_BUILD_ROOT/usr/local/etc
cp %{SOURCE1} $RPM_BUILD_ROOT/etc/init.d/pks
mv $RPM_BUILD_ROOT/usr/local/pks/share $RPM_BUILD_ROOT/usr/local
cp %{SOURCE2} $RPM_BUILD_ROOT/usr/local/share
chmod 755 $RPM_BUILD_ROOT/etc/init.d/pks
sed "s/\/usr\/local\/pks\/share/\/usr\/local\/share/" $RPM_BUILD_ROOT/usr/local/etc/pksd.conf > $RPM_BUILD_ROOT/usr/local/etc/pksd.conf2
sed "s/\/usr\/local\/pks\/var\/db/\/var\/local\/pks\/db/" $RPM_BUILD_ROOT/usr/local/etc/pksd.conf2 > $RPM_BUILD_ROOT/usr/local/etc/pksd.conf
#mv $RPM_BUILD_ROOT/usr/local/etc/pksd.conf2 $RPM_BUILD_ROOT/usr/local/etc/pksd.conf

%clean
rm -rf $RPM_BUILD_ROOT

%post
cat<<EOF
To use the mail server, add this to your aliases file:
    pgp-public-keys: "|/usr/local/pks/bin/pks-mail.sh /usr/local/etc/pksd.conf"
    pgp: pgp-public-keys

To create an empty database, run:
    /usr/local/pks/bin/pksclient /var/local/pks/db create

An init.d script has been installed for starting and stopping the server.

HTML files are in /usr/local/share/pks-html.tar.bz2. Expand them and place them
where your web server can find them. Edit them to match your servername.

Also, be sure to edit /usr/local/etc/pksd.conf. You will need to specify information
about the server admin email address.
EOF

%files
%defattr(-,root,bin)
/usr/local/pks/bin/*
/usr/local/share/pks_help.en
/usr/local/share/pks-html.tar.bz2
%config(noreplace)/usr/local/etc/pksd.conf
%config(noreplace)/etc/init.d/pks
/usr/local/man/man5/*
/usr/local/man/man8/*
/var/local/pks/db
