Name: gawk
Version: 3.1.1
Copyright: GPL
Group: Development/Languages
Summary: Gnu awk
Release: 1
Source0: gawk-%{version}.tar.gz
Source1: gawk-%{version}-doc.tar.gz
Source2: gawk-%{version}-ps.tar.gz
BuildRoot: /var/tmp/%{name}-root

%description
The awk programming language is a text processing language designed by
Alfred V. Aho, Peter J. Weinberger, and Brian W. Kernighan.  Install
this package if you wish to develop or run awk programs that use GNU
extensions to awk.

%prep
%setup -q
%setup -D -T -b 1
%setup -D -T -b 2

%build
./configure --prefix=/usr/local
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
		 /usr/local/info/gawk.info
fi

%preun
if [ -x /usr/local/bin/install-info ] ; then
	/usr/local/bin/install-info --delete --info-dir=/usr/local/info \
		 /usr/local/info/gawk.info
fi

%files
%defattr(-,root,root)
%doc COPYING
%doc doc/*ps
%doc doc/gawk.dvi
%doc doc/awkforai.txt
/usr/local/bin/*
/usr/local/share/awk/*
/usr/local/info/*info*
/usr/local/man/man1/*
/usr/local/libexec/awk/*
#/usr/local/lib/locale/*/LC_MESSAGES
#/usr/local/lib/locale/*/LC_TIME
