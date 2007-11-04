Name: gawk
Version: 3.1.6
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
PATH="/opt/SUNWspro/bin:${PATH}" \
CC="cc" CXX="CC" CPPFLAGS="-I/usr/local/include" \
LD="/usr/ccs/bin/ld" \
LDFLAGS="-L/usr/local/lib -R/usr/local/lib"
export PATH CC CXX CPPFLAGS LD LDFLAGS 

./configure --prefix=/usr/local --disable-nls

gmake -j3

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/local
gmake install DESTDIR=$RPM_BUILD_ROOT
cd %{buildroot}/usr/local
/usr/local/bin/unhardlinkify.py ./

# GO AWAY GNU INFO, no one wants you
rm -rf %{buildroot}/usr/local/share/info/dir

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
/usr/local/share/info/*info*
/usr/local/share/man/man1/*
/usr/local/libexec/awk/*

%changelog
* Sun Nov 04 2007 David Lee Halik <dhalik@nbcs.rutgers.edu> - 3.1.6
- Naveen stop building with gcc!!! :-p
* Tue Aug 14 2007 Naveen Gavini <ngavini@nbcs.rutgers.edu> - 3.1.5
- Updated to 3.1.5
