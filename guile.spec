Name:		guile
Version:	1.8.3
Copyright:	GPL
Group:		Development/Languages
Summary:	An extensible scripting language
Release:	4
Source:		%{name}-%{version}.tar.gz
Patch:		guile.inline-2.patch
BuildRoot:	/var/tmp/%{name}-root
BuildRequires:	gmp-devel >= 4.1 libtool-devel >= 1.5.26

%description
Guile is a Scheme interpreter that you can link into your programs
to make them more customizable, in the spirit of Emacs.  If you are
writing a program that requires a lot of configuring, consider using
Guile instead of an ad-hoc configuration language. 

%prep
%setup -q
%patch -p0 

%build
#LD="/usr/ccs/bin/ld -L/usr/local/lib -R/usr/local/lib" \
# LDFLAGS="-L/usr/local/lib -R/usr/local/lib" CPPFLAGS="-I/usr/local/include" \
#CPPFLAGS="-I/usr/local/include -I/usr/sfw/include"
#LDFLAGS="-L/usr/local/lib -R/usr/local/lib -L/usr/sfw/lib -R/usr/sfw/lib"
#LD_LIBRARY_PATH="/usr/local/lib:/usr/sfw/lib"
#LD_RUN_PATH="/usr/local/lib:/usr/sfw/lib"
#CC="gcc" CXX="g++"
#export CPPFLAGS LDFLAGS LD_LIBRARY_PATH LD_RUN_PATH CC CXX

PATH="/opt/SUNWspro/bin:${PATH}" \
CC="cc" CXX="CC" CPPFLAGS="-I/usr/local/include -I/usr/local/include/gmp32" \
LD="/usr/ccs/bin/ld" \
LDFLAGS="-L/usr/local/lib -R/usr/local/lib"
export PATH CC CXX CPPFLAGS LD LDFLAGS


./configure \
	--prefix=/usr/local \
	--enable-dynamic-linking \
	--disable-nls \
	--infodir=/usr/local/info
gmake

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/local
gmake install DESTDIR=$RPM_BUILD_ROOT
cd %{buildroot}/usr/local/lib/
rm *.la
cd ../info
rm dir

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc COPYING
/usr/local/share/aclocal/guile.m4
/usr/local/lib/*
/usr/local/include/*
/usr/local/bin/*
/usr/local/share/guile
/usr/local/info/*

%changelog
* Fri Feb 08 2008 David Diffenbaugh <davediff@nbcs.rutgers.edu> - 1.8.3-4
- corrected files section, removed info/dir
* Wed Feb 06 2008 David Diffenbaugh <davediff@nbcs.rutgers.edu> - 1.8.3-3
- updated patch to include read.c and strings.c, added /usr/local/share to files section
* Mon Feb 04 2008 David Diffenbaugh <davediff@nbcs.rutgers.edu> - 1.8.3-2
- added patch from guile developers added libtool-devel buildrequires added --disable-nls 
* Sat Oct 20 2007 David Lee Halik <dhalik@nbcs.rutgers.edu> - 1.8.3-1
- Bump tp 1.8.3
- De-gcc-ify
