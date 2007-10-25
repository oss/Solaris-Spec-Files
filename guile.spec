Name:		guile
Version:	1.8.3
Copyright:	GPL
Group:		Development/Languages
Summary:	An extensible scripting language
Release:	1
Source:		%{name}-%{version}.tar.gz
#Patch:		guile.patch
BuildRoot:	/var/tmp/%{name}-root
BuildRequires:	gmp-devel >= 4.1

%description
Guile is a Scheme interpreter that you can link into your programs
to make them more customizable, in the spirit of Emacs.  If you are
writing a program that requires a lot of configuring, consider using
Guile instead of an ad-hoc configuration language. 

%prep
%setup -q
#%patch -p1

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
	--enable-dynamic-linking
gmake

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/local
gmake install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post
if [ -x /usr/local/bin/install-info ] ; then
	/usr/local/bin/install-info --info-dir=/usr/local/share/info \
		 /usr/local/share/info/data-rep.info
fi

%preun
if [ -x /usr/local/bin/install-info ] ; then
	/usr/local/bin/install-info --delete --info-dir=/usr/local/share/info \
		 /usr/local/share/info/data-rep.info
fi

%files
%defattr(-,root,root)
%doc COPYING
/usr/local/share/guile/%{version}
/usr/local/share/guile/guile-procedures.txt
/usr/local/share/aclocal/guile.m4
/usr/local/lib/lib*.a
/usr/local/lib/lib*.so*
/usr/local/include/*
/usr/local/bin/*
/usr/local/share/info/data-rep.info

%changelog
* Sat Oct 20 2007 David Lee Halik <dhalik@nbcs.rutgers.edu> - 1.8.3-1
- Bump tp 1.8.3
- De-gcc-ify
