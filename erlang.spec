Summary: The erlang programming language
Name: erlang
%define preversion otp_src_
%define manpreversion otp_doc_man_
%define htmlpreversion otp_doc_html_
%define tarball_version R10B-10
Version: R10B10
Release: 6
License: EPL
Group: Development/Languages
Source: %{preversion}%{tarball_version}.tar.gz
Source1: %{manpreversion}%{tarball_version}.tar.gz
Source2: %{htmlpreversion}%{tarball_version}.tar.gz
Requires: openssl
BuildRequires: sed, make, tar, perl
BuildRoot: /var/tmp/%{name}-root

%description
erlang is a programming language designed at the Ericsson Computer Science Laboratory

%prep
%setup -q -n %{preversion}%{tarball_version}

%build
PATH=/opt/SUNWspro/bin:/usr/local/bin/sparcv9:/usr/ccs/bin:/usr/local/gnu/bin:$PATH
#CC=/opt/SUNWspro/bin/cc
CC=/usr/local/bin/sparcv9/gcc
#LD=/usr/ccs/bin/ld
CFLAGS="-mcpu=v9 -m64"
CPPFLAGS="-mcpu=v9 -m64 -I/usr/local/include"
LDFLAGS="-L/usr/local/lib/sparcv9 -R/usr/local/lib/sparcv9 -L/usr/local/ssl/lib/sparcv9 -R/usr/local/ssl/lib/sparcv9"
#export CC LD PATH CPPFLAGS LDFLAGS
export CC PATH CPPFLAGS LDFLAGS

./configure --enable-threads --enable-kernel-poll

cp lib/crypto/c_src/sparc-sun-solaris2.9/Makefile lib/crypto/c_src/sparc-sun-solaris2.9/Makefile.orig
awk '{if ($0 ~ /^SSL_LIBDIR = /) {print "SSL_LIBDIR = /usr/local/ssl/lib/sparcv9"} else {print}}' < lib/crypto/c_src/sparc-sun-solaris2.9/Makefile > lib/crypto/c_src/sparc-sun-solaris2.9/Makefile.ru
cp lib/crypto/c_src/sparc-sun-solaris2.9/Makefile.ru lib/crypto/c_src/sparc-sun-solaris2.9/Makefile

chmod 644 lib/crypto/priv/Makefile
cp lib/crypto/priv/Makefile lib/crypto/priv/Makefile.orig
awk '{if ($0 ~ /^SO_SSL_LIBDIR = /) {print "SO_SSL_LIBDIR = /usr/local/ssl/lib/sparcv9"} else {print}}' < lib/crypto/priv/Makefile > lib/crypto/priv/Makefile.ru
cp lib/crypto/priv/Makefile.ru lib/crypto/priv/Makefile

cp lib/ssl/c_src/sparc-sun-solaris2.9/Makefile lib/ssl/c_src/sparc-sun-solaris2.9/Makefile.orig
awk '{if ($0 ~ /^SSL_LIBDIR = /) {print "SSL_LIBDIR = /usr/local/ssl/lib/sparcv9"} else {print}}' < lib/ssl/c_src/sparc-sun-solaris2.9/Makefile > lib/ssl/c_src/sparc-sun-solaris2.9/Makefile.ru
cp lib/ssl/c_src/sparc-sun-solaris2.9/Makefile.ru lib/ssl/c_src/sparc-sun-solaris2.9/Makefile

gmake

%install
gmake install INSTALL_PREFIX=$RPM_BUILD_ROOT
#begin stupid hack because the erlang build sets up non-relative symlinks which point to the buildroot, so I'm going to make them relative
cd $RPM_BUILD_ROOT/usr/local/bin
for i in ear ecc elink erl erlc escript; do rm $i; ln -s ../lib/erlang/bin/$i .; done

cd $RPM_BUILD_ROOT/usr/local/lib/erlang/bin
for i in erl start; do sed -e "s#$RPM_BUILD_ROOT##" $i > $i.bak; mv $i.bak $i; chmod 755 $i; done

cd $RPM_BUILD_ROOT/usr/local/lib/erlang/erts-5.4.13/bin
for i in erl start; do sed -e "s#$RPM_BUILD_ROOT##" $i > $i.bak; mv $i.bak $i; chmod 755 $i; done

cd $RPM_BUILD_ROOT/usr/local/lib/erlang/bin
rm epmd
ln -s ../erts-5.4.13/bin/epmd .

cd $RPM_BUILD_ROOT/usr/local/lib/erlang
gtar xzf %{SOURCE1}
rm COPYRIGHT PR.template README
gtar xzf %{SOURCE2}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-, root, root)
%doc README
/usr/local/lib/erlang/*
/usr/local/bin/ear
/usr/local/bin/ecc
/usr/local/bin/elink
/usr/local/bin/erl
/usr/local/bin/erlc
/usr/local/bin/escript
