Summary:	The erlang programming language
Name:		erlang
%define		preversion otp_src_
%define		manpreversion otp_doc_man_
%define		htmlpreversion otp_doc_html_
%define		tarball_version R11B-4
Version:	R11B4
Release:	1
License:	EPL
Group:		Development/Languages
Source:		%{preversion}%{tarball_version}.tar.gz
Source1:	%{manpreversion}%{tarball_version}.tar.gz
Source2:	%{htmlpreversion}%{tarball_version}.tar.gz
Requires:	openssl >= 0.9.8
BuildRequires:	make, tar, perl, gcc >= 4.2.1, openssl >= 0.9.8, openssl-static >= 0.9.8
BuildRoot:	/var/tmp/%{name}-root

%description
erlang is a programming language designed at the Ericsson Computer Science Laboratory

%prep
%setup -q -n %{preversion}%{tarball_version}

%build
#########################################################################################
# NOTE: erlang MUST be compiled with gcc. Unless you know some secret magic that the world
# doesn't, suncc is a no go.
#########################################################################################
PATH="/opt/SUNWspro/bin:/usr/local/gnu/bin:/usr/ccs/bin:${PATH}" \
CC="gcc" CXX="CC" CPPFLAGS="-I/usr/local/include" \
LD="/usr/ccs/bin/ld" \
LDFLAGS="-L/usr/local/lib -L/usr/local/ssl/lib -R/usr/local/lib -R/usr/local/ssl/lib"
export PATH CC CXX CPPFLAGS LD LDFLAGS

./configure \
	--enable-threads \
	--enable-kernel-poll \
	--with-ssl="/usr/local/ssl" \
	--enable-smp-support

#cp lib/crypto/c_src/sparc-sun-solaris2.9/Makefile lib/crypto/c_src/sparc-sun-solaris2.9/Makefile.orig
#awk '{if ($0 ~ /^SSL_LIBDIR = /) {print "SSL_LIBDIR = /usr/local/ssl/lib/sparcv9"} else {print}}' < lib/crypto/c_src/sparc-sun-solaris2.9/Makefile > lib/crypto/c_src/sparc-sun-solaris2.9/Makefile.ru
#cp lib/crypto/c_src/sparc-sun-solaris2.9/Makefile.ru lib/crypto/c_src/sparc-sun-solaris2.9/Makefile

#chmod 644 lib/crypto/priv/Makefile
#cp lib/crypto/priv/Makefile lib/crypto/priv/Makefile.orig
#awk '{if ($0 ~ /^SO_SSL_LIBDIR = /) {print "SO_SSL_LIBDIR = /usr/local/ssl/lib/sparcv9"} else {print}}' < lib/crypto/priv/Makefile > lib/crypto/priv/Makefile.ru
#cp lib/crypto/priv/Makefile.ru lib/crypto/priv/Makefile

#cp lib/ssl/c_src/sparc-sun-solaris2.9/Makefile lib/ssl/c_src/sparc-sun-solaris2.9/Makefile.orig
#awk '{if ($0 ~ /^SSL_LIBDIR = /) {print "SSL_LIBDIR = /usr/local/ssl/lib/sparcv9"} else {print}}' < lib/ssl/c_src/sparc-sun-solaris2.9/Makefile > lib/ssl/c_src/sparc-sun-solaris2.9/Makefile.ru
#cp lib/ssl/c_src/sparc-sun-solaris2.9/Makefile.ru lib/ssl/c_src/sparc-sun-solaris2.9/Makefile

gmake

%install
PATH="/opt/SUNWspro/bin:/usr/local/gnu/bin:${PATH}" \
CC="gcc" CXX="CC" CPPFLAGS="-I/usr/local/include" \
LD="/usr/ccs/bin/ld" \
LDFLAGS="-L/usr/local/lib -L/usr/local/ssl/lib -R/usr/local/lib -R/usr/local/ssl/lib"
export PATH CC CXX CPPFLAGS LD LDFLAGS

gmake INSTALL_PREFIX=%{buildroot} install
#begin stupid hack because the erlang build sets up non-relative symlinks which point to the buildroot, so I'm going to make them relative
#cd $RPM_BUILD_ROOT/usr/local/bin
#for i in ear ecc elink erl erlc escript; do rm $i; ln -s ../lib/erlang/bin/$i .; done

#cd $RPM_BUILD_ROOT/usr/local/lib/erlang/bin
#for i in erl start; do sed -e "s#$RPM_BUILD_ROOT##" $i > $i.bak; mv $i.bak $i; chmod 755 $i; done

#cd $RPM_BUILD_ROOT/usr/local/lib/erlang/erts-5.4.13/bin
#for i in erl start; do sed -e "s#$RPM_BUILD_ROOT##" $i > $i.bak; mv $i.bak $i; chmod 755 $i; done

#cd $RPM_BUILD_ROOT/usr/local/lib/erlang/bin
#rm epmd
#ln -s ../erts-5.4.13/bin/epmd .

cd %{buildroot}/usr/local/lib/erlang
tar xzf %{SOURCE1}
rm -f COPYRIGHT PR.template README
tar xzf %{SOURCE2}

%clean
rm -rf %{buildroot}

%files
%defattr(-, root, root)
%doc README
/usr/local/lib/erlang/*
/usr/local/bin/*

%changelog
* Thu Aug 23 2007 David Lee Halik <dhalik@nbcs.rutgers.edu> - R11B4-1
- Updated to R11B4
