%define version 3.3.4
%define initdir /etc/init.d

Summary: SqWebmail CGI
Name: sqwebmail
Version: %{version}
Release: 2
Copyright: GPL
Group: Applications/Mail
Source: sqwebmail-%{version}.tar.gz
Packager: Rutgers University
BuildRoot: /var/tmp/%{name}-install
Requires: gnupg >= 1.0.5 expect
BuildPreReq: gdbm autoconf fileutils perl gnupg >= 1.0.5 expect

%description
sqwebmail lets you do mail things over the Web using https.

%prep
%setup -q

%build

bash -c "CC='/opt/SUNWspro/bin/cc' CXX='/opt/SUNWspro/bin/CC' \
LDFLAGS='-L/usr/local/lib -R/usr/local/lib' \
CPPFLAGS='-I/usr/local/include' \
./configure --prefix=/usr/local/sqwebmail-3.3.4 --with-db=gdbm \
--enable-cgibindir=/usr/local/sqwebmail-3.3.4/cgi-bin \
--enable-imagedir=/usr/local/sqwebmail-3.3.4/images \
--without-auth{userdb,ldap,pwd,shadow,vchkpw,pgsql,mysql,cram,custom,daemon} \
--with-ispell=/usr/local/bin/ispell \
--enable-https --enable-mimetypes=/usr/local/etc/mime.types --with-authpam"

make 

%install

%{__rm} -rf $RPM_BUILD_ROOT
#%{__mkdir_p} $RPM_BUILD_ROOT/etc/pam.d
make install DESTDIR=$RPM_BUILD_ROOT
make install-configure DESTDIR=$RPM_BUILD_ROOT

#%{__mkdir_p} $RPM_BUILD_ROOT%{initdir}
#sed s/'touch \/var\/lock\/subsys\/courier-imap'/'\[ -d \"\/var\/run\/authdaemon.courier-imap\" \] \|\| \/usr\/bin\/mkdir -p \/var\/run\/authdaemon.courier-imap'/g courier-imap.sysvinit > courier-imap.sysvinit.ru
#%{__cp} courier-imap.sysvinit.ru $RPM_BUILD_ROOT%{initdir}/courier-imap

%files
%defattr(-,root,root)
/usr/local/sqwebmail-%{version}

%clean
rm -rf $RPM_BUILD_ROOT
