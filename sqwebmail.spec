%define name sqwebmail
%define version 3.5.1
%define release 4
%define prefix /usr/local
%define initdir /etc/init.d

Summary: SqWebmail CGI
Name: %{name}
Version: %{version}
Release: %{release} 
Copyright: GPL
Group: Applications/Mail
Source: %{name}-%{version}.tar.gz
Packager: Rutgers University
Patch0: sqwebmail.patch
BuildRoot: /var/tmp/%{name}-install
Requires: gnupg >= 1.0.5 expect
BuildPreReq: gdbm autoconf fileutils perl gnupg >= 1.0.5 expect

%description
sqwebmail lets you do mail things over the Web using https.

%prep
%setup -q
%patch0 -p1

%build

CC=/opt/SUNWspro/bin/cc
CXX=/opt/SUNWspro/bin/CC
LDFLAGS="-L/usr/local/lib -R/usr/local/lib"
CPPFLAGS=-I/usr/local/include

export CC
export CXX
export LDFLAGS
export CPPFLAGS

./configure --prefix=/usr/local/%{name}-%{version} --with-db=gdbm \
--enable-cgibindir=/usr/local/%{name}-%{version}/cgi-bin \
--enable-imagedir=/usr/local/%{name}-%{version}/images \
--with-cachedir=/tmp --with-cacheowner=www \
--without-authuserdb --without-authldap --without-authpwd \
--without-authshadow --without-authvchkpw --without-authpgsql \
--without-authmysql --without-authcram --without-authcustom \
--without-authdaemon --with-ispell=/usr/local/bin/ispell \
--enable-https --enable-mimetypes=/usr/local/etc/mime.types \
--with-authpam --enable-webpass=no --disable-changepass \
--enable-imageurl=/sqwebimage

make

%install
%{__rm} -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT
make install-configure DESTDIR=$RPM_BUILD_ROOT

%post
echo "README & README-webtools is located at %{prefix}/doc/%{name}-%{version}";
echo "Do the following:";
echo "rm %{prefix}/%{name}";
echo "ln -s %{prefix}/%{name}-%{version} %{prefix}/%{name}";
echo "READ the README & README-webtools!!";

%files
%defattr(-,root,root)
%doc README-webtools README README.html README.pam INSTALL INSTALL.html 
/usr/local/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT
