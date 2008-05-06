Summary:	The erlang programming language
Name:		erlang
%define		preversion otp_src_
%define		manpreversion otp_doc_man_
%define		htmlpreversion otp_doc_html_
%define		tarball_version R12B-2
Version:	R12B2
Release:	1
License:	EPL
Group:		Development/Languages
Packager:	David Diffenbaugh <davediff@nbcs.rutgers.edu>
Source:		%{preversion}%{tarball_version}.tar.gz
Source1:	%{manpreversion}%{tarball_version}.tar.gz
Source2:	%{htmlpreversion}%{tarball_version}.tar.gz
Requires:	openssl >= 0.9.8
BuildRequires:	tar, perl, gcc >= 4.2.1, openssl >= 0.9.8, openssl-static >= 0.9.8
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
PATH="/opt/SUNWspro/bin:/usr/ccs/bin:/usr/local/gnu/bin:${PATH}" \
CC="gcc -mcpu=v9 -m64" CXX="g++ -mcpu=v9 -m64" CPPFLAGS="-I/usr/local/include" \
LD="/usr/ccs/bin/ld" CFLAGS="" \
LDFLAGS="-L/usr/local/lib/sparcv9 -L/usr/local/ssl/lib/sparcv9 -R/usr/local/lib/sparcv9 -R/usr/local/ssl/lib/sparcv9"
export PATH CC CXX CPPFLAGS LD LDFLAGS CFLAGS

./configure \
	--enable-threads \
	--enable-kernel-poll \
	--with-ssl="/usr/local/ssl" \
	--enable-smp-support \
	--prefix="/usr/local"


# Enable 64 bit libraries. configure uses the wrong set of static libs
cd lib/crypto/c_src/sparc-sun-solaris2.9/
sed -e "s/\/usr\/local\/ssl\/lib/\/usr\/local\/ssl\/sparcv9\/lib/g" Makefile > Makefile.test
mv Makefile.test Makefile
cd ../../../..

cd lib/ssl/c_src/sparc-sun-solaris2.9/
sed -e "s/\/usr\/local\/ssl\/lib/\/usr\/local\/ssl\/sparcv9\/lib/g" Makefile > Makefile.test
mv Makefile.test Makefile
cd ../../../..

gmake

%install
PATH="/opt/SUNWspro/bin:/usr/ccs/bin:/usr/local/gnu/bin:${PATH}" \
CC="gcc -mcpu=v9 -m64" CXX="g++ -mcpu=v9 -m64" CPPFLAGS="-I/usr/local/include" \
LD="/usr/ccs/bin/ld" CFLAGS="" \
LDFLAGS="-L/usr/local/lib/sparcv9 -L/usr/local/ssl/lib/sparcv9 -R/usr/local/lib/sparcv9 -R/usr/local/ssl/lib/sparcv9"
export PATH CC CXX CPPFLAGS LD LDFLAGS CFLAGS

gmake INSTALL_PREFIX=%{buildroot} install

#begin stupid hack because the erlang build sets up non-relative symlinks which point to the buildroot, so I'm going to make them relative
cd $RPM_BUILD_ROOT/usr/local/bin
for i in dialyzer epmd erl erlc escript run_erl to_erl typer; do rm $i; ln -s ../lib/erlang/bin/$i .; done

cd $RPM_BUILD_ROOT/usr/local/lib/erlang/bin
for i in erl start; do sed -e "s#$RPM_BUILD_ROOT##" $i > $i.bak; mv $i.bak $i; chmod 755 $i; done

cd $RPM_BUILD_ROOT/usr/local/lib/erlang/erts-5.6.2/bin
for i in erl start; do sed -e "s#$RPM_BUILD_ROOT##" $i > $i.bak; mv $i.bak $i; chmod 755 $i; done

cd $RPM_BUILD_ROOT/usr/local/lib/erlang/bin
rm epmd
ln -s ../erts-5.6.2/bin/epmd .

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
* Thu Apr 10 2008 David Diffenbaugh <davediff@nbcs.rutgers.edu> - R12B2-1
-bumped to R12B2, fixed reference to erts-5.5.5 to erts-5.6.2
* Wed Oct 24 2007 David Lee Halik <dhalik@nbcs.rutgers.edu> - R11B5-1
- Enable 64 bitness
- Bump to R11B5
* Thu Aug 23 2007 David Lee Halik <dhalik@nbcs.rutgers.edu> - R11B4-1
- Updated to R11B4
