Summary: The erlang programming language
Name: erlang
%define preversion otp_src_
Version: R10B7
Release: 1
License: EPL
Group: Development/Languages
Source: %{preversion}%{version}.tar.gz
Requires: openssl
BuildRequires: sed, make, tar, perl
BuildRoot: /var/tmp/%{name}-root

%description
erlang is a programming language designed at the Ericsson Computer Science Laboratory

%prep
%setup -q -n otp_src_R10B-7

%build
PATH=/opt/SUNWspro/bin:/usr/ccs/bin:/usr/local/gnu/bin:$PATH
CPPFLAGS="-I/usr/local/include"
export PATH CC CPPFLAGS

env
./configure --enable-threads
gmake PATH="$PATH" CPPFLAGS="$CPPFLAGS"
#gmake

%install
gmake install INSTALL_PREFIX=$RPM_BUILD_ROOT
#begin stupid hack because the erlang build sets up non-relative symlinks which point to the buildroot, so I'm going to make them relative
cd $RPM_BUILD_ROOT/usr/local/bin
for i in ear ecc elink erl erlc escript; do rm $i; ln -s ../lib/erlang/bin/$i .; done

cd $RPM_BUILD_ROOT/usr/local/lib/erlang/bin
for i in erl start; do sed -e "s#$RPM_BUILD_ROOT##" $i > $i.bak; mv $i.bak $i; chmod 755 $i; done

cd $RPM_BUILD_ROOT/usr/local/lib/erlang/erts-5.4.9/bin
for i in erl start; do sed -e "s#$RPM_BUILD_ROOT##" $i > $i.bak; mv $i.bak $i; chmod 755 $i; done

cd $RPM_BUILD_ROOT/usr/local/lib/erlang/bin
rm epmd
ln -s ../erts-5.4.9/bin/epmd .

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-, root, root)
/usr/local/lib/erlang/*
/usr/local/bin/ear
/usr/local/bin/ecc
/usr/local/bin/elink
/usr/local/bin/erl
/usr/local/bin/erlc
/usr/local/bin/escript
