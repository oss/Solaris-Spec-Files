Name: guile
Version: 1.4
Copyright: GPL
Group: Development/Languages
Summary: An extensible scripting language
Release: 4
Source: guile-1.4.tar.gz
Patch: guile.patch
BuildRoot: /var/tmp/%{name}-root

%description
Guile is a Scheme interpreter that you can link into your programs
to make them more customizable, in the spirit of Emacs.  If you are
writing a program that requires a lot of configuring, consider using
Guile instead of an ad-hoc configuration language. 

%prep
%setup -q
%patch -p1

%build
LD="/usr/ccs/bin/ld -L/usr/local/lib -R/usr/local/lib" \
 LDFLAGS="-L/usr/local/lib -R/usr/local/lib" CPPFLAGS="-I/usr/local/include" \
./configure --prefix=/usr/local --enable-dynamic-linking
make

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/local
make install prefix=$RPM_BUILD_ROOT/usr/local

%clean
rm -rf $RPM_BUILD_ROOT

%post
if [ -x /usr/local/bin/install-info ] ; then
	/usr/local/bin/install-info --info-dir=/usr/local/info \
		 /usr/local/info/data-rep.info
fi

%preun
if [ -x /usr/local/bin/install-info ] ; then
	/usr/local/bin/install-info --delete --info-dir=/usr/local/info \
		 /usr/local/info/data-rep.info
fi

%files
%defattr(-,root,root)
%doc COPYING
/usr/local/share/guile/%{version}
/usr/local/share/guile/guile-procedures.txt
/usr/local/share/aclocal/guile.m4
/usr/local/lib/lib*a
/usr/local/lib/lib*.so*
/usr/local/include/*
/usr/local/bin/*
/usr/local/info/data-rep.info
