%define version 3.4.0.20021026
%define initdir /etc/init.d

Summary: SqWebmail CGI
Name: sqwebmail
Version: %{version}
Release: 0
Copyright: GPL
Group: Applications/Mail
Source: sqwebmail-%{version}.tar.bz2
Packager: Rutgers University
BuildRoot: /var/tmp/%{name}-install
Requires: gnupg >= 1.0.5 expect ispell
BuildPreReq: gdbm autoconf fileutils perl gnupg >= 1.0.5 expect

%description
sqwebmail lets you do mail things over the Web using https.

%prep
%setup -q

%build

bash -c "CC='/opt/SUNWspro/bin/cc' CXX='/opt/SUNWspro/bin/CC' \
LDFLAGS='-L/usr/local/lib -R/usr/local/lib' \
CPPFLAGS='-I/usr/local/include' \
./configure --prefix=/usr/local/sqwebmail-%{version} --with-db=gdbm \
--enable-cgibindir=/usr/local/sqwebmail-%{version}/cgi-bin \
--enable-imagedir=/usr/local/sqwebmail-%{version}/images \
--without-auth{userdb,ldap,pwd,shadow,vchkpw,pgsql,mysql,cram,custom,daemon} \
--with-ispell=/usr/local/bin/ispell \
--enable-https --enable-mimetypes=/usr/local/etc/mime.types --with-authpam \
--enable-webpass=no --disable-changepass --enable-imageurl=/sqwebimage"

make 

%install

%{__rm} -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT
make install-configure DESTDIR=$RPM_BUILD_ROOT


%files
%defattr(-,root,root)
/usr/local/sqwebmail-%{version}

%clean
rm -rf $RPM_BUILD_ROOT
